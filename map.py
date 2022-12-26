import pygame

class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        
    def add_object(self, obj, x, y):
        pass
        
    def remove_object(self, x, y):
        self.grid[y][x] = None
        
    def get_object(self, x, y):
        return self.grid[y][x]

    def get_intersection_points(self, road1, road2):
        """Returns a list of tuples representing the intersection points of the two roads"""
        points = []
        # Check if the roads are vertical and horizontal
        if road1.direction == "vertical" and road2.direction == "horizontal":
            # Check if the vertical road starts within the range of the horizontal road
            # if road1.start > road2.start and road1.start < road2.start + road2.large:
                # Add the intersection point to the list
                points.append((road1.start, road2.start))
        elif road1.direction == "horizontal" and road2.direction == "vertical":
            # Check if the horizontal road starts within the range of the vertical road
            # if road2.start > road1.start and road2.start < road1.start + road1.large:
                # Add the intersection point to the list
                points.append((road2.start, road1.start))
        return points

    def color_points(self, surface, points, color):
        """Colors the specified points in the specified color"""
        for point in points:
            x, y = point
            pygame.draw.circle(surface, color, (x, y), 5)