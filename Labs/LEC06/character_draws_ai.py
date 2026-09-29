
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

def draw_rectangle():
    print("rectangle")
    
    # 아랫변
    for x in range(50, 750, 5):
        draw_character(x, 50)
    # 오른쪽변
    for y in range(50, 550, 5):
        draw_character(750, y)
    # 윗변
    for x in range(750, 50, -5):
        draw_character(x, 550)
    # 왼쪽변
    for y in range(550, 50, -5):
        draw_character(50, y)

def draw_triangle():
    print("triangle")
    
    # 밑변
    print('tri_BOTTOM')
    for x in range(200, 600, 5):
        draw_character(x, 100)
        
    # 오른쪽 변
    print('tri_RIGHT')
    for x, y in zip(range(600, 400, -5), range(100, 500, 10)):
        draw_character(x, y)
        
    # 왼쪽 변
    print('tri_LEFT')
    for x, y in zip(range(400, 200, -5), range(500, 100, -10)):
        draw_character(x, y)


draw_circle()
draw_rectangle()
draw_triangle()

while True:
    draw_circle()
    draw_rectangle()
    draw_triangle()

close_canvas()