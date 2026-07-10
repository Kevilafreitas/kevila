class Cliente:

    def __init__(self, nome, email, id=None):
        self.id = id
        self.nome = nome
        self.email = email

    def __str__(self):
        return f"{self.nome} <{self.email}>"