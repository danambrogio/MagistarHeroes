'''
Created on Jan 24, 2016

@author: Dan
'''

import pygame
import universe

pygame.init()

# Game setup
WIDTH = 800
HEIGHT = 600
gameDisplay = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Magistar Heroes')
clock = pygame.time.Clock()

def show_title_screen():
    gameDisplay.fill((0,0,0))
    logo = pygame.image.load('../img/magistar-logo.gif').convert()
    gameDisplay.blit(logo, (0,0))
    pygame.display.update()
    show_title = True
    while show_title:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show_title = False
            if event.type == pygame.KEYDOWN:
                show_title = False
    
def show_main_menu():
    # Give the user multiple options
    
    # TODO: Implement this
    
    # For now, assume they start a new game
    return "new game"
    
if __name__ == "__main__":
    # Title Screen
    show_title_screen()
    
    # Main menu
    option = show_main_menu()
    
    if option == "new game":
        playing = True
        dimension = universe.Universe("MagistarHeroes")    # this is the seed
        planet = dimension.galaxies[0].solars[0].planets[0]
    
    while playing:
        # Game loop
        
        # Handle events
        for event in pygame.event.get():
            
            if event.type == pygame.QUIT:
                playing = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    playing = False
                print(event)    #TODO: Pass key events to the key event handler, handle actions
            
            
        # Draw loop
        gameDisplay.fill((255,255,255))
    
        # Tick
        # TODO: only update dirty rects
        pygame.display.update()
        clock.tick_busy_loop(40)
        
