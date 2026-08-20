var nome = "fateco"
var idade = 38
var pontuacao = 300
var vida = 100
var dinheiro = 500.0
var jogadorAtivo = true
 
fun verJogador() {
 
    println()
    println("===== JOGADOR =====")
    println("Nome: $nome")
    println("Idade: $idade")
    println("Pontuação: $pontuacao")
    println("Vida: $vida")
    println("Dinheiro: R$ $dinheiro")
    println("Ativo: $jogadorAtivo")
}
 
 
fun ganharPontos() {
 
    print("Quantos pontos você ganhou? ")
    var pontosGanhos = readln().toInt()
 
    pontuacao = pontuacao + pontosGanhos
 
    println("Nova pontuação: $pontuacao")
}
 
 
fun comprarItem() {
 
    print("Digite o preço do item: ")
    var precoDoItem = readln().toDouble()
 
    if (dinheiro >= precoDoItem) {
 
        dinheiro = dinheiro - precoDoItem
 
        println("Compra realizada!")
        println("Saldo restante: R$ $dinheiro")
 
    } else {
 
        println("Dinheiro insuficiente!")
    }
}
 
 
fun verClassificacao() {
 
    if (pontuacao >= 1000) {
 
        println("Você é Mestre!")
 
    } else if (pontuacao >= 500) {
 
        println("Você é Avançado!")
 
    } else if (pontuacao >= 100) {
 
        println("Você é Intermediário!")
 
    } else {
 
        println("Você é Iniciante!")
    }
}
 
 
fun mostrarNumeros() {
 
    println()
    println("===== NUMEROS =====")
 
    for (i in 1..10) {
 
        println(i)
    }
}
 
fun perderVida() {
    
    print("Quanto de vida você perdeu? ")
    
    var vidaPerdida = readln().toInt()
 
    vida = vida - vidaPerdida
 
    if (vida < 0 ) {
        vida = 0  
    }
 
    println("Vida atual: $vida")
 
    if (vida <= 0) {
        println("Você Morreu!")
        jogadorAtivo = false
    }
 
}
 
fun batalhar() {

    var inimigo = "Goblin"
    var vidaInimigo = 50

    println()
    println("===== BATALHA =====")
    println("Inimigo: $inimigo")
    println("Vida: $vidaInimigo")

    println()
    println("1 - Atacar ")
    println("2 - Fugir ")

    print("Escolha uma opção:")
    var opcaoBatalha = readln().toInt()

when (opcaoBatalha) {
    1 -> {}
    }

}

fun main() {
 
    print("Digite seu nome: ")
    nome = readln()
 
    print("Digite sua idade: ")
    idade = readln().toInt()
 
    var opcao = 0
 
 
    while (opcao != 7 && jogadorAtivo) {
 
        println()
        println("==========================")
        println("       SISTEMA DE JOGO")
        println("==========================")
 
        println("1 - Ver jogador")
        println("2 - Ganhar pontos")
        println("3 - Comprar item")
        println("4 - Ver classificação")
        println("5 - Mostrar números")
        println("6 - Perder vida")
        println("7 - Sair")
 
        println("==========================")
 
        print("Escolha uma opção: ")
        opcao = readln().toInt()
 
 
        when (opcao) {
 
            1 -> {
                verJogador()
            }
 
            2 -> {
                ganharPontos()
            }
 
            3 -> {
                comprarItem()
            }
 
            4 -> {
                verClassificacao()
            }
 
            5 -> {
                mostrarNumeros()
            }
 
            6 -> {
                perderVida()
            }
            
            7 -> {
                println ("Saindo do sistema...")
            }
 
            else -> {
                println("Opção inválida!")
            }
        }
    }
}