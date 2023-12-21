from pokemon import Pokemon
from attack import Attack
from battle import Battle
from effect import Effect
from random import choice
import pygame


def tocar_musica(arquivo):
    pygame.mixer.music.load(arquivo)
    pygame.mixer.music.play()

def parar_musica():
    pygame.mixer.music.fadeout(700)  # Diminui o volume gradualmente em 700 milissegundos


pygame.init()

# Musicas e efeitos sonoros
TITLE_THEME = "static\Audios\Title_theme.mp3"
BATTLE_SOUND = "static\Audios\Battle_sound.mp3"
WINNER = "static\Audios\winner.mp3"
LOSER = "static\Audios\loser.mp3"

# Configuração inicial do volume
pygame.mixer.music.set_volume(1.0)  # Volume inicial (1.0 = 100%)


# Efeito dos ataques dos pokemons
queimadura = Effect("Queimadura", 5, duracao=4)
fratura = Effect("Fratura", 5, duracao=4)
congelamento = Effect("Congelamento", status="SM", duracao=4)
paralisia = Effect("Paralisia", status="SM", duracao=4)
defesa_diminuicao10 = Effect("Diminuiçao defesa 10%", status="DS+D")
ataque_aumento10 = Effect("Aumento ataque 10%", status="AS+A")
cura_metade = Effect("Cura metade", status="C+m")

# Ataques dos pokemons
leaf_blade = Attack("Leaf Blade", "Grass", 20)
brick_break = Attack("Brick Break", "Fighting", 25)
return_atk = Attack("Return", "Normal", 17)
dragon_claw = Attack("Dragon Claw", "Dragon", 25)
dig = Attack("Dig", "Ground", 30)
flamethrower = Attack("Flamethrower", "Fire", 35, queimadura)
crunch = Attack("Crunch", "Dark", 25, defesa_diminuicao10)
sky_uppercut = Attack("Sky Uppercut", "Fighting", 25)
bulk_up = Attack("Bulk Up", "Fighting", 15, fratura)
rock_tomb = Attack("Rock Tomb", "Rock", 20)
surf = Attack("Surf", "Water", 35)
earthquake = Attack("Earthquake", "Ground", 40)
ice_beam = Attack("Ice Beam", "Ice", 35, congelamento)
psychic = Attack("Psychic", "Psychic", 30)
thunderbolt = Attack("Thunderbolt", "Electric", 35, paralisia)
shadow_ball = Attack("Shadow Ball", "Ghost", 20)
energy_ball = Attack("Energy Ball", "Electric", 30, paralisia)
dragon_dance = Attack("Dragon Dance", "Dragon", efeito=ataque_aumento10)
roost = Attack("Roost", "Flying", efeito=cura_metade)


attacks_sceptile = [leaf_blade, brick_break, return_atk, dragon_claw]
sceptile = Pokemon("Sceptile", ["Grass"], 85, 85, 75, attacks_sceptile)

attacks_blaziken = [flamethrower, sky_uppercut, bulk_up, rock_tomb]
blaziken = Pokemon("Blaziken", ["Fire", "Fighting"], 80, 95, 70, attacks_blaziken)

attacks_swampert = [surf, earthquake, ice_beam, brick_break]
swampert = Pokemon("Swampert", ["Water", "Ground"], 80, 90, 85, attacks_swampert)

attacks_gardevoir = [psychic, thunderbolt, shadow_ball, energy_ball]
gardevoir = Pokemon("Gardevoir", ["Psychic"], 70, 75, 75, attacks_gardevoir)

attacks_flygon = [dig, flamethrower, dragon_claw, crunch]
flygon = Pokemon("Flygon", ["Ground", "Dragon"], 80, 90, 80, attacks_flygon)

attacks_altaria = [dragon_dance, dragon_claw]
altaria = Pokemon("Altaria", ["Dragon", "Flying"], 75, 70, 90, attacks_altaria)

pokemons = [sceptile, blaziken, swampert, gardevoir, flygon, altaria]


def escolher_pokemon_jogador():
    counter = 1
    for pokemon in pokemons:
        print(f"""   {counter}) {pokemon.mostrar_status()}""")
        counter += 1
    opcao = int(input("Com qual pokemon você gostaria de começar sua jornada: "))
    return pokemons[opcao - 1]


def escolher_ataque(pokemon: Pokemon):
    while True:
        print("Moves:")
        contador = 1
        for ataque in pokemon.ataques:
            print(f"""      {contador}) {ataque.nome} - atk: {ataque.dano} - tipo: {ataque.tipo}""")
            contador += 1
        opcao = input("Qual ataque deseja realizar: ")
        if (not opcao.isdigit()) or int(opcao) > 4:
            input('Por favor digite um numero correspondente para continuar')
            continue
        else:
            opcao = int(opcao)
            break
    return pokemon.ataques[opcao - 1]


tocar_musica(TITLE_THEME)

input(f"Bem vindo treinador pokemon!")
input(f"Para começar sua jornada no mundo pokemon, por favor, faça a escolha de seu pokemon")
pokemon_jogador = escolher_pokemon_jogador()
input("Maravilha! Vamos para sua primeira batalha pokemon!")
pokemon_ia = choice(pokemons)

batalha1 = Battle(pokemon_jogador, pokemon_ia)

parar_musica()
tocar_musica(BATTLE_SOUND)
count = 1
while batalha1.vencedor == None:
    print('\n')
    if count == 1:
        input(f"Você encontra um(a) {batalha1.pokemon2} no caminho!")
        input(f"Vai {batalha1.pokemon1.nome}, eu escolho você!")
        count += 1
    print(batalha1.pokemon1.mostrar_status())
    print(batalha1.pokemon2.mostrar_status())
    if batalha1.turno == batalha1.pokemon1.nome:
        batalha1.escolher_atk(escolher_ataque(batalha1.pokemon1))
    batalha1.turno_battle()
parar_musica()
if batalha1.vencedor == batalha1.pokemon1:
    tocar_musica(WINNER)
    input(f"""{batalha1.perdedor} desmaiou.
Parabéns você venceu!""")
else:
    tocar_musica(LOSER)
    input(f"""{batalha1.perdedor} desmaiou.
Que pena você perdeu.""")

pygame.quit()
