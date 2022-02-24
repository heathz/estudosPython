def jogar():
    print("*********************************")
    print("***Bem vindo ao jogo da Forca!***")
    print("*********************************")

    palavra_secreta = "banana"

    enforcou = False
    acertou = False

    while not enforcou and not acertou:
        chute = input("Qual letra? ")
        chute = chute.strip()

        posi = 0
        for letra in palavra_secreta:
            if chute.lower() == letra:
                print("Encontreio a letra > {} < na posição {}".format(letra, posi))
            posi = posi + 1

        print("jogando")

    print("Fim do jogo")


if __name__ == "__main__":
    jogar()
