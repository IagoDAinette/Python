#!/usr/bin/env python
# coding: utf-8

import json


def leitura_json(caminho: str) -> list:
    #Função para executar a leitura de dados em JSON, converte em lista para uso no tratamento
    leitura = False

    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            dicionario_json = json.load(arquivo)

    except FileNotFoundError:
        print('Arquivo inexistente\n')
    except Exception as err:
        print(f'Erro na leitura: {err}\n')
    else:
        leitura = True

    if leitura:
        chaves_json = list(dicionario_json.keys())
        valores_json = list(dicionario_json.values())

        lista_registro = valores_json.copy()

        # Inserindo o ID como primeiro elemento de cada lista
        for i in range(len(lista_registro)):
            lista_registro[i].insert(0, int(chaves_json[i]))

        lista_produtos = ['ID_Compra', 'Pão Francês', 'Bolo de Milho', 'Bolo de Fubá',
                          'Pão de Queijo', 'Leite', 'Manteiga', 'Margarina', 'Água', 'Refrigerante']

        return [lista_produtos, lista_registro]
    else:
        return []

    
if __name__ == '__main__':
    import os

    os.system('cls')
    lista_out = leitura_json('compras_novos.json')
   
    print('----> Nomes das colunas:')
    print(lista_out[0])
    print('\n ----> Dados das colunas:')
    for linha in lista_out[1]:
        print(linha)