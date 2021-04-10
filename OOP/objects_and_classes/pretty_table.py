from prettytable import PrettyTable

table = PrettyTable()

pokemons = ["Pikachu", "Squirtle", "Charmander"]
table.add_column("Pokemon", pokemons)
print(table)

table.add_column("Type", ["Electric", "Water", "Fire"])
print(table)

table.align = "l"
print(table)
