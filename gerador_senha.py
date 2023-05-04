import random
import string
import sys

if len(sys.argv) < 2:
  print("Você tem que especificar o tamanho da senha!")
  print("Forma correta de utilizar:")
  print("python gerador_senha.py 8")
  print("utilizando do modo acima irá gerar uma senha com 8 caracteres")
  sys.exit()
else:
  size = sys.argv[1]
  size = int(size)
  print(f"Sera gerada uma senha de {size} caracteres contendo letras maiusculas e minusculas, numeros e simbolos")

  random_characters = []
  random_characters.append(''.join(random.choice(string.ascii_letters + string.digits + string.punctuation) for _ in range(size)))
  print(random_characters)