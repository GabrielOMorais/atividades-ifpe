boolean = True

while boolean:
    numero1 = float(input("Digite um numero: "))
    numero2 = float(input("Digite outro numero: "))
    operador = (input("Digite o operador"))

    if operador == "+":
        print(numero1 + numero2)
    elif operador == "-":
        print(numero1 - numero2)
    elif operador == "*":
        print(numero1 * numero2)
    elif operador == "/":
        print(numero1 / numero2)
    else :
        print("Operador nao identificado,tente novamente.")
        boolean = True
    continuar = input("Deseja continuar? [S/N]").upper()
    if continuar == "N":
        boolean = False
    elif continuar == "S":
        boolean = True
    else:
        print("Encerrando o programa devido entrada invalida")
        boolean = False
print("Programa encerrado.")
