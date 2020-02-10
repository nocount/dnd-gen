# Randomnly generate a Dnd character (Race, Class) because I am an indecisive fuck
############ THIS HAS BEEN DEPRECATED for new up to date logic in scrape.py ######################
from random import randint

races = [
    'Dwarf',
    'Elf',
    'Halfling',
    'Human',
    'Dragonborn',
    'Gnome',
    'Half-Elf',
    'Half-Orc',
    'Tiefling',
    'Aarakocra',
    'Genasi',
    'Goliath',
    'Aasimar',
    'Bugbear',
    'Firbolg',
    'Goblin',
    'Hobgoblin',
    'Kenku',
    'Kobold',
    'Lizardfolk',
    'Orc',
    'Tabaxi',
    'Triton',
    'Yuan-ti'
]

classes = [
    'Barbarian',
    'Bard',
    'Cleric',
    'Druid',
    'Fighter',
    'Monk',
    'Paladin',
    'Ranger',
    'Rogue',
    'Sorcerer',
    'Warlock',
    'Wizard'
]

race_pick = races[randint(0,23)]
class_pick = classes[randint(0,11)]

print(f'You are now a {race_pick} {class_pick}. Congratulations.')
