#Relatório 1 - BD 2

class Animal:
    def __init__(self, nome, idade, especie, cor, som):
        self.nome = str(nome)
        self.idade = str(idade)
        self.especie = str(especie)
        self.cor = str(cor)
        self.som = str(som)

    def emitir_som(self, som):
        return som

    def mudar_cor(self, nova_cor):
        self.cor = nova_cor
        return nova_cor

#Inserindo os atributos
nome = input(str())
idade = input(str())
especie = input(str())
cor = input(str())
som = str("Brummm")
tamanho = input(str())

#Criando uma classe Elefante que herda de Animal
class Elefante(Animal):

    def __init__(self,nome, idade, especie, cor, som,tamanho):
        super().__init__(nome, idade, especie, cor, som)
        self.tamanho = str(tamanho)

    def trombar(self, som):
        return som

    def mudar_tamanho(self, novo_tamanho):
        self.tamanho = novo_tamanho
        return novo_tamanho

elefante = Elefante(nome, idade, especie, cor, som, tamanho)

if elefante.especie == "Africano" and int(elefante.idade) <= 10:
    print(elefante.mudar_tamanho("Pequeno"))
    print(elefante.trombar("Paaah"))

elif elefante.especie == "Africano" and int(elefante.idade) >= 10:
    print(elefante.mudar_tamanho("Grande"))
    print(elefante.trombar("PAHHHHH"))

else:
    print(elefante.tamanho)
    print(elefante.som)