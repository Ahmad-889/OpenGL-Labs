from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

angle = 0

def display():
    global angle
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    glRotatef(angle, 0, 0, 1)

    glColor3f(1, 0, 1)
    glBegin(GL_POLYGON)
    glVertex2f(-0.5, -0.5)
    glVertex2f(0.5, -0.5)
    glVertex2f(0.7, 0.2)
    glVertex2f(0.0, 0.7)
    glVertex2f(-0.7, 0.2)
    glEnd()

    glutSwapBuffers()

def update(value):
    global angle
    angle += 1
    glutPostRedisplay()
    glutTimerFunc(16, update, 0)

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(600, 500)
    glutCreateWindow(b"Polygon Animation")
    gluOrtho2D(-1, 1, -1, 1)
    glutDisplayFunc(display)
    glutTimerFunc(0, update, 0)
    glutMainLoop()

if __name__ == "__main__":
    main()
