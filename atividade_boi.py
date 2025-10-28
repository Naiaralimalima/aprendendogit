# ==========================
# CLASSE BASE: BOI
# ==========================
class Boi:
    def __init__(self, nome, cor):
        self.__nome = nome
        self.__cor = cor
        self.__pontuacao = 0.0

    def get_nome(self):
        return self.__nome

    def get_cor(self):
        return self.__cor

    def get_pontuacao(self):
        return self.__pontuacao

    def set_pontuacao(self, valor):
        if valor >= 0:
            self.__pontuacao = valor

    def adicionar_pontos(self, valor):
        if valor > 0:
            self.__pontuacao += valor

    def mostrar_info(self):
        print(f"Boi: {self.__nome}")
        print(f"Cor: {self.__cor}")
        print(f"Pontuação: {self.__pontuacao:.2f}")


# ==========================
# CLASSE DERIVADA: BOI ESPECIAL
# ==========================
class BoiEspecial(Boi):
    def __init__(self, nome, cor, categoria_especial):
        super().__init__(nome, cor)
        self.__categoria_especial = categoria_especial

    def mostrar_info(self):
        super().mostrar_info()
        print(f"Categoria Especial: {self.__categoria_especial}")
        print("-" * 30)


# ==========================
# CLASSE: JURADO
# ==========================
class Jurado:
    def __init__(self, nome, nota_caprichoso, nota_garantido):
        self.nome = nome
        self.nota_caprichoso = nota_caprichoso
        self.nota_garantido = nota_garantido

    def avaliar(self):
        return {
            "nome": self.nome,
            "caprichoso": self.nota_caprichoso,
            "garantido": self.nota_garantido
        }


# ==========================
# CLASSE: NÓ DA ÁRVORE DE JURADOS
# ==========================
class NoJurado:
    def __init__(self, jurado):
        self.jurado = jurado
        self.esquerda = None
        self.direita = None


# ==========================
# CLASSE: ÁRVORE DE JURADOS
# ==========================
class ArvoreDeJurados:
    def __init__(self):
        self.raiz = None

    def adicionar_jurado(self, jurado):
        novo_no = NoJurado(jurado)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            self._inserir(self.raiz, novo_no)

    def _inserir(self, no_atual, novo_no):
        if novo_no.jurado.nome < no_atual.jurado.nome:
            if no_atual.esquerda is None:
                no_atual.esquerda = novo_no
            else:
                self._inserir(no_atual.esquerda, novo_no)
        else:
            if no_atual.direita is None:
                no_atual.direita = novo_no
            else:
                self._inserir(no_atual.direita, novo_no)

    def percorrer_em_ordem(self):
        jurados = []
        self._em_ordem(self.raiz, jurados)
        return jurados

    def _em_ordem(self, no, jurados):
        if no:
            self._em_ordem(no.esquerda, jurados)
            jurados.append(no.jurado)
            self._em_ordem(no.direita, jurados)


# ==========================
# CLASSE: COMPETIÇÃO
# ==========================
class Competicao:
    def __init__(self, boi_azul, boi_vermelho, arvore_jurados):
        self.boi_azul = boi_azul
        self.boi_vermelho = boi_vermelho
        self.arvore_jurados = arvore_jurados

    def somar_pontuacoes(self):
        jurados = self.arvore_jurados.percorrer_em_ordem()
        for jurado in jurados:
            self.boi_azul.adicionar_pontos(jurado.nota_caprichoso)
            self.boi_vermelho.adicionar_pontos(jurado.nota_garantido)

    def mostrar_campeao(self):
        print("\n=== RESULTADO FINAL ===")
        self.boi_azul.mostrar_info()
        self.boi_vermelho.mostrar_info()

        if self.boi_azul.get_pontuacao() > self.boi_vermelho.get_pontuacao():
            print("🏆 O grande campeão é o BOI CAPRICHOSO! 💙")
        elif self.boi_azul.get_pontuacao() < self.boi_vermelho.get_pontuacao():
            print("🏆 O grande campeão é o BOI GARANTIDO! ❤️")
        else:
            print("🤝 Empate! Os bois brilharam igualmente este ano!")


# ==========================
# EXECUÇÃO DO PROGRAMA
# ==========================
if __name__ == "__main__":
    print("🎶 FESTIVAL DE PARINTINS 2026 🎶")
    print("--------------------------------\n")

    # Criação dos bois
    caprichoso = BoiEspecial("Caprichoso", "Azul", "Coreografia Perfeita")
    garantido = BoiEspecial("Garantido", "Vermelho", "Melhor Alegoria")

    # Criação da árvore de jurados
    arvore = ArvoreDeJurados()

    # Adicionando jurados
    arvore.adicionar_jurado(Jurado("Ana", 9.8, 9.6))
    arvore.adicionar_jurado(Jurado("Carlos", 9.7, 9.9))
    arvore.adicionar_jurado(Jurado("Bruna", 9.9, 9.8))

    # Criando competição
    disputa = Competicao(caprichoso, garantido, arvore)
    disputa.somar_pontuacoes()
    disputa.mostrar_campeao()
