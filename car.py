import pygame
class Car:
    def __init__(self, x, y, mapa, road):
        self.x = x
        self.y = y
        self.mapa = mapa
        self.road = road
        self.color = (210, 120, 66)
        self.size = (self.road.large/2, self.road.large/2)
    
    def draw(self, surface):
        # Use the Pygame draw.rect function to draw a rectangle at the current position
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size[0], self.size[1]))
        # Use the Pygame draw.rect function to draw a white rectangle at the previous position
        pygame.draw.rect(surface, self.road.color_street, (self.prev_x, self.prev_y, self.size[0], self.size[1]))
        
    def move(self):
        # move the car to the next position here
        # check if the car is on the road before moving
        if self.road.is_on_road(self.x, self.y):
            # move the car to the next position
            self.prev_x = self.x
            self.prev_y = self.y
            if self.road.direction == "vertical":
                self.y = self.y + self.size[1]
            if self.road.direction == "horizontal":
                self.x = self.x + self.size[0]
    
    def update(self, screen):
        self.move()
        self.draw(screen)