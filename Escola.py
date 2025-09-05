nome_aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))

media = (nota1 + nota2 + nota3) / 3

if media>= 7:
    print("O aluno {nome_aluno} Aprovado✅✅")
elif media >= 4:
    print("O aluno {nome_aluno} Está de recuperação⚠️⚠️")
else:
    print("O aluno {nome_aluno} Reprovado❌❌")

print(f"A média do aluno {nome_aluno} é: {media:.2f}")