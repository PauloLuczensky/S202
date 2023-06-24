from save_json import writeAJson
from database import Database
from ProductAnalyzer import ProductAnalyzer

db = Database(database="loja_de_roupas", collection="vendas")
db.resetDatabase()
data = db.collection.find()

result = ProductAnalyzer.gasto_cliente_B(db)
writeAJson(result, "gasto_cliente_B")

result2 = ProductAnalyzer.produto_menos_vendido(db)
writeAJson(result2, "produto_menos_vendido")

result3 = ProductAnalyzer.cliente_que_menos_gastou(db)
writeAJson(result3, "cliente_que_menos_gastou")

result4 = ProductAnalyzer.produtos_vendidos_acima_de_2_unid(db)
writeAJson(result4, "produtos_vendidos_acima_de_2_unid")
