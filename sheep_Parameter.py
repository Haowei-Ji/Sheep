import pygame
import sys

from networkx import radius

pygame.init()

screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("sheep")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


# Background color
screen.fill(WHITE)

# Hesh grid Draw
grid_size = 50
for x in range(0, 800, grid_size):
    pygame.draw.line(screen, BLACK, (x, 0), (x, 600), 1)
for y in range(0, 600, grid_size):
    pygame.draw.line(screen, BLACK, (0, y), (800, y), 1)

Radius = 200

# Body(ellipse)
#pygame.draw.circle(screen, BLACK, [400, 300], 200, 3)
body_width = 2 * Radius
body_height = Radius
body_x =screen_width//2 - Radius
body_y =screen_height//2 - Radius//2
pygame.draw.ellipse(screen, BLACK, [body_x , body_y, body_width , body_height],  3)

# Head
#pygame.draw.ellipse(screen, BLACK, [150, 150, 125, 200], 3)
head_width = Radius // 2
head_height = Radius
head_x = body_x
head_y =body_y -
pygame.draw.ellipse(screen, BLACK, [screen_width//2 - Radius, screen_height//2 - Radius, head_width, head_height], 3)


#Ears
ear_width = Radius // 8
ear_height = Radius // 2
pygame.draw.ellipse(screen, BLACK, [screen_width//2 - Radius, screen_height//2 - Radius + head_height//2, ear_width, ear_height])  # Left ear
pygame.draw.ellipse(screen, BLACK, [screen_width//2 - Radius +head_width, screen_height//2 - Radius + head_height//2, ear_width, ear_height])  # Right ear
#pygame.draw.ellipse(screen, BLACK, [135, 250, 30, 100])  # Left ear
#pygame.draw.ellipse(screen, BLACK, [260, 250, 30, 100])  # Right ear

#Face cleaning
#pygame.draw.ellipse(screen, WHITE, [152, 152, 120, 195])
pygame.draw.ellipse(screen, WHITE, [screen_width//2 - Radius +2 , screen_height//2 - Radius +2, head_width -5, head_height-5])

#Nose
pygame.draw.circle(screen, BLACK, [190, 300], 5, 3)
pygame.draw.circle(screen, BLACK, [225, 300], 5, 3)

# Eyes
pygame.draw.circle(screen, BLACK, [190, 220], 20, 3)  # Left eye
pygame.draw.circle(screen, BLACK, [235, 220], 20, 3)  # Right eye
pygame.draw.circle(screen, BLACK, [200, 225], 3)  # Left eye ball
pygame.draw.circle(screen, BLACK, [225, 225], 3)  # Right eye ball

# Tail
pygame.draw.circle(screen, BLACK, [625, 325], 25)

# Legs
pygame.draw.rect(screen, BLACK, [275, 450, 15, 100], 3)  # Right front leg
pygame.draw.rect(screen, BLACK, [325, 475, 15, 100], 3)  # Left front leg
pygame.draw.rect(screen, BLACK, [550, 425, 15, 150], 3)  # Left back leg
pygame.draw.rect(screen, BLACK, [525, 450, 15, 100], 3)  # Right back leg


pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
