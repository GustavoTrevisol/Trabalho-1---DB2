from pymongo import MongoClient
from pymongo.server_api import ServerApi

# Connection URI
uri = "mongodb+srv://gustavo_trevisol:123456gustavo@cursobdii20251.gvqegbw.mongodb.net/"

# cria um novo cliente e conecta a um servidor existente
client = MongoClient(uri, server_api=ServerApi('1'))

# acessa o banco de dados
db = client['sample_mflix']

# "pinga" para confirmar a conexão ao banco.
try:
    client.admin.command('ping')
    print("pinguei seu ambiente. A conexao ao MongoDB foi realizada com sucesso!")
except Exception as e:
    print(e)

# mostra os nomes das collections encontradas na base de dados
print(db.list_collection_names())