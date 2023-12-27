from __future__ import annotations
from typing import List
from attack import Attack
from effect import Effect
from damage_calculator import DamageCalculator
from random import uniform


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
        status (Effect): Status de efeito do pokemon.
    """
    def __init__(self, nome: str, tipos: List[str], hp: int, ataque: int, defesa: int, ataques: List[Attack], id: int = None, status: Effect = None) -> None:
        self.id = id
        self.nome = nome
        self.tipos = tipos
        self.hp = hp
        self.current_hp = hp
        self.ataque = ataque
        self.defesa = defesa
        self.current_defesa = defesa
        self.current_ataque = ataque
        self.ataques = ataques
        self.status = status

    def __str__(self) -> str:
        return f"{self.nome}, Tipo: {self.tipos}, {self.current_hp}/{self.hp}"
    
    def __repr__(self) -> str:
        return f"{self.nome}, Tipo: {self.tipos}, {self.current_hp}/{self.hp}"
    
    def mostrar_status(self) -> str:
        return f"{self.nome} - Tipo: {self.tipos} - HP: {self.current_hp}/{self.hp} - Atk: {self.ataque} - Dfe: {self.defesa}"

    def receber_dano(self, dano: int, quem: str) -> None:
        """Ação de receber dano
        
        Args:
            dano (int): Dano recebido pelo pokemon.
            quem (str): Quem deu o dano.
        """
        self.current_hp -= dano
        if quem == "Efeito":
            input(f"{self.nome} recebeu {dano} de dano pela {self.status.nome}!")
        if quem == "Pokemon":
            input(f"{self.nome} recebeu {dano} de dano!")

    def atacar(self, ataque: Attack, oponente: Pokemon) -> None:
        dano = DamageCalculator.calcular_dano(self.ataque, ataque.dano, ataque.tipo, oponente.tipos, oponente.defesa)
        input(f"{self.nome} usou {ataque.nome}")
        if ataque.efeito:
            oponente.aplicar_efeito(ataque.efeito, oponente)
        if ataque.dano != 0:
            oponente.receber_dano(dano, "Pokemon")

    def curar(self, vida: int):
        if self.current_hp + vida >= self.hp:
            self.current_hp = self.hp
            input(f"{self.nome} curou a vida ao máximo!")
        else:
            self.current_hp += vida
            input(f"{self.nome} curou {vida} pontos de vida!")
    
    def aplicar_efeito(self, efeito: Effect, oponente: Pokemon):
        """Aplica o efeito no pokemon
        
        Args:
            efeito (Effect): Efeito do ataque.
        """
        if self.status:
            if efeito.nome in ["Queimadura", "Fratura", "Congelamento", "Paralisia"]:
                porcentagem = uniform(0.0, 1.0)
                if porcentagem <= efeito.porcentagem:
                    self.status = efeito
                    print(f"{self.nome} foi afetado por {self.status.nome}!")
        if efeito.status == "DS+D":
            porcentagem = uniform(0.0, 1.0)
            if porcentagem <= efeito.porcentagem:
                if oponente.current_defesa - oponente.current_defesa * 0.1 <= 0:
                    oponente.current_defesa = 0
                else:
                    oponente.current_defesa -= oponente.current_defesa * 0.1
                input(f"A defesa de {oponente.nome} caiu!")
        if efeito.status == "AS+A":
            porcentagem = uniform(0.0, 1.0)
            if porcentagem <= efeito.porcentagem:
                if self.current_ataque - self.current_ataque * 0.1 <= 0:
                    self.current_ataque = 0
                else:
                    self.current_ataque -= self.current_ataque * 0.1
