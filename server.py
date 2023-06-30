import socket
from _thread import *
import pickle
from game import Game

server = "localhost"  # Endereço do servidor
port = 5556  # Porta utilizada pelo servidor

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Criação do objeto de socket

try:
    s.bind((server, port))  # Vincula o servidor ao endereço e porta especificados
except socket.error as e:
    str(e)

s.listen(2)  # O servidor começa a ouvir as conexões
print("Esperando conexão, Servidor Iniciado")

connected = set()  # Conjunto de clientes conectados
counter = 0  # Contador de clientes conectados
original_game = None  # Objeto de jogo original

def threaded_client(conn, p):
    conn.send(str.encode(str(p)))  # Envia a identificação do jogador para o cliente conectado

    while True:
        try:
            data = conn.recv(4096).decode()  # Recebe os dados enviados pelo cliente

            game = original_game  # Cria uma cópia do objeto de jogo original

            if game is not None:  # Verifica se o objeto de jogo existe
                if not data:  # Se os dados recebidos forem vazios, a conexão é encerrada
                    break
                else:
                    if data != "get":  # Se os dados não forem "get"
                        if data == "reset":  # Se os dados forem "reset", o jogo é reiniciado
                            game.reset()
                            conn.sendall(pickle.dumps(game))
                            break
                        else:
                            option = data.split('_')  # Divide os dados em opção e valor
                            if(option[0] == 'sn'):  # Se a opção for 'sn' (número secreto), o número é definido
                                game.set_secret_number(int(option[1]))
                            elif(option[0] == 'p'):  # Se a opção for 'p' (pontuação), a pontuação do jogador é definida
                                game.set_player_points(p, int(option[1]))
                            else:
                                print("RESPOSTA INVÁLIDA DO CLIENTE")  # Se a opção não for reconhecida, exibe uma mensagem de erro

                    conn.sendall(pickle.dumps(game))  # Envia o objeto de jogo serializado para o cliente
        except:
            break
    
    print("Perda de Conexão")  # Exibe uma mensagem de perda de conexão
    try:
        game = None
        print("Encerrando jogo")  # Exibe uma mensagem de encerramento do jogo
    except:
        pass
    conn.close()  # Fecha a conexão com o cliente

while True:
    conn, addr = s.accept()  # Aceita uma nova conexão
    print("Conectado ao:", addr)  # Exibe o endereço do cliente conectado

    p = 0  # Identificação do jogador

    counter += 1  # Incrementa o contador de clientes conectados
    if counter > 2:
        counter = 1

    if counter == 1:  # Se for o primeiro cliente conectado, cria um novo jogo
        original_game = Game()
        print("Criando novo jogo...")
    else:
        p = 1  # Se for o segundo cliente conectado, define a identificação do jogador como 1

    start_new_thread(threaded_client, (conn, p))  # Inicia uma nova thread para lidar com a conexão do cliente
