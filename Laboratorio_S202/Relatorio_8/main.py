from database import Database
from JogoDatabase import JogoDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://34.205.89.154:7687", "neo4j", "admiralty-hoist-semicolons")
db.drop_all()

jogo_db = JogoDatabase(db)

#Criando os jogadores, insere-se os id's e os nomes, respectivamente
jogo_db.create_player("1", "Wagner")
jogo_db.create_player("2", "Pedro")
jogo_db.create_player("3", "Pietro")
jogo_db.create_player("4", "Amanda")

#Criando as partidas, insere-se os id_match's e os resultados, respectivamente
jogo_db.create_match("1", "95")
jogo_db.create_match("2", "30")
jogo_db.create_match("3", "70")
jogo_db.create_match("4", "85")

#Criando os relacionamentos entre as partidas e os jogadores
#Insere-se o nome do jogador e o identificador_match, respectivamente
jogo_db.create_partida("Wagner", "1")
jogo_db.create_partida("Pedro", "2")
jogo_db.create_partida("Pietro", "3")
jogo_db.create_partida("Amanda", "4")

#Atualizando um nome de um jogador
jogo_db.update_player("Pedro", "Gabriel")
jogo_db.update_player("Pietro", "Mariana")

#Atualizando o resultado de um Match
jogo_db.update_match("95", "20")
jogo_db.update_match("30", "65")

#Deletando um jogador
jogo_db.delete_player("1")

#Deletando um Match
jogo_db.delete_match("2")

print("A lista de nomes de jogadores do Banco de Dados eh:")
print(jogo_db.get_player())
print("A lista de nomes de match's do Banco de Dados eh:")
print(jogo_db.get_match())

db.close()