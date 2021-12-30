import os

import numpy as np
import pyodbc
import pandas as pd
from datetime import datetime, date

# coloca aqui o nome da tabela
tabela = "nome_tabela"


# classe de acesso ao bd
class BD:

    def __init__(self, colunas):
        # preenche com os dados do BD
        server = 'seu_server'
        database = 'database'
        username = 'username'
        password = 'password'

        # aqui é para o caso do BD ser SQL Server, mas pode ser outro, só trocar
        self.connection = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
        self.cursor = self.connection.cursor()
        self.colunas = colunas

    # valida se a linha já existe no BD
    # Previne duplicação de dados
    def validacao(self, linha):
        inserir = True
        colunas = self.colunas
        cursor = self.cursor
        sql = "SELECT 1 FROM " + tabela + " WHERE "

        # montando a query
        for coluna in colunas:
            # primeira condição tem "AND" na frente, só as outras
            if coluna != colunas[0]:
                sql += "AND "

            if linha[coluna] is None:
                sql += coluna + " IS NULL "
            else:
                sql += coluna + " = '" + str(linha[coluna]) + "' "

        row = cursor.execute(sql)

        # se a consulta retornar dados então é por que eles já existem no BD, logo não deverão ser inseridos
        while row.fetchone():
            inserir = False

        return inserir

    # Inserindo dados no BD
    def inserir(self, linha):
        colunas = self.colunas
        cursor = self.cursor
        connection = self.connection

        sql = "INSERT INTO " + tabela + " ("

        # montando a query
        for coluna in colunas:
            if coluna != colunas[(len(colunas) - 1)]:
                sql += coluna + ", "
            else:
                sql += coluna

        sql += ") VALUES ("

        for coluna in colunas:
            # se não for a última coluna
            if coluna != colunas[(len(colunas) - 1)]:
                if linha[coluna] is None:
                    sql += "NULL,"
                else:
                    sql += "'" + str(linha[coluna]) + "',"
            else:
                if linha[coluna] is None:
                    sql += "NULL)"
                else:
                    sql += "'" + str(linha[coluna]) + "')"

        cursor.execute(sql)
        connection.commit()
