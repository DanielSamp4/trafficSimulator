
import pygame
import map 
import road
import car
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
road_1 = road.Road(my_map, 150, 20, "horizontal")
road_2 = road.Road(my_map, 142, 20, "vertical")
#draw the road
road_1.draw(screen)
road_2.draw(screen)
# road_2.draw_random(screen)
# my_map.color_points(screen, my_map.get_intersection_points(road_1, road_2), (255, 0, 0))


# Create a car and add it to the map
car = car.Car(100, 150, my_map, road_1)


# Update the display
pygame.display.flip()

# Run the Pygame loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    # Update the display
     # Update the car position and draw it on the map
    car.update(screen)
    pygame.display.flip()
    # my_vertical_road.draw_random(screen)
    # my_map.color_points(screen, my_map.get_intersection_points(my_horizontal_road, my_vertical_road), (255, 0, 0))
    pygame.time.delay(500)
# Quit Pygame
pygame.quit()