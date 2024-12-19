import pygame, random

class Platform:
    
    def __init__(self,screen,yCoord,  screen_width, screen_height):
        self.screen = screen
        self.height = 10
        self.width = random.randint(100, 150)
        self.y = yCoord
        self.x = random.randint(0, screen_width - self.width)
    
    
    def draw(self):
        pygame.draw.rect(self.screen, (0, 255, 0), (self.x, self.y, self.width, self.height))
        
        
        