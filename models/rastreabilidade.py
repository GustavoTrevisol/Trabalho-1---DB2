class Rastreabilidade:
    def __init__(self, pet_id, registros):
        self.pet_id = pet_id
        self.registros = registros

    def to_dict(self):
        return self.__dict__
