boolean = True

while boolean:
    peso = float(input("Digite seu peso em KG: "))
    altura = float(input("Digite sua altura em Metros: "))
    imc = peso / (altura * altura)
    print(f"Seu IMC é: {imc:.2f}")

    print("Deseja continuar? [S/N]")
    continuar = input().upper()
    if continuar == 'S':
        boolean = True
    elif continuar == 'N':
        boolean = False
        break
    else :
        print("Encerrando devido entrada invalida")
        boolean = False

print("Programa encerrado.")




