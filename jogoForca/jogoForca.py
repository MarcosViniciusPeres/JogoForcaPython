from random import randint

vida = 5
auxiliar = 0
vetorVerdadeiro = []
vetorAuxiliar = []

def comecarJogo(self):
    print('(1) - ESCOLHA O CONTEUDO DO JOGO DA FORCA')
    print('(2) - SORTEAR UMA PALAVRA')
    print('(3) - FALAR UMA LETRA')
    print('(4) - TENTAR ACERTAR A PALAVRA INTEIRA')
    print('(0) - SAIR DO PROGRAMA')

    opcao = input('ESCOLHA UMA OPÇÃO: ')

    if opcao == 1:
        print("Voce apertou o 1")

    elif opcao == 2:
        print("Voce apertou o 2")

    elif opcao == 3:
        print("Voce apertou o 3")

    elif opcao == 4:
        print("Voce apertou o 4")

    elif opcao == 0:
        print("Voce apertou o 0")


def escolherConteudo():

    variavelConteudo = input("Digite [1] para escolher Animal ou Digite [2] para escolher Fruta: ")
    if variavelConteudo == "1" or variavelConteudo == "2":
        if variavelConteudo == "1":
            print("Conteúdo Animal Foi Escolhido")
            vetorConteudo = ["leao", "macaco", "elefante", "girafa", "zebra", "hiena", "suricato", "javali", "baleia", "sucuri", "borboleta", "onça", "abelha", "anta", "boi", "cabra", "camundongo", "cachorro", "gato", "esponja", "enguia", "flamingo", "formiga", "gafanhoto", "galinha", "gnu", "harpia", "hamster", "iguana", "jararaca", "jacare", "lacraia", "morcego", "ostra", "ovelha", "panda", "pernilongo", "porco", "rinoceronte", "salamandra", "tamandua", "tartaruga", "urso", "vaca", "veado"]
            return vetorConteudo
        if variavelConteudo == "2":
            print("Conteúdo Fruta Foi Escolhido")
            vetorConteudo = ["banana", "melancia", "laranja", "kiwi", "acerola", "abacate", "abacaxi", "Amora", "cacau", "pinha", "caju", "carambola", "jabuticaba", "figo", "framboesa", "goiaba", "groselha", "jaca", "limao", "mamao", "manga", "maracuja", "melao", "morango", "pera", "pessego", "pitanga", "pitaya", "roma", "tangerina", "uva"]
            return vetorConteudo
    else:
        print("Escolha Uma Opção Proposta")
        return None

def sortearPalavra(conteudo):

    if len(conteudo) != 0:

        numeroRandomico = randint(0, len(conteudo))

        palavraEscolhida = conteudo[numeroRandomico]

        print("Sua Palavra Foi Sorteada com Sucesso. Bora Jogar ?")
        return palavraEscolhida
    else:
        print("Escolha um conteudo Primeiramente antes de sortear uma palavra.")
        return None



def acertarPalavra(palavra):
    if vida != 0:
        if palavra:
            palavraDigitada = input("Digite a Palavra a Ser Advinhada Sem Acentuação: ")
            palavraDigitada = palavraDigitada.lower()

            if palavraDigitada == palavra:
                print("Parabéns Você Venceu o Jogo Acertando a Palavra: ", palavra)
                exit()
            else:
                --vida
                print("Que pena Você Errou a Palavra a Ser Advinhada")
                print("Agora Você Tem um Total de:", vida, "Vidas")
        else:
            print("Sorteie uma Palavra Primeiramente para Tentar Acertar A palavra")
    else:
        print("Que pena suas Vidas Acabaram!! Recomece outro Jogo.")
        exit()


def acertarLetra(palavra):
    if vida != 0:
        if palavra:
            if vida == 0:
                print("Suas vidas Chegaram em: ", vida)
                print("Você Perdeu O Jogo")
                print("A palavra era: ", palavra)
                exit()

            vetorChar = list(palavra)

            if auxiliar < len(vetorChar):
               for i in range(auxiliar, len(vetorChar)):
                   vetorVerdadeiro.append("_")
                   ++auxiliar

            print("Você tem: ",vida," Vidas")
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
                    ++contador
                    vetorAuxiliar.append(letraChar)

            for i in range(len(vetorChar)):
                if letraChar != vetorChar[i]:
                    vetorAuxiliar.append(letraChar)

            str = ''.join(vetorVerdadeiro)

            if palavra == str:
                print("Parabéns Voce Ganhou O Jogo!!!")
                exit()

            if contador == 0:
                --vida
                print("Que Pena Nao Existe Essa Letra na Palavra.")
                print("Agora Você Tem um Total de: ", vida, " Vidas")

            if vida == 0:
                print("Acabou Suas Vidas, Voce perdeu o jogo !!!")
                print("A palavra era: ", palavra)
                exit()

            print("Palavra: ")
            for i in range(len(vetorVerdadeiro)):
                print(vetorVerdadeiro[i], end=" ")
        else:
            print("Sorteie uma Palavra Primeiramente para tentar Acertar A Letra")
    else:
        print("Que pena suas Vidas Acabaram!! Recomece outro Jogo.")