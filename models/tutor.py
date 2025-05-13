class Tutor:
    def __init__(self, nome, telefone, email, endereco, pets=None):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.pets = pets if pets else []

    def to_dict(self):
        return self.__dict__
