import random
from cell import Cell
from PIL import Image, ImageDraw

class Grid:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.grid = self.prepare_grid()
        self.configure_cells()

    def prepare_grid(self):
        return [[Cell(row, col) for col in range(self.columns)] for row in range(self.rows)]

    def configure_cells(self):
        for cell in self.each_cell():
            row, col = cell.row, cell.column
            cell.north = self[row - 1, col]
            cell.south = self[row + 1, col]
            cell.west = self[row, col - 1]
            cell.east = self[row, col + 1]

    def __getitem__(self, pos):
        row, column = pos
        if 0 <= row < self.rows and 0 <= column < len(self.grid[row]):
            return self.grid[row][column]
        return None

    def random_cell(self):
        row = random.randrange(self.rows)
        column = random.randrange(len(self.grid[row]))
        return self[row, column]

    def size(self):
        return self.rows * self.columns

    def each_row(self):
        for row in self.grid:
            yield row

    def each_cell(self):
        for row in self.each_row():
            for cell in row:
                if cell:
                    yield cell

    def to_png(self, cell_size=10):
        img_width = cell_size * self.columns
        img_height = cell_size * self.rows

        background = (255, 255, 255)
        wall = (0, 0, 0)

        img = Image.new('RGB', (img_width + 1, img_height + 1), background)
        draw = ImageDraw.Draw(img)

        for cell in self.each_cell():
            x1 = cell.column * cell_size
            y1 = cell.row * cell_size
            x2 = (cell.column + 1) * cell_size
            y2 = (cell.row + 1) * cell_size

            if cell.north is None:
                draw.line([(x1, y1), (x2, y1)], fill=wall)
            if cell.west is None:
                draw.line([(x1, y1), (x1, y2)], fill=wall)
            if not cell.linked(cell.east):
                draw.line([(x2, y1), (x2, y2)], fill=wall)
            if not cell.linked(cell.south):
                draw.line([(x1, y2), (x2, y2)], fill=wall)

        return img

    def background_color_for(self, cell):
        return None
