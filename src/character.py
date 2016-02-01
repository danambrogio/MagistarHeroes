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
    
    def __init__(self, image, position, object_container, name):
        super().__init__(image, position, object_container)
        #sprite.Sprite.__init__(self, image, position)
        
        self.object_container['player'] = self
        
        ''' Character-only attributes '''
        self.name = name
        self.stats = Stats()
        self.spellcasts = 0
        
        self.facing = "right"
        
        ''' Key presses '''
        self.left_flag = False
        self.right_flag = False
        self.jump_flag = False
        self.crouch_flag = False
        self.j_flag = False
        self.k_flag = False
        self.l_flag = False
        self.semicolon_flag = False
        self.i_flag = False
        self.o_flag = False
        
        
    def move_left(self):
        self.velocity = (self.velocity[0] - 50, self.velocity[1])
        if self.velocity[0] > (self.get_max_speed() * -1):
            self.velocity = (self.get_max_speed() * -1, self.velocity[1])
    def move_right(self):
        self.velocity = (self.velocity[0] + 50, self.velocity[1])
        if self.velocity[0] < self.get_max_speed():
            self.velocity = (self.get_max_speed(), self.velocity[1])
    def jump(self):
        if self.isGrounded():
            jump_power = -500 + (-400 * (1 / self.weight.value))
            self.velocity = (self.velocity[0], self.velocity[1] + jump_power)
    def crouch(self):
        if self.isGrounded():
            # On the ground, crouch
            pass
        else:
            # In the air, drop faster
            self.acceleration = (self.acceleration[0], self.acceleration[1] + 15)
            
    ''' Spells '''
    def getDefaultCastOrigin(self):
        if self.facing == "right":
            x = self.rect.x + self.rect.w
            y = self.rect.y
            return (x, y)
        else:
            x = self.rect.x
            y = self.rect.y
            return (x, y)
        
    def channel_fire(self):
        if self.stats.fire == 0:
            self.spellcasts = self.spellcasts + 1
            firebll = sprite.ShortLivedSprite(0.20, "fireball", self.getDefaultCastOrigin(), 
                                    self.object_container, sprite.Weight.Light, 
                                    sprite.GravityType.LowG)
            self.object_container['fireball'] = firebll
            firebll.velocity = self.velocity
            firebll.acceleration = self.acceleration
    def cast_fire(self):
        if self.stats.fire >= 1:
            self.spellcasts = self.spellcasts + 1
            firebll = sprite.ShortLivedSprite(1, "fireball", self.getDefaultCastOrigin(), 
                                    self.object_container, sprite.Weight.Light, 
                                    sprite.GravityType.LowG)
            self.object_container['fireball{0}'.format(self.spellcasts)] = firebll
            # Give it momentum
            firebll.velocity = (700 + (100 * self.stats.fire), (-70 - self.stats.fire))
    
class Stats(object):
    ''' Contains a character's spell stats '''
    #TODO: missing one
    def __init__(self, fire=0, ice=0, shock=0, bio=0, tele=0):
        self.fire = fire
        self.ice = ice
        self.shock = shock
        self.bio = bio
        self.tele = tele
        
    def upStat(self, stat):
        if stat == "fire":
            self.fire = self.fire + 1
        elif stat == "ice":
            self.ice = self.ice + 1
        elif stat == "shock":
            self.shock = self.shock + 1
        elif stat == "bio":
            self.bio = self.bio + 1
        elif stat == "tele":
            self.tele = self.tele + 1