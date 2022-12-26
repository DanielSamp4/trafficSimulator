import pygame

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.road_start = (15, 0)
        self.road_end = (15, height)
    
    def draw(self, surface):
        # Fill the background with the map color
        surface.fill((255, 255, 255))
        
        pygame.draw.line(surface, (0, 0, 0), self.road_start, self.road_end, 5)

# Example usage
pygame.init()
screen = pygame.display.set_mode((256, 256))

my_map = Map(256, 256)
my_map.draw(screen)

pygame.display.flip()

# Run the Pygame loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()