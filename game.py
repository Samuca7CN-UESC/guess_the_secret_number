class Game:
    def __init__(self):
        self.turn = True  # Flag que indica se é a vez do jogador atual
        self.current_player = 0  # Índice do jogador atual (0 ou 1)

        self.points = [0,0]  # Lista de pontos dos jogadores

        self.secret_number = None  # Número secreto a ser adivinhado pelos jogadores

        self.min_number = 1  # Menor número permitido para o número secreto
        self.max_number = 1000  # Maior número permitido para o número secreto

        self.gain_amount = 1000  # Quantidade de pontos ganhos ao acertar o número secreto
        self.lose_amount = 100  # Quantidade de pontos perdidos ao errar o palpite

        self.chances = 10  # Número máximo de tentativas para acertar o número secreto
        self.rounds = 6  # Número total de rodadas do jogo

        self.rounds_counter = 0  # Contador de rodadas atual

        self.reset_confirm = 0

    def set_secret_number(self, sn):
        self.secret_number = sn  # Define o número secreto
        self.change_current_player()  # Altera o jogador atual

    def set_player_points(self, p, points):
        if self.points[p] + points >= 0:
            self.points[p] += points  # Atualiza os pontos do jogador
        self.turn = not self.turn  # Altera a vez do jogador
        self.secret_number = None  # Reinicia o número secreto
        self.rounds_counter += 1  # Incrementa o contador de rodadas

    def change_current_player(self):
        if self.current_player == 0:
            self.current_player = 1
        else:
            self.current_player = 0  # Altera o jogador atual para o próximo

    def end_game(self):
        return self.rounds == self.rounds_counter  # Verifica se o jogo chegou ao fim (todas as rodadas foram jogadas)

    def show_placar(self):
        print("\n\n=========================")
        print("PLACAR")
        print("=========================")
        print("Jogador 1: " + str(self.points[0]))  # Exibe os pontos do Jogador 1
        print("Jogador 2: " + str(self.points[1]))  # Exibe os pontos do Jogador 2
        print("\n\n=========================")
        if self.points[0] > self.points[1]:
            print("O VENCEDOR É O JOGADOR 1")  # Exibe o vencedor (Jogador 1)
        elif self.points[0] < self.points[1]:
            print("O VENCEDOR É O JOGADOR 2")  # Exibe o vencedor (Jogador 2)
        else:
            print("EMPATE!")  # Exibe empate
        print("=========================")

    def reset(self):
        self.reset_confirm += 1
        if self.reset_confirm == 2:
            self.turn = True  # Reinicia a vez do jogador
            self.current_player = 0  # Reinicia o jogador atual
            self.points = [0,0]  # Reinicia os pontos dos jogadores
            self.secret_number = None  # Reinicia o número secreto
            self.rounds_counter = 0  # Reinicia o contador de rodadas
            self.reset_confirm = 0
