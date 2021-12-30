import pandas as pd


# Aqui podemos criar algumas funções pra tratar os dados (formato de data, correção de strings e etc)
# Cole sua planilha na pasta planilha
def coletar_dados():
    dir_planilha = "nome_tabela.xlsx"
    sheet_name = None  # None se tiver apenas uma

    if sheet_name is not None:
        df = pd.read_excel("planilha/" + dir_planilha, sheet_name=sheet_name, engine='openpyxl')
    else:
        df = pd.read_excel("planilha/" + dir_planilha, engine='openpyxl')

    df = df.fillna(0)
    colunas = list(df.columns)

    return [df, colunas]
