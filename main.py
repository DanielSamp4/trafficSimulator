
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
# road_1 = road.Road(my_map, 150, 20, "horizontal")
# road_2 = road.Road(my_map, 142, 20, "vertical")
#draw the road
# road_1.draw(screen)
# road_2.draw(screen)
# road_2.draw_random(screen)
# my_map.color_points(screen, my_map.get_intersection_points(road_1, road_2), (255, 0, 0))
# Create the roads
roads = []
road1 = road.Road(my_map, 100, 10, "horizontal")
road2 = road.Road(my_map, 200, 10, "horizontal")
road3 = road.Road(my_map, 300, 10, "horizontal")
road4 = road.Road(my_map, 400, 10, "horizontal")
road5 = road.Road(my_map, 500, 10, "horizontal")
road6 = road.Road(my_map, 100, 10, "vertical")
road7 = road.Road(my_map, 200, 10, "vertical")
road8 = road.Road(my_map, 300, 10, "vertical")
road9 = road.Road(my_map, 400, 10, "vertical")
road10 = road.Road(my_map, 500, 10, "vertical")
roads.append(road1)
roads.append(road2)
roads.append(road3)
roads.append(road4)
roads.append(road5)
roads.append(road6)
roads.append(road7)
roads.append(road8)
roads.append(road9)
roads.append(road10)


# Create a car and add it to the map
car = car.Car(100, 100, my_map, road1)
# Draw the roads on the screen
for road in roads:
    my_map.add_road(road)
    road.draw(screen)

# Set the starting and ending points
start = (100, 100)
end = (500, 500)

# Find the shortest path between the starting and ending points
path = my_map.bfs(start, end)

# Draw the path on the screen
for point in path:
    pygame.draw.circle(screen, (255, 0, 0), point, 1)


car.move_along_path( path, screen)
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
    # car.move_along_path( path, screen)
    pygame.display.flip()
    # my_vertical_road.draw_random(screen)
    # my_map.color_points(screen, my_map.get_intersection_points(my_horizontal_road, my_vertical_road), (255, 0, 0))
    pygame.time.delay(500)
# Quit Pygame
pygame.quit()