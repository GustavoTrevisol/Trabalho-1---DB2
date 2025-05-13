class Pet:
    def __init__(self, nome, especie, raca, porte, sexo, nascimento,
                 status, tratamento_continuo, necessidades_especiais,
                 doenca_cronica, com_outros_animais, exige_cuidados_constantes,
                 tutor_id=None):
        self.nome = nome
        self.especie = especie
        self.raca = raca
        self.porte = porte
        self.sexo = sexo
        self.nascimento = nascimento
        self.status = status
        self.tutor_id = tutor_id
        self.necessidades = {
            "tratamento_continuo": tratamento_continuo,
            "necessidades_especiais": necessidades_especiais,
            "doenca_cronica": doenca_cronica
        }
        self.social = {
            "com_outros_animais": com_outros_animais,
            "exige_cuidados_constantes": exige_cuidados_constantes
        }

    def to_dict(self):
        return self.__dict__
