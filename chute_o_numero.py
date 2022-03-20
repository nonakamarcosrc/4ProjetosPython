import random

class ChuteONumero:
    def __init__(self):
        self.valor_aleatorio = 0
        self.valor_minimo = 1
        self.valor_maximo = 100
        self.tentar_novamente = True
        self.numero_tentativa = 0

    def Iniciar(self):
        # Chamada da função
        self.GerarNumeroAleatorio()
        self.PedirValorAleatorio()
        try:
            while self.tentar_novamente == True:
                if int(self.valor_do_chute) > self.valor_aleatorio:
                    print('Chute um valor mais baixo')
                    self.numero_tentativa += 1
                    self.PedirValorAleatorio()
                elif int(self.valor_do_chute) < self.valor_aleatorio:
                    print('Chute um valor mais alto: ')
                    self.numero_tentativa += 1
                    self.PedirValorAleatorio()
                if int(self.valor_do_chute) == self.valor_aleatorio:
                    self.tentar_novamente = False
                    print('Você acertou!' + 'Número de tentativas' ,+ (self.numero_tentativa))
        except:
            print('Favor digitar apenas números!')
            self.Iniciar()

    def GerarNumeroAleatorio(self):
        self.valor_aleatorio = random.randint(self.valor_minimo,self.valor_maximo)

    def PedirValorAleatorio(self):
        self.valor_do_chute = input('Chute um número: ')

chute = ChuteONumero()
chute.Iniciar()