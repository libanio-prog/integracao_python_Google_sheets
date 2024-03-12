# Documentação Técnica

## Objetivo
O objetivo deste código é automatizar a atualização de dados de um DataFrame para uma planilha do Google Sheets. O script principal (`Main.py`) envia o DataFrame diretamente para a planilha, enquanto o script de preenchimento incremental (`preenchimento_incremental.py`) adiciona novos dados abaixo da última linha preenchida na coluna A.

## Dependências Externas
- [gspread](https://github.com/burnash/gspread): Biblioteca para interagir com o Google Sheets.
- [pandas](https://pandas.pydata.org/): Biblioteca para manipulação e análise de dados.
- [oauth2client](https://github.com/googleapis/oauth2client): Biblioteca para autenticação OAuth 2.0.
- [gspread_dataframe](https://github.com/robin900/gspread-dataframe): Biblioteca para integração entre pandas DataFrame e Google Sheets.

## Variáveis de Ambiente
- `credentials.json`: Arquivo JSON contendo as credenciais de autenticação para acessar a API do Google Sheets.
- ID da Planilha: Identificação única da planilha no Google Sheets.

## Como Usar
1. Certifique-se de ter instalado todas as dependências externas listadas acima.
2. Adquira as credenciais de autenticação do Google Sheets em formato JSON e salve como `credentials.json` no mesmo diretório que os scripts.
3. Crie uma nova planilha no Google Sheets e obtenha o seu ID.
4. Cole o ID da planilha no local indicado nos scripts (`'Coloque aqui o ID da sua planilha'`).
5. Execute o script principal (`Main.py`) para enviar o DataFrame para a planilha, ou o script de preenchimento incremental (`preenchimento_incremental.py`) para adicionar novos dados.
6. obtendo credenciais Primeiro, você precisará acessar o Console do Google. No seguinte https://console.developers.google.com/project, crie um Novo Projeto. Dê um nome que desejar.
    Na seção Biblioteca, à esquerda, pesquise por "Google Sheets API" e clique em ativar.
    Agora, vamos criar chaves e credenciais. Clique nos três pontos no canto superior esquerdo, depois em "APIs e Serviços" e "Credenciais". Selecione a opção Chave de conta de serviço, preenchendo o nome da conta. Em seguida, conceda acesso ao projeto, selecionando "Projeto" e "Proprietário". Clique em concluir.
    Para criar as chaves de acesso clique em "Adicionar Chave" e selecione a conta de serviço, uma nova chave JSON será criada e um arquivo será baixado em seu computador. Guarde esse arquivo.
    Agora, crie uma nova planilha dentro do Google Sheets e abra o arquivo JSON baixado. Copie o dado chamado "e-mail do cliente". Na planilha, vá em compartilhar e cole esse e-mail no campo endereço e de permissão e edição.
   

## Fluxo de Execução
1. Importação das bibliotecas necessárias.
2. Criação do DataFrame com os dados desejados.
3. Autenticação utilizando as credenciais do Google Sheets.
4. Abertura da planilha especificada.
5. Envio do DataFrame para a planilha utilizando a função `set_with_dataframe`.
6. (Opcional) No script `preenchimento_incremental.py`, os novos dados são adicionados abaixo da última linha preenchida na coluna A.

## Saída
- No script principal (`Main.py`), o DataFrame é enviado diretamente para a planilha especificada.
- No script de preenchimento incremental (`preenchimento_incremental.py`), os novos dados são adicionados abaixo da última linha preenchida na coluna A.

## Contribuições
Contribuições são bem-vindas! Se você encontrar problemas ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue ou enviar um pull request neste repositório.



