class Effect:
    """Representa os efeitos que os ataques receberão.
    
    Attributes:
        nome (str): Nome do efeito.
        dano (int): Dano do efeito.
        status (str): Detalhes: sem movimento(SM), aumento/diminuição de status(AS/DS) + status(A/D) + porcentagem(float), cura(C) + quantidade(int ou m=metade, t=total).
        porcentagem (float): Porcentagem de aderencia do efeito.
        duracao (int): Número de turnos que ficará com os efeitos.
    """
    def __init__(self, nome: str, dano: int = 0, status: str = None, porcentagem: float = 0.1, duracao: int = 0):
        self.nome = nome
        self.dano = dano
        self.status = status
        self.porcentagem = porcentagem
        self.duracao = duracao
        self.current_duracao = duracao
    