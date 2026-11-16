"""Coleta somente leitura de páginas públicas para o estudo de concorrentes.

- Pedido HTTP simples (FetcherSession), sem navegador, sem modo furtivo, sem proxy extra.
- robots_txt_obey ligado: o Scrapling lê o robots.txt de cada site e pula o que for proibido.
- User-Agent identificado, sem imitar navegador.
- Guarda apenas o texto visível, para leitura e resumo. Nada é republicado.

Uso: python coletar.py <pasta_de_saida> <url> [<url> ...]
"""

import json
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

from scrapling.fetchers import FetcherSession
from scrapling.spiders import Spider

USER_AGENT = "estudo-concorrentes/1.0 (leitura unica de paginas publicas; respeita robots.txt)"


def nome_arquivo(url: str) -> str:
    p = urlparse(url)
    caminho = re.sub(r"[^a-zA-Z0-9]+", "-", p.path).strip("-") or "home"
    return f"{p.netloc}__{caminho}.txt"


class EstudoSpider(Spider):
    name = "estudo-concorrentes"
    robots_txt_obey = True
    concurrent_requests = 1
    download_delay = 2.0
    logging_level = 20  # INFO

    def __init__(self, saida: Path, urls: list[str]):
        self.saida = saida
        self.start_urls = urls
        self.allowed_domains = {urlparse(u).netloc for u in urls}
        self.indice: list[dict] = []
        super().__init__()

    def configure_sessions(self, manager) -> None:
        manager.add(
            "default",
            FetcherSession(
                impersonate=None,
                stealthy_headers=False,
                headers={"User-Agent": USER_AGENT},
                retries=1,
                timeout=30,
            ),
        )

    async def parse(self, response):
        texto = response.get_all_text(separator="\n", strip=True, ignore_tags=("script", "style", "noscript", "svg"))
        links = sorted({response.urljoin(h) for h in response.css("a::attr(href)").getall() if h})
        arquivo = self.saida / nome_arquivo(response.url)
        arquivo.write_text(str(texto), encoding="utf-8")
        self.indice.append(
            {
                "url": response.url,
                "status": response.status,
                "titulo": str(response.css("title::text").get() or ""),
                "caracteres": len(texto),
                "arquivo": arquivo.name,
                "links": links,
            }
        )
        yield {"url": response.url, "status": response.status}


def main() -> None:
    saida = Path(sys.argv[1])
    saida.mkdir(parents=True, exist_ok=True)
    spider = EstudoSpider(saida, sys.argv[2:])
    spider.start()
    pedidas = set(sys.argv[2:])
    obtidas = {i["url"] for i in spider.indice}
    for item in spider.indice:
        print(f'{item["status"]} {item["caracteres"]:>7} {item["url"]}  [{item["titulo"][:60]}]')
    for falta in sorted(pedidas - obtidas):
        print(f"--- sem resposta salva (robots.txt, erro ou redirecionamento): {falta}")
    (saida / f"indice-{len(list(saida.glob('indice-*.json')))}.json").write_text(
        json.dumps(spider.indice, ensure_ascii=False, indent=1), encoding="utf-8"
    )


if __name__ == "__main__":
    main()
