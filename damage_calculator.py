from random import uniform
from abc import ABC
from typing import List


class DamageCalculator(ABC):
    """Calcula o dano recebido ao pokemon"""
    
    @staticmethod
    def calcular_dano(atacante_ataque: int, ataque_dano: int, ataque_tipo: str, oponente_tipos: List[str], oponente_defesa: int) -> int:
        """Calcula o dano que o Pokemon receberá.
        
        Args:
            atacante (Pokemon): Pokemon que vai atacar.
            ataque (Attack): Ataque que o pokemon vai utizar.
            oponente (Pokemon): Pokemon que receberá o ataque.
        """
        tipo_ataque = ataque_tipo
        efetividades = [DamageCalculator.__verificar_efetividade(tipo_ataque, tipo_oponente) for tipo_oponente in oponente_tipos]

        efetividade_total = 1
        for efetividade in efetividades:
            efetividade_total *= efetividade
        fator_aleatorio = uniform(0.85, 1.0)
        dano = (atacante_ataque / oponente_defesa) * ataque_dano * efetividade * fator_aleatorio
        return int(dano)
    
    @staticmethod
    def __verificar_efetividade(tipo_ataque, tipo_oponente):
        tabela_efetividade = {
            'Grass': {'Water': 2, 'Ground': 0.5, 'Fire': 0.5, 'Rock': 0.5},
            'Fighting': {'Normal': 2, 'Ice': 2, 'Rock': 0.5, 'Psychic': 0.5, 'Dark': 2},
            'Normal': {'Rock': 0.5, 'Ghost': 0},
            'Dragon': {'Dragon': 2},
            'Fire': {'Grass': 2, 'Ice': 2, 'Fire': 0.5, 'Water': 0.5, 'Rock': 2},
            'Rock': {'Fire': 2, 'Ice': 2, 'Fighting': 2, 'Ground': 0.5, 'Flying': 2},
            'Water': {'Fire': 2, 'Ground': 2, 'Rock': 2},
            'Ground': {'Water': 2, 'Ice': 2, 'Grass': 0.5},
            'Ice': {'Grass': 2, 'Ground': 2, 'Flying': 2, 'Fire': 0.5, 'Water': 0.5},
            'Psychic': {'Fighting': 2, 'Dark': 0.5},
            'Electric': {'Water': 2, 'Flying': 0.5},
            'Ghost': {'Ghost': 2, 'Dark': 2, 'Normal': 0},
            'Dark': {'Psychic': 2, 'Ghost': 0.5},
            'Flying': {'Fighting': 2, 'Grass': 2, 'Electric': 0.5, 'Rock': 0.5},
        }
        
        # Verificar a efetividade na tabela
        if tipo_ataque in tabela_efetividade and tipo_oponente in tabela_efetividade[tipo_ataque]:
            return tabela_efetividade[tipo_ataque][tipo_oponente]
        else:
            # Caso não esteja na tabela, consideramos efetividade normal (1x)
            return 1
