import sqlite3

class InicializadorBD:
    """Classe responsavel por inicializar o banco de dados."""

    @staticmethod
    def criar_tabelas(db_nome: str):
        """Cria as tabelas no banco de dados.
        
        Args:
            db_nome (str): Nome do banco de dados.
        """
        connection = sqlite3.connect(db_nome)
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pokemons (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                tipo TEXT NOT NULL,
                hp INTEGER NOT NULL,
                ataque INTEGER NOT NULL,
                defesa INTEGER NOT NULL,
                ataques TEXT NOT NULL
            );
            
            CREATE TABLE IF NOT EXISTS attacks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                tipo INTEGER NOT NULL,
                dano INTEGER NOT NULL
            );  
                       
            CREATE TABLE IF NOT EXISTS battles (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                vencedor_id INTEGER NOT NULL,
                perdedor_id INTEGER NOT NULL,
                turnos INTEGER NOT NULL
            );
            
            CREATE TABLE IF NOT EXISTS pokemons_attacks (
                id_pokemon INTEGER,
                id_attack INTEGER,
                PRIMARY KEY (id_pokemon, id_attack)
                
                FOREIGN KEY (id_pokemon)
                REFERENCES pokemons(id)
                ON DELETE CASCADE,
                    
                FOREIGN KEY (id_attack)
                REFERENCES attacks(id)
                ON DELETE CASCADE,
            );
        """)
        connection.commit()
        connection.close()
    