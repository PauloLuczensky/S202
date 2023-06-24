from pymongo import MongoClient
from bson.objectid import ObjectId
from Database import Database
from Classes_1 import Animal
from Classes_1 import Habitat
from Classes_1 import Cuidador

db = Database(database="Exercicio_Avaliativo", collection="Zoologico")
data = db.collection.find()

class ZoologicoDao(Animal):

    def __init__(self, database):
        self.db = database
        self.collection = database.collection

    def create_Animal(self, Animal, Habitat, Cuidador) -> str:
        try:
            result = self.collection.insert_one({"nome": Animal.nome, "especie": Animal.especie, "idade": Animal.idade,"habitat_id": Habitat.id, "habitat nome": Habitat.nome,"habitat tipo Ambiente":Habitat.tipoAmbiente,"cuidador_id": Cuidador.id, "cuidador nome": Cuidador.nome, "cuidador documento": Cuidador.documento})
            animal_id = str(result.inserted_id)
            print(f"Animal's name: {Animal.nome}  created with id: {animal_id} is {Animal.idade} belongs with {Animal.especie} and lives in {Habitat.nome}")
            print(f"Cuidador's name: {Cuidador.nome}  created with id: {Cuidador.id} , document {Cuidador.documento}")
            return animal_id
        except Exception as error:
            print(f"An error occurred while creating a new animal: {error}")
            return None


    def read_animal_by_id(self, animal_id: str) -> dict:
        try:
            animal = self.collection.find_one({"_id": ObjectId(animal_id)})
            if animal:
                print(f"Animal found: {animal}")
                return animal
            else:
                print(f"No animal found with id {animal_id}")
                return None
        except Exception as error:
            print(f"An error occurred while reading person: {error}")
            return None


    def update_animal(self, animal_id: str, nome: str, especie: str) -> str:
        try:
            result = self.collection.update_one({"_id": ObjectId(animal_id)}, {"$set": {"nome": nome, "especie": especie}})
            if result.modified_count:
                print(f"Animal {animal_id} updated with name {nome} and specie {especie}")
            else:
                print(f"No animal found with id {animal_id}")
            return result.modified_count
        except Exception as error:
            print(f"An error occurred while updating animal: {error}")
            return None


    def delete_animal(self, animal_id: str) -> int:
        try:
            result = self.collection.delete_one({"_id": ObjectId(animal_id)})
            if result.deleted_count:
                print(f"Animal {animal_id} deleted")
            else:
                print(f"No Animal found with id {animal_id}")
            return result.deleted_count
        except Exception as error:
            print(f"An error occurred while deleting person: {error}")
            return None

