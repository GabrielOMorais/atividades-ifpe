boolean = True

while boolean:
   primeira_nota = float(input("Insira a primeira nota: "))
   segunda_nota = float(input("Insira a segunda nota: "))
   terceira_nota = float(input("Insira a terceira nota: "))
   media = (primeira_nota + segunda_nota + terceira_nota)/3

   print(f"A media das tres notas é: {media:.2f}")

   continuar = input("Deseja continuar? [S/N] ").upper()
   if continuar == "N":
       boolean = False
       break

   elif continuar == "S":
       boolean = True

   else:
       print("Encerrando devido entrada invalida")
       boolean = False

print("Programa encerrado.")

