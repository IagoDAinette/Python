# Exercício 1

Tabelas de memória são importantes, e seu uso é fundamental para trabalhar com os dados inseridos nas operações 
executadas dentro da solução em desenvolvimento, e neste contexto:


DADOS:

Codigo_FIPE   Marca        Modelo                     Combustivel  Cambio_Tipo   Tamanho_Motor  Ano    Preco_Medio_BRL
38001         Acura        NSX 3.0                    Gasoline     manual        3.0            1995   40374.0
60001         Agrále       MARRUÁ 2.8 12V TDI         Diesel       manual        2.8            2006   42102.0
6001          Alfa Romeo   145 Elegant 2.0 16V        Gasoline     manual        2.0            1998   12507.0
37001         AM Gen       Hummer 6.5 4x4 Diesel TB   Diesel       manual        6.5            2000   211478.0
7016          Asia Motors  Topic Carga 2.7 Diesel     Diesel       manual        2.7            1999   15525.0



## 1-A Use os dados fornecidos acima para construir uma lista de dicionários (5 Pontos): 


lista_tabela_1 = [
    dicionário_1{}, 
    dicionário_2{},
    ..., 
    dicionário_n{}]

* Lembre-se que dicionários devem sempre conter informações com 'chave':'valor'!!!




## 1-B Agora vamos inverter as informações acima para o formato dicionário com chave e lista de valores (5 Pontos):

dicionário_tabela_2 = dicionário{
    'chave_característica_1': lista de valores_1[], 
    'chave_característica_2': lista de valores_2[],
    ...,
    'chave_característica_m': lista de valores_m[]}




## 1-C Desenvolva duas funções que façam a 'inserção' de um novo veículo em ambas as tabelas 
(uma para a primeira e uma para a segunda) (10 pontos):

Par isso utilize os dados abaixo:

Adicione o seguinte veículo na 'lista_tabela_1', e execute!

Codigo_FIPE  Marca         Modelo                 Combustivel   Cambio_Tipo  Tamanho_Motor  Ano    Preco_Medio_BRL
085002       Aston Martin  Vantage Coupe 4.7 V8   Gasoline      manual       4.7            2016   621746.0


Adicione este no 'dicionário_tabela_2', e execute!

Codigo_FIPE  Marca        Modelo                   Combustivel   Cambio_Tipo  Tamanho_Motor  Ano    Preco_Medio_BRL
008001       Audi         80 2.0                   Gasoline      manual       2.0            1995   13287.0




## 1-D Desenvolva duas funções que façam a 'extração' de um veículo em ambas as tabelas 
(uma para a primeira e uma para a segunda) utilizando o 'Codigo_FIPE' (10 pontos):

Elimine os veículos adicionados no item '1-C' em ambas as tabelas!


------------------------------------------------------------------------------------------------------------------------------------------------


# Exercício 2 - 10 Pontos

Usando a função 'open()', salve os dados do 'dicionário_tabela_2' criado acima em um arquivo '.txt'!

name_... = open () ....

!!!!Utilize o argumento 'x' para não sobrescrever os dados que já existem!!!!! 


!!!Utilize o try:, except:, else:, finaly: para mostrar o erro ao invés de deixar o programa 'falhar' na execução 
(caso exista o arquivo)!!!


!!!Não esqueça o arquivo aberto!!!


------------------------------------------------------------------------------------------------------------------------------------------------



# Exercício 3 - 20 Pontos

Usando  a função 'open()' e a variável de contexto 'with' salve o 'dicionário_tabela_2' em um arquivo ',csv'!

with open()....


!!!USE import csv!!!


!!!!Utilize o argumento 'x' para não sobrescrever os dados que já existem!!!!! 


!!!Utilize o try:, except:, else:, finaly: para mostrar o erro ao invés de deixar o programa 'falhar' na execução 
(caso exista o arquivo)!


!!!Aqui, salve na primeira linha as chaves, e nas outras os dados de cada veículo (1 por linha)!!!





------------------------------------------------------------------------------------------------------------------------------------------------


# Exercício 4 - 20 Pontos


Usando a bilbioteca 'json' faça primeiramente um 'dumps' do 'dicionário_tabela_2', em uma variável e depois com 'open' 
salve o arquivo no disco!!

!!!USE import json!!!

!!!Faça o dump com ignorar 'ascii'' e identação de 4!!!

!!!Grave usando 'with open()', ou 'open()' lembrando forçar o 'encoding' para 'utf-8'!!!



# Vídeo Explicativo - 20 Pontos

Faça um vídeo explicando o funcionamento de cada um dos exercícios, com a sua própria voz, 
com no máximo 5 minutos. Dê uma rápida introdução dos enunciados, e explique cada exercício e seu funcionamento. 
