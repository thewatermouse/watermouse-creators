# -*- coding: utf-8 -*-
"""Gera /guias/ (guias para creators de TikTok LIVE) no site creators.thewatermouse.com.
Uso (na raiz do repo): python -I scripts/guias.py
Reaproveita GTM e cookie banner de index.html. Fatos sobre o TikTok: so das paginas oficiais citadas em cada guia."""
import html, json, pathlib, re, sys, time
sys.stdout.reconfigure(encoding="utf-8")
ROOT = pathlib.Path(__file__).resolve().parent.parent
BASE = "https://creators.thewatermouse.com"
idx = (ROOT / "index.html").read_text(encoding="utf-8")
GTM = idx[idx.index("<!-- Google Tag Manager"):idx.index("</script>", idx.index("<!-- Google Tag Manager")) + 9]
COOKIE = idx[idx.index('<div id="wm-cookie"'):idx.index("</script>", idx.index("function wmCookie")) + 9]
OFF1 = '<a href="https://www.tiktok.com/live/creator-networks/en" target="_blank" rel="noopener">TikTok LIVE Creator Networks (página oficial)</a>'
OFF2 = '<a href="https://www.tiktok.com/live/creator-networks/en/blog/what-is-tiktok-live-backstage" target="_blank" rel="noopener">O que é o TikTok LIVE Backstage (página oficial)</a>'
OFF3 = '<a href="https://www.tiktok.com/live/creator-networks/en/article/product-tools" target="_blank" rel="noopener">Ferramentas do TikTok LIVE Backstage (página oficial)</a>'
NOTA = ('<p class="aviso"><b>Transparência:</b> o Watermouse está formando uma rede de criadores e enviou a candidatura ao programa de Creator Networks do TikTok LIVE. '
        'Enquanto a aprovação não sai, não somos uma Creator Network oficial do TikTok. O TikTok não endossa nem assume responsabilidade pelas atividades de nenhuma rede.</p>')
CTA = ('<div class="cta"><h3>Quer fazer parte da nossa rede de criadores?</h3><p>Entre na lista de interesse. Sem taxa de entrada e sem exclusividade obrigatória, e a gente explica tudo por escrito antes de qualquer compromisso.</p>'
       '<a class="btn" href="/#interesse">Entrar na lista de interesse</a></div>')

GUIAS = [
 dict(slug="o-que-e-agencia-de-tiktok-live", title="O que é uma agência de TikTok LIVE (Creator Network) e o que ela faz",
  desc="Entenda o que o TikTok chama de Creator Network, o que uma agência de LIVE faz de verdade, o que ela não pode prometer e como saber se vale a pena.",
  lede="Agência, rede, \"Creator Network\": os nomes variam, mas a pergunta do criador é a mesma. O que essa empresa faz por mim, e o que muda na minha LIVE?",
  card="O que uma Creator Network faz, o que o TikTok diz oficialmente e o que ele não diz.",
  corpo=f"""<h2>O que o TikTok diz</h2>
<p>Segundo a página oficial do programa, as Creator Networks são parceiras de negócio do TikTok LIVE que conectam criadores a ferramentas, programas e oportunidades de crescimento. Elas ajudam a alcançar e desenvolver criadores, e têm acesso a programas de incentivo e a ferramentas por meio do LIVE Backstage, a plataforma de operação oficial.</p>
<p>O mesmo material faz um aviso importante: as redes são empresas independentes. O TikTok não as endossa nem assume responsabilidade pelas atividades delas. Ou seja, ser uma rede registrada não é o mesmo que ter garantia do TikTok sobre como ela trata o criador.</p>
<h2>O que a rede consegue fazer pela sua LIVE</h2>
<p>Pelo que as páginas oficiais descrevem, uma rede aprovada pode, no LIVE Backstage:</p>
<ul><li>organizar grupos de criadores, atribuir tarefas e acompanhar o engajamento;</li><li>criar e gerenciar agendas de LIVE e acompanhar a participação;</li><li>ver métricas por criador e por equipe, como diamantes e horas ativas;</li><li>participar de campanhas e de eventos com ranking regional;</li><li>acompanhar contratos, bônus mensais e pagamentos;</li><li>distribuir ferramentas de impulsionamento, como flares e cupons Promote, quando o criador é elegível.</li></ul>
<p>Na prática, isso significa apoio de operação: agenda, metas, acompanhamento de desempenho e acesso a programas que não estão abertos ao criador sozinho. O criador individual não acessa o LIVE Backstage por conta própria.</p>
<h2>O que nenhuma agência pode prometer</h2>
<p>Nas páginas oficiais que consultamos, não há promessa de ganho garantido, de audiência ou de quanto você vai receber. Desconfie de quem promete número. O que uma boa rede entrega é método, calendário, análise do que funciona e informação clara sobre o que está no contrato.</p>
<h2>E o custo?</h2>
<p>A página oficial não detalha quanto, nem se, o criador paga ou divide valores com a rede. Por isso, pergunte e peça tudo por escrito antes de aceitar: se há divisão de ganhos, qual é, sobre o quê, como é calculada e quando é paga. Veja o checklist completo em <a href="/guias/checklist-antes-de-aceitar-convite-de-agencia/">o que perguntar antes de aceitar um convite de agência</a>.</p>
{NOTA}""",
  fontes=[OFF1, OFF2, OFF3]),
 dict(slug="como-entrar-numa-agencia-de-tiktok-live", title="Como entrar numa agência de TikTok LIVE: passo a passo e cuidados",
  desc="Como funciona a entrada de um criador numa Creator Network do TikTok LIVE: convite, aceite no app, o que conferir e quando dizer não.",
  lede="Entrar numa rede é uma decisão de negócio, não só um convite no app. Veja como o processo costuma funcionar e o que conferir em cada etapa.",
  card="Convite, aceite no app, o que conferir e quando recusar.",
  corpo=f"""<h2>Como o processo costuma funcionar</h2>
<p>As páginas oficiais explicam o lado da agência: ela se cadastra no LIVE Backstage, envia documentos da empresa e só ganha acesso à plataforma depois da aprovação do TikTok. Sobre o lado do criador, o material oficial é curto. Guias de terceiros descrevem um caminho típico: a rede envia um convite, o TikTok analisa a conta segundo as regras de elegibilidade e o criador aceita o convite no próprio app, em <i>Creator tools</i>, <i>LIVE Center</i>, <i>Creator Network Center</i>. Como esse trecho não vem de documentação oficial e o app muda, confirme no seu aplicativo antes de seguir.</p>
<h2>Antes de aceitar</h2>
<ol><li><b>Peça o contrato por escrito.</b> Condições combinadas só por mensagem não protegem você.</li><li><b>Pergunte como a rede ganha dinheiro.</b> Há divisão de valores? Sobre o quê? Qual o percentual?</li><li><b>Confirme se existe exclusividade e por quanto tempo.</b></li><li><b>Saiba como sair.</b> Qual o aviso prévio, e o que acontece com o que você tem a receber.</li><li><b>Nunca entregue sua senha.</b> O LIVE Backstage atribui acessos à equipe da rede, sem precisar da senha do criador.</li><li><b>Procure a rede por fora.</b> Pesquise o nome e a empresa, converse com criadores que já estão nela e desconfie de quem some quando você pergunta.</li></ol>
<h2>Quando dizer não</h2>
<p>Recuse se a rede pede dinheiro para entrar, promete ganho garantido, pressiona por resposta imediata ou não consegue explicar o que faz. Mais sinais em <a href="/guias/sinais-de-alerta-golpes-agencia-de-live/">sinais de alerta em agências de LIVE</a>.</p>
<h2>E se eu já tenho uma audiência?</h2>
<p>Uma rede é mais útil para quem já faz LIVE com alguma regularidade e quer organização, metas e acesso a programas. Quem está começando pode crescer sozinho primeiro e escolher uma rede depois, sem pressa.</p>
{NOTA}""",
  fontes=[OFF1, OFF2]),
 dict(slug="presentes-e-diamantes-no-tiktok-live", title="Presentes e diamantes no TikTok LIVE: o que se sabe e o que muda",
  desc="Como funciona o caminho dos presentes até o saque no TikTok LIVE, o que é público, o que varia por região e por que desconfiar de tabelas prontas de valores.",
  lede="Moedas, presentes, diamantes, recompensas. Muita gente conta essa história com números que não batem. Este guia separa o que dá para afirmar do que depende do app.",
  card="O caminho presente, diamante e saque, e por que os números variam.",
  corpo=f"""<h2>O caminho do dinheiro, em linhas gerais</h2>
<p>O fluxo descrito por vários guias de mercado é este: o espectador compra moedas, usa as moedas para enviar presentes durante a LIVE e o criador recebe diamantes. Depois, os diamantes podem ser convertidos em valor e sacados, seguindo as regras e os prazos da plataforma.</p>
<h2>Por que não há uma tabela única</h2>
<p>As taxas de conversão e as regras de saque são definidas pelo TikTok, podem mudar e variam conforme a região. É por isso que blogs e agências citam números diferentes para a mesma coisa, e alguns apontam proporções distintas de quanto fica com a plataforma. Nenhuma dessas contas vem de documentação oficial, então trate esses números como referência, nunca como promessa de ganho.</p>
<p>Na dúvida, a fonte certa é o seu próprio aplicativo: o valor que aparece na hora do saque e as regras mostradas na área de recompensas.</p>
<h2>Recompensas de LIVE são outra coisa</h2>
<p>Além dos presentes, existe o programa de recompensas, que calcula valores a partir de missões, como tempo de transmissão, novos seguidores e frequência semanal. O TikTok não publica um valor fixo: a estimativa aparece no app e depende do desempenho e da região.</p>
<h2>O que a rede muda nisso</h2>
<p>Uma Creator Network aprovada acessa, pelo LIVE Backstage, métricas como diamantes e horas ativas, além de bônus mensais e pagamentos. Isso ajuda na gestão, mas não cria dinheiro novo: quem promete multiplicar seus ganhos sem explicar como está vendendo esperança. Para saber como a divisão funcionaria na sua situação, peça a conta por escrito. Veja o <a href="/guias/checklist-antes-de-aceitar-convite-de-agencia/">checklist de perguntas</a>.</p>
<h2>Requisitos para fazer LIVE e receber</h2>
<p>As regras de idade e de número de seguidores também variam e mudam sem aviso. Muitos guias falam em 18 anos e em cerca de 1.000 seguidores, mas há divergência. O que vale é o que o app mostra para a sua conta, em <i>Creator tools</i> ou na central de ajuda do TikTok.</p>
{NOTA}""",
  fontes=[OFF1, OFF2, 'Os fluxos de moedas, presentes e diamantes aparecem em guias de terceiros; as taxas, requisitos e prazos devem ser conferidos no app e na central de ajuda do TikTok.']),
 dict(slug="checklist-antes-de-aceitar-convite-de-agencia", title="Checklist: 12 perguntas antes de aceitar um convite de agência de LIVE",
  desc="Perguntas simples que todo criador deve fazer antes de aceitar um convite de agência de TikTok LIVE: contrato, divisão de valores, exclusividade, saída e pagamento.",
  lede="Convite de agência costuma chegar com pressa e com emoji. Antes de responder, passe por estas 12 perguntas e peça cada resposta por escrito.",
  card="12 perguntas sobre contrato, divisão de valores, exclusividade e saída.",
  corpo=f"""<h2>Sobre o contrato</h2>
<ol><li>Existe contrato escrito? Posso levar um tempo para ler e tirar dúvidas, inclusive com alguém de confiança?</li><li>Qual é o nome completo da empresa e o CNPJ? Ela é uma Creator Network aprovada pelo TikTok?</li><li>Qual a duração e como funciona a renovação?</li></ol>
<h2>Sobre dinheiro</h2>
<ol start="4"><li>A agência fica com alguma parte dos valores que eu gero? Quanto, sobre o quê e como é calculado?</li><li>Quando e como eu recebo? Em que moeda e com que prazo depois do fechamento?</li><li>Há alguma taxa para entrar, treinamento pago ou desconto escondido? (Se houver cobrança para entrar, desconfie.)</li></ol>
<h2>Sobre a sua liberdade</h2>
<ol start="7"><li>Há exclusividade? Posso fechar parcerias com marcas por fora?</li><li>Posso sair quando quiser? Qual o aviso prévio e o que acontece com o que eu tenho a receber?</li><li>Quem controla minha conta? (Você nunca deve entregar a senha.)</li></ol>
<h2>Sobre a rotina</h2>
<ol start="10"><li>O que a agência espera de mim em horas e metas? O que acontece se eu não cumprir?</li><li>Que apoio concreto vou ter: agenda, treinamento, análise de desempenho, atendimento?</li><li>Posso falar com criadores que já estão na rede?</li></ol>
<p>Se alguma resposta vier vaga, atrasada ou com pressão para decidir rápido, trate isso como resposta. Veja também os <a href="/guias/sinais-de-alerta-golpes-agencia-de-live/">sinais de alerta</a>.</p>
{NOTA}""",
  fontes=[OFF1, 'Checklist elaborado pela equipe do Watermouse, com base em boas práticas de contratação; não é aconselhamento jurídico.']),
 dict(slug="sinais-de-alerta-golpes-agencia-de-live", title="Sinais de alerta em agências de TikTok LIVE: como não cair em golpe",
  desc="Seis sinais de que uma agência de LIVE pode ser golpe ou má prática: cobrança para entrar, ganho garantido, pedido de senha, pressa, falta de contrato.",
  lede="Há agências sérias e há quem se aproveite de criadores iniciantes. Estes são os sinais mais comuns de que é melhor recusar.",
  card="Cobrança para entrar, ganho garantido, pedido de senha: seis sinais de alerta.",
  corpo=f"""<h2>Os seis sinais</h2>
<ol><li><b>Pede dinheiro para entrar.</b> Taxa de adesão, \"treinamento\" obrigatório ou compra de presentes para \"subir de nível\" são motivos para sair.</li><li><b>Promete ganho garantido.</b> As páginas oficiais de Creator Networks que consultamos não garantem audiência nem renda. Quem garante está vendendo ilusão.</li><li><b>Pede sua senha.</b> Uma rede aprovada gerencia acessos pelo LIVE Backstage. Não existe motivo para você entregar a senha da conta.</li><li><b>Não tem contrato ou foge das perguntas.</b> Se a conversa só acontece por mensagem e evita escrever as condições, não aceite.</li><li><b>Pressiona por resposta rápida.</b> \"Só hoje\" e \"as vagas acabam\" funcionam para você decidir sem pensar.</li><li><b>Não prova que é uma Creator Network.</b> O acesso ao LIVE Backstage é exclusivo de redes registradas e aprovadas pelo TikTok. Peça o nome da empresa e confira o convite no seu aplicativo.</li></ol>
<h2>O que fazer se isso aconteceu com você</h2>
<p>Guarde as conversas e os comprovantes, pare de pagar, não entregue dados e acesse a central de ajuda do TikTok para denunciar. Se houve prejuízo financeiro, procure um órgão de defesa do consumidor ou um advogado.</p>
<h2>E as agências boas?</h2>
<p>Uma agência séria explica como ganha dinheiro, mostra o contrato, deixa você sair e não vende milagre. Veja o <a href="/guias/checklist-antes-de-aceitar-convite-de-agencia/">checklist de 12 perguntas</a> para comparar propostas.</p>
{NOTA}""",
  fontes=[OFF2, OFF1, 'Sinais elaborados pela equipe do Watermouse com base em práticas comuns de fraude contra criadores; não é aconselhamento jurídico.']),

 dict(slug="rotina-de-lives-no-tiktok-constancia-e-agenda", title="Rotina de LIVEs no TikTok: constância, agenda e o que testar",
  desc="Como montar uma rotina de LIVEs no TikTok: dias e horários fixos, como avisar o público e como testar o que funciona, com o que é dica de mercado e o que é regra do TikTok.",
  lede="Quase todo guia de LIVE repete a mesma palavra: constância. Aqui está o que costuma funcionar na prática e o que é só dica de blog, para você testar com o seu público.",
  card="Dias fixos, aviso na bio e testes de horário: o que é prática comum e o que não é regra.",
  corpo=f"""<h2>Primeiro, uma distinção</h2>
<p>As regras de LIVE (quem pode transmitir, o que é permitido, como funcionam presentes e programas) são definidas pelo TikTok e podem mudar. As dicas abaixo são práticas recomendadas por guias de mercado e redes de criadores. Não vêm da documentação oficial, e o resultado depende do seu nicho e da sua audiência.</p>
<h2>O que costuma ser recomendado</h2>
<ul><li><b>Horário recorrente.</b> Vários guias dizem que o público cria hábito em torno de um horário fixo, como um programa de TV. Escolha dias e horas que você consegue manter.</li><li><b>Comece com uma frequência realista.</b> Alguns guias sugerem começar com duas ou três LIVEs por semana. Outros lembram que não é preciso transmitir todo dia. Melhor poucas LIVEs que você cumpre do que um plano que você abandona na segunda semana.</li><li><b>Avise o público.</b> Colocar os dias e horários na bio é uma recomendação comum.</li><li><b>Teste um horário de cada vez.</b> Mantenha a mesma agenda por algumas semanas antes de julgar. Se for testar outro horário, mude só ele e compare.</li><li><b>Tenha um formato.</b> Abertura, bloco principal e encerramento ajudam quem chega no meio a entender o que está acontecendo.</li></ul>
<h2>O que medir</h2>
<p>Em vez de olhar só o pico de espectadores, observe quanto tempo as pessoas ficam, quantos comentários e novos seguidores cada LIVE traz, e em que momento o público sai. Anote isso depois de cada transmissão e compare semana a semana.</p>
<h2>O que não prometer a si mesmo</h2>
<p>Nenhuma rotina garante audiência nem renda. Uma Creator Network pode ajudar a organizar agenda e metas e a acompanhar números pelo LIVE Backstage, mas o trabalho de criar uma LIVE que as pessoas querem ver continua sendo seu. Veja o que uma rede faz em <a href="/guias/o-que-e-agencia-de-tiktok-live/">o que é uma agência de TikTok LIVE</a>.</p>
{NOTA}""",
  fontes=[OFF1, OFF2, 'As práticas de agenda e frequência vêm de guias de terceiros (redes de criadores, blogs e agências) e não são regras do TikTok. Confira regras e requisitos atuais no aplicativo e na central de ajuda.']),
 dict(slug="batalhas-de-live-no-tiktok-como-funcionam", title="Batalhas de LIVE no TikTok: como funcionam e cuidados",
  desc="O que são as batalhas (partidas) de LIVE do TikTok, como funcionam de forma geral, o que varia entre fontes e cuidados para não pressionar o público.",
  lede="Batalhas dão energia à LIVE, mas também geram dúvidas: como funciona a pontuação, quanto dura e o que pode dar errado. Veja o que os guias descrevem e o que você precisa conferir no app.",
  card="O que são as partidas de LIVE, como a pontuação costuma funcionar e o que confirmar no app.",
  corpo=f"""<h2>O que são</h2>
<p>Guias que descrevem as páginas de ajuda do TikTok explicam que as batalhas aparecem no app como "partidas de LIVE": uma disputa entre criadores em uma LIVE com co-host. Os espectadores apoiam o criador de sua preferência com presentes e curtidas, e quem somar mais pontos ao final vence. Existem formatos individuais e em equipe.</p>
<h2>Como costuma começar</h2>
<p>O caminho descrito é: durante a LIVE, convidar outro criador como co-host e então iniciar a partida pela opção específica. O app pode sugerir criadores para convidar. Os dois criadores precisam estar em LIVE ao mesmo tempo, e as regras de idade para transmitir e receber presentes valem normalmente.</p>
<h2>O que varia entre as fontes</h2>
<p>Muitos guias falam em uma partida de cerca de cinco minutos, em que contam os presentes enviados dentro do tempo. Já o limite de convidados em formatos com várias pessoas aparece com números diferentes. Como as regras mudam, use isso apenas como orientação e confira a duração, a pontuação e os limites atuais no seu aplicativo.</p>
<h2>Cuidados</h2>
<ul><li><b>Não pressione o público.</b> Pedir apoio é normal; insistir, constranger ou prometer o que você não vai cumprir afasta as pessoas e pode ir contra as diretrizes da plataforma. Leia as diretrizes de comunidade do TikTok.</li><li><b>Combine com o parceiro.</b> Defina antes quem entra, quanto tempo dura e como será o fechamento, para a batalha não virar confusão ao vivo.</li><li><b>Preserve a sua LIVE.</b> Uma batalha por dia não substitui conteúdo. Alterne com LIVEs de conversa ou de bastidores.</li><li><b>Desconfie de atalhos.</b> Ninguém pode garantir vitória nem ganho. Veja os <a href="/guias/sinais-de-alerta-golpes-agencia-de-live/">sinais de alerta</a>.</li></ul>
{NOTA}""",
  fontes=[OFF1, OFF2, 'O funcionamento das partidas de LIVE (formato, pontuação, duração e limites) foi descrito a partir de guias de terceiros que resumem as páginas de ajuda do TikTok. As regras mudam: confirme no aplicativo e na central de ajuda oficial.']),
]

CSS = """
:root{--bg:#170A33;--card:#24124D;--line:#3B2670;--tx:#F6F0FF;--mut:rgba(246,240,255,.68);--pk:#FF4FB8;--mint:#C8FF4A;--cy:#8AF3FF;--lav:#B79BFF}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}html{scroll-behavior:smooth}
body{font-family:'Manrope',system-ui,sans-serif;background:var(--bg);color:var(--tx);line-height:1.7;-webkit-font-smoothing:antialiased}
a{color:var(--cy)}nav{position:sticky;top:0;z-index:100;background:rgba(23,10,51,.9);backdrop-filter:blur(12px);border-bottom:1px solid rgba(246,240,255,.07)}
.nav-inner{max-width:900px;margin:0 auto;padding:16px 24px;display:flex;align-items:center;justify-content:space-between;gap:14px}
.logo{display:flex;align-items:center;gap:9px;text-decoration:none;color:var(--tx)!important;font-family:'Unbounded',sans-serif;font-weight:600;font-size:16px;letter-spacing:-.02em}.logo b{font-weight:400;color:var(--cy)}
.navlinks{display:flex;gap:18px;align-items:center;font-size:13px}.navlinks a{color:var(--mut);text-decoration:none}
.btn{display:inline-block;background:var(--pk);color:#170A33!important;font-weight:700;padding:13px 24px;border-radius:999px;text-decoration:none;font-size:15px}.btn:hover{background:var(--mint)}
.wrap{max-width:760px;margin:0 auto;padding:0 24px}
.hero{padding:56px 0 28px}.kicker{font-family:'Martian Mono',monospace;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--lav);margin-bottom:14px}
h1{font-family:'Unbounded',sans-serif;font-weight:700;letter-spacing:-.03em;line-height:1.1;font-size:clamp(28px,5vw,42px);margin-bottom:16px}
.lede{font-size:19px;color:var(--mut);font-weight:300}
article h2{font-family:'Unbounded',sans-serif;font-weight:600;font-size:22px;line-height:1.2;margin:38px 0 12px;letter-spacing:-.02em}
article p,article li{font-size:17px;margin-bottom:14px;color:rgba(246,240,255,.9)}article ul,article ol{padding-left:24px;margin-bottom:14px}
.aviso{border:1px solid var(--line);background:var(--card);border-radius:14px;padding:16px 18px;font-size:14.5px!important;color:var(--mut)!important;margin-top:30px}
.cta{margin:40px 0;padding:28px;border-radius:22px;background:linear-gradient(135deg,#3B2670,#24124D);border:1px solid var(--line)}
.cta h3{font-family:'Unbounded',sans-serif;font-size:20px;margin-bottom:8px}.cta p{color:var(--mut);margin-bottom:16px;font-size:16px}
.src{border-top:1px solid var(--line);margin-top:34px;padding-top:16px;font-size:14px;color:var(--mut)}.src h4{font-size:13px;letter-spacing:.08em;text-transform:uppercase;margin-bottom:8px;font-family:'Martian Mono',monospace}.src li{font-size:14px;margin-bottom:6px}
.grid{display:grid;gap:14px;margin:24px 0 40px}.gc{display:block;background:var(--card);border:1px solid var(--line);border-radius:18px;padding:20px 22px;text-decoration:none;color:var(--tx)}.gc:hover{border-color:var(--pk)}
.gc strong{display:block;font-family:'Unbounded',sans-serif;font-weight:600;font-size:17px;margin-bottom:6px;line-height:1.25}.gc span{color:var(--mut);font-size:15px}
footer{border-top:1px solid rgba(246,240,255,.07);margin-top:50px;padding:26px 0;font-size:13px;color:var(--mut)}footer .wrap{display:flex;flex-wrap:wrap;gap:14px;justify-content:space-between}footer a{color:var(--mut)}
@media(max-width:560px){.navlinks a:not(.btn){display:none}.btn{padding:11px 18px;font-size:14px}}
"""
FONTS = '<link href="https://fonts.googleapis.com/css2?family=Unbounded:wght@300..900&family=Manrope:wght@300..800&family=Martian+Mono:wght@400;600&display=swap" rel="stylesheet">'
LOGO = ('<svg width="30" height="30" viewBox="0 0 40 40" aria-hidden="true"><defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#FF4FB8"/><stop offset="1" stop-color="#7B4DFF"/></linearGradient></defs>'
        '<rect width="40" height="40" rx="14" fill="url(#g)"/><text x="20" y="25.5" text-anchor="middle" font-family="Unbounded, sans-serif" font-weight="800" font-size="13" fill="#F6F0FF">wm</text></svg>')


def shell(path, title, desc, h1, lede, body, kicker="Guia para creators de LIVE", jsonld=None):
    url = BASE + path
    ld = json.dumps(jsonld, ensure_ascii=False) if jsonld else ""
    return f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
{GTM}
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title, quote=False)} | Watermouse Creators</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{url}">
<link rel="icon" type="image/svg+xml" href="/favicon.svg">
<meta property="og:type" content="article"><meta property="og:site_name" content="The Watermouse"><meta property="og:locale" content="pt_BR">
<meta property="og:title" content="{html.escape(title)}"><meta property="og:description" content="{html.escape(desc)}"><meta property="og:url" content="{url}">
<meta property="og:image" content="{BASE}/og-image.png"><meta name="twitter:card" content="summary_large_image">
{('<script type="application/ld+json">' + ld + '</script>') if ld else ''}
{FONTS}
<style>{CSS}</style>
</head>
<body>
<nav><div class="nav-inner"><a class="logo" href="/">{LOGO}<span>watermouse <b>creators</b></span></a>
<div class="navlinks"><a href="/guias/">Guias</a><a href="/marcas.html">É uma marca?</a><a class="btn" href="/#interesse">Quero participar</a></div></div></nav>
<header class="hero"><div class="wrap"><div class="kicker">{kicker}</div><h1>{html.escape(h1)}</h1><p class="lede">{lede}</p></div></header>
<main class="wrap">{body}</main>
<footer><div class="wrap"><span>© 2026 The Watermouse</span><span><a href="https://thewatermouse.com">The Watermouse</a> · <a href="/guias/">Guias</a> · <a href="/marcas.html">Para marcas</a> · <a href="https://thewatermouse.com/privacidade/">Privacidade</a></span></div></footer>
{COOKIE}
</body>
</html>
"""


def write(rel, text):
    f = ROOT / rel; f.parent.mkdir(parents=True, exist_ok=True); f.write_text(text, encoding="utf-8")


def main():
    today = time.strftime("%Y-%m-%d")
    for g in GUIAS:
        assert chr(0x2014) not in json.dumps(g, ensure_ascii=False), g["slug"]
        src = "".join(f"<li>{s}</li>" for s in g["fontes"])
        body = f'<article>{g["corpo"]}{CTA}<div class="src"><h4>Fontes</h4><ul>{src}</ul><p style="font-size:13px;margin-top:10px">Este guia é informativo e não é aconselhamento jurídico ou financeiro. Regras do TikTok mudam: confirme no aplicativo e nas páginas oficiais. Viu algo errado? Escreva para <a href="mailto:digo@thewatermouse.com">digo@thewatermouse.com</a>.</p></div></article>'
        ld = {"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"], "inLanguage": "pt-BR", "datePublished": today, "dateModified": today,
              "mainEntityOfPage": f"{BASE}/guias/{g['slug']}/", "author": {"@type": "Organization", "name": "The Watermouse"}, "publisher": {"@type": "Organization", "name": "The Watermouse", "url": "https://thewatermouse.com/"}}
        write(f"guias/{g['slug']}/index.html", shell(f"/guias/{g['slug']}/", g["title"], g["desc"], g["title"], g["lede"], body, jsonld=ld))
    cards = "".join(f'<a class="gc" href="/guias/{g["slug"]}/"><strong>{html.escape(g["title"])}</strong><span>{html.escape(g["card"])}</span></a>' for g in GUIAS)
    body = f'<div class="grid">{cards}</div>{CTA}'
    write("guias/index.html", shell("/guias/", "Guias para criadores de TikTok LIVE", "Guias em português para criadores de TikTok LIVE: o que é uma agência, como entrar, presentes e diamantes, perguntas antes de aceitar um convite e sinais de alerta.",
                                    "Guias para criadores de TikTok LIVE", "Informação clara, em português, sobre agências, presentes e como proteger o seu trabalho. Só o que dá para sustentar com fontes oficiais.", body, kicker="Watermouse Creators"))
    sm = (ROOT / "sitemap.xml").read_text(encoding="utf-8")
    for p in ["/guias/"] + [f"/guias/{g['slug']}/" for g in GUIAS]:
        if f"<loc>{BASE}{p}</loc>" not in sm:
            sm = sm.replace("</urlset>", f"  <url><loc>{BASE}{p}</loc><lastmod>{today}</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>\n</urlset>")
    (ROOT / "sitemap.xml").write_text(sm, encoding="utf-8")
    print("guias ok:", len(GUIAS))


if __name__ == "__main__":
    main()
