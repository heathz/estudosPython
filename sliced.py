# pegar parte de uma variavel

# slice = [start:stop:step]
# default: inicio:fim:  1

x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
y = ["hi", "hello", "goodbye", "cya", "sure"]
s = "hello"

sliced = x[
    0:4:2
]  # inicia no índice 0 finaliza quando encontrar o número 4 (sem incluir o 4) e anda de 2 em 2 elementos
inverte = s[::-1]

print(sliced)
print(inverte)
