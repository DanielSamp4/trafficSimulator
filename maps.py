class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[None for _ in range(width)] for _ in range(height)]

    class Road:
        def __init__(self, start, large, direction):
            self.start = start
            self.large = large
            self.direction = direction
            
            # Set the end of the road
            if direction == "horizontal":
                self.end = (self.start + self.large, 0)
            elif direction == "vertical":
                self.end = (0, self.start + self.large)

        def add_vehicle(self, vehicle):
            # Add a vehicle to the road
            pass
            
        
    def add_object(self, obj, x, y):
        if isinstance(obj, self.Road):
            # Add the road to the map at multiple points
            for z in range(obj.large):
                for y in range(self.width):
                    if x + z < self.width and x + z >= 0:
                        self.grid[y][x + z] = obj
                    if x - z < self.width and x - z >= 0:
                        self.grid[y][x - z] = obj
        else:
            self.grid[y][x] = obj
        
    def remove_object(self, x, y):
        self.grid[y][x] = None
        
    def get_object(self, x, y):
        return self.grid[y][x]