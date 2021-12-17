import pandas as pd


# Aqui podemos criar algumas funções pra tratar os dados (formato de data, correção de strings e etc)
# Cole sua planilha na pasta planilha
def coletar_dados():
    dir_planilha = "sua_planilha.xlsx"
    sheet_name = "sheet"
    return pd.read_excel("planilha/" + dir_planilha, sheet_name=sheet_name, engine='openpyxl')
