from leitorarquivo import LeitorArquivo


def main():
    leitor = LeitorArquivo('data.txt')
    valores = leitor.getValores()
    print(valores)


main()