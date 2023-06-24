from database import Database
from FamilyDatabase import FamilyDatabase

# cria uma instância da classe Database, passando os dados de conexão com o banco de dados Neo4j
db = Database("bolt://54.225.21.33:7687", "neo4j", "associates-coordinate-strap")

familia_db = FamilyDatabase(db)

print("Olá! Bem vindo ao Banco de Dados da Family Tree!\n")
flag = True
while flag:
    print("Qual busca você gostaria de realizar?")
    print("Opção 1- Buscar uma determinada profissao realizada por um parente")
    print("Opção 2- Buscar os casais da familia")
    print("Opção 3- Buscar os universitários da família")
    print("Opção 4- Buscar os solteiros da família")
    print("Opção 5- Buscar os pais do Ben")
    print("Opção 6- Desde quando a Gwen namora com o Kevin?")
    print("Opção 7- Buscar os seus melhores amigos do Ben")
    print("Opção 8- Quando os pais da Helena se casaram e aonde eles passaram a Lua de Mel?")
    print("Opção 9- Busque os hobbies de todos memebros da família")
    print("Opção 10- Qual a comida favorita do Scooby?")
    print("Opção 11- Sair do Banco de Dados")
    opcao = int(input("Digite a sua opção:"))

    match opcao:
        case 1:
            print("Na sua familia há policial, medico, professor, secretaria, empresario, fazendeiro e dona de casa")
            profissao = input("Qual profissao voce deseja pesquisar?")
            if profissao == "Policial":
                print("O Policial da familia eh o", familia_db.get_policial())
            elif profissao == "Medico":
                print("O Medico da familia eh o", familia_db.get_medico())
            elif profissao == "Secretaria":
                print("A Secretaria da familia eh a", familia_db.get_secretaria())
            elif profissao == "Empresario":
                print("O Empresario da familia eh o", familia_db.get_empresario())
            elif profissao == "Fazendeiro":
                print("O Fazendeiro da familia eh o", familia_db.get_fazendeiro())
            elif profissao == "Dona de Casa":
                print("As Donas de Casa da familia são a", familia_db.get_dona_de_casa())

        case 2:
            print("Os casais da familia são:", familia_db.get_casados())

        case 3:
            print("Os Universitários da família são:", familia_db.get_universitarios())

        case 4:
            print("Os solteiros da familia são:", familia_db.get_solteiros())

        case 5:
            print("Os pais do Ben são:", familia_db.get_pais())

        case 6:
            print("Gwen e Kevin namoram há", familia_db.tempo_de_namoro(), "anos")

        case 7:
            print("Os melhores amigos do Ben são", familia_db.get_best_friends())

        case 8:
            print("Os pais da Helena se casaram em", familia_db.get_pais_Helena())

        case 9:
            print(familia_db.get_hobbies())

        case 10:
            print(familia_db.get_comida_favorita())

        case 11:
            flag = False
            print("Você saiu do Banco de Dados Family Tree")
            print("Tenha um bom dia! :)")
