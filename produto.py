nome_produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto"))
desconto = float(input("Digite a percentual de desconto"))

valor_desconto = preco * desconto / 100
preco_final = preco - valor_desconto

print("-----------------------------------------")
print(f"Produto: {nome_produto}")
print(f"Preço final: R$ {preco_final}")
print(f"Desconto: R$ {valor_desconto:.2f}")
print("-----------------------------------------")              