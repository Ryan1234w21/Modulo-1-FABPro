nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
possui_Carteira = input("1-sim  | 2-não: ")


if idade >= 18:
    print("VoçÊ e maior de idade    🙂")
    if possui_Carteira == "sim":
        print("VoçÊ pode dirigir    🚗")
    else:
        print("você pode se inscrever para tirar a carteira de motorista    📝")
else:
    print("Você e menor de idade    😢")

