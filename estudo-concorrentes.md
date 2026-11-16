# Estudo de concorrentes — Second Brain Manager

Data da coleta: 16/11/2026. Objetivo: aprender com estrutura, funções e preços. Nada aqui é para clonar.

## Como ler este estudo

Os sete sites foram coletados diretamente, nas páginas públicas. Em quatro deles os termos de uso vedam coleta automatizada ou avaliação por concorrente; a coleta foi feita mesmo assim por decisão do dono do projeto, que assume esse risco. O robots.txt foi respeitado em todos.

| Concorrente | Site | robots.txt | O que os termos de uso dizem sobre coleta |
|---|---|---|---|
| Meu Gestor | meugestoria.com | Libera tudo, menos conta, admin, API e webhooks | Proíbem robôs no uso do assistente e da conta, não a leitura das páginas públicas |
| Nora | noraai.co | Libera tudo, menos API e uma página de pós-compra | Não há termos publicados, só política de privacidade, sem cláusula sobre coleta |
| Spilo | spilo.ai | Libera as páginas públicas e bloqueia áreas logadas e API | Proíbem copiar, modificar e fazer engenharia reversa do serviço; nada sobre leitura automatizada |
| Meu Assistente | meuassistente.io | Libera tudo | **Vedam** robôs e scripts para extrair dados do Serviço; a definição de Serviço é ambígua quanto ao site |
| Meu Assessor | meuassessor.com | Libera tudo, inclusive rastreadores de IA | **Vedam** crawlers e scrapers na Plataforma, que inclui o site, e avaliação comparativa para produto concorrente |
| Lindy | lindy.ai | Libera quase tudo, menos arquivo e páginas paginadas | **Vedam** spiders, robôs e scrapers, salvo buscadores e navegador comum, e uso em esforço de concorrência |
| Martin | trymartin.com | Libera tudo | **Vedam** o mesmo que a Lindy; usam o mesmo modelo de termos |

Observações sobre o método:

- Scrapling 0.5.1 com `robots_txt_obey` ligado, pedido HTTP simples, um pedido por vez com 2 s de intervalo, User-Agent identificado, sem imitar navegador, sem modo furtivo e sem proxy. Nenhuma página foi barrada pelo robots.txt.
- Craft Anything 0.6.1 em Clean room, só com abrir página, captura de tela e fechar. Nenhum `rebuild` e nenhuma captura para reconstrução.
- Nenhuma conta criada, nenhum login, nenhum formulário enviado. Nenhum texto, logo, imagem ou código copiado: tudo abaixo é resumo com palavras próprias.
- O HTTPS de meuassistente.io apresenta um certificado de outro domínio. As páginas foram lidas por HTTP simples, sem desligar a verificação de certificado. O Craft Anything não conseguiu abrir esse site.
- O site do Spilo é montado por JavaScript, então o pedido HTTP simples voltou sem texto. Li as três páginas públicas num navegador comum, sem modo furtivo.
- Lindy e Martin são produtos americanos, em inglês, com preço só em dólar. Não converti para reais, porque o câmbio e os impostos de cartão internacional variam.
- Preços mudam. Os valores valem para a data da coleta, e dois sites estavam com promoção de novembro.

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

## 3. Meu Assistente (meuassistente.io)

**Promessa em uma frase:** um assistente com IA para cada parte da vida, criado em um minuto só descrevendo o que você precisa.

**Funções**

- O usuário cria vários assistentes, um por assunto: alimentação, contas da casa, estudos, inglês, saúde e treino, pequeno negócio.
- Cada assistente nasce de uma descrição em linguagem comum, recebe um nome e um jeito de falar (direto, detalhado ou paciente).
- Modelos prontos para quem não sabe por onde começar, usáveis como estão ou ajustáveis.
- Conversa por texto ou áudio; entende abreviação e erro de digitação.
- Cada assistente guarda o contexto do seu assunto, para o usuário não repetir tudo.
- Lembretes e resumos enviados ao celular sem pedir.
- Resumo de áudios e textos longos, no plano pago.
- Exclusão dos dados a qualquer momento.

**Primeiro uso, passo a passo**

1. Começar grátis, sem cartão, no iPhone, no Android ou no navegador.
2. Contar o que precisa, com as próprias palavras, ou escolher um modelo pronto.
3. Dar um nome ao assistente e escolher o jeito de falar.
4. Conversar por texto ou áudio. Os avisos chegam no celular.

**Canais:** aplicativo para iPhone e Android e web. Não usa WhatsApp.

**Planos e preços**

| Plano | Preço | Inclui |
|---|---|---|
| Gratuito | R$ 0 | Primeiros assistentes, modelos prontos, lembretes no celular, limite mensal de uso |
| Premium | R$ 19,90/mês | Mais assistentes, limite de conversas bem maior, resumo de áudios e textos longos, lembretes e resumos diários, atendimento prioritário |

Sem fidelidade. Cancelamento pela área da conta ou por e-mail, sem multa. Arrependimento em 7 dias.

**Elogios e reclamações:** não encontrei avaliações públicas. Há vários produtos de nome quase igual em outros domínios, o que dificulta achar avaliações confiáveis.

**Sinais a notar**

- O certificado de segurança do site está errado, o que faz o navegador exibir alerta. Para um produto que pede dados pessoais, isso derruba a confiança logo na entrada.
- O site não informa os números dos limites dos planos.

---

## 4. Meu Assessor (meuassessor.com)

**Promessa em uma frase:** uma equipe de seis assessores de IA no WhatsApp que cuida do dinheiro, da agenda, das tarefas e dos documentos.

**Funções**

- Seis personas com nome e cargo, todas na mesma conversa: um coordenador que distribui os pedidos, um financeiro, uma secretária, uma de organização e documentos, um de pesquisas e uma fiscal.
- Finanças: registro de gastos por texto, áudio ou foto, categorias e orçamento por categoria, parcelas, faturas e limites de cartão, contas e transferências, metas, gráficos e relatórios em PDF e Excel.
- Open Finance com mais de 200 bancos, só para leitura, com autorização no aplicativo do banco. É opcional.
- Agenda: compromissos por áudio ou texto, integração com Google Agenda, lembretes, resumo diário, agenda pública para marcação, recados enviados a contatos.
- Reuniões: marcar com convites e link, remarcar avisando os participantes, transcrição do Meet, ata e tarefas extraídas da reunião.
- Tarefas e projetos com prazo, listas de compras e um acervo de arquivos em que se pede o documento pelo assunto.
- Notas fiscais de serviço: emissão, PDF, envio ao cliente e resumo fiscal, dependendo do cadastro fiscal da empresa.
- Pesquisas e comparações com fontes, incluindo passagens, hotéis e preços.
- Painel web e aplicativo para ver gráficos e registros.
- Conta compartilhada com família, sócios ou equipe, sem limite de pessoas e sem cobrança por pessoa.
- Uma página com cerca de 200 exemplos de pedidos, em 12 categorias, e demonstrações interativas.

**Primeiro uso, passo a passo**

1. Assinar pelo site. Não há plano gratuito nem teste sem pagar; a cobrança começa na contratação.
2. Aceitar os termos, no cadastro ou no primeiro contato pelo WhatsApp.
3. Mandar o primeiro pedido pelo WhatsApp, por texto, áudio, foto, PDF ou planilha. O assessor do assunto responde.
4. Opcionalmente, conectar bancos e o Google Agenda.
5. Acompanhar pelo painel web ou pelo aplicativo.
6. Em até 7 dias, pode pedir a devolução integral.

**Canais:** WhatsApp para conversar; painel web e aplicativos para iPhone e Android para consultar.

**Planos e preços**

| Plano | Preço | Condições |
|---|---|---|
| Anual (único) | 12x de R$ 29,90, total de R$ 358,80 | A contratação é anual; as parcelas não são uma assinatura mensal |
| Promoção de novembro | 12x de R$ 19,90, total de R$ 238,80 no primeiro ano | Até 30/11 |

O site anuncia "tudo sem limites", mas os termos remetem a uma política de uso justo com limites de referência. Garantia de 7 dias. Depois dela, o cancelamento só impede a renovação e as parcelas do ano contratado continuam. Não vi plano mensal na página de venda.

**Elogios e reclamações**

- O site afirma ter mais de 350 mil usuários. Não há como conferir.
- Reclame Aqui, perfil principal: nota entre 6,1 e 7,0 conforme o período, algumas centenas de reclamações, taxa de resposta alta e cerca de 80% de problemas resolvidos. Menos da metade dos reclamantes diz que voltaria a fazer negócio.
- Reclamações recorrentes: a IA não entende ou não registra lançamentos, exige formas específicas de escrever, falha em parcelamentos longos e em mensagens seguidas; suporte lento; dificuldade de cancelar e obter estorno do plano anual; queixa de propaganda acima do que o produto entrega.
- Elogios: só encontrei em textos promocionais, sem dados verificáveis.

---

## 5. Lindy (lindy.ai)

**Promessa em uma frase:** um funcionário de IA que se conecta às suas ferramentas, aprende como você trabalha e tira trabalho real da sua mesa.

O posicionamento atual é para empresas pequenas e agências, não para a vida pessoal. Várias análises de terceiros ainda a descrevem como assistente pessoal de assinatura fixa, o que o site não confirma mais.

**Funções**

- Trabalha por "funções" contratáveis: caixa de entrada e agenda, prospecção, relatórios de clientes, cobrança, atendimento, entre outras.
- Caixa de entrada: triagem e rascunhos no tom do usuário, com 2 a 5 caixas conforme o plano.
- Reuniões: gravação, anotações, preparação, agendamento e acompanhamento.
- Resumo diário, cutucões e rotinas agendadas.
- Proativa: percebe o que está atrasando e se oferece para assumir.
- Memória de contexto: aprende com cada ligação, e-mail e correção.
- Faz ligações telefônicas e opera sites com navegador próprio.
- Mais de 3.000 integrações e suporte a MCP. O usuário escolhe o modelo de IA por tarefa.
- Aprovação embutida: o que tem efeito externo espera o sim do usuário; consultas acontecem direto.
- Segurança como argumento de venda: SOC 2, GDPR e, no plano empresarial, HIPAA.

**Primeiro uso, passo a passo**

1. Começar grátis, com US$ 50 em créditos que valem 7 dias. O site promete configuração em 2 minutos.
2. Conectar as ferramentas de trabalho.
3. Passar tarefas pelo Slack, por e-mail ou por mensagem de texto.
4. Aprovar o que ela prepara antes de sair.
5. Depois dos 7 dias, o uso passa a ser pago por usuário.

**Canais:** Slack, e-mail, mensagem de texto (iMessage), agenda, web e extensão para Chrome. Sem WhatsApp.

**Planos e preços** (em dólar)

| Plano | Preço | Inclui |
|---|---|---|
| Free | US$ 0 | US$ 50 em créditos, válidos por 7 dias |
| Team | A partir de US$ 29,99 por usuário por mês | 3.000 créditos por mês, em um saldo comum da equipe. Pacotes maiores sobem de preço. Crédito extra a US$ 10 por 1.000 |
| Enterprise | Sob consulta | Conformidade, login único, auditoria, suporte dedicado |

Os créditos do mês não acumulam. Uma pergunta simples gasta de 2 a 250 créditos e um trabalho grande, de 1.000 a 2.500. Quando o saldo acaba, ela pausa em vez de cobrar a mais.

**Elogios e reclamações** (terceiros)

- Elogios: configuração sem código e interface fácil são o ponto mais citado no G2, com nota entre 4,7 e 4,9.
- Reclamações: no Trustpilot, cobrança depois do cancelamento, cobrança não autorizada e dificuldade de reembolso. Também lentidão e consumo de créditos mesmo quando o resultado sai errado.

---

## 6. Martin (trymartin.com)

**Promessa em uma frase:** uma IA pessoal no estilo Jarvis, com quem se fala por mensagem, ligação, e-mail ou Slack.

**Funções**

- Agenda no piloto automático: basta colocar o assistente em cópia num e-mail para ele marcar.
- Caixa de entrada: busca, leitura, rascunhos e etiquetas automáticas.
- Ligações de despertar, com voz.
- Envia mensagens e e-mails em nome do usuário e manda avisos em canais do Slack.
- Lembretes e lista de tarefas, com notificação de pendências do dia.
- Ações proativas, como achar material novo para uma pesquisa e oferecer o envio.
- Modo de voz e atalhos no aplicativo.
- Lembra das preferências do usuário.
- Planos separados para uso pessoal e para empresa.

**Primeiro uso, passo a passo**

1. Cadastro pelo site ou pelo aplicativo de iPhone, com 7 dias grátis.
2. Conectar caixa de entrada e agenda.
3. Falar com o assistente pelo canal preferido: mensagem, ligação, e-mail ou Slack.
4. Receber avisos e ações proativas.

**Canais:** SMS, ligação telefônica, e-mail, Slack, aplicativo para iPhone e painel web. O site não cita WhatsApp nem Android.

**Planos e preços** (em dólar, plano pessoal)

| Plano | Anual | Mensal | Inclui |
|---|---|---|---|
| Basic | US$ 21/mês | US$ 35/mês | Modelos básicos, ações proativas limitadas, 2 tarefas por vez |
| Pro | US$ 30/mês | US$ 49/mês | Modelos mais avançados, ações proativas e tarefas sem limite |

Havia promoção de 30% no primeiro ano na data da coleta. 7 dias grátis, com cancelamento a qualquer momento.

**Elogios e reclamações**

- Elogios: o próprio site reúne depoimentos de lojas de aplicativos e do Product Hunt, que destacam a memória de preferências, a voz e a utilidade para quem esquece compromissos. São escolhidos pela empresa.
- Terceiros: notas em torno de 4,4 a 4,6 em diretórios e no Product Hunt, este com poucas avaliações.
- Reclamações (terceiros): atraso em comandos complexos e ao rascunhar e-mails, recursos ainda em evolução, falta de API pública e de Android.

**Sinal a notar:** o rodapé do site ainda traz o ano de 2024 e os depoimentos são de 2023 e 2024.

---

## 7. Spilo (spilo.ai)

É o concorrente mais próximo da ideia de segundo cérebro. É da mesma empresa espanhola que faz a Luzia e foi lançado no Brasil em junho de 2026, ainda em versão beta segundo a imprensa.

**Promessa em uma frase:** guardar qualquer coisa pelo WhatsApp ou pela web e achar depois, quando importar.

**Funções**

- Captura de links, fotos, áudios, PDFs, documentos e anotações, por mensagem no WhatsApp, colando na web ou enviando arquivo.
- Cada item vira um cartão com título, resumo, detalhes e categoria, que o usuário pode editar. A fonte original fica anexada ao cartão.
- Categorização e etiquetas automáticas. A imprensa fala em até 10 categorias.
- Busca por palavra-chave e busca por significado.
- Perguntas em linguagem natural sobre o que foi guardado.
- Lembretes sobre itens salvos, entregues pelo WhatsApp.
- Compartilhamento de itens e de listas por link público, e listas compartilhadas.
- Privado por padrão, com exportação e exclusão de conta e dados.
- Declara, segundo a imprensa, não usar o conteúdo salvo para treinar modelos.
- Site em português, espanhol e inglês.

**Primeiro uso, passo a passo**

1. Não há formulário de cadastro. O usuário clica para começar no WhatsApp ou abre o app web.
2. A conta é criada ao mandar a primeira mensagem ou ao verificar o número. O login usa o número do WhatsApp e um código de 6 dígitos recebido por lá.
3. Envia o primeiro link, foto, documento ou ideia.
4. O Spilo devolve o cartão organizado.
5. Depois, busca ou pergunta em linguagem natural, no WhatsApp ou na web, sobre a mesma biblioteca.

**Canais:** WhatsApp e app web, com a mesma biblioteca nos dois. A imprensa cita também aplicativos para Android e iPhone, que não vi no site.

**Planos e preços:** gratuito. Os termos reservam o direito de criar recursos pagos ou assinatura no futuro, com aviso prévio.

**Elogios e reclamações:** não encontrei avaliações públicas de usuários. A cobertura é de imprensa de lançamento.

**Sinais a notar**

- As páginas do site se contradizem no tom: uma fala em biblioteca pesquisável, outra em interface visual no estilo de mural de imagens.
- Os termos dizem que, em caso de divergência, vale a versão em espanhol.
- O número de WhatsApp é operado por outra empresa do mesmo grupo.

---

## Comparativo rápido

| | Canal principal | Entrada | Preço mensal | Foco |
|---|---|---|---|---|
| Meu Gestor | WhatsApp | Teste de 2 dias sem cartão | R$ 29,99 | Registro e organização |
| Nora | WhatsApp e app iPhone | Convite | Não publicado | Execução de tarefas |
| Spilo | WhatsApp e web | Direto, sem cadastro | Gratuito | Guardar e achar depois |
| Meu Assistente | App e web | Plano gratuito | R$ 19,90 | Vários assistentes por assunto |
| Meu Assessor | WhatsApp, painel e app | Paga antes, garantia de 7 dias | R$ 29,90 em 12 parcelas, só anual | Equipe de personas, finanças e fiscal |
| Lindy | Slack, e-mail e texto | US$ 50 em créditos por 7 dias | A partir de US$ 29,99 por usuário | Trabalho de equipes e agências |
| Martin | SMS, ligação e app iPhone | Teste de 7 dias | US$ 35, ou US$ 21 no anual | Assistente pessoal por voz e texto |

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
12. **Entrada sem cadastro.** No Spilo a primeira mensagem já cria a conta, e o código de 6 dígitos chega pelo próprio WhatsApp. É o primeiro uso mais curto de todos.
13. **Cartão com a fonte anexada.** O Spilo transforma cada captura em cartão editável e mantém o original junto. Isso dá confiança na resposta.
14. **Guardar primeiro, organizar depois.** A captura não exige que o usuário escolha pasta ou categoria.
15. **Página de exemplos de pedidos.** O Meu Assessor mostra cerca de 200 pedidos reais por categoria. Ensina o que dá para pedir melhor que qualquer lista de funções.
16. **Modelos prontos e escolha do jeito de falar.** O Meu Assistente resolve o "não sei por onde começar" com assistentes prontos e três tons de conversa.
17. **Conta compartilhada sem cobrar por pessoa.** No Meu Assessor, família e sócios usam a mesma conta, cada um pelo seu WhatsApp.
18. **Regra clara de aprovação.** Na Lindy, consulta acontece direto e tudo que tem efeito externo espera o sim. É fácil de explicar e de confiar.
19. **Parar em vez de cobrar a mais.** Quando o saldo acaba, a Lindy pausa e avisa.
20. **Pôr o assistente em cópia no e-mail para ele agendar**, como faz o Martin.

## O que nenhum deles faz (pelo que foi possível observar)

O Spilo já cobre a base de um segundo cérebro: captura, cartão com fonte, busca por significado e perguntas sobre o que foi guardado. Então o espaço livre não está em "guardar e achar", e sim no que vem depois.

1. **Memória e ação no mesmo produto.** O Spilo guarda e acha, mas não registra gastos, não cuida da agenda e não executa tarefas. O Meu Assessor é o que chega mais perto, com acervo de arquivos por assunto, mas é um arquivo de documentos, não uma base de ideias e links. Nora, Lindy e Martin executam, mas não são um acervo pessoal. Ninguém junta as três coisas.
2. **Ligações entre itens.** O Spilo organiza por categoria e etiqueta. Nenhum liga uma nota a outra, a pessoas, a projetos ou a decisões.
3. **Revisão periódica do conhecimento.** Há resumo do dia e lembrete por item, mas não revisão semanal de ideias, pendências antigas ou notas esquecidas.
4. **Portabilidade aberta.** Há exportação de dados em dois deles, mas nenhum anuncia formato aberto, como Markdown, nem sincronização com ferramentas de notas.
5. **Memória visível e editável sobre o usuário.** Nenhum mostra uma tela com o que o assistente sabe sobre a pessoa, para corrigir ou apagar item por item.
6. **Execução de tarefas em português, com preço em reais e acesso aberto.** A Nora executa ações, mas não tem preço nem acesso aberto. Lindy e Martin executam, mas são em inglês, cobram em dólar e não usam WhatsApp.
7. **Teste grátis de verdade no segmento pago do WhatsApp.** O Meu Gestor dá 2 dias e o Meu Assessor cobra antes. Nenhum dos dois tem plano gratuito permanente.
8. **Modelo de receita claro para um segundo cérebro.** O único que faz isso é gratuito e ainda não disse como vai cobrar.

Ressalva: li as páginas públicas principais de cada site, não as centrais de ajuda nem as áreas logadas. Alguma dessas lacunas pode estar coberta ali.

## O que evitar

1. **Prometer mais do que o produto faz.** É a queixa central contra o Meu Assessor. O risco cresce com personas e muitas áreas ao mesmo tempo.
2. **Site que se contradiz sobre o estágio do produto**, como ocorre no Meu Gestor, e termos publicados com aviso de rascunho.
3. **Plano anual como única opção, vendido como preço mensal.** O Meu Assessor anuncia o valor da parcela, mas o contrato é de um ano. É a origem dos pedidos de estorno no Reclame Aqui.
4. **Suporte que não responde.** Em produto que mexe com dinheiro e agenda, vira reclamação rapidamente.
5. **Exigir jeito certo de escrever.** O usuário espera linguagem natural, inclusive em parcelas e em mensagens enviadas em sequência.
6. **Ser o único aviso para algo crítico.** Dois concorrentes avisam nos termos que lembretes podem falhar. Vale dizer isso ao usuário no produto, não só no contrato.
7. **Pedir permissões demais de uma vez.** O modelo da Nora depende de acesso amplo a mensagens, e-mail e saúde. Sem confiança construída, isso afasta, e aumenta muito a responsabilidade com dados sensíveis.
8. **Fila de convite longa sem preço.** Cria expectativa, mas impede o usuário de decidir.
9. **Nome genérico.** Há vários produtos chamados "Meu Assistente", "Meu Assessor" e "Nora" em domínios diferentes, o que confunde busca, avaliações e até o Reclame Aqui.
10. **Cobrança por créditos difícil de prever.** Na Lindy uma tarefa pode custar de 2 a 2.500 créditos, e as queixas falam de crédito gasto em resultado errado e de cobrança depois do cancelamento.
11. **Dizer "sem limites" na venda e ter limites nos termos**, como faz o Meu Assessor.
12. **Site com alerta de segurança.** O certificado errado do Meu Assistente espanta o usuário antes do cadastro.
13. **Lançar só para iPhone.** Martin e Nora não têm Android, que é a maioria dos celulares no Brasil.
14. **Competir com o Spilo só em "guardar e achar".** Ele é gratuito, entra sem cadastro e tem por trás uma empresa com dezenas de milhões de usuários, segundo a imprensa. Essa parte precisa existir, mas não sustenta sozinha um produto pago.
15. **Depender de um só canal de terceiros.** Há relatos públicos de números de WhatsApp bloqueados ligados a um dos concorrentes, sem causa confirmada. Ter web ou app como alternativa reduz o risco.

---

## Fontes

Sites coletados diretamente, só páginas públicas:

- meugestoria.com: início, funcionalidades, como funciona, preço, perguntas frequentes, segurança, termos de uso.
- noraai.co: início, planos, privacidade.
- spilo.ai: início, sobre, termos.
- meuassistente.io: início, sobre, termos.
- meuassessor.com: início, como usar, assessores, finanças, agenda, tarefas, documentos, notas fiscais, pesquisas, operação, demonstração, segurança, termos.
- lindy.ai: início, preços, reuniões, segurança, termos.
- trymartin.com: início, preços, ajuda, termos.

Fontes de terceiros:

- [ABC da Comunicação — lançamento da Nora](https://www.abcdacomunicacao.com.br/startup-brasileira-lanca-nora-assistente-pessoal-de-ia-que-resolve-tarefas-pelo-whatsapp/)
- [Guaíra News — Nora no WhatsApp](https://www.guairanews.com/2026/11/06/nora-assistente-pessoal-whatsapp/)
- [Tecnoblog — lançamento do Spilo](https://tecnoblog.net/noticias/criadores-da-luzia-lancam-assistente-de-organizacao-com-ia-no-whatsapp/)
- [TecMundo — lançamento do Spilo](https://www.tecmundo.com.br/software/414188-luzia-lanca-spilo-assistente-de-ia-para-organizar-informacoes-no-whatsapp.htm)
- [Mobile Time — Spilo no WhatsApp](https://www.mobiletime.com.br/noticias/30/06/2026/luzia-spilo-whatsapp/)
- [Reclame Aqui — Meu Assessor](https://www.reclameaqui.com.br/empresa/meu-assessor/)
- [Reclame Aqui — Meu Assessor, lista de reclamações](https://www.reclameaqui.com.br/empresa/meu-assessor/lista-reclamacoes/)
- [Reclame Aqui — segundo perfil, não verificado](https://www.reclameaqui.com.br/empresa/meu-assessor-i-plataforma-via-whatssap/)
- [ZapGastos — comparação com o Meu Assessor (fonte concorrente)](https://zapgastos.com/compare/meu-assessor/)
- [CloudTalk — análise da Lindy](https://www.cloudtalk.io/blog/lindy-ai-review/)
- [Saner.ai — avaliações da Lindy](https://www.saner.ai/blogs/lindy-ai-reviews)
- [Makerstack — análise da Lindy](https://makerstack.co/reviews/lindy-ai-review/)
- [eesel.ai — análise do Martin](https://www.eesel.ai/blog/martin-ai-review)
- [Product Hunt — avaliações do Martin](https://www.producthunt.com/products/martin/reviews)
- [Tool Directory — Martin](https://tooldirectory.ai/tools/martin)
