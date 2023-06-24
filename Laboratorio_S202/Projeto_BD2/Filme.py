class Filme:

    def __init__(self, database):
        self.db = database

    def create_filme(self, nome_filme, lancamento, duracao, oscar, musica_principal):
        query = "CREATE (f:Filme {nome_filme: $nome_filme, lancamento: $lancamento, duracao: $duracao, oscar: $oscar, musica_principal: $musica_principal}) "
        parameters = {"nome_filme": nome_filme, "lancamento": lancamento, "duracao": duracao, "oscar": oscar, "musica_principal": musica_principal}
        self.db.execute_query(query, parameters)

    def update_musica(self, nome_filme, musica_nova):
        query = "MATCH (f:Filme {nome_filme: $nome_filme}) SET f.musica_principal = $musica_nova "
        parameters = {"nome_filme": nome_filme, "musica_nova": musica_nova}
        self.db.execute_query(query, parameters)

    def update_genero(self, nome_filme, genero_novo):
        query = "MATCH (f:Filme {nome_filme: $nome_filme}) SET f.genero = $genero_novo "
        parameters = {"nome_filme": nome_filme, "genero_novo": genero_novo}
        self.db.execute_query(query, parameters)

    def delete_filme(self, nome_filme):
        query = "MATCH (f:Filme {nome_filme: $nome_filme}) DETACH DELETE f"
        parameters = {"nome_filme": nome_filme}
        self.db.execute_query(query, parameters)

    def create_relationship_estudio_filme(self, nome_filme, diretor, bilheteria):
        query = "MATCH (e:Estudio {nome: 'Disney'}), (f:Filme {nome_filme: $nome_filme}) CREATE (e)-[:PRODUZIU {diretor: $diretor, bilheteria: $bilheteria}]->(f)"
        parameters = {"nome_filme": nome_filme, "diretor": diretor, "bilheteria": bilheteria}
        self.db.execute_query(query, parameters)

    def get_filmes_disney(self):
        query = "MATCH (e:Estudio {nome:'Disney'})-[:PRODUZIU]->(f:Filme) RETURN f.nome_filme AS nome_filme"
        results = self.db.execute_query(query)
        filmes = [result["nome_filme"] for result in results]
        return filmes

    def get_filmes_pixar(self):
        query = "MATCH (e:Estudio {nome:'Pixar'})-[:PRODUZIU]->(f:Filme) RETURN f.nome_filme AS nome_filme"
        results = self.db.execute_query(query)
        filmes = [result["nome_filme"] for result in results]
        return filmes

    def get_bilheteria(self):
        query = "MATCH (e:Estudio{nome:'Disney'})-[p:PRODUZIU]->(f:Filme) RETURN SUM(p.bilheteria) AS bilheteria "
        results = self.db.execute_query(query)
        return [result["bilheteria"] for result in results]

    def create_filme_pixar(self, nome_filme, lancamento, duracao, oscar, genero):
        query = "CREATE (f:Filme {nome_filme: $nome_filme, lancamento: $lancamento, duracao: $duracao, oscar: $oscar, genero: $genero}) "
        parameters = {"nome_filme": nome_filme, "lancamento": lancamento, "duracao": duracao, "oscar": oscar, "genero": genero}
        self.db.execute_query(query, parameters)

    def create_relationship_estudio_filme_pixar(self, nome_filme, diretor, bilheteria, nota_rotten_tomatoes):
        query = "MATCH (e:Estudio {nome: 'Pixar'}), (f:Filme {nome_filme: $nome_filme}) " \
                "CREATE (e)-[:PRODUZIU {diretor: $diretor, bilheteria: $bilheteria, nota_rotten_tomatoes: $nota_rotten_tomatoes}]->(f)"
        parameters = {"nome_filme": nome_filme, "diretor": diretor, "bilheteria": bilheteria, "nota_rotten_tomatoes": nota_rotten_tomatoes}
        self.db.execute_query(query, parameters)

    def get_oscar(self):
        query = "MATCH (e:Estudio{nome: 'Pixar'})-[p:PRODUZIU]->(f:Filme) WHERE f.oscar = 'true' RETURN f.nome_filme AS oscar "
        results = self.db.execute_query(query)
        return [result["oscar"] for result in results]

    def get_maior_bilheteria(self):
        query = "MATCH (e:Estudio{nome: 'Pixar'})-[p:PRODUZIU]->(f:Filme) " \
                "RETURN p.bilheteria AS bilheteria, f.nome_filme AS nome_filme ORDER BY p.bilheteria DESC LIMIT 1"
        result = self.db.execute_query(query)
        if result:
            nome_filme = result[0]["nome_filme"]
            bilheteria = result[0]["bilheteria"]
            return nome_filme + " arrecadou " + str(bilheteria)
        else:
            return "Nenhum filme encontrado"

    def get_nota_rotten_tomatoes(self):
        query = "MATCH (e:Estudio{nome: 'Pixar'})-[p:PRODUZIU]->(f:Filme) RETURN p.nota_rotten_tomatoes AS rotten_tomatoes, f.nome_filme AS nome_filme" \
                " ORDER BY p.nota_rotten_tomatoes DESC LIMIT 1"
        results = self.db.execute_query(query)
        nota_rotten_tomatoes = [result["nome_filme"] + " e a nota da Rotten Tomatoes " + str(result["rotten_tomatoes"]) for result in results]
        return nota_rotten_tomatoes







