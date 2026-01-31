import time
import math

from linalg import Vec3, Mat4
from screen import Screen

WIDTH = 80
HEIGHT = 40

screen = Screen(WIDTH, HEIGHT)

# Cube vertices
vertices = [
    Vec3(-1, -1, -1),
    Vec3( 1, -1, -1),
    Vec3( 1,  1, -1),
    Vec3(-1,  1, -1),
    Vec3(-1, -1,  1),
    Vec3( 1, -1,  1),
    Vec3( 1,  1,  1),
    Vec3(-1,  1,  1),
]

# Cube edges
edges = [
    (0, 1), (1, 2), (2, 3), (3, 0),
    (4, 5), (5, 6), (6, 7), (7, 4),
    (0, 4), (1, 5), (2, 6), (3, 7),
]

def ndc_to_screen(v: Vec3):
    x = int((v.x + 1) * 0.5 * (WIDTH - 1))
    y = int((1 - v.y) * 0.5 * (HEIGHT - 1))
    return x, y

angle = 0.0
print("\033[2J", end="") # Clear screen

while True:
    screen.clear()

    model = (
        Mat4.rotation_y(angle) @
        Mat4.rotation_x(angle * 0.5)
    )

    view = Mat4.translation(0, 0, -5)
    proj = Mat4.perspective(
        fov=math.radians(70),
        aspect=WIDTH / HEIGHT,
        near=0.1,
        far=100.0
    )

    mvp = proj @ view @ model

    projected = []
    for v in vertices:
        p = mvp.transform_point(v)
        projected.append(ndc_to_screen(p))

    for a, b in edges:
        x0, y0 = projected[a]
        x1, y1 = projected[b]
        screen.draw_line(x0, y0, x1, y1, "#")

    screen.present()

    angle += 0.03
    time.sleep(0.03)
