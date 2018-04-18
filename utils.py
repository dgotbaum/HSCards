import json
import pandas as pd
import ipywidgets as widgets

def show_cards(filtered, images): 
    rows = []
    cur_row = []
    for name in filtered.index.values:
        if name not in images: 
            continue
        if len(cur_row) < 10: 
            cur_row.append(widgets.Image(value=images[name], format="jpg", width=130, height=180))
        else: 
            rows.append(widgets.HBox(cur_row))
            cur_row = [widgets.Image(value=images[name], format="jpg", width=130, height=180)]
    print(len(rows))
    return widgets.VBox(rows + [widgets.HBox(cur_row)])


def load_standard_cards():
    data = json.loads(open("Cards.json", "r").read())
    rows = []
    for card_set in data: 
        rows += data[card_set]
    df = pd.DataFrame(rows)
    standard = df[df.cardSet.isin(STANDARD_SETS)]
    return standard

info_cols = [
    'name', 'cost', 'health','attack', 'text', 'armor',  'playerClass', 'race', 'rarity', 
    'cardSet', 'classes', 'durability',  'faction', 
    'img', 'mechanics',
    'multiClassGroup', 'type'
]


CLASSES = [
    "Druid",
    "Hunter",
    "Mage",
    "Paladin",
    "Priest",
    "Rogue",
    "Shaman",
    "Warlock",
    "Warrior",
    "Dream"
  ]

SETS = ['Basic',
 'Classic',
 'Hall of Fame',
 'Naxxramas',
 'Goblins vs Gnomes',
 'Blackrock Mountain',
 'The Grand Tournament',
 'The League of Explorers',
 'Whispers of the Old Gods',
 'One Night in Karazhan',
 'Mean Streets of Gadgetzan',
 "Journey to Un'Goro",
 'Knights of the Frozen Throne',
 'Kobolds & Catacombs',
 'The Witchwood',
 'Tavern Brawl',
 'Hero Skins',
 'Missions',
 'Credits']
STANDARD_SETS = [
    "Basic",
    "Classic",
     "Journey to Un'Goro",
 'Knights of the Frozen Throne',
 'Kobolds & Catacombs',
 'The Witchwood'
]

TYPES = [
    "Hero",
    "Minion",
    "Spell",
    "Enchantment",
    "Weapon",
    "Hero Power"
  ]
FACTIONS = [
    "Horde",
    "Alliance",
    "Neutral"
  ]
QUALITIES = [
    "Free",
    "Common",
    "Rare",
    "Epic",
    "Legendary"
  ],
RACES =  [
    "Demon",
    "Dragon",
    "Mech",
    "Murloc",
    "Beast",
    "Pirate",
    "Totem"
  ]
 