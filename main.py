import pygame, random
from Player import Player
from Platform import Platform

pygame.init()
screen_width = 400
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Doodle Jump")

player = Player(screen, screen_width, screen_height)
platformCount = screen_height // 100
platforms = []
for i in range(platformCount - 1):
    platforms.append(Platform(screen, 100 * i + random.randint(0, 25) , screen_width, screen_height))


running = True
while running:
    
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
    screen.fill((59, 184, 182))       
    player.update()
    
    
    player.draw()
    for platform in platforms:
        platform.draw()
    pygame.display.flip() 

pygame.quit()