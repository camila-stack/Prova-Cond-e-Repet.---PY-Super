email = "usuario@gmail.com"
senha = "usuario123"

while True:
    tent_email = input("Digite seu email: ")
    tent_senha = input("Digite sua senha: ")
    if tent_email != email:
        print(f"Email não encontrado")
    elif tent_email == email and tent_senha != senha:
        print(f"Senha incorreta")
    else:
        break
print(f"\033[32mLogin feito com sucesso!\033")