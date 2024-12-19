import pygame

class Player:
    def __init__(self, screen, screen_width, screen_height):
        self.screen = screen
        self.coordinates = pygame.Vector2(screen_width //2, screen_height //2)
        self.color = (255, 255, 255)
        self.radius = 10
    
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.coordinates.x -= 1
        if keys[pygame.K_d]:
            self.coordinates.x += 1
        
    def draw(self):
        pygame.draw.circle(self.screen, self.color, self.coordinates, self.radius)   # surface, rgb, coord, radius
    
        