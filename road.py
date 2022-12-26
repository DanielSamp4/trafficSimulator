import random
import map
import pygame
class Road:
        def __init__(self, map , start, large, direction):
            self.start = start
            self.large = large
            self.direction = direction
            self.color_street = (0, 0, 0)

        def draw(self, surface):
            if self.direction == "horizontal":
                # Draw the road in the specified color
                pygame.draw.line(surface, self.color_street , (0 ,self.start),(640 ,self.start), self.large)
            elif self.direction == "vertical":
                # Draw the road in the specified color
                pygame.draw.line(surface, self.color_street , (self.start , 0),(self.start,640), self.large)
            
        def draw_random(self, surface):
            self.seed = random.randrange(0, 640, 1)
            self.direction = random.choice(['horizontal', 'vertical'])
            if self.direction == "horizontal": # Horizontal road
                # Draw the road in the specified color
                pygame.draw.line(surface, self.color_street , (0 ,self.seed),(640 ,self.seed), self.large)
            elif self.direction == "vertical": # Vertical road
                # Draw the road in the specified color
                pygame.draw.line(surface, self.color_street , (self.seed , 0),(self.seed,640), self.large)
            

        def add_vehicle(self, vehicle):
            # Add a vehicle to the road
            pass