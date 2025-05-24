boolean = None
print("Calculadora de temperatura")
escolha = input("Digite 's' para utilizar o programa ou 'n' para sair: ")
if escolha.lower() == 'n':
	print("Programa encerrado.")
	boolean = False
elif escolha.lower() == 's':
	boolean = True
else:
	print("Por favor, digite 's' para utilizar o programa ou 'n' para sair.")
	boolean = False

while boolean:
	temp = float(input("Digite a temperatura em Celsius: "))
	soma_temp = temp + 1.5
	print(f"A temperatura em Celsius é: {soma_temp}°C")
	continuar = input("Deseja continuar? (s/n): ")
	if continuar.lower() == 's':
		boolean = True
	elif continuar.lower() == 'n':
		boolean = False
	else:
		print("Comando nao reconhecido, encerrando o programa.")
	break
print("Programa encerrado.")
