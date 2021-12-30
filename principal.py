import coleta_planilha
from conexaoBD import BD
import pandas

# Coleta os dados
dados = coleta_planilha.coletar_dados()
df_dados = dados[0]
bd = BD(colunas=dados[1])

linhasInseridas = 0

# Valida e insere cada linha
for index, linha in df_dados.iterrows():
    if bd.validacao(linha):
        bd.inserir(linha)
        linhasInseridas += 1

print("=========================================\n")
print("Planilha importada com sucesso!")
print("Linhas inseridas: " + str(linhasInseridas) + "\n")
print("=========================================")

