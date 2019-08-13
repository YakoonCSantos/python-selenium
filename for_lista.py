"""lista = []
cont = 1

while cont <= 10:
    lista.append(cont)
    print(lista)
    print()
    cont = cont + 1



quant = int(input("Informe um numero! "))
lista2 = []
i = 1

while i <= quant:
    item = input("item {} : ".format(i))
    lista2.append(item)
    i = i + 1
print("itens informados:")
for item in lista2:
    print(item)
    print()


lista3 = ["João","Pedro","Thiago","Junior"]

quant1 = len(lista3)

print("Itens informados:")
for itens in lista3:
    print(itens)
print("Quantidade de itens( " + str( quant1 ) + ")" )


    if num == "":
    break
    else:
        lista.append(num)
        num = num + num
        controle = controle + 1
print("números informadas ")
for item in lista:
print(item)
print("média dos números é " + str(num / controle))

lista = []
controle = 1

print("Vamos lá!!!") # quebra de linha
while true:
num = input("Informe um numero ou pressione enter, para continuar: ")
if num != "":
    break
else:
    lista.append(num)
    num = num + num
    controle = controle + 1
else:
    print("números informadas ")
    for item in lista:
        print(item)
    print("média dos números é " + str(num / controle))




f = open('c:/temp/teste.txt', 'a')
for i in range(1, 1001):
  f.write(str(i) + '\n')
f.close()


import datetime
hoje = datetime.date.today()
print("Hoje: " + str(hoje)

agora = datetime.datetime.now()
print("hora: " + str(agora))
hora: 2019-07-31 19:39:45.847756



import datetime
data = datetime.datetime.strptime("31/07/2018","%d/%m/%Y")
print(data)

#Faça um programa que lê um arquivo e conta a quantidade de linhas
lista = []
f = open('c:/temp/teste.txt', 'r')
for linha in f:
    lista.append(linha)
    #qtd = len(lista)
print ("Quantidade de linhas: " + str(len(lista)))
f.close()
#Faça um programa que lê um arquivo e conta a quantidade de linhas



#Faça um programa que lê um arquivo e gera outro invertido (a primeira linha é a última)

lista = []
f = open('c:/temp/teste.txt', 'r')
d = open('c:/temp/teste_invertido.txt', 'a')
for linha in f:
    lista.append(int(linha))
    lista.sort(reverse=True)
    #print(lista)
    d.write(str(lista))
f.close()

#outro metodo


lista = []
f = open('c:/temp/Simples_Carga_de_Energia_Dia_Hora_data-8.csv', 'r')
d = open('c:/temp/Simples_Carga_de_Energia_Dia_Hora_data-8_2.csv', 'w')
for linha in f:
    linha = linha.replace(",",";")
    linha = linha.split(';')
    lista.append(linha)
for linha in f:
    d.write(";".join(linha).split())
#qtd = len(lista)
#print ("Quantidade de linhas: " + str(len(lista)))
    print(linha)
f.close()


f = open('c:/temp/Simples_Carga_de_Energia_Dia_Hora_data-8.csv', 'r')
d = open('c:/temp/Simples_Carga_de_Energia_Dia_Hora_data-8_2.csv', 'w')

linhas = list(f)
cabecalho = linhas[0].strip() + ";coluna2\n"
d.write(cabecalho)

for linha in linhas[1:]:
    colunas = linha.split(';')
    ultima_coluna = colunas[-1]
    del colunas[-1]
    del colunas[3]
    valores = ultima_coluna.split(',')
    colunas = colunas + valores
    d.write( ";".join(colunas).strip() + "\n")
    print(linha)

f.close()
d.close()

print("fim")


bd = ["joão","maria","sergio","João"]
bd2 = ["joão","sergio","João","maria"]
c = [(n, l) for n in bd == for l in letras]

#aula 01/08/2019 quinta

#1 Transforme uma lista de números numa lista de textos

#com for (NORMAL)
l = list(range(1,11))
for n in l:
    print(str(n))

#com Comprehensions
l = list(range(1,11))
l2 = [str(n) for n in l]
print(l2)

#2 Crie uma lista de números com valores repetidos e remova-os utilizando um set
l = [1,2,3,3,4,5,6,7,8,8,9,10,10]
my_set = set()
l2 = list(set(l))
print(l2)

""" 
#2 Transforme uma lista de números em uma lista de tuplas com o número, o anterior e o próximo
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
la = [n - 1 for n in l]
lp = [n + 1 for n in l]
lap =  [(origem, anterior, proximo) for origem in l for anterior in la for proximo in lp]
print(l)
print(la)
print(lp)
print(lp)
