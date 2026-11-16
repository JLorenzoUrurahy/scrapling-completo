"""Inspeção em Clean room com o Craft Anything, por uma sessão MCP.

Só usa ferramentas que observam a página como um visitante: abrir o site,
tirar uma captura de tela e fechar. Não roda rebuild nem captura para reconstruir.

Uso: python inspecionar.py <craft-anything-cli> <pasta_de_saida> <url> [<url> ...]
     python inspecionar.py <craft-anything-cli> --listar
"""

import base64
import json
import re
import subprocess
import sys
from pathlib import Path


class Mcp:
    def __init__(self, cli: str):
        # --clean-room: nada de dentro do alvo é lido. --allow-run vale só para esta execução.
        self.p = subprocess.Popen(
            [cli, "--clean-room", "--allow-run", "mcp"],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL, text=True,
        )
        self.n = 0
        self.call("initialize", {"protocolVersion": "2025-06-18", "capabilities": {},
                                 "clientInfo": {"name": "estudo-concorrentes", "version": "1.0"}})
        self.send({"jsonrpc": "2.0", "method": "notifications/initialized"})

    def send(self, msg: dict) -> None:
        self.p.stdin.write(json.dumps(msg) + "\n")
        self.p.stdin.flush()

    def call(self, method: str, params: dict) -> dict:
        self.n += 1
        self.send({"jsonrpc": "2.0", "id": self.n, "method": method, "params": params})
        while True:
            line = self.p.stdout.readline()
            if not line:
                raise RuntimeError("o servidor MCP encerrou")
            msg = json.loads(line)
            if msg.get("id") == self.n:
                return msg

    def tool(self, name: str, args: dict) -> dict:
        return self.call("tools/call", {"name": name, "arguments": args})

    def close(self) -> None:
        self.p.stdin.close()
        self.p.wait(timeout=20)


def achar_png(obj):
    """Procura a imagem (base64) em qualquer ponto da resposta."""
    if isinstance(obj, dict):
        if obj.get("type") == "image" and obj.get("data"):
            return obj["data"]
        for chave in ("base64", "png_base64", "data"):
            v = obj.get(chave)
            if isinstance(v, str) and v.startswith("iVBOR"):
                return v
        for v in obj.values():
            r = achar_png(v)
            if r:
                return r
    elif isinstance(obj, list):
        for v in obj:
            r = achar_png(v)
            if r:
                return r
    elif isinstance(obj, str) and obj.lstrip().startswith("{"):
        try:
            return achar_png(json.loads(obj))
        except ValueError:
            return None
    return None


def resumo(msg: dict) -> str:
    return json.dumps(msg.get("result", msg.get("error")), ensure_ascii=False)[:700]


def main() -> None:
    cli = sys.argv[1]
    mcp = Mcp(cli)
    if sys.argv[2] == "--listar":
        for t in mcp.call("tools/list", {})["result"]["tools"]:
            print(t["name"], "-", (t.get("description") or "")[:110].replace("\n", " "))
        mcp.close()
        return
    saida = Path(sys.argv[2])
    saida.mkdir(parents=True, exist_ok=True)
    ligado = mcp.tool("enable_toolset", {"toolset": "browser"})
    print("TOOLSET browser ->", resumo(ligado)[:300])
    for url in sys.argv[3:]:
        nome = re.sub(r"[^a-zA-Z0-9]+", "-", url.split("://", 1)[1]).strip("-")
        aberto = mcp.tool("web_site_open", {"url": url, "width": 1440, "height": 900})
        print("ABRIR", url, "->", resumo(aberto)[:400])
        foto = mcp.tool("web_page_screenshot_take", {})
        png = achar_png(foto)
        if png:
            (saida / f"{nome}.png").write_bytes(base64.b64decode(png))
            print("  captura salva:", f"{nome}.png")
        else:
            print("  sem captura:", resumo(foto)[:400])
        print("  fechar:", resumo(mcp.tool("web_site_close", {}))[:160])
    mcp.close()


if __name__ == "__main__":
    main()
