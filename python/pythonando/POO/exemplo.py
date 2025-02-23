# pokemon_list = [
#     {"name": "Pikachu", "type": "Eletric", "hp": 35},
#     {"name": "Charizard", "type": "Fire/Flying", "hp": 78},
#     {"name": "Bulbasaur", "type": "Grass/Poison", "hp": 45},
#     {"name": "Squirtle", "type": "water", "hp": 44},
#     {"name": "Jigglypuff", "type": "Normal/Fairy", "hp": 115},
#     {"name": "Gyarados", "type": "water/Flying", "hp": 95}
# ]

# high_hp_pokemon = [pokemon["name"] for pokemon in pokemon_list if pokemon["hp"] > 50]

# print(high_hp_pokemon)

# memory_addresses = [0x1000, 0x1004, 0x1010, 0x1018, 0x1020, 0x1024, 0x1030]

# aligned_address = [hex(addr) for addr in memory_addresses if addr % 0x10 == 0]

# print(aligned_address)


# binary_data = [0x41, 0x42, 0x03, 0x7A, 0x20, 0x2E, 0x10, 0x65, 0x66]

# printable_chars = [chr(b) for b in binary_data if 32 <= b <= 126]

# print(printable_chars)