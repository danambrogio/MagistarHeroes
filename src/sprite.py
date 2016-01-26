'''
Created on Jan 25, 2016

@author: Dan
'''

import pygame
from enum import Enum

class GravityType(Enum):
    Normal = 1
    ZeroG = 0
    Reversed = -1
    
class Weight(Enum):
    Light = 4
    Medium = 6
    Heavy = 8
    
class Sprite(object):
    '''
    Sprites are things that exist on the screen. Some move, some don't.
    '''
    fps = (1 / 60) # 40fps

    def __init__(self, image, position):
        '''
        Constructor
        '''
        self.load_image(image)
        self.rect = self.image.get_rect()
        self.position = position            # tuple
        self.velocity = (0, 0)              # tuple
        self.acceleration = (0, 0)          # tuple
        self.grounded = False               # Can you jump?
        self.gravity = GravityType.Normal   # What is gravity at the moment
        self.weight = Weight.Medium         # How much gravity affects you
        
    def load_image(self, image):
        try:
            self.image = pygame.image.load('../img/' + image + '.png').convert()
        except pygame.error:
            print("oops!")
            raise SystemExit
        
    def update(self, clock):
        # Add gravity
        if self.gravity == GravityType.Normal:
            gravity_accel = (0, (60 + (4 * self.weight.value)))
        elif self.gravity == GravityType.Reversed:
            gravity_accel = (0, (-60 - (4 * self.weight.value)))
        else:
            gravity_accel = (0, 0)
        
        print("Gravity acceleration:")
        print(gravity_accel)
        
        # Movement acceleration
        
        
        # Friction
        
        gravity_velocity = tuple(Sprite.fps * _ for _ in gravity_accel)
        
        print("Gravity velocity:")
        print(gravity_velocity)
        
        # Find new velocity
        self.velocity = tuple([vel + grav for vel, grav in zip(self.velocity, gravity_velocity)])
        # Check for ground
        if self.position[1] >= 500 and self.velocity[1] > 0:
            self.velocity = (self.velocity[0], 0)
            self.grounded = True
            print("Grounded!")
        else:
            self.grounded = False
        velocity_step = tuple(Sprite.fps * _ for _ in self.velocity)
        
        print("Velocity step:")
        print(velocity_step)
        
        # Find new position
        self.position = tuple([vel + pos for vel, pos in zip(velocity_step, self.position)])
        print("Position:")
        print(self.position)
    
    def jump(self):
        if self.grounded:
            print("Jump!")
            jump_power = -110
            self.velocity = (self.velocity[0], self.velocity[1] + jump_power)
            
    def move_left(self):
        self.acceleration = ((self.acceleration[0] - 10), self.accceleration[1])
        
    def move_right(self):
        print(self.acceleration)
        self.acceleration = ((self.acceleration[0] + 10), self.accceleration[1])