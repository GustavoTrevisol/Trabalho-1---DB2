from pymongo import MongoClient

# Substitua pela sua URI do MongoDB Atlas
client = MongoClient("mongodb+srv://<usuario>:<senha>@<cluster>.mongodb.net")
db = client["adocao_pets"]

# Coleções
pets = db["pets"]
rastreabilidade = db["rastreabilidade"]
tutores = db["tutores"]
adotantes = db["adotantes"]
pos_adocao = db["pos_adocao"]

# Inserir um pet
pets.insert_one({
    "nome": "Luna",
    "especie": "Cachorro",
    "raca": "SRD",
    "porte": "Médio",
    "sexo": "Fêmea",
    "nascimento": "2023-02-15",
    "status": "disponível",
    "necessidades": {
        "tratamento_continuo": True,
        "necessidades_especiais": False,
        "doenca_cronica": False
    },
    "social": {
        "com_outros_animais": True,
        "exige_cuidados_constantes": False
    },
    "tutor_id": None
})

# Rastreabilidade
rastreabilidade.insert_one({
    "pet_id": None,
    "registros": [
        {
            "data_inicio": "2024-01-01",
            "data_fim": "2024-02-15",
            "localizacao": "Porto Alegre - RS"
        },
        {
            "data_inicio": "2024-02-15",
            "data_fim": None,
            "localizacao": "Abrigo Esperança"
        }
    ]
})

# Tutor
tutores.insert_one({
    "nome": "João da Silva",
    "telefone": "(51) 99999-9999",
    "email": "joao@email.com",
    "endereco": "Rua Tal, 123",
    "pets": []
})

# Adotante
adotantes.insert_one({
    "nome": "Maria Oliveira",
    "email": "maria@email.com",
    "telefone": "(51) 98888-8888",
    "caracteristicas_desejadas": {
        "especie": "Gato",
        "porte": "Pequeno",
        "sexo": "Fêmea",
        "aceita_necessidades": True,
        "aceita_doenca_cronica": False,
        "possui_outros_animais": True,
        "tempo_disponivel": True
    },
    "pets_atuais": []
})

# Pós adoção
pos_adocao.insert_one({
    "pet_id": None,
    "adotante_id": None,
    "data_adocao": "2025-03-01",
    "visitas": [
        {
            "data": "2025-04-01",
            "relato": "Animal bem adaptado ao lar."
        }
    ],
    "saude": [
        {
            "tipo": "vacinação",
            "data": "2025-04-10",
            "descricao": "Vacina antirrábica aplicada."
        }
    ]
})

print("Todas as coleções foram criadas e populadas com dados de exemplo.")