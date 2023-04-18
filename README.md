# auto-clicker

O código selecionado é um script Python que utiliza a biblioteca pynput para criar um programa que efetua cliques automáticos do mouse em uma determinada posição. 


O programa permite especificar um atraso, definir a tecla de início e parada, adicionar novos cliques, definir sequências de cliques e reproduzi-los. 


A classe ClickMouse estende a classe threading.Thread e tem como atributos o atraso, o estado de execução do programa, o estado de execução dos cliques, a lista de cliques e um método para adicionar novos cliques. O método run() é responsável por executar o programa. 


O programa tem um listener que monitora as teclas pressionadas e executa as ações correspondentes. As teclas start_stop_key, exit_key e play_sequence_key iniciam/param a execução do programa, saem do programa e reproduzem sequências de cliques, respectivamente. 


As teclas set_position_key, left_click_key e right_click_key definem uma nova posição, adicionam um novo clique com o botão esquerdo ou direito do mouse na última posição definida, respectivamente. 


Para utilizar esse código é necessário ter instalada a biblioteca pynput.

