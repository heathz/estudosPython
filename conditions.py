idade = input("Digite sua idade: ")

if int(idade) >= 18 and int(idade) < 60:
    print("De maior")
elif int(idade) < 18:
    print("De menor")
else:
    print("Idoso")
