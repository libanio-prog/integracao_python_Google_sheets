Um belo dia eu estava com o seguinte problema: eu tinha um dataframe que era atualizado diariamente e precisava envia-lo a uma planilha do Google Sheets.

Primeiro, você precisará acessar o Console do Google. No seguinte https://console.developers.google.com/project, crie um Novo Projeto. Dê um nome que desejar. 

Na seção Biblioteca, à esquerda, pesquise por "Google Sheets API" e clique em ativar.
Agora, vamos criar chaves e credenciais. Clique nos três pontos no canto superior esquerdo, depois em "APIs e Serviços" e "Credenciais". Selecione a opção Chave de conta de serviço, preenchendo o nome da conta. Em seguida, conceda acesso ao projeto, selecionando "Projeto" e "Proprietário". Clique em concluir.

Para criar as chaves de acesso clique em "Adicionar Chave" e selecione a conta de serviço, uma nova chave JSON será criada e um arquivo será baixado em seu computador. Guarde esse arquivo.

Agora, crie uma nova planilha dentro do Google Sheets e abra o arquivo JSON baixado. Copie o dado chamado "e-mail do cliente". Na planilha, vá em compartilhar e cole esse e-mail no campo endereço e de permissão e edição.
Vamos para o código!

Antes de iniciar você deve instalar as seguintes bibliotecas.
Biblioteca para gravar data frame no google sheets 

* `pip install gspread-dataframe`

Documentação https://github.com/robin900/gspread-dataframe

Biblioteca que auxilia na manipulação do documento 

* `pip install gspread oauth2client`

Documentação https://docs.gspread.org/en/latest/



No arquivo main.ipynb, o data frame será gravado na planilha. 
Explicando os detalhes: 
Os dados de autenticação são obtidos do arquivo JSON que você baixou, deve estar no mesmo diretório que contém seu código, detalhe importante altere o nome dele para credentials.json. Na variável "wks", onde está escrito o "id da planilha", você deve preencher com o ID da sua planilha. Para encontrá-lo, acesse sua planilha e na barra de endereço, ele estará entre os caracteres "d/" e "/edit".

Neste exemplo citado acima os dados da planilha serão subscritos, se o seu caso for atualizar a planilha, mas os novos dados devem ser adicionados abaixo da última linha com conteúdo, você pode usar o seguinte arquivo preenchimento_incremental.ipynb
