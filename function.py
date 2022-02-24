def operacoes(x, y):
    print("Resultado das operacoes basicas usando o primeiro e segundo valor: ")
    return x + y, x - y, x * y, x / y


num1 = input("Digite o primeiro numero: ")
num2 = input("Digite o segundo numero: ")

soma, subt, multi, divi = operacoes(int(num1), int(num2))
print("Soma: ", soma)
print("Subtracao: ", subt)
print("Multiplicacao: ", multi)
print("Divisao: ", divi)
