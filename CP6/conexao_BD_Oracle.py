#!/usr/bin/env python
# coding: utf-8

import cx_Oracle
from user_data import user_, pass_

host_ = 'oracle.fiap.com.br'
port_ = '1521'
SID_ = 'orcl'

def CRUD_Connect(user_ID, user_pass, host=host_, port=port_, SID=SID_, only_test=False):
    try:
        cx_Oracle.init_oracle_client(lib_dir=r"C:\Program Files\instantclient_23_9")
    except Exception as e:
        print("Erro na inicialização do 'client': ", e)
    else:
        print('Inicializado com sucesso!!!\n')

    # Conecta o servidor
    dsn_string = cx_Oracle.makedsn(host, port, SID)

    try:
        print("Fazendo conexão com o banco...\n")
        # Efetua a conexão com o Usuário
        connection = cx_Oracle.connect(
            user=user_ID, 
            password=user_pass,
            dsn=dsn_string,
            encoding="UTF-8"
        )

    except Exception as e:
        # Informa o erro
        print("Erro: ", e)
        # Flag para não executar a Aplicação
        conection_flag = False
        return False, False, False, False, False, conection_flag

    else:
        # Flag para executar a Aplicação
        conection_flag = True

        try:
            # Cria as instruções para cada módulo
            print("Criando cursores...\n")
            inst_cadastro = connection.cursor()
            inst_consulta = connection.cursor()
            inst_alteracao = connection.cursor()
            inst_exclusao = connection.cursor()

        except Exception as err:
            print(f'Houve uma falha na conexao {err}!\n')
            print('Não foi possível criar os cursores do BD!')
            return False, False, False, False, False, conection_flag
        
        else:
            print('Conectado com sucesso!!!')
            if only_test:
                connection.close()
                print('A Conexão apenas para teste foi encerrada com sucesso!')
            
            return inst_cadastro, inst_consulta, inst_alteracao, inst_exclusao, connection, conection_flag
    

if __name__ == "__main__":
    lista = CRUD_Connect(user_, pass_, host=host_, port=port_, SID=SID_, only_test=True)
    print(f'A conexão é {lista[-1]}')
    print(lista[0])