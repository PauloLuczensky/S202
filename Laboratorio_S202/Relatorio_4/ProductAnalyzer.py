from database import Database

db = Database(database="loja_de_roupas", collection="vendas")
db.resetDatabase()
data = db.collection.find()


# 1- Retorne o total que o cliente B gastou
class ProductAnalyzer:
    def gasto_cliente_B(db):
        return db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$match": {"cliente_id": "B"}},
            {"$group": {"_id": {"cliente": "$cliente_id"},
                        "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
        ])

    # 2- Retorne o produto menos vendido em todas as compras
    def produto_menos_vendido(db):
        return db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.nome", "total": {"$sum": "$produtos.quantidade"}}},
            {"$sort": {"total": 1}},
            {"$limit": 1}
        ])

    # 3- Encontre o cliente que menos gastou em uma única compra
    def cliente_que_menos_gastou(db):
        return db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": {"cliente": "$_id", "letra_cliente": "$cliente_id"},
                        "total": {"$sum": {"$multiply": ["$produtos.quantidade", "$produtos.preco"]}}}},
            {"$sort": {"total": 1}},
            {"$group": {"_id": {"$first": "$cliente._id"}, "id": {"$first": "$_id"}, "total": {"$first": "$total"}}}

        ])

    # 4- Liste todos os produtos que tiveram uma quantidade de venda acima de 2 unidades
    def produtos_vendidos_acima_de_2_unid(db):
        return db.collection.aggregate([
            {"$unwind": "$produtos"},
            {"$group": {"_id": "$produtos.nome", "quantidade": {"$sum": "$produtos.quantidade"}}},
            {"$match": {"quantidade": {"$gt": 2}}}
        ])
