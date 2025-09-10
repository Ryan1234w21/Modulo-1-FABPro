try:

        nome = input("digite seu nome")
        peso = float(input("digite seu peso (Kg)"))
        altura = float(input("digite sua altura (m)"))


        imc = peso /( altura * altura)

        print(f"O nome dele é : {nome} e o imc é: {imc: .2f}")


        if imc < 18.5:
            print("ABAIXO DO PESO💀💀")
        elif imc < 25:
            print("PESO NORMAL😁😁")
        elif imc < 30:
            print("OBESIDADE🍔🍔")
        elif imc < 35:
             print("OBESIDADE GRAU1🍔🍔")
        elif imc < 40:
             print("OBESIDADE GRAU2🍔🍔")
        else:
             print("OBESIDADE GRAU3🍔🍔")
except ValueError:
    print("Valor Incorreto, tente novamente")

