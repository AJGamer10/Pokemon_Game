class Attack:
    """Representa um ataque do pokemon.
    
    Attributes:
        id (int) = ID do ataque
        nome (str): Nome do ataque.
        dano (int): Dano do ataque.
        tipo (str): Tipo elemental do ataque.
        efeito (str): efeito do ataque.
    """
    def __init__(self, nome: str, tipo: str, dano: int = 0, efeito: str = None, id: int = None) -> None:
        self.id = id
        self.nome = nome
        self.tipo = tipo
        self.dano = dano
        self.efeito = efeito

    def __str__(self) -> str:
        if self.efeito != None:
            return f"Nome: {self.nome}, Tipo: {self.tipo}, Dano: {self.dano}, Efeito: {self.efeito}"
        else:
            return f"Nome: {self.nome}, Tipo: {self.tipo}, Dano: {self.dano}"
        
    def __repr__(self) -> str:
        if self.efeito != None:
            return f"Nome: {self.nome}, Tipo: {self.tipo}, Dano: {self.dano}, Efeito: {self.efeito}"
        else:
            return f"Nome: {self.nome}, Tipo: {self.tipo}, Dano: {self.dano}"
