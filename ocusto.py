print("Digite o preço dos combustíveis: ")

etanol = float(input("Etanol: "))
gasolina = float(input("Gasolina: "))

result = etanol / gasolina

if result <= 0.73:
    print(f"Resultado: {result:.2f} - Abasteça com Etanol")
else:
    print(f"Resultado: {result:.2f} - Abasteça com Gasolina")
