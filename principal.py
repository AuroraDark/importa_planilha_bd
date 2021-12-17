import coleta_planilha
from conexaoBD import BD
import pandas

# Coleta os dados
bd = BD()
df_dados = coleta_planilha.coletar_dados()
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

