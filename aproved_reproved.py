nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

if media >= 7:
    print("Aprovado")
elif media >= 5 and media <7:
    print("Recuperaçao")
elif media <5 :
    print("Reprovado")


