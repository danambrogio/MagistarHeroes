'''
Created on Jan 24, 2016

@author: Dan
'''

import sprite

class Character(sprite.Sprite):
    '''
    Additional functionality for a sprite that is a character.
    Characters are sprites that have character attributes, like HP
    or behaviour.
    '''
    
    def __init__(self, image, position, name):
        sprite.Sprite.__init__(self, image, position)
        
        self.name = name
        self.stats = None