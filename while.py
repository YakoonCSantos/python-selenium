"""
print("vamos lá")

n1 = int(input("Informe um número! "))
print("")

while n1 >= 0:
    if n1 % 2 == 0:
        print (str(n1) + " número e par")
    else: 
        print (str(n1) + " número e impar")
    n1 = n1 - 1
print("")
print("tá fluindo")

 
login = input("Informe o usuário!" )
senha = input("Informe a senha!" )

while login != "python" and senha != "python132":
    print("Login e Senha incorreta, tente novamente!")
    login = input("Informe o usuário!" )
    senha = input("Informe a senha!" )
print("Login e Senha correta, Vamos Lá!")
"""


print("Vamos Calcular!!!")


num1 = int(input("informe um número! "))
num2 = 0
result = 0
print("")

while num2 >= 0 and num2 <= 9:
    num2 = num2 + 1
    result = num1 * num2
    print(str(num1) + " x " + str(num2) + " = " + str(result))
print()
    

