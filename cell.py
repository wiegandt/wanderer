class Cell:

    def __init__(self, x, y, cell_type, cell_image):
        self.x = x
        self.y = y
        self.cell_type = cell_type
        self.cell_image = cell_image
        self.image_size = 72

    def draw(self, canvas):
        canvas.create_image(
            self.x * self.image_size + (self.image_size / 2),
            self.y * self.image_size + (self.image_size / 2),
            image=self.cell_image
        )
