class Personagem:

    def __init__(self, database):
        self.db = database

    def create_personagem(self, nome, sexo, tipo):
        query = "CREATE (p:Personagem {nome: $nome, sexo: $sexo, tipo: $tipo}) "
        parameters = {"nome": nome, "sexo": sexo, "tipo": tipo}
        self.db.execute_query(query, parameters)

    def update_personagem(self, nome, novo_nome):
        query = "MATCH (p:Personagem {nome: $nome}) SET p.nome = $novo_nome "
        parameters = {"nome": nome, "novo_nome": novo_nome}
        self.db.execute_query(query, parameters)

    def delete_personagem(self, nome):
        query = "MATCH (p:Personagem {nome: $nome}) DETACH DELETE p"
        parameters = {"nome": nome}
        self.db.execute_query(query, parameters)

    def create_relationship_filme_personagem(self, nome_filme, nome_personagem, protagonista):
        query = "MATCH (f:Filme {nome_filme: $nome_filme}), (p:Personagem {nome: $nome_personagem}) " \
                "CREATE (f)-[:POSSUI {protagonista: $protagonista}]->(p)"
        parameters = {"nome_filme": nome_filme, "nome_personagem": nome_personagem, "protagonista": protagonista}
        self.db.execute_query(query, parameters)

    def create_relationship_entre_personagens(self, nome_p1, nome_p2, tipo_relacionamento, amigos, casal, inimigos):
        query = "MATCH (p1:Personagem {nome: $nome_p1}), (p2:Personagem {nome: $nome_p2}) " \
                "CREATE (p1)-[r:" + tipo_relacionamento + " {amigos: $amigos, casal: $casal, inimigos: $inimigos}]->(p2)"
        parameters = {"nome_p1": nome_p1, "nome_p2": nome_p2, "amigos": amigos, "casal": casal, "inimigos": inimigos}
        self.db.execute_query(query, parameters)

    def get_casal(self):
        query = "MATCH (e:Estudio {nome:'Disney'})-[:PRODUZIU]->(f:Filme)-[p:POSSUI]->(p1:Personagem)-[:NAMORA_COM]->(p2:Personagem) RETURN p1.nome AS nome1, p2.nome AS nome2"
        results = self.db.execute_query(query)
        nomes_casais = [result["nome1"] + " e " + result["nome2"] for result in results]
        return nomes_casais

    def get_protagonista_disney(self):
        query = "MATCH (e:Estudio {nome:'Disney'})-[:PRODUZIU]->(f:Filme)-[p:POSSUI]->(p2:Personagem) WHERE p.protagonista = 'true' RETURN p2.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]






