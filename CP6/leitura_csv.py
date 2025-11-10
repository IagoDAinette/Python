import csv


def leitura_csv(caminho: str) -> list:
    '''Função para executar a leitura de dados em CSV, 
    convertendo em lista para uso no tratamento'''
    leitura = False
    try:
        with open(caminho, 'r', encoding='utf-8') as arquivo:
            leitor = csv.reader(arquivo, delimiter=',')
            registro_compra = [list(row) for row in leitor]

    except FileNotFoundError:
        print('Arquivo inexistente!\n')
    except Exception as err:
        print(f'Erro na leitura: {err}\n')
    else:
        leitura = True

    if leitura:
        chaves_registro = registro_compra[0]
        lista_registro = []

        # Percorre todas as linhas exceto o cabeçalho
        for i in range(1, len(registro_compra)):
            linha_convertida = []
            for valor in registro_compra[i]:
                linha_convertida.append(int(valor))
            lista_registro.append(linha_convertida)
      
        return [chaves_registro, lista_registro]
    else:
        return []


if __name__ == '__main__':
    import os

    os.system('cls')
    lista_out = leitura_csv('compras.csv')
    print('----> Nomes das colunas:')
    print(lista_out[0])
    print('\n ----> Dados das colunas:')
    for linha in lista_out[1]:
        print(linha)