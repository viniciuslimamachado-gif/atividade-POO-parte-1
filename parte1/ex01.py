# ex01.py - Classe e Objeto
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

p = Pessoa("Maria", 25)
print("Nome:", p.nome)
print("Idade:", p.idade)
