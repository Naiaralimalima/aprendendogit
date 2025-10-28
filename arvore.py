# Classe base: Personagem
class Personagem:
    def __init__(self, nome, nivel_poder, tipo):
        self.nome = nome
        self.nivel_poder = nivel_poder
        self.tipo = tipo

    def mostrar_info(self):
        print(f"Nome: {self.nome} | Nível de Poder: {self.nivel_poder} | Tipo: {self.tipo}")


# Classe derivada: Chefe (herda de Personagem)
class Chefe(Personagem):
    def __init__(self, nome, nivel_poder, tipo, reino):
        super().__init__(nome, nivel_poder, tipo)
        self.reino = reino

    def mostrar_info(self):
        print(f"Nome: {self.nome} | Nível de Poder: {self.nivel_poder} | Tipo: {self.tipo} | Reino: {self.reino}")


# Nó da árvore
class NoPersonagem:
    def __init__(self, personagem):
        self.personagem = personagem
        self.esquerda = None
        self.direita = None


# Árvore da Floresta
class ArvoreFloresta:
    def __init__(self):
        self.raiz = None

    def adicionar(self, personagem):
        novo_no = NoPersonagem(personagem)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            self._adicionar_recursivo(self.raiz, novo_no)

    def _adicionar_recursivo(self, no_atual, novo_no):
        if novo_no.personagem.nivel_poder < no_atual.personagem.nivel_poder:
            if no_atual.esquerda is None:
                no_atual.esquerda = novo_no
            else:
                self._adicionar_recursivo(no_atual.esquerda, novo_no)
        else:
            if no_atual.direita is None:
                no_atual.direita = novo_no
            else:
                self._adicionar_recursivo(no_atual.direita, novo_no)

    def percorrer_em_ordem(self):
        print("\n🌿 Personagens da Floresta Encantada (do menos ao mais poderoso):\n")
        self._percorrer_em_ordem_recursivo(self.raiz)

    def _percorrer_em_ordem_recursivo(self, no_atual):
        if no_atual is not None:
            self._percorrer_em_ordem_recursivo(no_atual.esquerda)
            no_atual.personagem.mostrar_info()
            self._percorrer_em_ordem_recursivo(no_atual.direita)


# --- Execução / Teste ---
if __name__ == "__main__":
    floresta = ArvoreFloresta()

    # Criando personagens
    p1 = Personagem("Lupi", 15, "Animal")
    p2 = Personagem("Mago Merlin", 40, "Mago")
    p3 = Personagem("Fada Luzia", 25, "Fada")
    p4 = Personagem("Elfo Darlan", 30, "Elfo")
    c1 = Chefe("Dragão Vermelho", 70, "Dragão", "Montanhas Flamejantes")
    c2 = Chefe("Rainha das Sombras", 55, "Maga", "Floresta das Sombras")

    # Adicionando à árvore
    floresta.adicionar(p1)
    floresta.adicionar(p2)
    floresta.adicionar(p3)
    floresta.adicionar(p4)
    floresta.adicionar(c1)
    floresta.adicionar(c2)

    # Percorrer e exibir
    floresta.percorrer_em_ordem()
