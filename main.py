import tkinter
import json
from resources import Resources
from hero import Hero
from grid import Grid

# Create the tk environment as usual

with open("level.json", 'r') as file:
    level = json.load(file)


image_size = 72
board_size_x = len(level[0])
board_size_y = len(level)

root = tkinter.Tk()
canvas = tkinter.Canvas(
    root,
    width=image_size * board_size_x,
    height=image_size * board_size_y + 30
)


hero = Hero(0, 0, 0)

# Create a function that can be called when a key pressing happens
def on_key_press(e):

    grid.draw()
    if e.keycode == 37: # LEFT
        if level[hero.y][hero.x - 1] != 1:
            hero.x -= 1
        if hero.x <= 0:
            hero.x = 0
        canvas.create_image((hero.x * 72) + 36, (hero.y * 72) + 36, image=resources.images["hero-left"])
    elif e.keycode == 38: # UP
        if level[hero.y - 1][hero.x] != 1:
            hero.y -= 1
        if hero.y <= 0:
            hero.y = 0
        canvas.create_image((hero.x * 72) + 36, (hero.y * 72) + 36, image=resources.images["hero-up"])
    elif e.keycode == 39: # RIGHT
        if hero.x >= 9:
            hero.x = 9
        elif level[hero.y][hero.x + 1] != 1:
            hero.x += 1
        canvas.create_image((hero.x * 72) + 36, (hero.y * 72) + 36, image=resources.images["hero-right"])
    elif e.keycode == 40: # DOWN
        if hero.y >= 9:
            hero.y = 9
        elif level[hero.y + 1][hero.x] != 1:
            hero.y += 1
        canvas.create_image((hero.x * 72) + 36, (hero.y * 72) + 36, image=resources.images["hero-down"])

    canvas.create_image(180, 252, image=resources.images["skeleton"])
    canvas.create_image(468, 36, image=resources.images["skeleton"])
    canvas.create_image(36, 540, image=resources.images["skeleton"])
    canvas.create_image(540, 396, image=resources.images["boss"])

# Create a function that can be called when a key pressing happens

canvas.bind("<KeyPress>", on_key_press)
canvas.pack()

def white_box():
    canvas.create_rectangle(0, 720, 720, 750, fill="white")



resources = Resources()
grid = Grid(board_size_x, board_size_y, canvas, level, resources)


# Create a function that can be called when mouse click happens
def on_mouse_click(loc):
    print(loc.x, loc.y)


canvas.bind("<ButtonRelease>", on_mouse_click)
canvas.pack()


canvas.focus_set()

# Draw the box in the initial position
grid.draw()


print(white_box())


root.mainloop()