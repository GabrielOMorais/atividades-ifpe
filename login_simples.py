login = input("Login: ")
senha = input("Senha: ")

login_real = "admin"
senha_real = "1234"

if login == login_real and senha == senha_real:
    print("Acesso concedido")
else:
    print("Acesso negado")

