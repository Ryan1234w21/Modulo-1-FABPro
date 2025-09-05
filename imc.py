try:

    def login():
        nome = input("digite seu nome")
        peso = float(input("digite seu peso"))
        altura = float(input("digite sua altura"))


        imc = peso /( altura * altura)

        print(f"O nome dele é : {nome} e o imc é: {imc: .2f}")


        if imc < 18.5:
            print("ABAIXO DO PESO💀💀")
        elif imc < 24.9:
            print("PESO NORMAL😁😁")
        else: 
            print("OBESIDADE🍔🍔")
except ValueError:
    print("")

    login();