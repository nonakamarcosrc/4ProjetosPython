import random
import PySimpleGUI as sg


class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True
        self.numero_tentativa = 0

    def Iniciar(self):
        # Layout
        layout = [
            [sg.Text('Seu chute ', size=(39, 0))],
            [sg.Input(size=(18, 0), key='ValorChute')],
            [sg.Button('Chutar!')],
            [sg.Output(size=(39, 10))]
        ]
        # Criar janela
        self.janela = sg.Window('Chute o número!', layout=layout)
        self.GerarNumeroAleatorio()
        try:
            while True:
                # Receber valores
                self.evento, self.valores = self.janela.Read()
                # Fazer alguma coisa com valores
                if self.evento == 'Chutar!':
                    self.valor_do_chute = self.valores['ValorChute']
                    while self.tentar_novamente == True:
                        if int(self.valor_do_chute) > self.valor_aleatorio:
                            self.numero_tentativa += 1
                            print('Chute um valor mais baixo')
                            break
                        elif int(self.valor_do_chute) < self.valor_aleatorio:
                            self.numero_tentativa += 1
                            print('Chute um valor mais alto: ')
                            break
                        if int(self.valor_do_chute) == self.valor_aleatorio:
                            self.tentar_novamente = False
                            print('Você acertou! ' + 'Número de tentativas', + (self.numero_tentativa))
        except:
            print('Favor digitar apenas números!')
            self.Iniciar()

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo, self.valor_maximo)

    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um número: ')


chute = ChuteONumero()
chute.Iniciar()
