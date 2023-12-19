from pokemon import Pokemon


class Effect:
    """Representa os efeitos que os ataques receberão.
    
    Attributes:
        nome (str): Nome do atributo.
        porcentagem (float): Porcentagem de aderencia do efeito
        duracao (int): Número de turnos que ficará com os efeitos.
    """
    def __init__(self, nome: str, porcentagem: float = 0.1, duracao: int = 0):
        self.nome = nome
        self.duracao = duracao
        self.porcentagem = porcentagem
    