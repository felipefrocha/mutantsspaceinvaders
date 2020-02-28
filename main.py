import pygame
import random
from msi.Constants import *
from msi.SpaceShip import SpaceShip
from msi.Screen import Screen
from msi.EnemyFactory import EnemyFactory

# Initialize the src engine
pygame.init()

# Hide the mouse cursor
pygame.mouse.set_visible(False)

mscreen = Screen(pygame)
screen = pygame.display.set_mode(SIZE)

# Add a caption for the window 
pygame.display.set_caption("Mutant Space Invaders")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
enemy_list = [EnemyFactory.create("Rectangle")]

space_ship = SpaceShip(SPACE_SHIP_INITIAL_POS_X, SPACE_SHIP_INITIAL_POS_Y)

# -------- Main Program Loop -----------
mousePosition = 0
while not done:
    # --- Main event loop
    pos = pygame.mouse.get_pos()
    space_ship.set_pos_x(pos[0])

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                space_ship.super_shot()
            print("User pressed a KEY")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            space_ship.shot()
 
    # --- Game logic should go here

    space_ship.update_space_ship_shots()
    for enemy in enemy_list:
      enemy.update()
 
    # --- Drawing code should go here

    mscreen.clear()

    mscreen.draw_background_stars()

    mscreen.draw_space_ship(space_ship)

    mscreen.draw_enemies(enemy_list)

    mscreen.draw_score(0)
    mscreen.draw_super_shot(space_ship.get_current_number_of_super_shots())
    
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()