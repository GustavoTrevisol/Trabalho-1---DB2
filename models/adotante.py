class Adotante:
    def __init__(self, nome, email, telefone, especie, porte, sexo,
                 aceita_necessidades, aceita_doenca_cronica,
                 possui_outros_animais, tempo_disponivel, pets_atuais=None):
        self.nome = nome
        self.email = email
        self.telefone = telefone
        self.caracteristicas_desejadas = {
            "especie": especie,
            "porte": porte,
            "sexo": sexo,
            "aceita_necessidades": aceita_necessidades,
            "aceita_doenca_cronica": aceita_doenca_cronica,
            "possui_outros_animais": possui_outros_animais,
            "tempo_disponivel": tempo_disponivel
        }
        self.pets_atuais = pets_atuais if pets_atuais else []

    def to_dict(self):
        return self.__dict__
