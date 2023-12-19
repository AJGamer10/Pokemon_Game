from pokemon import Pokemon
from damage_calculator import DamageCalculator
from random import choice


class Battle:
    """Representa uma batalha pokemon.
    
    Args:
        pokemon1 (Pokemon): Pokemon jogador.
        pokemon2 (Pokemon): Pokemon oponente.
    """
    def __init__(self, pokemon1: Pokemon, pokemon2: Pokemon) -> None:
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.turno = choice([self.pokemon1.nome, self.pokemon2.nome])
        self.vencedor = None
        self.perdedor = None
        self.current_atk = None

    def turno_battle(self):
        """Realiza um turno"""
        print(self.pokemon1)
        print(self.pokemon2)

        if self.turno == self.pokemon1.nome:
            self.pokemon1.atacar(self.current_atk, self.pokemon2)
            if self.pokemon2.current_hp <= 0:
                return self.__terminar_battle(self.pokemon1, self.pokemon2)
            else:
                self.__trocar_turno()

        elif self.turno == self.pokemon2.nome:
            input(f"{self.pokemon2.nome} se prepara para atacar!")
            ataque_usado = choice(self.pokemon2.ataques)
            self.pokemon2.atacar(ataque_usado, self.pokemon1)
            if self.pokemon1.current_hp <= 0:
                return self.__terminar_battle(self.pokemon2, self.pokemon1)
            else:
                self.__trocar_turno()
        
    def __trocar_turno(self):
        """Troca o pokemon que irá realizar uma ação"""
        if self.turno == self.pokemon1.nome:
            self.turno = self.pokemon2.nome
        else:
            self.turno = self.pokemon1.nome

    def __terminar_battle(self, vencedor: Pokemon, perdedor: Pokemon):
        """Termina a batalha pokemon
        
        Args:
            vencedor (Pokemon): Pokemon vencedor
            perdedor (Pokemon): Pokemon perdedor
        """
        self.vencedor = vencedor
        self.perdedor = perdedor

    def escolher_atk(self, nome_ataque_jogador: str):
        for ataque in self.pokemon1.ataques:
            if ataque.nome == nome_ataque_jogador:
                self.current_atk = ataque