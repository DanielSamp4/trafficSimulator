import random
import map
import pygame
class Road:
        def __init__(self, map , start, large, direction):
            self.start = start
            self.large = large
            self.direction = direction
            self.color_street = (0, 0, 0)
            self.map = map
            self.points = set()
            self.get_points()
            
        def get_points(self):
            if self.direction == "horizontal":
                for i in range(640):
                    self.points.add((i, self.start))
            elif self.direction == "vertical":
                for i in range(640):
                    self.points.add((self.start, i))

        def draw(self, surface):
            if self.direction == "horizontal":
                # Draw the road in the specified color
                pygame.draw.line(surface, self.color_street , (0 ,self.start),(self.map.width ,self.start), self.large)
            elif self.direction == "vertical":
                # Draw the road in the specified color
                pygame.draw.line(surface, self.color_street , (self.start , 0),(self.start,self.map.width), self.large)
            
        def draw_random(self, surface):
            self.seed = random.randrange(0, self.map.width, 1)
            self.direction = random.choice(['horizontal', 'vertical'])
            if self.direction == "horizontal": # Horizontal road
                # Draw the road in the specified color
                pygame.draw.line(surface, self.color_street , (0 ,self.seed),(self.map.width ,self.seed), self.large)
            elif self.direction == "vertical": # Vertical road
                # Draw the road in the specified color
                pygame.draw.line(surface, self.color_street , (self.seed , 0),(self.seed,self.map.width), self.large)
            

        def add_vehicle(self, vehicle):
            # Add a vehicle to the road
            pass

        def is_on_road(self, x, y):
            if self.direction == "horizontal":
                return self.start - self.large // 2 <= y <= self.start + self.large // 2
            elif self.direction == "vertical":
                return self.start - self.large // 2 <= x <= self.start + self.large // 2
        
        def which_direction(self):
            return self.direction