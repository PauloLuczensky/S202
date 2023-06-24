from save_json import writeAJson
from pokedex import Database

db = Database(database="dex", collection="pokemons")
db.resetDatabase()
pokemons = db.collection.find()

#Realizando as queries no MongoDB

#1-Filtrando os pokemons com Speed <= 45
def Speed_less_than_45(speed: int):
    return db.collection.find({"base.Speed":{"$lte":speed}})

speed = Speed_less_than_45(45)
writeAJson(speed, "pokemon_speed")

#2-Selecionando os nomes dos pokemons que possuem menos ou 5 letras em ingles e frances
def get_5_letters_or_less(collection):
    names = collection.find({}, {"name.english": 1, "name.french": 2})
    five_letters = []
    for name in names:
        if len(name["name"].keys()) <= 5:
            if all(len(word) <= 5 for word in name["name"].values()):
                five_letters.append(name["name"].values())
    return five_letters

writeAJson(get_5_letters_or_less(db.collection), "pokemon_5_letters_or_less")

#3-Filtrando os Pokemons pelo tipo "Fire"
def getPokemonByType(type: str):
    return db.collection.find({"type": type})

fire = getPokemonByType("Fire")
writeAJson(fire, "Fire")

#4-Filtrando os Pokemons pelo tipo("Bug") e velocidade(<=30)
def Type_And_Speed(type:str, speed: int):
    return db.collection.find({"type":type, "base.Speed":{"$lte":speed}})

type_speed = Type_And_Speed("Bug", 45)
writeAJson(type_speed, "type_and_speed")


#5-Retornando o pokemon de id = 579
def getPokemonById(number: id):
    return db.collection.find({"id": number})

pokemon_misterioso = getPokemonById(579)
writeAJson(pokemon_misterioso, "pokemon_misterioso")

