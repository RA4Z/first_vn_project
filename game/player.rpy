# Definindo uma classe Personagem
init python:
    class Player:
        def __init__(self, nome):
            self.nome = nome
            self.condicoes = {
                'vivo': True,
                'digitais_criminosas': False
            }
            self.item_chave = {
                'carteira': False,
                'celular':False
            }
            self.pistas = {
                'nome_vitima_parque': False
            }
