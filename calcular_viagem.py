boolean = True

while boolean:
    print("Digite o valor da gasolina")
    gasolina = float(input())
    print("Digite quantos litros serao consumidos")
    litros = float(input())

    total = litros * gasolina

    print(f"Voce ira precisar de {total} reais")

    resposta = input("Deseja continuar? [S/N]").strip().upper()
    if resposta == "N":
        boolean = False
        break
    elif resposta == "S":
        boolean = True
    else:
        print("Encerrando devido entrada invalida")
        boolean = False

print("Programa encerrado.")
