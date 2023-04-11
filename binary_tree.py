import random


class BinaryTree:
    @staticmethod
    def on(grid):
        for cell in grid.each_cell():
            neighbors = []
            if cell.north:
                neighbors.append(cell.north)
            if cell.east:
                neighbors.append(cell.east)

            if neighbors:
                neighbor = random.choice(neighbors)
                cell.link(neighbor)
        return grid
