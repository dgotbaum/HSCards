"""
Program Descriptions 
"""
import pandas as pd
import numpy as np
__author__ = 'Drew.gotbaum'
__date__ = '12/13/2016'
__version__ = '1.0'
__copyright__ = 'The Oakleaf Group, LLC.'


class Cards(object):
    JSON_PATH = 'input/Cards.json'
    PRINT_COLS = [
        'name',
        'cost',
        'type',
        'classes',
        'playerClass',
        'attack',
        'health',
        'mechanics',
        'durability',
        'rarity',
        'text'
    ]

    def __init__(self):
        self.data = pd.read_json(self.JSON_PATH)
        self.data.text = self.data.text.replace(np.nan, '')

    @staticmethod
    def add_specialties(card_text):
        """
        Adds the battlecries/deathrattle.
        """
        if pd.isnull(card_text):
            return
        if 'Battlecry:' in card_text:
            return 'Battlecry'
        elif 'Deathrattle:' in card_text:
            return 'Deathrattle'

    def simplify(self, df):
        return df[self.PRINT_COLS]

    def find_card(self, player_class='NEUTRAL', mechanics=[], text_includes=[]):
        if player_class != 'NEUTRAL':
            player_classes = ['NEUTRAL', player_class]
        else:
            player_classes = ['NEUTRAL']
        if len(mechanics) > 0 and len(text_includes) > 0:
            data = self.data[(pd.notnull(self.data.text)) & (pd.notnull(self.data.mechanics))]
            return data[
                (data.mechanics.map(lambda card_mechs: all(mechanic in card_mechs for mechanic in mechanics))) &
                (data.text.str.contains('&'.join(text_includes))) &
                (data.playerClass.isin(player_classes))
                ][self.PRINT_COLS]

        elif len(text_includes) > 0:
            data = self.data[pd.notnull(self.data.text)]
            return data[
                (data.text.str.contains('&'.join(text_includes))) &
                (data.playerClass.isin(player_classes))
                ][self.PRINT_COLS]
        elif len(mechanics) > 0:
            data = self.data[pd.notnull(self.data.mechanics)]
            return data[
                (data.mechanics.map(lambda card_mechs: all(mechanic in card_mechs for mechanic in mechanics))) &
                (data.playerClass.isin(player_classes))
                ][self.PRINT_COLS]
        else:
            return self.data[
                (self.data.playerClass.isin(player_classes))
                ]
