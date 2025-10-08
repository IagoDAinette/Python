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
#print(listTable)

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
#Função de inserção para a lista ListTable
def addListaDeTable ():
    listaDeTabela.extend([{"Codigo FIPE": "085002", "Marca": "Aston Martin", "Modelo": "Vantage Coupe 4.7 V8", "Combustivel": "Gasolina", "Tipo do Cambio": "Manual", "Tamanho do Motor": 4.7, "Ano": 2016, "Preco Medio R$": 621746.0}])
    #print(listaDeTabela)
#addListaDeTabela()

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
addDicionarioDeTabela()

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

#Função de extração da dicionarioDeTabela
def extractDicionarioTabela():  #deletar ultimo insert
    # Remove os últimos valores
