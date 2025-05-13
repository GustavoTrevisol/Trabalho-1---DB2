class PosAdocao:
    def __init__(self, pet_id, adotante_id, data_adocao, visitas=None, saude=None):
        self.pet_id = pet_id
        self.adotante_id = adotante_id
        self.data_adocao = data_adocao
        self.visitas = visitas if visitas else []
        self.saude = saude if saude else []

    def to_dict(self):
        return self.__dict__