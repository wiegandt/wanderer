from tkinter import *


class Resources:
    def __init__(self):
        self.images = {}
        self.images["boss"] = self.load_image("images/boss.gif")
        self.images["floor"] = self.load_image("images/floor.gif")
        self.images["hero-down"] = self.load_image("images/hero-down.gif")
        self.images["hero-left"] = self.load_image("images/hero-left.gif")
        self.images["hero-right"] = self.load_image("images/hero-right.gif")
        self.images["hero-up"] = self.load_image("images/hero-up.gif")
        self.images["skeleton"] = self.load_image("images/skeleton.gif")
        self.images["wall"] = self.load_image("images/wall.gif")

    def load_image(self, path):
        img = PhotoImage(file=path)
        return img
