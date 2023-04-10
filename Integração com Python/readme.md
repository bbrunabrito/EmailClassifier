Na task 5 gostaria de esclarecer que o leitor verá sobre:
    Parte 1:
        a. Como criar um ambiente virtual (caso necessário)
        b. Procedimento para fazer a primeira conexão do Python com o Gmail.
    Parte 2:
        a. Procedimento para fazer a primeira interação com o Gmail utilizando o Python (leitura de emails não lidos)

Para este "readme", gostaria de aprofundar sobre o propósito e aprendizados em relação a Task 5.

O objetivo da pesquisa (e de colocá-la em prática) foi: compreender, por mais que inicialmente, as vantagens e limitações ao utilizar a API do Gmail com o Python comparado a outras formas de conectar com o GMail (considerando que o foco para essa Task foi singularmente a integração da API do Gmail com Python).

Ao longo da pesquisa, percebi que existem alguns modos distintos de lidar com a conexão com o Gmail.

1. Trabalhar com o Apps Script (que é uma plataforma online para diferentes aplicativos do Google Workspace, exige Javascript)
2. Trabalhar com Python enquanto tem acesso a funções do Apps Script. (https://developers.google.com/apps-script/api/how-tos/execute?hl=pt-br#python)
(também por meio do Execution API, que lida com o Apps Script como se este fosse uma API -- essa forma parece ser mais adequada pra situações que o projeto é uma aplicação paralela fora do Google, cheque aqui pra mais informações: https://developers.googleblog.com/2015/09/run-apps-script-code-from-anywhere.html)
3. Trabalhar com a API do Gmail (que é uma API REST, o que indica que podemos trabalhar com api por meio de diferentes linguagens)
4. Trabalhar com IMAP/SMTP protocols (usando Python) acessando o Gmail.

A documentações sobre o Apps Script parecem ser mais compreensiveis (sem contar com o fato de que é uma documentação mais moderna, é natural que seja necessário um grau de organização maior da documentação de uma ferramenta quando essa ferramenta lida com diferentes aplicativos que possuem funcionalidades completamente distintas i.e., Google Workspace).

APIs individuais do Google como "Gmail API" são mais focadas em prover acesso a dados, e podem ser mais convenientes/apropriadas caso não haja necessidade de editar dados.

Protocolos IMAP/SMTP possuem documentação menos compreensiva, e utilizar essas ferramentas é um acesso "menos direto" ao Gmail (caso comparado a utilizar Apps Script ou Gmail API), e a verdade é que os dois sistemas não possuem "match" porque nenhum dos dois foi projetado com objetivo principal de integrar o outro.
Em compensação, IMAP/SMTP são mais gerais e podem lidar com diferentes tipos de emails, não apenas gmail (e.g. yahoo, outlook, hotmail, etc).

Trabalhar com ferramentas que se conectam diretamente ao GMail é um processo mais seguro devido ao uso do OAuth (Open authentication).
Usar OAuth é uma forma de pedir autorização de acesso apenas ao que será necessário para uma solução.
IMAP/SMTP, por padrão, utiliza autorização de acesso geral. Ou tem acesso a conta inteira do usuário, ou não tem acesso a nada.
De qualquer forma, existe uma documentação que informa a existência de uma maneira de utilizar OAuth com o SMTP (https://developers.google.com/gmail/imap/imap-smtp), mas ainda assim o OAuth não foi projetado de início para suportar IMAP/SMTP, ou melhor, essa possibilidade a mais trata-se de uma otimização do OAuth, sem contar que o sistema desenvolvido pela Google funciona de forma distinta do sistema IMAP/SMTP.

IMAP/SMTP lida com uma noção de "mailbox", i.e., o procedimento de enquadrar emails em uma caixa só.
Gmail API trabalha com labels como se cada label fosse uma pasta de emails (mais fácil de acompanhar e de acessar).
Entretanto, existem sim formas de lidar com Labels do Gmail com o IMAP/SMTP, ainda assim é por meio de extensões que não são padronizadas do IMAP/SMTP.

Protocolo IMAP: https://www.rfc-editor.org/rfc/rfc3501
GMail API: https://developers.google.com/gmail/api/
https://stackoverflow.com/questions/25431022/what-makes-the-gmail-api-more-efficient-than-imap
A API do gmail tem suporte embutido (https://developers.google.com/gmail/api/guides/sync) para sincronizar a aplicação (client) com o gmail, incluindo a sincronia com quaisquer atualizações que ocorram (e.g., acabou de receber um email, sincronia permite atualização constante). Garantir essa sincronia com IMAP/SMTP é mais complexo (cheque: https://www.ietf.org/rfc/rfc4549.txt)

Procurar por messagens/threads usando a API do Gmail (https://developers.google.com/gmail/api/guides/filtering) parece ser mais poderoso do que a forma que o IMAP/SMTP lida com isso (https://www.rfc-editor.org/rfc/rfc3501#section-6.4.4)

https://www.gmass.co/blog/gmail-api-vs-imap/#:~:text=The%20advantages%20of%20using%20an,Better%20security
A API do Gmail oferece mais segurança, em geral é mais eficiente que a IMAP/SMTP, e também oferece mais flexibilidade.
Adicionalmente, a API do Gmail entrega melhor performance caso comparada ao IMAP/SMTP.
"Conexões do IMAP com o Gmail" e "conexões diretas com o gmail" fornecem um sistema de batching para requests (https://developers.google.com/gmail/api/guides/batch). Cada conexão HTTP que a aplicação tem que fazer resulta em uma quantidade de requests.
As vezes é necessário fazer muitas conexões HTTP de uma vez só, o que pode estourar o limite de requests diário facilmente (como por exemplo quando você está iniciando com a ferramenta e tem muitos dados para fazer upload).
Não queremos ter nenhum "problema"/empecilho com o GMail, portanto
1- pode ser interessante trabalhar com batches. Você seleciona um conjunto de requests pra acontecer em um batch request. Assim você consegue controlar a quantidade de requests a cada conexão HTTP que você faz.
2- pode ser interessante trabalhar com um email pra testes caso vá mexer com batches ao invés de ficar usando um email consideravelmente "importante" (e.g. email profissional, empresarial ou institucional).


https://stackoverflow.com/questions/9205590/can-you-use-google-apps-script-with-python

Apps Script funciona como uma plataforma online para trabalhar com aplicativos do Google Workspace (o que inclui o nosso foco: Gmail).
Não há necessidade de instalar nada para trabalhar com o Apps Script.
Tudo que é codado no Apps Script é executado nos servidores da Google.

Aparentemente, trabalhar com a API do Gmail usando Python gera a possibilidade de requestar funções do Apps Script em um momento oportuno (caso necessário), sendo requisito apenas o desenvolvimento de uma maior noção com o uso de JavaScript (caso esteja em falta).

Apps Script também é mais geral, mas no sentido de trabalhar com diferentes aplicativos da Google, sendo que cada um possui um propósito diferente.
Isso não muda o fato de que o uso do Apps Script pode ser direcionado e focado em um único aplicativo em individual (e.g. uso direcionado ao Gmail).

De acordo com as pesquisas, não há diferenças comprometedoras para o nosso objetivo ao usar o Apps Script ou usar a API do Gmail, sem contar que os dois são versionados e administrados pela mesma empresa.
A diferença relevante é o fato do Apps Script poder integrar os aplicativos do workspace da Google em um mesmo ambiente. Porém, esse ambiente trabalha restritamente com JavaScript.
Enquanto usar a API do Gmail permite trabalhar com diferentes linguagens (o que podemos direcionar para o uso de Python), enquanto por meio de ferramentas distintas podemos ter acesso as funções do Apps Script enquanto lidamos com a API do Gmail (o que exigirá uma noção de JavaScript, mas não tão um entendimento de maior profundidade como quando é necessário trabalhar com o ambiente do Apps Script em si).
