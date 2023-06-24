class JogoDatabase:
    def __init__(self, database):
        self.db = database

    #Criando os nós Player e Match
    def create_player(self,identificador, nome):
        query = "CREATE(p:Player {identificador: $identificador, nome: $nome})"
        parameters = {"identificador": identificador, "nome": nome}
        self.db.execute_query(query, parameters)

    def create_match(self,identificador_match, resultado):
        query = "CREATE(m:Match {identificador_match: $identificador_match, resultado: $resultado})"
        parameters = {"identificador_match": identificador_match, "resultado": resultado}
        self.db.execute_query(query, parameters)

    #Definindo as fuções de CRUD para o nó Player
    def get_player(self):
        query = "MATCH (p:Player) RETURN p.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]

    def update_player(self, nome_antigo, nome_novo):
        query = "MATCH (p:Player {nome: $nome_antigo}) SET p.nome = $nome_novo"
        parameters = {"nome_antigo": nome_antigo, "nome_novo": nome_novo}
        self.db.execute_query(query, parameters)


    def delete_player(self, identificador):
        query = "MATCH (p:Player {identificador: $identificador}) DETACH DELETE p"
        parameters = {"identificador": identificador}
        self.db.execute_query(query, parameters)

    #Definindo as funções de CRUD para o nó Match
    def get_match(self):
        query = "MATCH (m:Match) RETURN m.identificador_match AS identificador_match"
        results = self.db.execute_query(query)
        return [result["identificador_match"] for result in results]

    def update_match(self, resultado_antigo, resultado_novo):
        query = "MATCH (m:Match {resultado: $resultado_antigo}) SET m.resultado = $resultado_novo"
        parameters = {"resultado_antigo": resultado_antigo, "resultado_novo": resultado_novo}
        self.db.execute_query(query, parameters)


    def delete_match(self, identificador_match):
        query = "MATCH (m:Match {identificador_match: $identificador_match}) DETACH DELETE m"
        parameters = {"identificador_match": identificador_match}
        self.db.execute_query(query, parameters)

    #Criando os relacionamentos entre os nós Player e Match

    def create_partida(self, nome, identificador_match):
        query = "MATCH (p:Player {nome: $nome}) MATCH (m:Match {identificador_match: $identificador_match}) CREATE (p)-[:JOGANDO_PARTIDA]->(m)"
        parameters = {"nome": nome, "identificador_match": identificador_match}
        self.db.execute_query(query, parameters)




