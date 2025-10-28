# class abstratas e interface 
# class abstrata é incompleta 
'''


class maquina(ABC): # classe abstrata
    @abstractmethod
    def ligar(self):
        pass

class liquidificador(maquina):
    def ligar(self):
        print("Liquidificador ligado bzzzz")


class ventilador(maquina):
    def ligar(self):
        print("Ventilador ligado")

#teste
liq = liquidificador()
vent = ventilador()
liq.ligar() # invocação do método ligar
vent.ligar()



from abc import ABC, abstractmethod

class carro(ABC): # classe abstrata
    @abstractmethod
    def ligar(self):
        pass
    def acelerar(self):
        pass
    def freiar(self):
        pass

class carro_popular(carro):
    def ligar(self):
        print("Ligar carro")
    def acelerar(self):
        print("carro acelerado")
    def freiar(self):
        print("carro freiar")
 




corsa = carro_popular()
corsa.ligar() # chamando o método ligar
corsa.acelerar() # chamando o método acelerar
corsa.freiar() # chamando o método freiar



from abc import ABC, abstractmethod

class PagamentoInterface(ABC): # classe abstrata
    @abstractmethod
    def processar_pagamento(self, valor):
        pass

class Pagamento_cartao(PagamentoInterface):
   def processar_pagamento(self, valor):
        print(f"processando pagemnto com cartão valor {valor} ")

class PagamentoPix(PagamentoInterface):
    def processar_pagamento(self, valor):
        print(f"Processando pagamento de {valor} via pix.")

def realizar_pagamento(servico:PagamentoInterface, valor ):
    servico.processar_pagamento(valor)

realizar_pagamento(Pagamento_cartao(), 100)
realizar_pagamento(PagamentoPix(), 50)



from abc import ABC, abstractmethod

class animalFalante(ABC): # classe abstrata
    @abstractmethod
    def falar(sel):
        pass
class Papagaio(animalFalante):
    def falar(self):
        print("Eu sou o loiro falante")

class GatoFofoqueiro(animalFalante):
    def falar(sef):
        print(" miauuuuu")
Papagaio_falante = Papagaio()
Gato = GatoFofoqueiro()
Papagaio_falante.falar()
Gato.falar()


'''
