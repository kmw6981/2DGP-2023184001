# 실습 과제 진행
from pico2d import *
import math

open_canvas(800, 600)

character = load_image('character.png')

def draw_circle():
    print("circle")
    for degree in range(0, 360, 5):
        rad=math.radians(degree)
        x=400 + 200 * math.cos(rad)
        y=300 + 200 * math.sin(rad)
        draw_character(x, y)
    pass

def draw_top():
    print('TOP')
    for x in range(50, 750, 5):
        draw_character(x,550)

def draw_character(x, y):
    clear_canvas()
    character.draw(x, y)
    update_canvas()
    delay(0.01)
  

def draw_right():
    print('RIGHT')
    for y in range(550, 50, -5):
        draw_character(750, y)
    
    pass

def draw_bottom():
    print('BOTTOM')
    for x in range(750, 50, -5):
        draw_character(x, 50)
    pass

def draw_left():
    print('LEFT')
    for y in range(50, 550, 5):
        draw_character(50, y)
    pass

def draw_rectangle():
    print("rectangle")
    draw_top()
    draw_right()
    draw_bottom()
    draw_left()
    pass

def draw_triangle_bottom():
    print('tri_BOTTOM')
    for x in range(200, 600, 5):
        draw_character(x, 100)
    pass

def draw_triangle_right():
    print('tri_RIGHT')
    for x, y in zip(range(600, 400, -5), range(100, 500, 10)):
        draw_character(x, y)
    pass

def draw_triangle_left():
    print('tri_LEFT')
    for x, y in zip(range(400, 200, -5), range(500, 100, -10)):
        draw_character(x, y)

    pass

def draw_triangle():
    print("triangle")
    draw_triangle_bottom()
    draw_triangle_right()
    draw_triangle_left()
    pass


while True:
    draw_circle()
    draw_rectangle()
    draw_triangle()
    break
    pass

close_canvas()