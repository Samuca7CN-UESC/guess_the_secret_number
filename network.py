import socket
import pickle


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Cria um objeto de socket para o cliente
        self.server = "localhost"  # Endereço do servidor
        self.port = 5556  # Porta de comunicação
        self.addr = (self.server, self.port)  # Endereço e porta do servidor
        self.p = self.connect()  # Realiza a conexão com o servidor e recebe a identificação do jogador


    def getP(self):
        return self.p  # Retorna a identificação do jogador


    def connect(self):
        try:
            self.client.connect(self.addr)  # Conecta ao servidor
            return self.client.recv(2048).decode()  # Recebe a identificação do jogador do servidor
        except:
            pass  # Tratamento de exceção caso a conexão falhe


    def send(self, data):
        try:
            self.client.send(str.encode(data))  # Envia os dados (mensagem) ao servidor
            return pickle.loads(self.client.recv(2048*2))  # Recebe e decodifica os dados recebidos do servidor
        except socket.error as e:
            print(e)  # Tratamento de exceção caso ocorra um erro de socket
