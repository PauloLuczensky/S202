class FamilyDatabase:
    def __init__(self, database):
        self.db = database

    #Buscando as profissoes
    def get_policial(self):
        query = "MATCH (p:Policial) RETURN p.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]

    def get_medico(self):
        query = "MATCH (m:Medico) RETURN m.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]

    def get_secretaria(self):
        query = "MATCH (s:Secretaria) RETURN s.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]

    def get_empresario(self):
        query = "MATCH (e:Empresario) RETURN e.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]

    def get_fazendeiro(self):
        query = "MATCH (f:Fazendeiro) RETURN f.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]

    def get_dona_de_casa(self):
        query = "MATCH (d:Dona_de_Casa) RETURN d.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]

    #Consultando os homens casados da familia
    def get_casados(self):
        query = "MATCH (p1:Pessoa)-[:CASADA_COM]->(p2:Pessoa) RETURN p1.nome AS nome1, p2.nome AS nome2"
        results = self.db.execute_query(query)
        nomes_casais = [result["nome1"] + " e " + result["nome2"] for result in results]
        return nomes_casais

    #Consultando os universitários da família
    def get_universitarios(self):
        query = "MATCH (u:Universitaria) RETURN u.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]

    #Consultando os solteiros da familia
    #OBS: Daniel eh separado, será considerado como solteiro
    def get_solteiros(self):
        query = "MATCH (p1:Pessoa {status: 'solteira'}) RETURN p1.nome AS nome"
        query1 = "MATCH (p2:Pessoa {status: 'separado'}) RETURN p2.nome AS nome"
        results = self.db.execute_query(query)
        nomes = [result["nome"] for result in results]
        results1 = self.db.execute_query(query1)
        nomes1 = [result["nome"] for result in results1]
        return nomes + nomes1

    #Buscando os pais do Ben
    def get_pais(self):
        query = "MATCH (p1:Pessoa{nome: 'Ben'})-[:FILHO_DE]->(p2:Pessoa) RETURN p2.nome AS nome"
        results = self.db.execute_query(query)
        return [result["nome"] for result in results]

    #Buscando o tempo de namoro entre a Gwen e o Kevin
    def tempo_de_namoro(self):
        query = "MATCH (p1:Pessoa{nome:'Gwen'})-[n:NAMORA_COM]->(p2:Pessoa{nome:'Kevin'}) RETURN n.anos_juntos AS anos_juntos "
        results = self.db.execute_query(query)
        return [result["anos_juntos"] for result in results]

    #Buscando os melhores amigos do Ben
    def get_best_friends(self):
        query = "MATCH (c:Cahorro{nome: 'Scooby'})-[:CACHORRO_DO]->(p:Pessoa{nome:'Ben'}) RETURN c.nome AS nome"
        query1 = "MATCH (p1:Pessoa{nome: 'Ben'})-[:PRIMO_DO]->(p2:Pessoa{nome:'Gilbert'}) RETURN p2.nome AS nome"
        results = self.db.execute_query(query)
        nomes = [result["nome"] for result in results]
        results1 = self.db.execute_query(query1)
        nomes1 = [result["nome"] for result in results1]
        return nomes + nomes1

    #Buscando quando os pais da Helena se casaram e aonde eles passaram a lua de mel
    def get_pais_Helena(self):
        query = "MATCH (p1:Pessoa{nome:'Maria'})-[c:CASADA_COM]->(p2:Pessoa{nome:'Antonio'}) RETURN c.data_casamento AS data_casamento" \
                ", c.lua_de_mel AS lua_de_mel"
        results = self.db.execute_query(query)
        casamento = [result["data_casamento"] + " e passaram a lua de mel em " + result["lua_de_mel"] for result in results]
        return casamento

    #Buscando os hobbies de cada membro da família
    def get_hobbies(self):
        query = "MATCH (p1:Pessoa) RETURN p1.nome AS nome, p1.hobby AS hobby  "
        results = self.db.execute_query(query)
        return ["O hobby do(a) " + result["nome"] + " eh " + result["hobby"] for result in results]

    #Buscando a comida favorita do Scooby
    def get_comida_favorita(self):
        query = "MATCH (p:Pet) RETURN p.nome AS nome, p.comida_favorita AS comida_favorita  "
        results = self.db.execute_query(query)
        return ["A comida favorita do " + result["nome"] + " eh " + result["comida_favorita"] for result in results]





