import math
import os


def contas(x, y):

    errei = False

    def soma():
        return x + y

    def subtracao():
        return x - y

    def multiplicacao():
        return x * y

    def divisao():
        return x/y

    def potencia():
        return x**y

    def raizquadrada():
        return math.sqrt(x)

    def porcentagem():
        return x * y/100

    def posi_nega():
        return x * -1

    if x is not None and errei is False:
        clear = input(f"Deseja Limpar a calculadora? (O último valor é {x}) ")
        clear = clear.lower()
        if clear in ("sim", "s"):
            x = None
        os.system("cls")

    print("\r")
    print("-"*50)
    print("Selecione a operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potência")
    print("6. Raiz Quadrada")
    print("7. Porcentagem")
    print("8. Inverter de positivo-negativo")
    print("-"*50)
    print("\r")

    if x is not None:
        print("O último valor é", x)
        print("\r")
    choice = input("Digite sua opção (1/2/3/4/5/6/7/8/exit): ")
    choice = choice.lower()

    if choice == "exit":
        exit()
    elif choice in ("1", "2", "3", "4", "5", "6", "7", "8"):
        pass
    else:
        os.system("cls")
        print("Digite um dos números acima!")
        errei = True
        contas(x, y)

    if x is None:
        print("\r")
        x = float(input("Digite o primeiro número: "))

    if choice in ("1", "2", "3", "4", "5", "7"):
        y = float(input("Digite o segundo número: "))

    if choice == '1':
        os.system("cls")
        print(f"{x} + {y} = {soma()}")
        x = soma()
        contas(x, y)
    elif choice == '2':
        os.system("cls")
        print(f"{x} - {y} = {subtracao()}")
        x = subtracao()
        contas(x, y)
    elif choice == '3':
        os.system("cls")
        print(f"{x} * {y} = {multiplicacao()}")
        x = multiplicacao()
        contas(x, y)
    elif choice == '4':
        os.system("cls")
        print(f"{x} * {y} = {divisao()}")
        x = divisao()
        contas(x, y)
    elif choice == '5':
        os.system("cls")
        print(f"{x} ** {y} = {potencia()}")
        x = potencia()
        contas(x, y)
    elif choice == '6':
        os.system("cls")
        print(f"Raiz quadrada de {x} = {raizquadrada()}")
        x = raizquadrada()
        contas(x, y)
    elif choice == '7':
        print("\r")
        print(f"{x} * {y}% = {porcentagem()}")
        x = porcentagem()
        contas(x, y)
    elif choice == '8':
        os.system("cls")
        print(f"{x} * -1 = {posi_nega()}")
        x = posi_nega()
        contas(x, y)


contas(x=None, y=None)
