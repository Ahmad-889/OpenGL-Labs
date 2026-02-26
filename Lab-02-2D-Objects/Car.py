from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

car_x = -1.0

def draw_circle(cx, cy, r):
    glBegin(GL_TRIANGLE_FAN)
    glVertex2f(cx, cy)
    for i in range(100):
        angle = 2 * math.pi * i / 100
        glVertex2f(cx + r * math.cos(angle),
                   cy + r * math.sin(angle))
    glEnd()

def draw_car():
    global car_x

    # Car body
    glColor3f(0.0, 0.0, 1.0)
    glBegin(GL_QUADS)
    glVertex2f(car_x, -0.2)
    glVertex2f(car_x + 0.6, -0.2)
    glVertex2f(car_x + 0.6, 0.1)
    glVertex2f(car_x, 0.1)
    glEnd()

    # Top
    glBegin(GL_QUADS)
    glVertex2f(car_x + 0.15, 0.1)
    glVertex2f(car_x + 0.45, 0.1)
    glVertex2f(car_x + 0.35, 0.3)
    glVertex2f(car_x + 0.25, 0.3)
    glEnd()

    # Wheels
    glColor3f(0, 0, 0)
    draw_circle(car_x + 0.15, -0.25, 0.08)
    draw_circle(car_x + 0.45, -0.25, 0.08)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    draw_car()
    glutSwapBuffers()

def update(value):
    global car_x
    car_x += 0.01
    if car_x > 1:
        car_x = -1
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 500)
    glutCreateWindow(b"Car Animation")
    gluOrtho2D(-1, 1, -1, 1)
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
