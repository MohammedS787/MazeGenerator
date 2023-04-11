import pygame
import random
from cell import Cell
from grid import Grid
from binary_tree import BinaryTree

# Initialize pygame
pygame.init()

# Maze dimensions
rows = 25
columns = 25

# Screen dimensions
width = 640
height = 480

# Cell size
cell_size = 40

# Create the screen with the RESIZABLE flag
screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
pygame.display.set_caption("Maze Visualization")

# Create a grid and generate a maze using the BinaryTree algorithm
grid = Grid(rows, columns)
BinaryTree.on(grid)

# Convert the grid to a pygame Surface
maze_image = pygame.image.fromstring(grid.to_png(cell_size).tobytes(), (cell_size * columns + 1, cell_size * rows + 1), "RGB")

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.VIDEORESIZE:
            # Update the screen size when the window is resized or maximized
            width, height = event.size
            screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)

    # Draw the maze
    screen.fill((255, 255, 255))
    screen.blit(maze_image, ((width - maze_image.get_width()) // 2, (height - maze_image.get_height()) // 2))
    pygame.display.flip()

pygame.quit()
