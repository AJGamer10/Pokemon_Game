from pokemon import Pokemon
from random import choice
from attack import Attack


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
        if self.turno == self.pokemon1.nome:
            if self.pokemon1.status:
                if self.pokemon1.status.nome in ["Queimadura", "Fratura"]:
                    self.pokemon1.receber_dano(self.pokemon1.status.dano, "Efeito")
                    input(f"{self.pokemon1.nome} recebeu {self.pokemon1.status.dano} pelo status de {self.pokemon1.status.nome}")
                if self.pokemon1.status.status == "SM":
                    input(f"{self.pokemon1.nome} está {self.pokemon1.status.nome}, ele não pode atacar!")
                else:
                    input(f"{self.pokemon1.nome} se prepara para atacar!")

                    if self.current_atk.efeito:
                        if self.current_atk.efeito.status == "C+m":
                            self.pokemon1.curar(self.pokemon1.hp / 2)
                        else:
                            self.pokemon1.atacar(self.current_atk, self.pokemon2)
                    else:
                        self.pokemon1.atacar(self.current_atk, self.pokemon2)

                    if self.pokemon2.current_hp <= 0:
                        self.pokemon2.current_hp = 0
                        self.__terminar_battle(self.pokemon1, self.pokemon2)
                        return
                    else:
                        self.__trocar_turno()
            else:
                input(f"{self.pokemon1.nome} se prepara para atacar!")

                if self.current_atk.efeito:
                    if self.current_atk.efeito.status == "C+m":
                        self.pokemon1.curar(self.pokemon1.hp / 2)
                    else:
                        self.pokemon1.atacar(self.current_atk, self.pokemon2)
                else:
                    self.pokemon1.atacar(self.current_atk, self.pokemon2)

                if self.pokemon2.current_hp <= 0:
                    self.pokemon2.current_hp = 0
                    self.__terminar_battle(self.pokemon1, self.pokemon2)
                    return
                else:
                    self.__trocar_turno()

        elif self.turno == self.pokemon2.nome:
            if self.pokemon2.status:
                if self.pokemon2.status.nome in ["Queimadura", "Fratura"]:
                    self.pokemon2.receber_dano(self.pokemon2.status.dano)
                    input(f"{self.pokemon2.nome} recebeu {self.pokemon2.status.dano} pelo status de {self.pokemon2.status.nome}")

                if self.pokemon2.status.status == "SM":
                    input(f"{self.pokemon2.nome} está {self.pokemon2.status.nome}, ele não pode atacar!")
                else:
                    input(f"{self.pokemon2.nome} se prepara para atacar!")
                    ataque_usado = choice(self.pokemon2.ataques)

                    if ataque_usado.efeito:
                        if ataque_usado.efeito.status == "C+m":
                            self.pokemon2.curar(self.pokemon2.hp / 2)
                        else:
                            self.pokemon2.atacar(ataque_usado, self.pokemon1)
                    else:
                        self.pokemon2.atacar(ataque_usado, self.pokemon1)

                    if self.pokemon1.current_hp <= 0:
                        self.pokemon1.current_hp = 0
                        self.__terminar_battle(self.pokemon2, self.pokemon1)
                        return
                    else:
                        self.__trocar_turno()

            else:
                input(f"{self.pokemon2.nome} se prepara para atacar!")
                ataque_usado = choice(self.pokemon2.ataques)
                if ataque_usado.efeito:
                    if ataque_usado.efeito.status == "C+m":
                        self.pokemon2.curar(self.pokemon2.hp / 2)
                    else:
                        self.pokemon2.atacar(ataque_usado, self.pokemon1)
                else:
                    self.pokemon2.atacar(ataque_usado, self.pokemon1)

                if self.pokemon1.current_hp <= 0:
                    self.pokemon1.current_hp = 0
                    self.__terminar_battle(self.pokemon2, self.pokemon1)
                    return
                else:
                    self.__trocar_turno()
        
    def escolher_atk(self, ataque_jogador: Attack):
        """Esculhe o ataque que o jogador quer usar
        
        Args:
            ataque_jogador (Attack): Ataque escolhido pelo jogador.
        """
        self.current_atk = ataque_jogador

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
