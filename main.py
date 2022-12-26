
import pygame
import map 
import road

# Initialize Pygame
pygame.init()

# Set the window size
window_size = (640, 640)

# Create the window
screen = pygame.display.set_mode(window_size)

# Set the background color
screen.fill((255, 255, 255))

# Create the map and the road
my_map = map.Map(640, 640)
my_horizontal_road = road.Road(my_map, 150, 10, "horizontal")
my_vertical_road = road.Road(my_map, 142, 10, "vertical")

#draw the road
# my_horizontal_road.draw(screen)
# my_vertical_road.draw(screen)
# my_vertical_road.draw_random(screen)

# Update the display
pygame.display.flip()

# Run the Pygame loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update the display
    pygame.display.flip()
    my_vertical_road.draw_random(screen)
    my_map.color_points(screen, my_map.get_intersection_points(my_horizontal_road, my_vertical_road), (255, 0, 0))
    pygame.time.delay(500)
# Quit Pygame
pygame.quit()