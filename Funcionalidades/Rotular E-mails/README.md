## Descrição

ste código utiliza a API do Gmail para listar e rotular e-mails que possuem uma determinada palavra no assunto, e rotulá-los em uma categoria criada especificamente para isso.

O código usa o Python para se autenticar na conta do Gmail, criar uma categoria para armazenar os e-mails com a palavra-chave no assunto e, em seguida, rotular os e-mails correspondentes na categoria recém-criada.

### Como usar
Antes de executar o código, é necessário que você tenha uma conta do Google e habilite a API do Gmail em seu console de desenvolvedor.

Em seguida, você precisará criar um arquivo JSON contendo as suas credenciais de autenticação e token da API do Gmail. As credenciais e o token são necessários para autorizar o acesso do código à sua conta do Gmail. Você pode obter o token acessando a página do console de desenvolvedor do Google.

Depois de configurar suas credenciais e token, você pode executar o código e ele listará os e-mails que contêm a palavra-chave no assunto e rotulá-los na categoria que você criou. Certifique-se de que o ID da categoria criada é fornecido corretamente no código para que os e-mails possam ser rotulados corretamente.

### Bibliotecas Utilizadas

- google-auth
- google-auth-oauthlib
- google-auth-httplib2
- google-api-python-client