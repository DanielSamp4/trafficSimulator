import pygame
from collections import deque
class Map:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.roads = []
        self.grid = [[None for _ in range(width)] for _ in range(height)]
        
    def add_object(self, obj, x, y):
        pass
        
    def remove_object(self, x, y):
        self.grid[y][x] = None
        
    def get_object(self, x, y):
        return self.grid[y][x]

    def add_road(self, road):
        # Add a road to the map
        self.roads.append(road)    

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

    def bfs(self, start, end):
        # Create a queue to store the nodes to be visited
        queue = deque()
        # Add the starting node to the queue
        queue.append(start)
        # Create a set to store the visited nodes
        visited = set()
        # Create a dictionary to store the predecessor of each node
        predecessor = {}
        # Add the starting node to the visited set
        visited.add(start)
        # While the queue is not empty
        while queue:
            # Get the next node from the queue
            node = queue.popleft()
            # If the node is the end node, we are done
            if node == end:
                break
            # Get the neighbors of the node
            neighbors = self.get_neighbors(node)
            # For each neighbor of the node
            for neighbor in neighbors:
                # If the neighbor has not been visited
                if neighbor not in visited:
                    # Add the neighbor to the visited set
                    visited.add(neighbor)
                    # Add the neighbor to the queue
                    queue.append(neighbor)
                    # Set the predecessor of the neighbor to be the current node
                    predecessor[neighbor] = node
        # Create a list to store the path from the start to the end
        path = []
        # Set the current node to be the end node
        node = end
        # While the current node is not the starting node
        while node != start:
            # Add the current node to the path
            path.append(node)
            # Set the current node to be its predecessor
            node = predecessor[node]
        # Add the starting node to the path
        path.append(start)
        # Reverse the path to get the correct order
        path.reverse()
        # Return the path
        return path

    def get_neighbors(self, node):
        # Get the neighbors of a node on the map
        x, y = node
        neighbors = []
        # For each road on the map
        for road in self.roads:
            # If the road is horizontal
            if road.direction == "horizontal":
                # If the node is on the road
                if road.start == y:
                    # Check if the node has a neighbor to the left
                    if (x - 1, y) not in neighbors and (x - 1, y) in road.points:
                        neighbors.append((x - 1, y))
                    # Check if the node has a neighbor to the right
                    if (x + 1, y) not in neighbors and (x + 1, y) in road.points:
                        neighbors.append((x + 1, y))
            # If the road is vertical
            if road.direction == "vertical":
                # If the node is on the road
                if road.start == x:
                    # Check if the node has a neighbor above
                    if (x, y - 1) not in neighbors and (x, y - 1) in road.points:
                        neighbors.append((x, y - 1))
                    # Check if the node has a neighbor below
                    if (x, y + 1) not in neighbors and (x, y + 1) in road.points:
                        neighbors.append((x, y + 1))
        # Return the list of neighbors
        return neighbors