# Import a library of functions called 'pygame'
import pygame
import math
import random

# Constants
PI = 3.141592653
# Define some colors
BLACK  = (   0,   0,   0)
WHITE  = ( 255, 255, 255)
GREEN  = (   0, 255,   0)
RED    = ( 255,   0,   0)
BLUE   = (   0,   0, 255)
YELLOW = ( 255, 255,   0)

# Initialize the src engine
pygame.init()

# Hide the mouse cursor
pygame.mouse.set_visible(False)

size = (700, 500)
screen = pygame.display.set_mode(size)

# Add a caption for the window 
pygame.display.set_caption("Mutant Space Invaders")

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
rect_x = random.randrange(100, 550)
rect_y = random.randrange(100, 350)
rect_change_x = 3 * random.choice([1, -1])
rect_change_y = 2 * random.choice([1, -1])
snow_list = []
for i in range(50):
    x = random.randrange(0, 700)
    y = random.randrange(0, 500)
    snow_list.append([x, y])

spaceShipPos = 0
def drawSpaceShip(x):
    pygame.draw.polygon(screen, BLUE, [[x - 6, 450], [x + 1, 425], [x + 8, 450]])
    pygame.draw.rect(screen, BLUE, [x - 2, 450 , 3, 5])
    pygame.draw.rect(screen, BLUE, [x + 3 , 450 , 3, 5])

numberOfSuperShots = 1
shotList = []
def spaceShipShot(x):
    shotList.append([x, 415, False])

def spaceShipSpecialShot(x):
    shotList.append([x, 415, True])

def drawShots():
    for shot in shotList:
        if (shot[2]):
            pygame.draw.circle(screen, RED, [shot[0], shot[1]], 10)
        else:
            pygame.draw.rect(screen, YELLOW, [shot[0], shot[1], 2, 6])

# -------- Main Program Loop -----------
mousePosition = 0
while not done:
    # --- Main event loop
    pos = pygame.mouse.get_pos()
    spaceShipPos = pos[0]

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if numberOfSuperShots > 0:
                    spaceShipSpecialShot(pos[0])
                    numberOfSuperShots -= 1
            print("User pressed a KEY")
        elif event.type == pygame.KEYUP:
            print("User let go of a key.")
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if len(shotList) < 3:
                spaceShipShot(pos[0])
 
    # --- Game logic should go here
 
    # --- Drawing code should go here

    # First, clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(BLACK)

    # Process each snow flake in the list
    for i in range(len(snow_list)):
        # Draw the snow flake
        pygame.draw.circle(screen, WHITE, snow_list[i], 2)
        # Move the snow flake down one pixel
        snow_list[i][1] += 1    
        snow_list[i][0] += int(math.sin(snow_list[i][1]))
        # If the snow flake has moved off the bottom of the screen
        if snow_list[i][1] > 500:
            # Reset it just above the top
            y = random.randrange(-50, -10)
            snow_list[i][1] = y
            # Give it a new x position
            x = random.randrange(0, 700)
            snow_list[i][0] = x

    pygame.draw.rect(screen, GREEN, [rect_x,rect_y,50,50])
    rect_x += rect_change_x
    rect_y += rect_change_y
    # Bounce the rectangle if needed
    if rect_y > 450 or rect_y < 0:
        rect_change_y = rect_change_y * -1
    if rect_x > 650 or rect_x < 0:
        rect_change_x = rect_change_x * -1

    drawSpaceShip(spaceShipPos)
    shotsToRemove = []
    for i, shot in enumerate(shotList):
        shot[1] -= 3
        if shot[1] <= 0:
            shotsToRemove.append(i)
        else:
            drawShots()
    
    for i in shotsToRemove:
        del shotList[i]
    
    # Select the font to use, size, bold, italics
    fontScore = pygame.font.SysFont('Calibri', 25, True, False)
    # Render the text. "True" means anti-aliased text.
    # Black is the color. The variable BLACK was defined
    # above as a list of [0, 0, 0]
    # Note: This line creates an image of the letters,
    # but does not put it on the screen yet.
    text = fontScore.render("Score: " + str(0), True, WHITE)
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [550, 30])

    fontSuperShot = pygame.font.SysFont('Calibri', 18, True, False)
    text = fontSuperShot.render("Super shot: " + str(numberOfSuperShots), True, WHITE)
    # Put the image of the text on the screen at 250x250
    screen.blit(text, [10, 50])
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 60 frames per second
    clock.tick(60)

pygame.quit()