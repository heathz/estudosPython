x = [4, True, "hi"]
print(len(x))
x.append("hello")  # adiciona ao final da lista
x.extend([1, 2, 3, 4, 5])  # adiciona outra lista ao final da lista original
x.pop()  # retorna o último item da lista e remove-o / caso especificado, remove o item referente ao índice especificado
print(x[1])
x[0] = "hello"
