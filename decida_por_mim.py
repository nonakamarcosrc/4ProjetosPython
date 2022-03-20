# Projeto 5 - Decida por mim
# Faça uma pergunta para o programa e ele terá que te dar uma resposta
import random
import PySimpleGUI as sg


class DecidaPorMim:
    def __init__(self):
        self.respostas = [
            'Com certeza, você deve fazer isso!',
            'Não sei, você que sabe',
            'Não faz isso Não!',
            'Acho que tá na hora certa!'
        ]

    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Faça sua pergunta:')],
            [sg.Input()],
            [sg.Output(size=(50, 10))],
            [sg.Button('Decida por mim')]
        ]
        # criar a janela
        self.janela = sg.Window('Decida por Mim!', layout=layout)
        while True:
            # Ler os valores
            self.eventos, self.valores = self.janela.Read()
            # Fazer algo com os valores
            if self.eventos == 'Decida por mim':
                print(random.choice(self.respostas))
            if self.eventos == sg.WIN_CLOSED:
                break
        self.janela.close()

decida = DecidaPorMim()
decida.Iniciar()