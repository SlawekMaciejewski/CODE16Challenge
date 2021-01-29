from turtle import Screen, Turtle
import random

COLOR_PALETTE = [(201, 164, 112), (239, 246, 241), (152, 75, 50), (221, 201, 138), (57, 95, 126), (170, 152, 44),
                 (138, 31, 20), (135, 163, 183), (196, 94, 75), (49, 121, 88), (143, 177, 149), (95, 75, 77),
                 (76, 39, 32), (164, 146, 157), (16, 98, 71), (232, 176, 165), (54, 46, 48), (32, 61, 76), (22, 83, 89),
                 (182, 204, 176), (141, 22, 25), (86, 147, 127), (45, 66, 85), (8, 68, 53), (177, 94, 97),
                 (222, 177, 182), (109, 128, 151)]

screen = Screen()
screen.colormode(255)
paint = Turtle()


def draw_row():
    for _ in range(10):
        paint.dot(20, random.choice(COLOR_PALETTE))
        paint.forward(50)


draw_row()

screen.exitonclick()
