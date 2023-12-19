from typing import Any
import sqlite3
from pokemon import Pokemon

class PokemonRepositorio:
    """Repositório dos pokemons.
    
    Attributes:
        db_nome (str): Nome do banco de dados.
    """
    def __init__(self, db_nome: str):
        self.db_nome = db_nome

    def __executar_query(self, query: str, *params: Any):
        """Executa uma query no banco de dados.
        
        Args:
            query (str): Query que será executada.
            params (Any): Parâmetros da query.
        """
        connection = sqlite3.connect(self.db_nome) # Abriu uma conexão com sqlite
        cursor = connection.cursor()
        cursor.execute(query, params) # Executar a query
        connection.commit() # Commitar as alterações feitas pela consulta
        connection.close() # Fecha a conexão com o banco de dados

    def inserir_pokemon(self, pokemon: Pokemon) -> Pokemon:
        """Insere um pokemon no banco de dados. O objeto pokemon é atualizado com o ID do banco.
        
        Args:
            pokemon (Pokemon): Pokemon que será criado no banco de dados.
        """
        query = "INSERT INTO pokemons (nome, tipos, hp, ataque, defesa) VALUES (?, ?, ?, ?, ?)"
        self.__executar_query(query, pokemon.nome, pokemon.tipos, pokemon.hp, pokemon.ataque, pokemon.defesa)

        pokemon.id = self.__get_ultimo_id_inserido()
        return pokemon
    
    def __get_ultimo_id_inserido(self) -> int:
        """Retorna o ID do ultimo registro inserido na tabela de usuários."""
        query = "SELECT id FROM usuarios ORDER BY id DESC LIMIT 1"
        connection = sqlite3.connect(self.db_nome)
        cursor = connection.cursor()
        cursor.execute(query)
        row = cursor.fetchone()
        connection.close()
        return row[0]
    