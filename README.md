# Jogo de Adivinhação em Rede - Documentação

Este é um jogo de adivinhação jogado em rede, onde dois jogadores competem para adivinhar o número secreto escolhido por um dos jogadores. Serão realizadas 3 pares de rodadas, onde o jogador selecionado para adivinhar terá 10 chances para adivinhar o número escolhido pelo outro jogador. Após finalizar as rodadas, o jogo mostrará o placar e apresentará o ganhador. O jogo é implementado em Python e utiliza os recursos da biblioteca da linguagem (socket e threading) para a comunicação e gerencimanento entre os jogadores (cliente) e o servidor.

## Requisitos

- Python 3.x

## Instruções de Uso

1. Certifique-se de que todos os arquivos necessários estão no mesmo diretório:
   - `server.py`: Implementa o servidor do jogo.
   - `client.py`: Implementa o cliente do jogo.
   - `game.py`: Define a classe `Game` que representa o estado do jogo.
   - `network.py`: Implementa a classe `Network` que gerencia a comunicação em rede.

2. Execute o arquivo `server.py` em um terminal para iniciar o servidor do jogo.

3. Em dois terminais separados, execute o arquivo `client.py` para cada jogador. O jogo iniciará automaticamente, exibindo o menu do jogo onde existem 4 opções no menu. 

4. No terminal do jogador 1, será exibida a mensagem "Você é o jogador 0" quando for selecionado a opção do menu "Iniciar o Jogo". No terminal do jogador 2, será exibida a mensagem "Você é o jogador 1" quando for selecionado a opção do menu "Iniciar o Jogo".

5. A rodada começa com um jogador escolhendo o número secreto para o outro jogador tentar adivinhar. 

6. A rodada finaliza até que o jogador adivinhe o número secreto ou o número máximo de tentativas seja atingido. 

7. Na próxima rodada, os papeis serão invertidos: o outro jogador tenta adivinhar o número secreto escolhido por um jogador; voltaremos por passo 5 e isso acontece até finalizar o número de rodadas. 

8. Quando finalizar o número de rodadas, será mostrado o placar do jogo para os dois jogadores, apresentando quantos pontos cada jogador realizou no total e quem foi o ganhador. Todos os jogadores retornará para o menu principal.

9. Para encerrar o jogo, basta escolher a opção "sair" no menu.

## Protocolo na Camada de Aplicação

O protocolo na camada de aplicação consiste em uma troca de mensagens entre o cliente e o servidor usando o formato de texto onde cada um tem um socket TCP. As mensagens são enviadas e recebidas codificadas em strings ou através do objeto `game`. O gerenciamento da conexão do cliente com o servidor é gerenciado através do Network.py e o servidor tem um módulo próprio para inicializar seu socket e gerenciar a comunicação com os clientes. 

Assim que o servidor é inicializado, ele prepara o socket TCP e espera as conexões do cliente. Por outro lado, o cliente monta o socket TCP e estabelece a conexão, criando um "three-way handshake", especificado pela documentação da biblioteca socket do Python. 

A lógica da comunicação é que toda vez que o cliente envia uma mensagem para o servidor, este o responde de volta com o objeto `game`, contendo todo estado do jogo. 

### Mensagens do Cliente para o Servidor

O cliente envia as seguintes mensagens para o servidor através de funções montadas no Network.py:

- `connect`: Faz a conexão do cliente para receber o seu identificador como jogador
- `send`: Método para enviar uma mensagem para o servidor e retorna o que o servidor responde para ele

Nos casos de envio de dados da pontuação ou do número secreto, o cliente envia dois dados em formato de string separado por underline para ser recebida pelo servidor como dados diferentes através do comando split do Python no server.py

### Mensagens do Servidor para o Cliente

O servidor envia as seguintes mensagens para o cliente através dos comandos `send` e `sendall` da biblioteca socket:

- `conn.send(str.enconde(str(p)))`: Envia o número do jogador para o cliente. O número do jogador é representado por um número inteiro convertido em string.
- `conn.sendall(pickle.dumps(game))`: Envia o objeto `game` serializado usando o módulo `pickle` do Python. O objeto `game` contém o estado atual do jogo.

## Estrutura do Código

### `server.py`

- Inicializa o servidor e aguarda conexões dos jogadores.
- Gerencia a lógica do jogo e a comunicação entre os jogadores.
- Para cada jogador conectado, ele cria uma threaded com a função `threaded_client` que vai gerenciar a comunicação e a lógica do jogo. 
- Utiliza a classe `Game` para representar o estado do jogo.

### `client.py`

- Conecta-se ao servidor e obtém o número do jogador atribuído pelo servidor.
- Interage com o jogador, envia os palpites e recebe as atualizações do estado do jogo.
- Utiliza a classe `Network` para gerenciar a comunicação em rede.

### `game.py`

- Define a classe `Game` que representa o estado do jogo.
- Contém métodos para definir o número secreto, pontuação dos jogadores, verificar o fim do jogo, mostrar o placar e reiniciar o jogo.

### `network.py`

- Implementa a classe `Network` que gerencia a comunicação em rede.
- Utiliza sockets para estabelecer a conexão com o servidor e enviar/receber dados.
- Converte os objetos Python em strings codificadas e vice-versa usando o módulo `pickle`.

## Contribuidores

- Samuel Correia Nascimento, 201920081
- Guilherme Guimarães Souza, 201920069