class jogador():
    def __init__(self, nome, altura, velocidade, passe, dible, precisao):
        self.nome = nome
        self.altuta = altura
        self.velocidade = velocidade
        self.passe = passe
        self.dible = dible
        self.precisao = precisao

    def chutar (self):
        print(" chutar a bola  ")
    
    def corre(self):
        print(" correr no campo")

    def defender(self):
        print(" Tentar tirar a bola do adversario")

class goleiro(jogador):
    def agarra(self):
        print("segurar a bola")

    def defender(self):
        fora_da_area = False
        if goleiro == fora_da_area:
            print(" usar apenas os pés cabeça e ombro")
        else:
            print("Pode usar qualquer parte de corpo")

class jogador_linha(jogador):
    def defender(self):
        print("contra atacar")
        super().defender()

#jogador1 = goleiro("sidney", 1.78, 70, 60, 80, 90)
#jogador1.chutar()
#jogador1.corre()
#jogador1.agarra()
jogador1 = jogador("sidney", 1.78, 70, 60, 80, 90)
jogador1.defender()