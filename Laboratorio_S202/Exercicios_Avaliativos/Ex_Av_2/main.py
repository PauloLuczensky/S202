from database import Database
from TeacherCRUD import TeacherCRUD

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://54.209.178.42:7687", "neo4j", "hashmark-sets-alkalinity")
db.drop_all()

teacher_db = TeacherCRUD(db)

#Criando os professores
teacher_db.create_teacher("Chris Lima", 1956, "189.052.396-66")
teacher_db.create_teacher("Renzo", 1987, "179.142.999-00")
teacher_db.create_teacher("Marcelo", 1978, "576.051.453-33")
teacher_db.create_teacher("Guilherme", 2000, "222.222.292-22")

#Procurando um professor específico
print(teacher_db.read_teacher("Chris Lima"))

#Atualizando o cof de um determinado professor
teacher_db.update_player("Chris Lima", "162.052.777-77")
