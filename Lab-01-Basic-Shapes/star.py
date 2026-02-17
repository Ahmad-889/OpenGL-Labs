from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math

# Window size
width, height = 500, 500

def draw_star():
    glColor3f(1.0, 1.0, 0.0)  # Yellow color
    glBegin(GL_TRIANGLE_FAN)

    # Center of the star
    glVertex2f(0.0, 0.0)

    num_points = 5
    radius_outer = 0.5
    radius_inner = 0.2

    for i in range(11):  # 5 outer + 5 inner + 1 to close
        angle = math.pi / 5 * i
        if i % 2 == 0:
            radius = radius_outer
        else:
            radius = radius_inner

        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        glVertex2f(x, y)

    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    draw_star()
    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)   # You wrote 'e' instead of 0
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"OpenGL Star")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()
