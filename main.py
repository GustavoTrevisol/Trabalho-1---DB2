from database.acesso import db
from service.compatibilidade import calcular_compatibilidade
from models.adotante import Adotante
from models.pets import Pet
from models.posAdocao import PosAdocao
from models.rastreabilidade import Rastreabilidade
from models.tutor import Tutor

if db is None:
    print("Erro ao conectar no banco. Encerrando a aplicação.")
else:
    
    pets = db["pets"]
    rastreabilidade = db["rastreabilidade"]
    tutores = db["tutores"]
    adotantes = db["adotantes"]
    pos_adocao = db["pos_adocao"]

    
    pet = Pet(
        nome="Luna",
        especie="Cachorro",
        raca="SRD",
        porte="Médio",
        sexo="Fêmea",
        nascimento="2023-02-15",
        status="disponível",
        tratamento_continuo=True,
        necessidades_especiais=False,
        doenca_cronica=False,
        com_outros_animais=True,
        exige_cuidados_constantes=False
    )
    pets.insert_one(pet.to_dict())

    
    rastreabilidade_obj = Rastreabilidade(
        pet_id=None,
        registros=[
            {"data_inicio": "2024-01-01", "data_fim": "2024-02-15", "localizacao": "Porto Alegre - RS"},
            {"data_inicio": "2024-02-15", "data_fim": None, "localizacao": "Abrigo Esperança"}
        ]
    )
    rastreabilidade.insert_one(rastreabilidade_obj.to_dict())

    
    tutor = Tutor(
        nome="João da Silva",
        telefone="(51) 99999-9999",
        email="joao@email.com",
        endereco="Rua Tal, 123",
        pets=[]
    )
    tutores.insert_one(tutor.to_dict())

    
    adotante = Adotante(
        nome="Maria Oliveira",
        email="maria@email.com",
        telefone="(51) 98888-8888",
        especie="Gato",
        porte="Pequeno",
        sexo="Fêmea",
        aceita_necessidades=True,
        aceita_doenca_cronica=False,
        possui_outros_animais=True,
        tempo_disponivel=True
    )
    adotantes.insert_one(adotante.to_dict())

    
    pos_adocao_obj = PosAdocao(
        pet_id=None,
        adotante_id=None,
        data_adocao="2025-03-01",
        visitas=[{"data": "2025-04-01", "relato": "Animal bem adaptado ao lar."}],
        saude=[{"tipo": "vacinação", "data": "2025-04-10", "descricao": "Vacina antirrábica aplicada."}]
    )
    pos_adocao.insert_one(pos_adocao_obj.to_dict())

    
    compatibilidade = calcular_compatibilidade(pet.to_dict(), adotante.to_dict())

    print("Todas as coleções foram criadas e populadas com dados de exemplo.")
    print(f"A compatibilidade entre o pet '{pet.nome}' e o adotante '{adotante.nome}' é: {compatibilidade}")
