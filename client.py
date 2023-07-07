from network import Network


def main():
    run = True  # Variável de controle do loop principal
    n = Network()  # Criação de um objeto de rede
    player = int(n.getP())  # Obtém a identificação do jogador
    print("VOCÊ É O JOGADOR " + str(player + 1))  # Exibe a identificação do jogador

    while run:
        try:
            game = n.send("get")  # Obtém o estado atual do jogo do servidor
        except:
            run = False  # Encerra o loop caso ocorra um erro de conexão
            print("\n\nERRO!")
            print("NÃO FOI POSSÍVEL RECEBER O ESTADO ATUAL DO JOGO\n\n!")
            break
        
        if game.end_game():  # Verifica se o jogo chegou ao fim
            print("\nFIM DE JOGO\n")
            game.show_placar()  # Exibe o placar final do jogo
            n.send("reset")  # Solicita a reinicialização do jogo ao servidor
            break

        if game.current_player == player:  # Verifica se é a vez do jogador atual
            print("\n\n===========================")
            print("RODADA: " + str(game.rounds_counter + 1))
            print("===========================\n\n")
            if game.turn:  # Verifica se é a vez do jogador definir o número secreto
                if player == 0:
                    n.send(f"sn_{get_secret_number(game)}")  # Envia o número secreto ao servidor
                    print("\nO outro jogador deve tentar acertar o número!\n")
                else:
                    if game.secret_number is not None:
                       n.send(f"p_{start_guesses(game)}")  # Envia o palpite ao servidor
            else:  # Caso contrário, é a vez do jogador tentar adivinhar o número secreto
                if player == 0:
                    if game.secret_number is not None:
                       n.send(f"p_{start_guesses(game)}")  # Envia o palpite ao servidor
                else:
                    n.send(f"sn_{get_secret_number(game)}")  # Envia o número secreto ao servidor
                    print("\nO outro jogador deve tentar acertar o número!\n")
                

def start_guesses(game):
    points = 0  # Variável para armazenar a pontuação do jogador
    flag = 0  # Variável de controle para verificar se o jogador acertou o número secreto
    for i in range(game.chances):  # Loop para as tentativas do jogador

        guess = get_guess(game, i)  # Obtém o palpite do jogador

        if guess == int(game.secret_number):  # Verifica se o palpite é igual ao número secreto
            print("\nVocê acertou! Ganha "+str(game.gain_amount)+" pontos!")
            points += game.gain_amount  # Incrementa a pontuação do jogador
            flag = 1  # Sinaliza que o jogador acertou
            break
        else:
            print("\nVocê errou! Menos "+str(game.lose_amount)+" pontos")
            
            if guess > int(game.secret_number):
                print("O numero secreto é menor! ")
            else:
                print("O numero secreto é maior! ")

            points -= game.lose_amount  # Decrementa a pontuação do jogador

    
    if flag == 0:
        print("\n\nAcabaram suas chances!")
        print("O número secreto era: ", game.secret_number)
    
    return points


def get_secret_number(game):
    try:
        secret = int(input("\nQual o número secreto?\n"))  # Obtém o número secreto do jogador
    except:
        secret = game.min_number - 1
    while secret < game.min_number or secret > game.max_number:  # Verifica se o número está dentro do intervalo permitido
        print("O número secreto deve ser entre "+str(game.min_number)+" e "+str(game.max_number) + "!")
        print("Tente novamente")
        try:
            secret = int(input("\nQual o número secreto?\n"))
        except:
            secret = game.min_number - 1
    return secret


def get_guess(game, i):
    try:
        guess = int(input("\nTentativa " + str(i + 1) + ": "))# Obtém o palpite do jogador
    except:
        guess = game.min_number - 1

    while guess < game.min_number or guess > game.max_number:  # Verifica se o palpite está dentro do intervalo permitido
        print("Seu palpite deve ser um número entre "+str(game.min_number)+" e "+str(game.max_number) + "!")
        print("Tente novamente")
        try:
            guess = int(input("\nTentativa " + str(i + 1) + ": "))
        except:
            guess = game.min_number - 1

    return guess


def show_instructions():
    print("\n\n=======================\n")
    print("INSTRUÇÕES: \n")
    print("1. Dois jogadores competem para adivinhar um número secreto.")
    print("2. O número secreto está entre 1 e 1000.")
    print("3. A cada rodada um jogador insere o numero secreto e o outro tenta adivinhá-lo.")
    print("4. O jogador tem 10 chances para fazer um palpite.")
    print("5. Se o jogador acertar o número secreto, ele ganha 1000 pontos.")
    print("6. Se o jogador errar o palpite, ele perde 100 pontos.")
    print("7. Após 10 tentativas, se o jogador errar todas as tentativas, o número secreto é revelado.")
    print("8. O jogo é disputado em 6 rodadas.")
    print("9. Ao final das rodadas, o placar é exibido e o vencedor é determinado.")
    print("\n=======================\n")


def show_credits():
    print("\n\n=======================\n")
    print("CRÉDITOS: \n")
    print("201920069 | Guilherme Guimarães Souza")
    print("201920081 | Samuel Correia Nascimento")
    print("\nCiência da Computação")
    print("UESC - Universidade Estadual de Santa Cruz")
    print("Ilhéus / BA")
    print("\n=======================\n")         


def menu_screen():
    while True:
        print("\n\n=======================")
        print("MENU PRINCIPAL")
        print("=======================")
        print("0.Iniciar Jogo")
        print("1.Instruções")
        print("2.Créditos")
        print("3.Sair")

        try:
            op = int(input("Insira a opção desejada: "))
        except:
            op = 4
        
        if op == 0:
            main()  # Inicia o jogo
            print("Fim de jogo")
            break
        elif op == 1:
            show_instructions()  # Exibe as instruções do jogo
        elif op == 2:
            show_credits()  # Exibe os créditos do jogo
        elif op == 3:
            print("Adeus!")
            return -1  # Encerra o programa
        else:
            print("Opção inválida!")


while True:
    menu_result = menu_screen()  # Exibe o menu principal e aguarda a seleção do usuário
    if menu_result == -1:
        break  # Encerra o programa caso o usuário selecione sair
