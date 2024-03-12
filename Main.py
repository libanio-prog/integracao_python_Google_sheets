import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd

lista = [['Lucas', 20], ['Ana', 24], ['José', 34], ['Manuel', 56]]

df_teste = pd.DataFrame(lista=['Nome', 'Idade'])

# Escopo utilizado
scope = ['https://spreadsheets.google.com/feeds']

# Dados de autenticação
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'prencha com o arquivo .json gerado', scope
)

# Autenticando
gc = gspread.authorize(credentials)

# Abrindo a planilha
wks = gc.open_by_key('Coloque aqui o ID da sua planilha')

# Selecionando a primeira página da planilha
worksheet = wks.get_worksheet(0)

# Caso queira relaizar um teste execute a linha de baixo ela vai gravar “Deu Certo” na célula A1 da planilha
# worksheet.update_acell('a1','Deu Certo')

from gspread_dataframe import get_as_dataframe, set_with_dataframe

# Enviando o data frame para a planilha
set_with_dataframe(worksheet, df_teste)
