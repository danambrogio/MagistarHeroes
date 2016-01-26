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
        super().__init__(image, position)
        #sprite.Sprite.__init__(self, image, position)
        
        ''' Character-only attributes '''
        self.name = name
        self.stats = None
        
        self.left_flag = False
        self.right_flag = False
        self.jump_flag = False
        self.crouch_flag = False