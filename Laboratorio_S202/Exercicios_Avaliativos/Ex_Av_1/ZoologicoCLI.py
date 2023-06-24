from Database import Database
from Classes_1 import Cuidador
from Classes_1 import Habitat
from Classes_1 import Animal
from ZoologicoDAO import ZoologicoDao

db = Database(database="Exercicio_Avaliativo", collection="Zoologico")
data = db.collection.find()
zoologico = ZoologicoDao(db)

#Criando um Animal com habitat e cuidador

print("Opcao 1 - Inserir um novo Animal, incluindo um cuidador e um habitat ")
print("Opcao 2 - Ler um animal do banco")
print("Opcao 3 - Atualizar um animal")
print("Opcao 4 - Deletar um animal")
print("Opcao 5 - Sair do Banco de Dados")
flag = True

while (flag):
    opcao = int(input("Digite uma opcao"))
    match opcao:
        case 1:
            print("Inserindo um cuidador")
            print("Digite o id do cuidador")
            id_cuidador = int(input())
            print("Insira o nome do cuidador")
            nome_cuidador = input()
            print("Insira o documento do cuidador")
            documento_cuidador = input()
            print("Cuidador inserido com sucesso")

            print("--------------------------")

            print("Inserindo um habitat")
            print("Digite o id do habitat")
            id_habitat = int(input())
            print("Insira o nome do habitat")
            nome_habitat = input()
            print("Insira o tipo Ambiente")
            tipo_ambiente = input()
            print("Habitat inserido com sucesso")

            print("--------------------------")

            print("Inserindo um animal")
            print("Insira o nome do animal")
            nome_animal = input()
            print("Insira a especie do animal")
            especie_animal = input()
            print("Insira a idade do animal")
            idade = int(input())
            print("Animal inserido com sucesso")

            cuidador = Cuidador(id_cuidador, nome_cuidador, documento_cuidador)
            habitat = Habitat(id_habitat, nome_habitat, tipo_ambiente,cuidador)
            animal = Animal(nome_animal, especie_animal, idade, habitat)

            #Realizando um create
            zoologico.create_Animal(animal, habitat, cuidador)
            flag = True

        case 2:
            #Lendo os dados do banco referente a um animal
            print("Insira o id do animal desejado para buscar seu documento")
            id = input()
            zoologico.read_animal_by_id(id)
            flag = True


        case 3:
            #Atualizando um animal
            print("Insira o id do animal")
            id = input()
            print("Digite o novo nome do animal")
            nome_atualizado = input()
            print("Digite a nova especie do animal atualizado")
            especie_atualizada = input()
            zoologico.update_animal(id, nome_atualizado, especie_atualizada )
            flag = True

        case 4:
            #Deletando um animal
            print("Insira o id para deletar o animal")
            id = input()
            zoologico.delete_animal(id)
            flag = True

        case 5:
            print("Voce saiu do Banco de Dados")
            flag = False

