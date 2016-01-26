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

    def __init__(self, image, position):
        '''
        Constructor
        '''
        self.load_image(image)
        self.rect = self.image.get_rect()
        self.position = position            # tuple
        self.velocity = (0, 0)              # tuple
        self.acceleration = (0.0, 0.0)          # tuple
        self.grounded = False               # Can you jump?
        self.gravity = GravityType.Normal   # What is gravity at the moment
        self.weight = Weight.Medium         # How much gravity affects you
        
    def load_image(self, image):
        try:
            self.image = pygame.image.load('../img/' + image + '.png').convert()
        except pygame.error as message:
            print("oops!")
            raise SystemExit(message)
        
    def update(self, clock):
        if clock.get_fps() == 0:
            fps = 1 / 60
        else:
            fps = (1 / clock.get_fps())
        ''' Gravity '''
        if self.gravity == GravityType.Normal:
            gravity_accel = (0, (1000 + (4 * self.weight.value)))
        elif self.gravity == GravityType.Reversed:
            gravity_accel = (0, (-1000 - (4 * self.weight.value)))
        else:
            gravity_accel = (0, 0)
        
        #print("Gravity acceleration:")
        #print(gravity_accel)
        
        # Movement acceleration
        # Handle friction (lower acceleration to 0)
        temp = self.acceleration
        self.acceleration = (temp[0] * 0.2, self.acceleration[1])
        me_velocity = tuple(fps * _ for _ in self.acceleration)
        #print("Me acceleration:")
        #print(self.acceleration)
        
        gravity_velocity = tuple(fps * _ for _ in gravity_accel)
        
        #print("Gravity velocity:")
        #print(gravity_velocity)
        ''' Gravity ends '''
        
        # Find new velocity
        self.velocity = tuple([vel + grav for vel, grav in zip(self.velocity, gravity_velocity)])
        self.velocity = tuple([vel + move for vel, move in zip(self.velocity, me_velocity)])
        
        # Check for ground
        if self.position[1] >= 500 and self.velocity[1] > 0:
            self.velocity = (self.velocity[0], 0)
            self.acceleration = (self.acceleration[0], 0)
            self.grounded = True
            #print("Grounded!")
        else:
            self.grounded = False
        velocity_step = tuple(fps * _ for _ in self.velocity)
        
        #print("Velocity step:")
        #print(velocity_step)
        
        # Find new position
        self.position = tuple([vel + pos for vel, pos in zip(velocity_step, self.position)])
        #print("Position:")
        #print(self.position)
    
    def jump(self):
        if self.grounded:
            jump_power = -500
            self.velocity = (self.velocity[0], self.velocity[1] + jump_power)
            
    def crouch(self):
        if self.grounded:
            # On the ground, crouch
            pass
        else:
            # In the air, drop faster
            self.acceleration = (self.acceleration[0], self.acceleration[1] + 10)
            
    def get_max_speed(self):
        return (self.weight.value * 10)
        
    def move_left(self):
        if self.velocity[0] > (self.get_max_speed() * -1):
            self.velocity = (self.velocity[0] - 10, self.velocity[1])
        
    def move_right(self):
        if self.velocity[0] < self.get_max_speed():
            self.velocity = (self.velocity[0] + 10, self.velocity[1])