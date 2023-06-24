class TeacherCRUD:
    def __init__(self, database):
        self.db = database

    #Criando os nós Teacher
    def create_teacher(self,name, ano_nasc, cpf):
        query = "CREATE(p:Professor {name: $name, ano_nasc: $ano_nasc, cpf: $cpf})"
        parameters = {"name": name, "ano_nasc": ano_nasc, "cpf": cpf}
        self.db.execute_query(query, parameters)

    #Lendo um nó Professor
    def read_teacher(self, name):
        query = "MATCH (p:Professor{name: $name}) RETURN p.name AS name"
        parameters = {"name": name}
        results = self.db.execute_query(query, parameters)
        return [result["name"] for result in results]

    #Deletando um nó Professor
    def delete_teacher(self, name):
        query = "MATCH (p:Professor {name: $name}) DETACH DELETE p"
        parameters = {"name": name}
        self.db.execute_query(query, parameters)

    #Atualizando um cpf através do nome
    def update_player(self, name, newCpf):
        query = "MATCH (p:Professor {name: $name}) SET p.cpf = $new_Cpf"
        parameters = {"name": name, "new_Cpf": newCpf}
        self.db.execute_query(query, parameters)


