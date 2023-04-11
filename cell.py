from distances import Distances

class Cell:
    def __init__(self, row, column):
        self.row = row
        self.column = column
        self.links = {}  # type: ignore
        self.north = None
        self.south = None
        self.east = None
        self.west = None

    def link(self, cell, bidi=True):
        self.links[cell] = True # type: ignore
        if bidi:
            cell.link(self, False)
        return self

    def unlink(self, cell, bidi=True):
        self.links.pop(cell, None)
        if bidi:
            cell.unlink(self, False)
        return self

    def linked(self, cell):
        return cell in self.links

    def neighbors(self):
        list = []
        if self.north:
            list.append(self.north)
        if self.south:
            list.append(self.south)
        if self.east:
            list.append(self.east)
        if self.west:
            list.append(self.west)
        return list

    def links(self):
        return self.links.keys()

    def distances(self):
        distances = Distances(self)
        frontier = [self]

        while frontier:
            new_frontier = []
            for cell in frontier:
                for linked in cell.links():
                    if not distances[linked]:
                        distances[linked] = distances[cell] + 1
                        new_frontier.append(linked)
            frontier = new_frontier

        return distances
