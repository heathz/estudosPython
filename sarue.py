nota1 = float(input("primeira nota: "))
nota2 = float(input("segunda nota: "))
nota3 = float(input("terceira nota: "))
nota4 = float(input("quarta nota: "))
media = (nota1 + nota2 + nota3 + nota4) / 4

if media >= 7:
    print("Aprovado com média ", media)
else:
    print("Aluno precisa de recuperação")
    recuperacao = float(input("recuperação: "))
    media = (nota1 + nota2 + nota3 + nota4 + recuperacao) / 5
    if media >= 7:
        print("Aprovado com a média: ", media)
    else:
        print("Reprovado com a média: ", media)

# ***************************************************************** #

ano_de_nascimento = int(input("Digite seu ano de nascimento: "))
idade = 2022 - ano_de_nascimento
if idade >= 16 and idade < 18:
    print("Você já pode votar mas não pode dirigir")
elif idade >= 18:
    print("Você já pode votar e dirigir!")
else:
    print("Guri d+")
