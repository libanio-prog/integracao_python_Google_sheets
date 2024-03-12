# Importanto bibliotecas necessárias
import gspread
import pandas as pd
from gspread_dataframe import get_as_dataframe, set_with_dataframe
from oauth2client.service_account import ServiceAccountCredentials

lista = [['Lucas', 20], ['Ana', 24], ['José', 34], ['Manuel', 56]]

df_teste = pd.DataFrame(lista=['Nome', 'Idade'])

scope = ['https://spreadsheets.google.com/feeds']

# Dados de autenticação
credentials = ServiceAccountCredentials.from_json_keyfile_name(
    'prencha com o arquivo .json gerado', scope
)

gc = gspread.authorize(credentials)

# Abrindo a planilha
wks = gc.open_by_key('Coloque aqui o ID da sua planilha')

worksheet = wks.get_worksheet(0)

column_a_values = worksheet.col_values(1)

# Contar as linhas com células não vazias na coluna A
linhas_com_conteudo_na_coluna_a = sum(1 for cell in column_a_values if cell)

print(
    f'O número de linhas com conteúdo na coluna A é: {linhas_com_conteudo_na_coluna_a}'
)

# Adiciona o DataFrame abaixo da última linha com conteúdo na coluna A
linha_inicio_dataframe = linhas_com_conteudo_na_coluna_a + 1

set_with_dataframe(
    worksheet,
    df_teste,
    row=linha_inicio_dataframe,
    include_index=False,
    include_column_header=False,
)
