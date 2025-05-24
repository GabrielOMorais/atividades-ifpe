cracha = input("Voce possui cracha ? [S/N]").upper()
digital = input("Digital reconhecida ? [S/N]").upper()

if cracha == 'S' and digital == 'S':
    print("Acesso Liberado")
else:
    print("Acesso Negado")