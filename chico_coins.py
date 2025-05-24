boolean = True

while boolean:
   valor_reais = float(input("Insira o valor em reais: "))
   cotacao_dolar = float(input("Insira a cotacao atual do dolar: "))
   dolar= valor_reais / cotacao_dolar
   print(f"{valor_reais}Reais equivalem a {dolar:.2f} Dolares.")

   print("Deseja continuar? [S/N]")
   continuar = input().upper()
   if continuar == 'S':
       boolean = True
   elif continuar == 'N':
       boolean = False

   else:
       print("Encerrando devido entrada invalida")
       boolean = False

print("Programa encerrado.")


