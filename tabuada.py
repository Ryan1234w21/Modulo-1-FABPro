try:
        numero = int(input("Digite um número para ver sua tabuada: "))

        for i in range(1, 11):
                print(f"{i} x {numero} = {i * numero}")
except ValueError:
        print("Valor inválido! Por favor, insira um número inteiro válido.")