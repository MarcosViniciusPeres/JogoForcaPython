from random import randint

vida = 5
auxiliar = 0
vetorVerdadeiro = []
vetorAuxiliar = []
conteudo = []
palavraSorteada = ""
auxiliarEscolher = 0


def escolherConteudo():
    global auxiliarEscolher
    if auxiliarEscolher == 0:
        auxiliarEscolher += 1
        variavelConteudo = int(input("Digite [1] para escolher Animal ou Digite [2] para escolher Fruta: "))

        if variavelConteudo == 1 or variavelConteudo == 2:
            if variavelConteudo == 1:
                print("Conteúdo Animal Foi Escolhido")
                vetorConteudo = ["leao", "macaco", "elefante", "girafa", "zebra", "hiena", "suricato", "javali", "baleia", "sucuri", "borboleta", "onça", "abelha", "anta", "boi", "cabra", "camundongo", "cachorro", "gato", "esponja", "enguia", "flamingo", "formiga", "gafanhoto", "galinha", "gnu", "harpia", "hamster", "iguana", "jararaca", "jacare", "lacraia", "morcego", "ostra", "ovelha", "panda", "pernilongo", "porco", "rinoceronte", "salamandra", "tamandua", "tartaruga", "urso", "vaca", "veado"]
                return vetorConteudo
            if variavelConteudo == 2:
                print("Conteúdo Fruta Foi Escolhido")
                vetorConteudo = ["banana", "melancia", "laranja", "kiwi", "acerola", "abacate", "abacaxi", "Amora", "cacau", "pinha", "caju", "carambola", "jabuticaba", "figo", "framboesa", "goiaba", "groselha", "jaca", "limao", "mamao", "manga", "maracuja", "melao", "morango", "pera", "pessego", "pitanga", "pitaya", "roma", "tangerina", "uva"]
                return vetorConteudo
        else:
            print("Escolha Uma Opção Proposta")
            return
    else:
        print("Voce ja Escolheu um conteudo")
        return

def sortearPalavra(conteudo):
    if conteudo:
        numeroRandomico = randint(0, len(conteudo))
        palavraEscolhida = conteudo[numeroRandomico]

        print("Sua Palavra Foi Sorteada com Sucesso. Bora Jogar ?")
        return palavraEscolhida
    else:
        print("Escolha um conteudo Primeiramente antes de sortear uma palavra.")
        return



def acertarPalavra(palavra):
    global vida
    if vida != 0:
        if palavra:
            palavraDigitada = input("Digite a Palavra a Ser Advinhada Sem Acentuação: ")
            palavraDigitada = palavraDigitada.lower()

            if palavraDigitada == palavra:
                print("Parabéns Você Venceu o Jogo Acertando a Palavra: ", palavra)
                exit()
            else:
                vida -= 1
                print("Que pena Você Errou a Palavra a Ser Advinhada")
                print("Agora Você Tem um Total de:", vida, "Vidas")
        else:
            print("Sorteie uma Palavra Primeiramente para Tentar Acertar A palavra")
    else:
        print("Que pena suas Vidas Acabaram!! Recomece outro Jogo.")
        exit()


def acertarLetra(palavra):
    global auxiliar
    global vida
    if vida != 0:
        if palavra:
            if vida == 0:
                print("Suas vidas Chegaram em: ", vida)
                print("Você Perdeu O Jogo")
                print("A palavra era: ", palavra)
                exit()

            vetorChar = list(palavra)

            if auxiliar < len(vetorChar):
               for i in range(0, len(vetorChar)):
                   vetorVerdadeiro.append("_")
                   auxiliar += 1

            print("Você tem: ", vida, " Vidas")
            letraChar = input("Escolha Uma Letra A Ser Adivinhada: ")

            letraChar.lower()
            letraChar = letraChar[0]

            for i in range(len(vetorAuxiliar)):
                if letraChar == vetorAuxiliar[i]:
                    print("Você Já Usou Essa Letra, Por favor Escolha Outra")
                    return

            contador = 0

            for i in range(len(vetorChar)):
                if letraChar == vetorChar[i]:
                    vetorVerdadeiro[i] = letraChar
                    contador += 1
                    vetorAuxiliar.append(letraChar)

            for i in range(len(vetorChar)):
                if letraChar != vetorChar[i]:
                    vetorAuxiliar.append(letraChar)

            str = ''.join(vetorVerdadeiro)

            if palavra == str:
                print("Parabéns Voce Ganhou O Jogo!!!")
                exit()

            if contador == 0:
                vida -= 1
                print("Que Pena Nao Existe Essa Letra na Palavra.")
                print("Agora Você Tem um Total de: ", vida, " Vidas")

            if vida == 0:
                print("Acabou Suas Vidas, Voce perdeu o jogo !!!")
                print("A palavra era: ", palavra)
                exit()

            print("Palavra: ")
            for i in range(len(vetorVerdadeiro)):
                print(vetorVerdadeiro[i], end=" ")
            print("")
        else:
            print("Sorteie uma Palavra Primeiramente para tentar Acertar A Letra")
            return
    else:
        print("Que pena suas Vidas Acabaram!! Recomece outro Jogo.")
        exit()


def menuInicial():
    print('(1) - ESCOLHA O CONTEUDO DO JOGO DA FORCA')
    print('(2) - SORTEAR UMA PALAVRA')
    print('(3) - FALAR UMA LETRA')
    print('(4) - TENTAR ACERTAR A PALAVRA INTEIRA')
    print('(0) - SAIR DO PROGRAMA')


def comecaJogo():
    global conteudo
    global palavra
    global palavraSorteada

    opcao = 1
    while opcao != 0:
        menuInicial()
        opcao = int(input('ESCOLHA UMA OPÇÃO: '))

        if opcao == 0 or opcao == 1 or opcao == 2 or opcao == 3 or opcao == 4:
            if opcao == 1:
                conteudo = escolherConteudo()
            elif opcao == 2:
                palavraSorteada = sortearPalavra(conteudo)
            elif opcao == 3:
                acertarLetra(palavraSorteada)
            elif opcao == 4:
                acertarPalavra(palavraSorteada)
            elif opcao == 0:
                print("Saindo do Programa")
                exit()
        else:
            print("ERRO: Opção inválida.")

comecaJogo()