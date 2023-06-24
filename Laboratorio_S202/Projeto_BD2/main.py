from database import Database
from Filme import Filme
from Personagem import Personagem

db = Database("bolt://54.172.159.100:7687", "neo4j", "name-jump-safeguard")

print("Ola! Bem vindo ao Banco de Dados!\n")
filme_db = Filme(db)
personagem_db = Personagem(db)

flag = True
disney = True
pixar = True

while flag:
    print("Qual estudio voce deseja acessar?")
    print("Opcao: 1 - Disney")
    print("Opcao: 2 - Pixar")
    print("Opcao: 3 - Sair do Banco de Dados")

    opcao = int(input("Digite a opcao:"))

    match opcao:
        case 1:
            while disney:
                print("Bem-vindo ao Banco de Dados da Disney!")
                print("O que voce deseja fazer hoje?")
                print("1- Criar um filme")
                print("2- Atualizar um filme")
                print("3- Deletar um filme")
                print("4- Criar um personagem")
                print("5- Atualizar um personagem")
                print("6- Deletar um personagem")
                print("7- Criar um relacionamento entre filme e estudio")
                print("8- Criar um relacionamento entre filme e personagem")
                print("9- Criar um relacionamento entre os personagens")
                print("10- Buscando todos os filmes")
                print("11- Buscando os casais dos filmes")
                print("12- Buscando os protagonistas dos filmes")
                print("13- Qual foi a bilheteria total arrecadada?")
                print("14- Sair do Banco de Dados da Disney")


                opcao_disney = int(input("Digite a opcao desejada:"))

                match opcao_disney:
                    case 1:
                        print("Adicionando um filme:")
                        nome = input("Digite o nome do filme: ")
                        lancamento = int(input("Quando o filme foi lançado? "))
                        duracao = (input("Digite a duração do filme: "))
                        oscar = (input("O filme ganhou o Oscar? (True - Sim; False - Não)"))
                        musica_principal = input("Digite a musica principal:")
                        filme_db.create_filme(nome, lancamento, duracao, oscar, musica_principal)
                        print("Filme criado com sucesso!")

                    case 2:
                        print("Atualizando a musica do filme:")
                        nome = input("Digite o nome do filme: ")
                        musica_nova = input("Digite a musica nova: ")
                        filme_db.update_musica(nome, musica_nova)
                        print("Musica atualizada com sucesso!")

                    case 3:
                        nome = input("Digite o nome do filme que você deseja deletar: ")
                        filme_db.delete_filme(nome)
                        print("Filme deletado com sucesso!")

                    case 4:
                        print("Adicionando um personagem:")
                        nome = input("Digite o nome: ")
                        sexo = input("Digite o sexo do personagem: ")
                        tipo = input("O personagem eh o quê? (Ex: humano, brinquedo, fada) ")
                        personagem_db.create_personagem(nome, sexo, tipo)
                        print("Personagem criado com sucesso!")

                    case 5:
                        print("Atualizando um personagem")
                        nome_antigo = input("Digite o nome do personagem que se deseja atualizar")
                        nome_novo = input("Digite o nome novo do personagem: ")
                        personagem_db.update_personagem(nome_antigo, nome_novo)
                        print("Personagem atualizado com sucesso!")

                    case 6:
                        print("Deletando um personagem")
                        nome = input("Digite o nome do personagem a ser deletado: ")
                        personagem_db.delete_personagem(nome)
                        print("Personagem deletado com sucesso!")

                    case 7:
                        print("Criando um relacionamento entre filme e estudio")
                        nome_filme = input("Digite o nome do filme: ")
                        diretor = input("Digite o nome do diretor do filme: ")
                        bilheteria = int(input("Quanto foi a bilheteria do filme: "))
                        filme_db.create_relationship_estudio_filme(nome_filme, diretor, bilheteria)
                        print("Relacionamento criado com sucesso!")

                    case 8:
                        print("Criando um relacionamento entre filme e personagem")
                        nome_filme = input("Digite o nome do filme: ")
                        nome_personagem = input("Digite o nome do personagem do filme: ")
                        protagonista = (input("O personagem eh o protagonista? (True - Sim; False - Não )"))
                        personagem_db.create_relationship_filme_personagem(nome_filme, nome_personagem, protagonista)
                        print("Relacionamento criado com sucesso!")

                    case 9:
                        print("Criando um relacionamento entre personagens")
                        nome_personagem1 = input("Digite o nome do personagem 1: ")
                        nome_personagem2 = input("Digite o nome do personagem 2: ")
                        tipo_relacionamento = input("Digite o tipo do relacionamento entre os personagens")
                        amigos = (input("Os personagens são amigos?"))
                        casal = (input("Eles formam um casal?"))
                        inimigo = (input("Eles são inimigos?"))
                        personagem_db.create_relationship_entre_personagens(nome_personagem1, nome_personagem2, tipo_relacionamento, amigos, casal, inimigo)
                        print("Relacionamento criado com sucesso!")

                    case 10:
                        print("Retornando todos os filmes da Disney presentes no BD: ")
                        print(filme_db.get_filmes_disney())

                    case 11:
                        print("Retornando todos os casais dos filmes")
                        print("Os casais dos filmes da Disney são: ", personagem_db.get_casal())

                    case 12:
                        print("Retornando os protagonistas dos filmes")
                        print("Os protagonistas dos filmes são", personagem_db.get_protagonista_disney())

                    case 13:
                        print("A bilheteria total arrecadada foi de: ", filme_db.get_bilheteria(), "milhões de dólares")

                    case 14:
                        disney = False
                        print("Saindo do Banco de Dados relacionados à Disney")

        case 2:
            while pixar:
                print("Bem vindo ao Banco de Dados da Pixar!")
                print("O que voce deseja fazer hoje?")
                print("1- Criar um filme")
                print("2- Atualizar um filme")
                print("3- Deletar um filme")
                print("4- Criar um personagem")
                print("5- Atualizar um personagem")
                print("6- Deletar um personagem")
                print("7- Criar um relacionamento entre filme e estudio")
                print("8- Criar um relacionamento entre filme e personagem")
                print("9- Criar um relacionamento entre os personagens")
                print("10- Buscando todos os filmes")
                print("11- Retornar os filmes que ganharam o Oscar")
                print("12- Buscar o filme com maior bilheteria")
                print("13- Buscar o filme com maior nota no Rotten Tomatoes")
                print("14- Sair do Banco de Dados da Pixar")

                opcao_pixar = int(input("Digite a opcao desejada:"))

                match opcao_pixar:

                    case 1:
                        print("Adicionando um filme:")
                        nome = input("Digite o nome do filme: ")
                        lancamento = int(input("Quando o filme foi lançado? "))
                        duracao = int(input("Digite a duração do filme: "))
                        oscar = (input("O filme ganhou o Oscar? (True - Sim; False - Não) "))
                        genero = input("Digite o genero do filme:")
                        filme_db.create_filme_pixar(nome, lancamento, duracao, oscar, genero)
                        print("Filme criado com sucesso!")

                    case 2:
                        print("Atualizando um filme:")
                        nome = input("Digite o nome do filme: ")
                        genero_novo = input("Digite o genero novo: ")
                        filme_db.update_genero(nome, genero_novo)
                        print("Gênero atualizado com sucesso!")

                    case 3:
                        nome = input("Digite o nome do filme que você deseja deletar: ")
                        filme_db.delete_filme(nome)
                        print("Filme deletado com sucesso!")

                    case 4:
                        print("Adicionando um personagem:")
                        nome = input("Digite o nome: ")
                        sexo = input("Digite o sexo do personagem: ")
                        tipo = input("O personagem eh o quê? (Ex: humano, brinquedo, fada) ")
                        personagem_db.create_personagem(nome, sexo, tipo)
                        print("Personagem criado com sucesso!")

                    case 5:
                        print("Atualizando um personagem")
                        nome_antigo = input("Digite o nome do personagem que se deseja atualizar")
                        nome_novo = input("Digite o nome novo do personagem: ")
                        personagem_db.update_personagem(nome_antigo, nome_novo)
                        print("Personagem atualizado com sucesso!")

                    case 6:
                        print("Deletando um personagem")
                        nome = input("Digite o nome do personagem a ser deletado: ")
                        personagem_db.delete_personagem(nome)
                        print("Personagem deletado com sucesso!")

                    case 7:
                        print("Criando um relacionamento entre filme e estudio")
                        nome_filme = input("Digite o nome do filme: ")
                        diretor = input("Digite o nome do diretor do filme: ")
                        bilheteria = int(input("Quanto foi a bilheteria do filme: "))
                        nota_rotten_tomatoes = int(input("Qual a nota do filme no Rotten Tomatoes (nota de 0 a 10)"))
                        filme_db.create_relationship_estudio_filme_pixar(nome_filme, diretor, bilheteria, nota_rotten_tomatoes)
                        print("Relacionamento criado com sucesso!")

                    case 8:
                        print("Criando um relacionamento entre filme e personagem")
                        nome_filme = input("Digite o nome do filme: ")
                        nome_personagem = input("Digite o nome do personagem do filme: ")
                        protagonista = (input("O personagem eh o protagonista? (True - Sim; False - Não )"))
                        personagem_db.create_relationship_filme_personagem(nome_filme, nome_personagem, protagonista)
                        print("Relacionamento criado com sucesso!")

                    case 9:
                        print("Criando um relacionamento entre personagens")
                        nome_personagem1 = input("Digite o nome do personagem 1: ")
                        nome_personagem2 = input("Digite o nome do personagem 2: ")
                        tipo_relacionamento = input("Digite o tipo do relacionamento entre os personagens")
                        amigos = (input("Os personagens são amigos?"))
                        casal = (input("Eles formam um casal?"))
                        inimigo = (input("Eles são inimigos?"))
                        personagem_db.create_relationship_entre_personagens(nome_personagem1, nome_personagem2, tipo_relacionamento,
                                                                            amigos, casal, inimigo)
                        print("Relacionamento criado com sucesso!")

                    case 10:
                        print("Retornando os filmes da Pixar:", filme_db.get_filmes_pixar())

                    case 11:
                        print("Os filmes que ganharam da Oscar ", filme_db.get_oscar())

                    case 12:
                        print("O filme da Pixar com maior bilheteria foi ", filme_db.get_maior_bilheteria())

                    case 13:
                        print("O filme com maior nota do Rotten Tomatoes", filme_db.get_nota_rotten_tomatoes())

                    case 14:
                        pixar = False
                        print("Saindo do Banco de Dados da Pixar!")

        case 3:
            flag = False
            print("Você saiu do Banco de Dados! Tenha um bom dia! :)")


db.close()