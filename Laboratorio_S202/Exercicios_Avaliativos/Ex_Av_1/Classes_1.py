class Cuidador:
    def __init__(self, id, nome, documento):
        self.id  = int(id)
        self.nome = str(nome)
        self.documento = str(documento)


class Habitat:
    def __init__(self, id, nome, tipoAmbiente, cuidador):
        self.id = int(id)
        self.nome = str(nome)
        self.tipoAmbiente = str(tipoAmbiente)
        self.cuidador = Cuidador


class Animal:
    def __init__(self,  nome, especie, idade, habitat):
        #self.id = int(id)
        self.nome = str(nome)
        self.especie = str(especie)
        self.idade = int(idade)
        self. habitat = Habitat


