import csv
import json

'''DADOS:

Codigo_FIPE   Marca        Modelo                     Combustivel  Cambio_Tipo   Tamanho_Motor  Ano    Preco_Medio_BRL
38001         Acura        NSX 3.0                    Gasoline     manual        3.0            1995   40374.0
60001         Agrále       MARRUÁ 2.8 12V TDI         Diesel       manual        2.8            2006   42102.0
6001          Alfa Romeo   145 Elegant 2.0 16V        Gasoline     manual        2.0            1998   12507.0
37001         AM Gen       Hummer 6.5 4x4 Diesel TB   Diesel       manual        6.5            2000   211478.0
7016          Asia Motors  Topic Carga 2.7 Diesel     Diesel       manual        2.7            1999   15525.0

'''
#1-A.  5/100
listaDeTabela = [
    {"Codigo FIPE": "38001", "Marca": "Acura", "Modelo": "NSX 3.0", "Combustivel": "Gasolina", "Tipo do Cambio": "Manual", "Tamaho do motor": 3.0, "Ano": 1995, "Preco medio R$": 40374.0}, 

    {"Codigo FIPE": "60001", "Marca": "Agrale", "Modelo": "MARRUÁ 2.8 12V TDI", "Combustivel": "Disel", "Tipo do Cambio": "manual", "Tamanho Motor": 2.8, "Ano": 2006, "Preco Medio R$": 42102.0},

    {"Codigo FIPE": "6001", "Marca": "Alfa Romeo", "Modelo": "145 Elegant 2.0 16V", "Combustivel": "Gasolina", "Tipo do Cambio": "manual","Tamanho Motor": 2.0, "Ano": 1998, "Preco Medio R$": 12507.0},

    {"Codigo FIPE": "37001", "Marca": "AM Gen", "Modelo": "Hummer 6.5 4x4 Diesel TB", "Combustivel": "Disel", "Tipo do Cambio": "manual", "Tamanho Motor": 6.5, "Ano": 2000, "Preco Medio R$": 211478.0},

    {"Codigo FIPE": "7016", "Marca": "Asia Motors", "Modelo": "Topic Carga 2.7 Diesel", "Combustivel": "Disel", "Tipo do Cambio": "manual", "Tamanho Motor": 2.7, "Ano": 1999, "Preco Medio R$": 15525.0}
]
print(listaDeTabela)

#1-B.  5/100

dicionarioDeTabela2 = {
    "Codigo FIPE": ["38001", "60001", "6001", "37001", "7016"],
    "Marca": ["Acura", "Agrale", "Alfa Romeo", "AM Gen", "Asia Motors"],
    "Modelo": ["NSX 3.0", "MARRUÁ 2.8 12V TDI", "145 Elegant 2.0 16V", "Hummer 6.5 4x4 Diesel TB", "Topic Carga 2.7 Diesel"],
    "Combustivel": ["Gasoline", "Diesel", "Gasoline", "Diesel", "Diesel"],
    "Tipo de Cambio": ["manual", "manual", "manual", "manual", "manual"],
    "Tamanho do Motor": [3.0, 2.8, 2.0, 6.5, 2.7],
    "Ano": [1995, 2006, 1998, 2000, 1999],
    "Preco medio R$": [40374.0, 42102.0, 12507.0, 211478.0, 15525.0] 
}
print(dicionarioDeTabela2)

#1-C.  10/100
#Função de inserção para a lista listaDeTabela
def addListaDeTabela():
    listaDeTabela.extend([{"Codigo FIPE": "085002", "Marca": "Aston Martin", "Modelo": "Vantage Coupe 4.7 V8", "Combustivel": "Gasolina", "Tipo do Cambio": "Manual", "Tamanho do Motor": 4.7, "Ano": 2016, "Preco Medio R$": 621746.0}])

#Função de inserção para dicionario dicionarioDeTabela2
def addDicionarioDeTabela():
    dicionarioDeTabela2["Codigo FIPE"] =  "38001", "60001", "6001", "37001", "7016", "008001"
    dicionarioDeTabela2["Marca"] = "Acura", "Agrale", "Alfa Romeo", "AM Gen", "Asia Motors", "Audi"
    dicionarioDeTabela2["Modelo"] = "NSX 3.0", "MARRUÁ 2.8 12V TDI", "145 Elegant 2.0 16V", "Hummer 6.5 4x4 Diesel TB", "Topic Carga 2.7 Diesel", "80 2.0"
    dicionarioDeTabela2["Combustivel"] = "Gasoline", "Diesel", "Gasoline", "Diesel", "Diesel", "Gasolina"
    dicionarioDeTabela2["Tipo de Cambio"] = "manual", "manual", "manual", "manual", "manual", "Manual"
    dicionarioDeTabela2["Tamanho do Motor"] = 3.0, 2.8, 2.0, 6.5, 2.7, 2,0
    dicionarioDeTabela2["Ano"] = 1995, 2006, 1998, 2000, 1999, 1995
    dicionarioDeTabela2["Preco Medio R$"] = 40374.0, 42102.0, 12507.0, 211478.0, 15525.0, 13287.0
    print("-"*80)
    print(dicionarioDeTabela2)

#1-D.  10/100
#Função de extração da listaDeTabela
def extractListaTabela():
    del listaDeTabela[5] #Deleta o ultimo insert

    fipeCode = input("Qual o codigo FIPE do veiculo desejado: \n")
    for veiculo in listaDeTabela:  # veiculo é cada dicionário na lista
        if veiculo["Codigo FIPE"] == fipeCode:
            print(f"Veículo encontrado: \n{veiculo}")
            break
        else:
            print("Veículo não encontrado")
            return None  # Retorna None se não encontrar

#1-E.  10/1000 
#Função de extração da dicionarioDeTabela2
def extractDicionarioTabela():  #deletar ultimo insert
    #Restaura o dicionario de listas para o formato original
    dicionarioDeTabela2["Codigo FIPE"] =  "38001", "60001", "6001", "37001", "7016"
    dicionarioDeTabela2["Marca"] = "Acura", "Agrale", "Alfa Romeo", "AM Gen", "Asia Motors",
    dicionarioDeTabela2["Modelo"] = "NSX 3.0", "MARRUÁ 2.8 12V TDI", "145 Elegant 2.0 16V", "Hummer 6.5 4x4 Diesel TB", "Topic Carga 2.7 Diesel", 
    dicionarioDeTabela2["Combustivel"] = "Gasoline", "Diesel", "Gasoline", "Diesel", "Diesel"
    dicionarioDeTabela2["Tipo de Cambio"] = "manual", "manual", "manual", "manual", "manual"
    dicionarioDeTabela2["Tamanho do Motor"] = 3.0, 2.8, 2.0, 6.5, 2.7
    dicionarioDeTabela2["Ano"] = 1995, 2006, 1998, 2000, 1999
    dicionarioDeTabela2["Preco Medio R$"] = 40374.0, 42102.0, 12507.0, 211478.0, 15525.0

    fipeCode = input("Qual o codigo FIPE do veiculo desejado: ")
    
    # Encontra o índice do código FIPE na lista
    if fipeCode in dicionarioDeTabela2["Codigo FIPE"]:
        indice = dicionarioDeTabela2["Codigo FIPE"].index(fipeCode)
        
        # Extrai todos os dados do veículo nesse índice
        veiculoEncontrado = {}
        for chave in dicionarioDeTabela2:
            veiculoEncontrado[chave] = dicionarioDeTabela2[chave][indice]
        
        print("\n Veiculo Encontrado")
        for chave, valor in veiculoEncontrado.items():
            print(f"{chave}: {valor}")
        
        return veiculoEncontrado #pq o print acima não retorna os valores e sim o return? o Return é de retornar a um local ou de devolver algum comando?
    else:
        print(f"\n Veículo com código FIPE '{fipeCode}' não encontrado")
        return None #Como funciona o return

#2 - 10/100
def txt():
    try:
        arquivotxt = open("veiculos_fipe.txt", "x", encoding="utf-8")
    
    except FileExistsError:
        print("Erro: O arquivo 'veiculos_fipe.txt' já existe!") # Se o arquivo existir retorna a mensagem de erro
        return None
    
    else:
        try:
            for chave, valores in dicionarioDeTabela2.items():# Escreve os dados no arquivo
                arquivotxt.write(f"{chave}: {valores}\n")
            print("Dados salvos com sucesso em 'veiculos_fipe.txt'!")
        
        except Exception as e:
            print(f"Erro durante a escrita: {e}") # Verifica se tem algum outro erro
        
        finally:
            arquivotxt.close() # FECHA o arquivo
            print("Arquivo fechado.")
    
    finally:
        print("Operação de salvamento finalizada.") # Executa SEMPRE, independente de erros
txt()

#3 - 20/100
def arquivoCsv():
    try:
        with open("veiculos_fipe.csv", "x", newline="", encoding="utf-8") as arquivoCsv:
            
            escritorCsv = csv.writer(arquivoCsv) #Cria o arquivo CSV
                        
            chaves = list(dicionarioDeTabela2.keys()) #Escreve o cabeçalho
            escritorCsv.writerow(chaves)
            print("Cabeçalho escrito com sucesso!")
            
            numeroDeVeiculos = len(dicionarioDeTabela2["Codigo FIPE"]) #ESCREVE os dados de cada veículo
            
            for indice in range(numeroDeVeiculos): #Cria uma linha com todos os dados do veículo no índice atual
                linhaVeiculo = []
                for chave in chaves:
                    linhaVeiculo.append(dicionarioDeTabela2[chave][indice])
                
                escritorCsv.writerow(linhaVeiculo) # Escreve a linha no arquivo CSV
            
            print(f"Dados de {numeroDeVeiculos} veículos salvos em 'veiculos_fipe.csv'!")
    
    except FileExistsError:
        print("Erro: O arquivo 'veiculos_fipe.csv' já existe!")
        return None
    
    except Exception as erro:
        print(f"Erro durante a operação CSV: {erro}")
    
    finally:
        print("Operação de salvamento CSV finalizada.")
arquivoCsv()

#4 - 20/100
def arquivoJson():
    try:
        dadosJson = json.dumps(  #Converte o dicionário para string JSON formatada
            dicionarioDeTabela2,
            ensure_ascii=False,  #Permite caracteres especiais (acentos)
            indent=4,            #Formata com 4 espaços de identação
            sort_keys=False      #Mantém a ordem original das chaves
        )
        print("Dados convertidos para JSON com sucesso!")
        
        with open("veiculos_fipe.json", "x", encoding="utf-8") as arquivoJson: #Salva a string JSON no arquivo usando with open()
            arquivoJson.write(dadosJson)
            print("Dados salvos em 'veiculos_fipe.json'!")
    
    except FileExistsError:

        print("Erro: O arquivo 'veiculos_fipe.json' já existe!")
        return None
    
    except Exception as erro:
        print(f"Erro durante a operação JSON: {erro}")
    
    finally:
        print("Operação de salvamento JSON finalizada.")
arquivoJson()