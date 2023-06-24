from database import Database
from model import BookModel
from save_json import writeAJson

db = Database(database="Relatorio_5", collection="Livros_2")
data = db.collection.find()
bookModel = BookModel(db)

#Fazendo um CRUD no database Relatorio 5, collection Livros

#1- Inserindo um novo livro
new_book = bookModel.create_book("Dom Casmurro", "Machado de Assis", 1899, 20.59)
new_book_1 = bookModel.create_book("Angustia", "Graciliano Ramos", 1936, 24.99)
new_book_2 = bookModel.create_book("Quincas Borba", "Machado de Assis", 1888, 45.99)
new_book_3 = bookModel.create_book("Casa Grande e Senzala", "Gilberto Freyre", 1933, 49.99)

#2- Lendo um livro do banco de dados
read_book = bookModel.read_book_by_id(new_book)
read_book1 = bookModel.read_book_by_id(new_book_1)
read_book2 = bookModel.read_book_by_id(new_book_2)
read_book3 = bookModel.read_book_by_id(new_book_3)
writeAJson((read_book,read_book1,read_book2, read_book3), "Livros_inseridos")

#3- Atualizando o dado de um determinado livro
updatebook = bookModel.update_book(new_book_1, "Vidas Secas", 19.9)
updatebook1 = bookModel.update_book(new_book_2, "Memorias Postumas de Braz Cubas", 21.99)

#4- Deletando um livro do Bando de Dados
delete_book = bookModel.delete_book(new_book_2)

