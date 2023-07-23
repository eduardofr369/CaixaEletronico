print("=" * 30, "CAIXA ELETRÔNICO", "=" * 30)


def prosseguir():
    saque = int(input("digite o valor do saque:"))
    if saque < 10 or saque > 600:
        print("Valor inválido, por favor digite novamente")
        return prosseguir()

    # criando as variáveis notas
    ncem = int(saque / 100)
    saque = saque % 100

    nciquenta = int(saque / 50)
    saque = saque % 50

    ndez = int(saque / 10)
    saque = saque % 10

    ncinco = int(saque / 5)
    saque = saque % 5

    num = int(saque / 1)
    saque = saque % 1

    # imprimindo os valores de saída

    print("{} notas de 100\n{} notas de 50\n{} notas de 10\n{} notas de 5\n{} notas de 1"
          .format(ncem, nciquenta, ndez, ncinco, num))

    # Retorna para o programa principal
    def retornar():
        pergunta = str(input("Deseja fazer um novo saque?\n"))
        if pergunta.strip().lower() == "sim":
            return prosseguir()
        else:
            exit()

    retornar()


prosseguir()
