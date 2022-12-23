import pygame
import maps 

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (640, 480)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the background color
screen.fill((255, 255, 255))

# Create the map and the road
my_map = maps.Map(256, 256)
my_horizontal_road = my_map.Road(15, 60, "horizontal")
my_vertical_road = my_map.Road(15, 60, "vertical")

# Add the roads to the map
for x in range(my_horizontal_road.start, my_horizontal_road.end[1]):
    my_map.add_object(my_horizontal_road, x, my_horizontal_road.start)
# for y in range(my_vertical_road.start, my_vertical_road.end[1]):
#     my_map.add_object(my_vertical_road, my_vertical_road.start, y)

# Draw the map
for y in range(my_map.height):
    for x in range(my_map.width):
        object = my_map.get_object(x, y)
        if isinstance(object, my_map.Road):
            # Draw the outline of the road
            if object.direction == "horizontal":
                if x == 0 or x == my_map.width - 1:
                    pygame.draw.rect(screen, (128, 128, 128), (x * 2, y * 2, 2, 2))
            elif object.direction == "vertical":
                if y == 0 or y == my_map.height - 1:
                    pygame.draw.rect(screen, (128, 128, 128), (x * 2, y * 2, 2, 2))
        elif object == "Tree":
            # Draw a tree at (x, y)
            pygame.draw.rect(screen, (0, 128, 0), (x * 2, y * 2, 2, 2))
        elif object == "Car":
            # Draw a car at (x, y)
            pygame.draw.rect(screen, (0, 0, 128), (x * 2, y * 2, 2, 2))

# Update the display
pygame.display.flip()

# Run the Pygame loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Quit Pygame
pygame.quit()