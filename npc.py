# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 19:38:27 2018

@author: kopur
"""

import deckOfCards as dc

difficulties = ['easy', 'medium', 'hard']

def npc(self):
    def __init__(self, difficulty):
        if difficulty not in difficulties:
            self.difficulty = difficulty
        
        
    