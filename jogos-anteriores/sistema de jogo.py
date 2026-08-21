nome = "fateco"
idade = 38
pontuacao = 300
vida = 100
dinheiro = 500.0
jogador_ativo = True


def ver_jogador():
    print()
    print("===== JOGADOR =====")
    print(f"Nome: {nome}")
    print(f"Idade: {idade}")
    print(f"Pontuação: {pontuacao}")
    print(f"Vida: {vida}")
    print(f"Dinheiro: R$ {dinheiro}")
    print(f"Ativo: {jogador_ativo}")


def ganhar_pontos():
    global pontuacao

    pontos_ganhos = int(input("Quantos pontos você ganhou? "))

    pontuacao = pontuacao + pontos_ganhos

    print(f"Nova pontuação: {pontuacao}")


def comprar_item():
    global dinheiro

    preco_do_item = float(input("Digite o preço do item: "))

    if dinheiro >= preco_do_item:
        dinheiro = dinheiro - preco_do_item

        print("Compra realizada!")
        print(f"Saldo restante: R$ {dinheiro}")

    else:
        print("Dinheiro insuficiente!")


def ver_classificacao():

    if pontuacao >= 1000:
        print("Você é Mestre!")

    elif pontuacao >= 500:
        print("Você é Avançado!")

    elif pontuacao >= 100:
        print("Você é Intermediário!")

    else:
        print("Você é Iniciante!")


def mostrar_numeros():

    print()
    print("===== NÚMEROS =====")

    for i in range(1, 11):
        print(i)


def perder_vida():
    global vida
    global jogador_ativo

    vida_perdida = int(input("Quanto de vida você perdeu? "))

    vida = vida - vida_perdida

    if vida < 0:
        vida = 0

    print(f"Vida atual: {vida}")

    if vida <= 0:
        print("Você Morreu!")
        jogador_ativo = False


def batalhar():
    global pontuacao
    global dinheiro

    inimigo = "Goblin"
    vida_inimigo = 50

    while vida_inimigo > 0:

        print()
        print("===== BATALHA =====")
        print(f"Inimigo: {inimigo}")
        print(f"Vida: {vida_inimigo}")

        print()
        print("1 - Atacar")
        print("2 - Fugir")

        opcao_batalha = int(input("Escolha uma opção: "))

        if opcao_batalha == 1:

            dano = 15

            vida_inimigo = vida_inimigo - dano

            if vida_inimigo < 0:
                vida_inimigo = 0

            print(f"Você atacou o {inimigo}!")
            print(f"Dano causado: {dano}")
            print(f"Vida do {inimigo}: {vida_inimigo}")

            if vida_inimigo == 0:
                print("Inimigo derrotado!")

                pontuacao = pontuacao + 100
                dinheiro = dinheiro + 50

                print("+100 pontos")
                print("+R$ 50")

        elif opcao_batalha == 2:

            print("Você fugiu da batalha!")
            break

        else:
            print("Opção inválida!")


def main():
    global nome
    global idade

    nome = input("Digite seu nome: ")
    idade = int(input("Digite sua idade: "))

    opcao = 0

    while opcao != 8 and jogador_ativo:

        print()
        print("==========================")
        print("       SISTEMA DE JOGO")
        print("==========================")

        print("1 - Ver jogador")
        print("2 - Ganhar pontos")
        print("3 - Comprar item")
        print("4 - Ver classificação")
        print("5 - Mostrar números")
        print("6 - Perder vida")
        print("7 - Batalhar")
        print("8 - Sair")

        print("==========================")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            ver_jogador()

        elif opcao == 2:
            ganhar_pontos()

        elif opcao == 3:
            comprar_item()

        elif opcao == 4:
            ver_classificacao()

        elif opcao == 5:
            mostrar_numeros()

        elif opcao == 6:
            perder_vida()

        elif opcao == 7:
            batalhar()

        elif opcao == 8:
            print("Saindo do sistema...")

        else:
            print("Opção inválida!")


main()