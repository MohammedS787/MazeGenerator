import pygame
import random
from cell import Cell
from grid import Grid
import grid
from binary_tree import BinaryTree

# Initialize pygame
pygame.init()

# Maze dimensions
rows = 10
columns = 10

# Screen dimensions
width = 640
height = 480

# Cell size
cell_size = 40

# Create the screen with the RESIZABLE flag
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Maze Visualization")

# Determine the longest path in the maze
start = grid.Cell(0, 0)
distances = start.distances()
new_start, _ = distances.max()
new_distances = new_start.distances()
goal, _ = new_distances.max()
path = new_distances.path_to(goal)

# Create a list of positions in the longest path
path_positions = [(cell.row * cell_size + cell_size // 2, cell.column * cell_size + cell_size // 2) for cell in path.cells]

# Load the character sprite
character_sprite = pygame.image.load("mushroom.png").convert_alpha()
character_sprite = pygame.transform.scale(character_sprite, (cell_size // 2, cell_size // 2))

# Create a grid and generate a maze using the BinaryTree algorithm
grid = Grid(rows, columns)
BinaryTree.on(grid)

# Convert the grid to a pygame Surface
maze_image = pygame.image.fromstring(grid.to_png(cell_size).tobytes(), (cell_size * columns + 1, cell_size * rows + 1), "RGB")

# Initialize path index and character position
path_index = 0
character_pos = path_positions[path_index]

# Animation loop
running = True
clock = pygame.time.Clock()
while running:
    clock.tick(5)  # Set animation speed (5 frames per second)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            width, height = event.size
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    # Update character position
    path_index += 1
    if path_index < len(path_positions):
        character_pos = path_positions[path_index]
    else:
        running = False

    # Draw the maze and character
    screen.fill((255, 255, 255))
    screen.blit(maze_image, ((width - maze_image.get_width()) // 2, (height - maze_image.get_height()) // 2))
    screen.blit(character_sprite, (character_pos[1] + (width - maze_image.get_width()) // 2 - cell_size // 4,
                                   character_pos[0] + (height - maze_image.get_height()) // 2 - cell_size // 4))
    pygame.display.flip()

pygame.quit()
