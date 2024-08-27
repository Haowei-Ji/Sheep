import pygame
import sys
import math
import os


pygame.init()

# set up the display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Sheep on Dynamic Grass ')



# load images path
grass_1_path = os.path.join('Pic', 'grass_1.png')
grass_2_path = os.path.join('Pic', 'grass_2.png')
sheep_image_path = os.path.join('Pic', 'sheep_yang.png')

# load images
grass_1 = pygame.image.load(grass_1_path)
grass_2 = pygame.image.load(grass_2_path)
sheep_image = pygame.image.load(sheep_image_path)

'''# get the rect of the image
grass_rect = grass_1.get_rect()
sheep_rect = sheep_image.get_rect()'''

# scale factor
r = 0.1

# new dimensions
new_width = int(sheep_image.get_width() * r)
new_height = int(sheep_image.get_height() * r)
# scale the image
scaled_image = pygame.transform.scale(sheep_image, (new_width, new_height))


# Creating a Dictionary of Grasses
grasses_1 = [
    {"x": 100, "y": 100, "amplitude": 5, "frequency": 0.005, "phase": 0},
    {"x": 300, "y": 300, "amplitude": 8, "frequency": 0.003, "phase": math.pi / 4},
    {"x": 650, "y": 450, "amplitude": 6, "frequency": 0.004, "phase": math.pi / 2},
    {"x": 400, "y": 550, "amplitude": 6, "frequency": 0.004, "phase": math.pi / 2},
]

grasses_2 = [
    {"x": 150, "y": 500, "amplitude": 3, "frequency": 0.002, "phase": 0},
    {"x": 600, "y": 300, "amplitude": 4, "frequency": 0.003, "phase": math.pi / 4},
   
]

# original image position
x_sheep, y_sheep = 400, 300
speed_sheep = 1


# main loop
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # calculate the time
    t = pygame.time.get_ticks()  # (ms)

    '''# calculate the new position of the grass
    offset = amplitude * math.sin(frequency * t)
    new_x = x + offset    
    screen.blit(grass_1, (new_x, y))'''

    # fill the screen's background color
    screen.fill((191, 254, 137))  # light green

    # dynamic grass
    for grass1 in grasses_1:
        # calculate the new position of the grass_1
        offset = grass1["amplitude"] * math.sin(grass1["frequency"] * t + grass1["phase"])
        new_x = grass1["x"] + offset
        screen.blit(grass_1, (new_x, grass1["y"]))

    for grass2 in grasses_2:
        # calculate the new position of the grass_2
        offset = grass2["amplitude"] * math.sin(grass2["frequency"] * t + grass2["phase"])
        new_x = grass2["x"] + offset
        screen.blit(grass_2, (new_x, grass2["y"]))
    
    # key control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x_sheep -= speed_sheep
    if keys[pygame.K_RIGHT]:
        x_sheep += speed_sheep
    if keys[pygame.K_UP]:
        y_sheep -= speed_sheep
    if keys[pygame.K_DOWN]:
        y_sheep += speed_sheep

    # sheep
    screen.blit(scaled_image, (x_sheep,y_sheep))
    pygame.display.flip()

    # control the speed of the game
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
