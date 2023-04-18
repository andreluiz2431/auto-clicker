# Nesta primeira seção do código, são importados os módulos necessários para a execução do programa, incluindo time, threading, pynput.mouse, pynput.keyboard.
import time
import threading
from pynput.mouse import Button, Controller
from pynput.keyboard import Listener, KeyCode

# Aqui são definidas algumas variáveis que serão usadas posteriormente no programa. O delay é o tempo que será dado entre os cliques, button define qual botão do mouse será usado (no caso, o botão esquerdo), e start_stop_key e exit_key definem as teclas de atalho que o usuário poderá usar para iniciar/parar o programa e sair do programa, respectivamente.
delay = 1.0
button = Button.left
start_stop_key = KeyCode(char='s')
exit_key = KeyCode(char='e')

# Nesta parte do código é definida a classe ClickMouse, que é responsável por criar um objeto que, 
# quando iniciado, simula o clique do mouse em uma posição específica. 
# O objeto ClickMouse é uma thread, o que significa que ele é executado independentemente do restante do programa. 
# As funções start_clicking(), stop_clicking(), exit(), add_click() e play_sequence() definem as ações que podem ser realizadas no objeto ClickMouse. 
# A função run() é responsável por executar o objeto ClickMouse em um loop até que o programa seja encerrado.
class ClickMouse(threading.Thread):
    def __init__(self, delay):
        super(ClickMouse, self).__init__()
        self.delay = delay
        self.running = False
        self.program_running = True
        self.clicks = []

    # Função que inicia o clique do mouse
    def start_clicking(self):
        self.running = True

    # Função que para o clique do mouse
    def stop_clicking(self):
        self.running = False

    # Função que encerra o programa
    def exit(self):
        self.stop_clicking()
        self.program_running = False

    # Função que adiciona um novo clique na lista
    def add_click(self, position, button):
        self.clicks.append((position, button))

    # Função que executa a sequência de cliques armazenada na lista
    def play_sequence(self):
        for position, button in self.clicks:
            mouse.position = position
            mouse.click(button)
            time.sleep(self.delay)

    # Função que é executada quando a thread é iniciada
    def run(self):
        while self.program_running:
            while self.running:
                self.play_sequence()
            time.sleep(0.1)

# Aqui, é criado um objeto Controller para controlar o mouse. 
# Em seguida, um objeto ClickMouse é criado com base no valor da variável delay definida anteriormente
# iniciado com a função start(). 
mouse = Controller()
click_thread = ClickMouse(delay)
click_thread.start()

# As variáveis set_position_key, left_click_key, right_click_key e play_sequence_key definem as teclas de atalho que o usuário pode usar para executar ações.
set_position_key = KeyCode(char='w')
left_click_key = KeyCode(char='z')
right_click_key = KeyCode(char='x')
play_sequence_key = KeyCode(char='q')

# Função que é executada quando uma tecla é pressionada
def on_press(key):
    if key == start_stop_key:
        if click_thread.running:
            click_thread.stop_clicking()
        else:
            click_thread.start_clicking()
    elif key == exit_key:
        click_thread.exit()
        listener.stop()
    elif key == set_position_key:
        global last_position
        last_position = mouse.position
    elif key == left_click_key:
        click_thread.add_click(last_position, Button.left)
    elif key == right_click_key:
        click_thread.add_click(last_position, Button.right)
    elif key == play_sequence_key:
        if not click_thread.running:
            click_thread.start_clicking()

# Criando um listener para as teclas de atalho
with Listener(on_press=on_press) as listener:
    listener.join()
