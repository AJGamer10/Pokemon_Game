from __future__ import annotations
from typing import List
from attack import Attack
from damage_calculator import DamageCalculator


class Pokemon:
    """Representa um pokemon.
    
    Attributes:
        id (int): ID do pokemon.
        nome (str): Nome do pokemon.
        tipos (List[str]): Lista de tipos elementais do pokemon.
        hp (int): HP do pokemon.
        ataque (int): Ataque do pokemon.
        defesa (int): Defesa do pokemon.
        ataques (List[Attack]): Lista de ataques do pokemon.
    """
    def __init__(self, nome: str, tipos: List[str], hp: int, ataque: int, defesa: int, ataques: List[Attack], id: int = None) -> None:
        self.id = id
        self.nome = nome
        self.tipos = tipos
        self.hp = hp
        self.current_hp = hp
        self.ataque = ataque
        self.defesa = defesa
        self.ataques = ataques
        self.status = None

    def __str__(self) -> str:
        return f"{self.nome}, Tipo: {self.tipos}, {self.current_hp}/{self.hp}"
    
    def __repr__(self) -> str:
        return f"{self.nome}, Tipo: {self.tipos}, {self.current_hp}/{self.hp}"
    
    def mostrar_status(self) -> None:
        print(f"{self.nome} - Tipo: {self.tipos} - HP: {self.hp} - Atk: {self.ataque} - Dfe: {self.defesa}")

    def __receber_dano(self, dano: int) -> str:
        self.current_hp -= dano
        input(f"{self.nome} recebeu {dano} de dano!")

    def atacar(self, ataque: Attack, oponente: Pokemon) -> None:
        dano = DamageCalculator.calcular_dano(self.ataque, self.tipos, ataque.dano, ataque.tipo, oponente.tipos, oponente.defesa)
        input(f"{self.nome} usou {ataque.nome}")
        oponente.__receber_dano(dano)

    def curar(self, vida: int):
        if self.current_hp + vida >= self.hp:
            self.current_hp = self.hp
            input(f"{self.nome} curou a vida ao máximo!")
        else:
            self.current_hp += vida
            input(f"{self.nome} curou {vida} pontos de vida!")
