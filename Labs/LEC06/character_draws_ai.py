
from pico2d import *
import math

open_canvas(800, 600)
character = load_image('character.png')

def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)

def draw_circle():
    print("circle")
    for degree in range(0, 360, 5):
        rad = math.radians(degree)
        x = 400 + 200 * math.cos(rad)
        y = 300 + 200 * math.sin(rad)
        draw_character(x, y)


draw_circle()

close_canvas()