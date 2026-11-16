# Estudo de concorrentes — Second Brain Manager

Data da coleta: 16/11/2026. Objetivo: aprender com estrutura, funções e preços. Nada aqui é para clonar.

## Como ler este estudo

Dois dos seis sites foram coletados diretamente e quatro foram pulados, porque os termos de uso deles vedam coleta automatizada. Para os pulados, o que aparece vem só da página de termos (que li para decidir) e de fontes públicas de terceiros, e está marcado como tal.

| Concorrente | Site | robots.txt | Termos de uso | Coleta direta |
|---|---|---|---|---|
| Meu Gestor | meugestoria.com | Libera tudo, menos conta, admin, API e webhooks | Proíbem robôs no uso do assistente e da conta, não a leitura das páginas públicas | **Feita** |
| Nora | noraai.co | Libera tudo, menos API e uma página de pós-compra | Não há termos de uso publicados, só política de privacidade, sem cláusula sobre coleta | **Feita** |
| Meu Assistente | meuassistente.io | Libera tudo | Vedam "robôs, scripts ou meios automatizados" para extrair dados do Serviço; a definição de Serviço é ambígua e pode incluir o site | **Pulada** |
| Meu Assessor | meuassessor.com | Libera tudo, inclusive rastreadores de IA | Vedam crawlers e scrapers na Plataforma, que inclui o site institucional, e vedam avaliação comparativa para produto concorrente sem autorização escrita | **Pulada** |
| Lindy | lindy.ai | Libera quase tudo, menos arquivo e páginas paginadas | Vedam spiders, robôs e scrapers, salvo buscadores e navegador comum, e vedam usar o serviço em esforço de concorrência | **Pulada** |
| Martin | trymartin.com | Libera tudo | Mesmo modelo de termos da Lindy, com as mesmas duas vedações | **Pulada** |

Observações sobre o método:

- Scrapling 0.5.1 com `robots_txt_obey` ligado, pedido HTTP simples, um pedido por vez com 2 s de intervalo, User-Agent identificado, sem imitar navegador, sem modo furtivo e sem proxy.
- Craft Anything 0.6.1 em Clean room, só com abrir página, captura de tela e fechar. Nenhum `rebuild` e nenhuma captura para reconstrução.
- Nenhuma conta criada, nenhum login, nenhum formulário enviado. Nenhum texto, logo, imagem ou código copiado: tudo abaixo é resumo com palavras próprias.
- O HTTPS de meuassistente.io apresenta um certificado de outro domínio. Só o robots.txt e a página de termos foram lidos, por HTTP simples, sem desligar a verificação de certificado.
- Para achar o link dos termos do Martin, a página inicial dele foi baixada uma vez. Usei só a lista de links e descartei o texto.
- Lindy e Martin são produtos americanos, em inglês, com preço só em dólar. Não converti para reais, porque o câmbio e os impostos de cartão internacional variam.
- Preços mudam. Os valores valem para a data da coleta.

---

## 1. Meu Gestor (meugestoria.com)

**Promessa em uma frase:** organizar finanças, compromissos, tarefas e lembretes conversando com um assistente no WhatsApp, sem aprender aplicativo novo.

**Funções**

- Finanças pessoais: gasto ou receita registrado em uma frase, categorias, saldo e resumo do mês, compras parceladas, contas fixas lançadas todo mês, orçamento por categoria com aviso perto do limite, controle de quem deve a quem com pagamento parcial.
- Agenda: marcar, remarcar e cancelar em linguagem natural, consulta de horários livres, alerta de conflito, aviso antes do compromisso com antecedência escolhida.
- Resumo do dia enviado toda manhã, no horário escolhido.
- Tarefas com prazo e prioridade, listas de compras, notas com busca.
- Lembretes únicos ou recorrentes (diário, dias úteis, semanal, mensal, anual), com edição pela conversa.
- Memória de preferências e datas, como aniversários e apelido.
- Entende áudio e lê foto de cupom ou comprovante. Diz que áudios e fotos não ficam guardados.
- Confirma cada registro e pergunta quando falta um dado, em vez de adivinhar.
- Em desenvolvimento, e marcado assim no site: guarda e busca de documentos.

**Primeiro uso, passo a passo**

1. Criar conta no site com e-mail e senha.
2. Entrar na área do cliente e gerar um código de uso único, válido por poucos minutos.
3. Enviar o código ao número do assistente pelo WhatsApp, a partir do próprio celular.
4. O vínculo é concluído e o teste grátis de 2 dias começa, sem cartão.
5. Conversar por texto, áudio ou foto.
6. Para continuar, assinar por Pix com débito mensal autorizado no banco ou por cartão. A cobrança exige CPF.

**Canais:** WhatsApp para o assistente (API oficial do WhatsApp Business). Web só para conta, assinatura e dados. Sem aplicativo.

**Planos e preços**

| Plano | Preço | Condições |
|---|---|---|
| Mensal (único) | R$ 29,99/mês | Sem fidelidade, sem plano gratuito e sem plano anual. Teste de 2 dias sem cartão. Sem limite fixo de mensagens para uso pessoal, com tetos técnicos contra abuso. Arrependimento em 7 dias. |

**Elogios e reclamações:** não encontrei avaliações públicas de usuários nem perfil no Reclame Aqui ligado a este domínio.

**Sinais a notar**

- O site se contradiz sobre o estágio do produto: a página de funções marca o assistente como disponível, a página inicial diz que a integração com o WhatsApp ainda será disponibilizada, e os termos dizem que o acesso é por convite.
- Os termos trazem um aviso de que são uma versão inicial ainda não revisada por advogado.
- A página de segurança é incomum pela franqueza: lista só controles já implementados e admite não ter certificações nem auditoria externa.

---

## 2. Nora (noraai.co)

**Promessa em uma frase:** uma assistente que não só lembra, mas executa por você dentro dos apps que você já usa, e só interrompe quando vale a pena.

**Funções** (segundo o site e a política de privacidade)

- Detecta conversas do WhatsApp sem resposta e propõe a resposta pronta, para editar ou enviar.
- Rascunha respostas e cobranças de e-mails parados.
- Transforma combinados em convites de agenda.
- Pesquisa e compra passagens e produtos, com aprovação do usuário antes do pagamento.
- Avisos proativos filtrados em três frentes: pessoas, tempo e trabalho. A proposta é não mandar resumos nem notificação por notificação.
- Gravação de áudio com transcrição, resumo, tópicos e lembretes, e reconhecimento de quem está falando a partir de uma amostra de voz.
- Lembretes por localização.
- Rotinas e ações executadas nas contas conectadas.
- Integrações declaradas: Google (Gmail, Agenda, Drive, Documentos, Planilhas, Tarefas), Microsoft (Outlook, Teams, OneDrive, Excel), Slack, Notion, Linear, WhatsApp, redes sociais, Whoop e Oura, além de ferramentas como GitHub, Figma, Trello, Todoist e Stripe.
- Declara não usar o conteúdo do usuário para treinar modelos nem para publicidade, e nomeia os provedores de IA que processam os dados.
- Segundo a imprensa, desde outubro de 2026 executa tarefas na web com navegador próprio, a partir do WhatsApp.

**Primeiro uso, passo a passo**

1. Pedir convite no site, informando nome, e-mail, WhatsApp e por que quer usar. O site avisa que uma boa justificativa aumenta a chance de aprovação.
2. Aguardar a análise da equipe. O convite chega por WhatsApp, e-mail ou ambos.
3. Criar conta, com e-mail e senha ou com login da Apple ou do Google.
4. Configuração inicial: idioma, áreas de foco e gravação da amostra de voz.
5. Conectar as contas desejadas, cada uma com autorização própria, e conceder as permissões do aparelho uma a uma.
6. Segundo a imprensa, cada membro pode convidar até cinco pessoas.

**Canais:** WhatsApp, aplicativo para iPhone e uso no computador. Há um painel web com login.

**Planos e preços:** a página de planos existe, mas mostra apenas "em breve". Acesso só por convite. Nenhum preço em reais publicado. Cuidado: um valor em dólar que aparece em buscas pertence a outro produto, de nome parecido e de outro país.

**Elogios e reclamações:** não encontrei avaliações públicas de usuários. A cobertura disponível é de imprensa de lançamento, que tende a repetir o material da empresa.

---

## 3. Meu Assistente (meuassistente.io) — coleta direta pulada

Fontes: a página de termos de uso do próprio site e o trecho do site que aparece em buscadores. Não verifiquei preço nem funções nas páginas oficiais.

**Promessa em uma frase:** um assistente com IA para cada parte da vida, feito para a rotina brasileira.

**Funções** (pelos termos)

- Lembretes e alarmes.
- Organização da agenda.
- Listas de compras e de tarefas.
- Resumo de textos e de áudios.
- Respostas a perguntas, sugestões de receitas e planejamento.
- O usuário cria vários assistentes, e há exemplos prontos para começar (pelo buscador).

**Primeiro uso, passo a passo** (parcial)

1. Começar grátis, sem cartão.
2. Fazer cadastro. Idade mínima de 18 anos, ou de 13 a 17 com consentimento do responsável.
3. Criar os primeiros assistentes, a partir dos exemplos prontos.
4. Os detalhes da jornada não foram coletados.

**Canais:** aplicativo para iPhone e Android e web. Os termos não citam o WhatsApp como canal.

**Planos e preços** (pelo buscador, a conferir no site)

| Plano | Preço | Inclui |
|---|---|---|
| Gratuito | R$ 0 | Primeiros assistentes, exemplos prontos, lembretes no celular, limite mensal de uso |
| Premium | R$ 19,90/mês | Mais assistentes, limite mensal maior, resumo de áudios e textos longos, lembretes e resumos diários, atendimento prioritário |

Cancelamento sem multa, inclusive pela própria conversa com o assistente. Arrependimento em 7 dias.

**Elogios e reclamações:** não encontrei avaliações públicas. Existem vários produtos com nome quase igual em outros domínios, o que dificulta achar avaliações confiáveis.

---

## 4. Meu Assessor (meuassessor.com) — coleta direta pulada

Fontes: a página de termos de uso do próprio site, trechos do site em buscadores, Reclame Aqui e uma comparação publicada por um concorrente dele (portanto parcial).

**Promessa em uma frase:** uma equipe de assessores de IA no WhatsApp para cuidar de finanças, agenda, documentos e tarefas.

**Funções** (pelos buscadores e pelo mapa do site)

- Seis assessores com nome e personalidade, cada um com uma área.
- Finanças com Open Finance.
- Agenda e tarefas.
- Documentos e atas.
- Notas fiscais e links de cobrança.
- Pesquisas.
- Painel web além do WhatsApp.

**Primeiro uso, passo a passo** (parcial)

1. Assinar pelo site.
2. Aceitar os termos no cadastro ou no primeiro contato pelo WhatsApp, por um botão de confirmação.
3. Conversar com os assessores pelo WhatsApp. Uma reclamação pública menciona código de convite e bloqueio de acesso por cadastro com outro número.
4. O restante da jornada não foi coletado.

**Canais:** WhatsApp e painel web. Os termos citam aplicativos móveis "quando disponíveis".

**Planos e preços** (pelos buscadores, a conferir no site)

| Plano | Preço | Condições |
|---|---|---|
| Anual | 12x de R$ 29,90 | Promoção de novembro anunciada a 12x de R$ 19,90, até 30/11 |
| Mensal | R$ 59,90/mês | Sem fidelidade |

Garantia de 7 dias com devolução integral. As fontes divergem sobre a existência do plano mensal na página de venda.

**Elogios e reclamações** (Reclame Aqui, perfil principal)

- Números: nota entre 6,1 e 7,0 conforme o período consultado, algumas centenas de reclamações, taxa de resposta alta e cerca de 80% de problemas resolvidos. Menos da metade dos reclamantes diz que voltaria a fazer negócio.
- Reclamações recorrentes: a IA não entende ou não registra lançamentos, exige formas específicas de escrever, falha em parcelamentos longos e em mensagens seguidas; suporte lento; dificuldade de cancelar e obter estorno em plano anual; queixa de propaganda acima do que o produto entrega.
- Elogios: só encontrei em textos promocionais, sem dados verificáveis. Dou pouco peso.
- Há um segundo perfil no Reclame Aqui, não verificado e sem respostas, que pode ser duplicado.

---

## 5. Lindy (lindy.ai) — coleta direta pulada

Fontes: a página de termos do próprio site, o trecho da página de preços exibido por buscadores e análises de terceiros, várias delas com cara de conteúdo de afiliado e com números que não batem entre si.

**Promessa em uma frase:** um assistente de trabalho com IA que cuida da caixa de entrada, das reuniões, da agenda e dos retornos pendentes.

**Funções** (por terceiros)

- Triagem e gestão automática da caixa de entrada, com rascunhos de resposta.
- Reuniões: preparação, anotações e acompanhamento depois.
- Agenda e cobrança de retornos.
- Delegação por mensagem, pelo iMessage e pelo Slack.
- Uso de computador, em que o assistente opera sites por conta do usuário.
- Criação de agentes próprios em linguagem natural, com muitas integrações.
- Pede aprovação antes de agir.
- Extensão para Chrome e oferta para empresas.

**Primeiro uso, passo a passo** (parcial)

1. Iniciar o teste de 7 dias. Não há mais plano gratuito permanente, segundo as análises.
2. Conectar e-mail e agenda.
3. Delegar por mensagem ou instalar no Slack, o que uma análise descreve como um clique.
4. O restante da jornada não foi coletado.

**Canais:** web, iMessage, Slack, e-mail e extensão de navegador. Os termos citam aplicativo móvel. Não encontrei menção a WhatsApp.

**Planos e preços** (em dólar, a conferir no site)

| Plano | Preço | Observação |
|---|---|---|
| Plus | US$ 49,99/mês | É o valor que aparece na página oficial via buscador. Uma análise cita US$ 29,99 |
| Pro | US$ 99,99/mês | Citado por uma única análise |
| Max | US$ 199,99/mês | Citado por uma única análise |
| Enterprise | Sob consulta | |

No início de 2026 a empresa teria trocado o modelo de créditos por assinatura fixa. As fontes ainda divergem sobre créditos embutidos nos planos.

**Elogios e reclamações**

- Elogios: configuração sem código e interface fácil são o ponto mais citado no G2, onde a nota fica entre 4,7 e 4,9.
- Reclamações: no Trustpilot, cobrança depois do cancelamento, cobrança não autorizada e dificuldade de reembolso. Também lentidão, consumo de créditos mesmo quando o resultado sai errado e dificuldade com fluxos mais complexos.

---

## 6. Martin (trymartin.com) — coleta direta pulada

Fontes: a página de termos, o robots.txt e análises e diretórios de terceiros. As notas variam muito entre as fontes.

**Promessa em uma frase:** um assistente pessoal de IA no estilo Jarvis, com quem se fala por mensagem ou ligação.

**Funções** (por terceiros)

- Agenda, caixa de entrada, lembretes e lista de tarefas.
- Faz ligações e envia mensagens em nome do usuário, e confirma os detalhes antes de enviar.
- Ligações de despertar e tarefas em segundo plano.
- Conversa por voz, inclusive por telefonema.
- Alternância entre perfil pessoal e de trabalho nos planos.

**Primeiro uso, passo a passo** (parcial)

1. Cadastro no painel web, com verificação por e-mail ou telefone.
2. Teste grátis de 7 dias, com cancelamento a qualquer momento.
3. Conectar agenda e caixa de entrada.
4. Falar com o assistente pelo canal preferido.

**Canais:** SMS, ligação telefônica, e-mail, Slack, aplicativo para iPhone e painel web. Algumas fontes citam WhatsApp. Não há aplicativo Android listado.

**Planos e preços** (em dólar, a conferir no site)

| Plano | Anual | Mensal |
|---|---|---|
| Basic | cerca de US$ 21/mês | US$ 35/mês |
| Pro | cerca de US$ 30/mês | até US$ 49/mês |

Os valores vêm de capturas de terceiros feitas entre maio e outubro de 2026 e não coincidem totalmente.

**Elogios e reclamações**

- Elogios: bom suporte e notas em torno de 4,4 a 4,6 em diretórios e no Product Hunt, este com poucas avaliações.
- Reclamações: atraso em comandos complexos e ao rascunhar e-mails, recursos ainda em evolução, falta de webhooks e de API pública, ausência de Android.

---

## Comparativo rápido

| | Canal principal | Entrada | Preço mensal | Foco |
|---|---|---|---|---|
| Meu Gestor | WhatsApp | Teste de 2 dias | R$ 29,99 | Registro e organização |
| Nora | WhatsApp e app iPhone | Convite | Não publicado | Execução de tarefas |
| Meu Assistente | App e web | Plano gratuito | R$ 19,90 | Vários assistentes simples |
| Meu Assessor | WhatsApp e painel web | Garantia de 7 dias | R$ 59,90, ou cerca de R$ 29,90 no anual | Equipe de personas, finanças |
| Lindy | Web, iMessage e Slack | Teste de 7 dias | A partir de US$ 49,99 | Trabalho: e-mail e reuniões |
| Martin | SMS, ligação e app iPhone | Teste de 7 dias | US$ 35, ou cerca de US$ 21 no anual | Assistente pessoal por voz e texto |

Só Meu Gestor e Nora foram conferidos nos sites oficiais.

---|---|---|---|---|
| Canal principal | WhatsApp | WhatsApp e app iPhone | App e web | WhatsApp e painel web |
| Entrada | Teste de 2 dias | Convite | Plano gratuito | Garantia de 7 dias |
| Preço mensal | R$ 29,99 | Não publicado | R$ 19,90 | R$ 59,90, ou cerca de R$ 29,90 no anual |
| Foco | Registro e organização | Execução de tarefas | Vários assistentes simples | Equipe de personas, finanças |
| Integrações externas | Nenhuma declarada | Muitas | Não identificadas | Open Finance |

---

## O que vale trazer para o Second Brain

1. **Confirmar o que foi entendido e perguntar o que falta.** O Meu Gestor confirma cada registro e pergunta em vez de adivinhar. As reclamações do Meu Assessor mostram o custo de errar em silêncio.
2. **Vínculo do WhatsApp por código de uso único gerado na área logada.** É simples e impede que alguém acesse dados só informando um número.
3. **Resumo do dia em horário escolhido pelo usuário.**
4. **Captura sem atrito por áudio e foto**, com a regra clara de que a mídia não fica guardada.
5. **Sugestão pronta com aprovação humana.** A Nora propõe a resposta ou a compra e o usuário só aprova. Bom padrão para qualquer ação com consequência.
6. **Interromper pouco.** Avisar só o que o usuário se arrependeria de não saber é um critério melhor que mandar tudo.
7. **Marcar no site o que está disponível e o que está em desenvolvimento**, e uma página de segurança que só lista o que já existe.
8. **Controle dos dados à vista:** baixar, corrigir e apagar pela área do cliente e pela conversa, e dizer com quais provedores de IA os dados são compartilhados.
9. **Preço simples e cancelamento fácil**, inclusive pela conversa. Um plano gratuito ou teste curto sem cartão reduz a barreira.
10. **Pix com débito mensal autorizado** como forma de pagamento, além do cartão.
11. **Voz como canal.** O Martin atende por ligação e faz ligações de despertar. Para lembrete crítico, uma chamada é mais difícil de ignorar que uma mensagem.
12. **Começar por uma dor só.** A Lindy entra pela caixa de entrada e pelas reuniões, e só depois amplia. É mais fácil de explicar do que "faz tudo".

## O que nenhum deles faz (pelo que foi possível observar)

1. **Segundo cérebro de verdade.** Os brasileiros guardam itens soltos (gasto, tarefa, nota) e os americanos focam em executar tarefas de e-mail e agenda. Nenhum liga uma nota a outra, a pessoas, a projetos ou a decisões, nem responde perguntas cruzando tudo o que o usuário já guardou.
2. **Busca com fonte.** Nenhum mostra de onde tirou a resposta, com a nota ou a mensagem original ao lado.
3. **Revisão periódica do conhecimento.** Há resumo do dia, mas não revisão semanal de ideias, pendências antigas ou notas esquecidas.
4. **Portabilidade aberta.** O Meu Gestor oferece cópia dos dados, mas nenhum anuncia exportação em formato aberto, como Markdown, nem sincronização com ferramentas de notas.
5. **Mesma memória em todos os canais.** Cada um privilegia um canal. Nenhum promete WhatsApp, web e app com a mesma memória e o mesmo histórico.
6. **Memória visível e editável.** Nenhum mostra uma tela com o que o assistente sabe sobre o usuário, para corrigir ou apagar item por item.
7. **Execução de tarefas em português, com preço em reais e acesso aberto.** A Nora executa ações, mas não tem preço nem acesso aberto. Lindy e Martin executam, mas são em inglês, cobram em dólar e não têm o WhatsApp como canal central.
8. **Finanças pessoais junto com execução de tarefas.** Os brasileiros registram gastos, os americanos não tratam de finanças pessoais.

Ressalva: quatro sites não foram coletados, então alguma dessas lacunas pode estar coberta em páginas que não li.

## O que evitar

1. **Prometer mais do que o produto faz.** É a queixa central contra o Meu Assessor. O risco cresce com personas e muitas áreas ao mesmo tempo.
2. **Site que se contradiz sobre o estágio do produto**, como ocorre no Meu Gestor, e termos publicados com aviso de rascunho.
3. **Plano anual como porta de entrada com cancelamento difícil.** Gera pedidos de estorno e reclamação pública.
4. **Suporte que não responde.** Em produto que mexe com dinheiro e agenda, vira reclamação rapidamente.
5. **Exigir jeito certo de escrever.** O usuário espera linguagem natural, inclusive em parcelas e em mensagens enviadas em sequência.
6. **Ser o único aviso para algo crítico.** Dois concorrentes avisam nos termos que lembretes podem falhar. Vale dizer isso ao usuário no produto, não só no contrato.
7. **Pedir permissões demais de uma vez.** O modelo da Nora depende de acesso amplo a mensagens, e-mail e saúde. Sem confiança construída, isso afasta, e aumenta muito a responsabilidade com dados sensíveis.
8. **Fila de convite longa sem preço.** Cria expectativa, mas impede o usuário de decidir.
9. **Nome genérico.** Há vários produtos chamados "Meu Assistente", "Meu Assessor" e "Nora" em domínios diferentes, o que confunde busca, avaliações e até o Reclame Aqui.
10. **Cobrança por créditos e cobrança depois do cancelamento.** São as queixas mais fortes contra a Lindy. Crédito gasto em resultado errado irrita mais que preço alto.
11. **Lançar só para iPhone.** Martin e Nora não têm Android, que é a maioria dos celulares no Brasil.
12. **Depender de um só canal de terceiros.** Há relatos públicos de números de WhatsApp bloqueados ligados a um dos concorrentes, sem causa confirmada. Ter web ou app como alternativa reduz o risco.

---

## Fontes

Sites coletados diretamente: meugestoria.com (início, funcionalidades, como funciona, preço, perguntas frequentes, segurança, termos de uso) e noraai.co (início, planos, privacidade).

Páginas lidas só para decidir sobre a coleta: termos de uso de meuassistente.io, meuassessor.com, lindy.ai e trymartin.com, e o robots.txt dos seis sites.

Fontes de terceiros:

- [ABC da Comunicação — lançamento da Nora](https://www.abcdacomunicacao.com.br/startup-brasileira-lanca-nora-assistente-pessoal-de-ia-que-resolve-tarefas-pelo-whatsapp/)
- [Guaíra News — Nora no WhatsApp](https://www.guairanews.com/2026/11/06/nora-assistente-pessoal-whatsapp/)
- [Reclame Aqui — Meu Assessor](https://www.reclameaqui.com.br/empresa/meu-assessor/)
- [Reclame Aqui — Meu Assessor, lista de reclamações](https://www.reclameaqui.com.br/empresa/meu-assessor/lista-reclamacoes/)
- [Reclame Aqui — segundo perfil, não verificado](https://www.reclameaqui.com.br/empresa/meu-assessor-i-plataforma-via-whatssap/)
- [ZapGastos — comparação com o Meu Assessor (fonte concorrente)](https://zapgastos.com/compare/meu-assessor/)
- Trechos de meuassistente.io, meuassessor.com e lindy.ai exibidos por buscadores, usados para preço e funções.
- [CloudTalk — análise da Lindy](https://www.cloudtalk.io/blog/lindy-ai-review/)
- [CloudTalk — preços da Lindy](https://www.cloudtalk.io/blog/lindy-ai-pricing/)
- [Saner.ai — avaliações da Lindy](https://www.saner.ai/blogs/lindy-ai-reviews)
- [Makerstack — análise da Lindy](https://makerstack.co/reviews/lindy-ai-review/)
- [eesel.ai — análise do Martin](https://www.eesel.ai/blog/martin-ai-review)
- [Product Hunt — avaliações do Martin](https://www.producthunt.com/products/martin/reviews)
- [Tool Directory — Martin](https://tooldirectory.ai/tools/martin)
- [xpay — preços do Martin](https://www.xpay.sh/saas-pricing/try-martin/)
