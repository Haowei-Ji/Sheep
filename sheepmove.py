import pygame
import sys
import io

pygame.init()
pygame.display.set_caption('sheepmove')
screen = pygame.display.set_mode((800, 600))
sheep_image = pygame.image.load('sheep_bmp_ori.bmp')   

# scale factor
r = 0.08 

# new dimensions
new_width = int(sheep_image.get_width() * r)
new_height = int(sheep_image.get_height() * r)
# scale the image
scaled_image = pygame.transform.scale(sheep_image, (new_width, new_height))

pygame.display.flip()  

# original image position
x, y = 400, 300
speed = 0.5


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # key control
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    screen.fill((191, 254, 137))
    
    screen.blit(scaled_image, (x,y))
    pygame.display.flip()

pygame.quit()
