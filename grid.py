from cell import Cell


class Grid:
    def __init__(self, size_x, size_y, canvas, level, resources):
        self.size_x = size_x
        self.size_y = size_y
        self.level = level
        self.resources = resources
        self.canvas = canvas
        self.cells = self.build()

    #drawing the game area

    def build(self):
        cells = []
        pos_x = 0
        for x in self.level:
            pos_y = 0
            for y in x:
                if y == 0:
                    cells += [Cell(pos_y, pos_x, "floor", self.resources.images["floor"])]
                elif y == 1:
                    cells += [Cell(pos_y, pos_x, "wall", self.resources.images["wall"])]
                pos_y += 1
            pos_x += 1
        return cells

    def draw(self):
        for cell in self.cells:
            cell.draw(self.canvas)




