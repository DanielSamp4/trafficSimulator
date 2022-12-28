import pygame
class Car:
    def __init__(self, x, y, mapa, road):
        self.x = x
        self.y = y
        self.mapa = mapa
        self.road = road
        self.color = (210, 120, 66)
        self.size = (self.road.large/2, self.road.large/2)
        self.path = []
    
    def draw(self, surface):
        # Use the Pygame draw.rect function to draw a rectangle at the current position
        pygame.draw.rect(surface, self.color, (self.x, self.y, self.size[0], self.size[1]))
        # Use the Pygame draw.rect function to draw a white rectangle at the previous position
        pygame.draw.rect(surface, self.road.color_street, (self.prev_x, self.prev_y, self.size[0], self.size[1]))
        pygame.display.flip()
    def move(self):
        # move the car to the next position here
        # check if the car is on the road before moving
        if self.road.is_on_road(self.x, self.y):
            self.prev_x = self.x
            self.prev_y = self.y
            # move the car to the next position
            if self.road.direction == "vertical":
                self.y = self.y + self.size[1]
                return True
            if self.road.direction == "horizontal":
                self.x = self.x + self.size[0]
                return True
        else:
            return False
        
    def update(self, screen):
        if self.move():
            self.draw(screen)
    
    def move_along_path(self, path, screen):
        # Set the current position of the car to be the first point in the path
        self.path = path
        self.x, self.y = self.path[0]
        # For each point in the path, starting from the second point
        for point in path[1:]:
            # Set the previous position of the car to be the current position
            self.prev_x, self.prev_y = self.x, self.y
            # Set the current position of the car to be the next point in the path
            self.x, self.y = point

            # if self.road.direction == "vertical":
            #     self.y = point[1] + self.size[1]
            # if self.road.direction == "horizontal":
            #     self.x = point[0] + self.size[0]
            # Draw the car on the screen
            self.draw(screen)
            # Wait for a short time before moving to the next point
            pygame.time.delay(10)