from pokemon import Pokemon
from attack import Attack
from battle import Battle


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


leaf_blade = Attack("Leaf Blade", "Grass", 20)
brick_break = Attack("Brick Break", "Fighting", 25)
return_atk = Attack("Return", "Normal", 15)
dragon_claw = Attack("Dragon Claw", "Dragon", 25)
dig = Attack("Dig", "Ground", 30)
flamethrower = Attack("Flamethrower", "Fire", 35)
crunch = Attack("Crunch", "Dark", 25)
sky_uppercut = Attack("Sky Uppercut", "Fighting", 25)
bulk_up = Attack("Bulk Up", "Fighting", 0, )


attacks_sceptile = [leaf_blade, brick_break, return_atk, dragon_claw]
sceptile = Pokemon("Sceptile", ["Grass"], 70, 85, 75, attacks_sceptile)

# attacks_blaziken = [flamethrower, ]
# blaziken = Pokemon("Blaziken", ["Fire", "Fighting"], 80, 95, 70, attacks_blaziken)

attacks_flygon = [dig, flamethrower, dragon_claw, crunch]
flygon = Pokemon("Flygon", ["Ground", "Dragon"], 80, 90, 80, attacks_flygon)

batalha1 = Battle(sceptile, flygon)

count = 1
while batalha1.vencedor == None:
    if count == 1:
        input(f"Você encontra um(a) {batalha1.pokemon2} no caminho!")
        input(f"Você lança {batalha1.pokemon1.nome}, e ele se prepara para atacar!")
        count += 1
    batalha1.escolher_atk(escolher_ataque(batalha1.pokemon1))
    batalha1.turno_battle()

input(f"O vencedor da batalha foi {batalha1.vencedor} e seu perdedor foi {batalha1.vencedor}")
