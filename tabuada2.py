numero = int(input("Digite o numero: "));
inicio=int(input("Digite o numero de Onde começara a tabuada: "))
fim=int(input("Digite até qual numero o multi deve ir: "))
i = 1

while inicio <= fim:
    print(f"{inicio} x {numero} = {inicio * numero}")
    inicio += 1