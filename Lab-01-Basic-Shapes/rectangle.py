from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

# Window size
width, height = 500, 500

def draw_rectangle():
    glBegin(GL_QUADS)                 # Using GL_QUADS to create rectangle
    glColor3f(0.0, 1.0, 0.0)          # Green color
    glVertex2f(-0.5, -0.5)            # Bottom-left
    glVertex2f(0.5, -0.5)             # Bottom-right
    glVertex2f(0.5, 0.5)              # Top-right
    glVertex2f(-0.5, 0.5)             # Top-left
    glEnd()

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    glLoadIdentity()
    draw_rectangle()
    glutSwapBuffers()

def reshape(w, h):
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluOrtho2D(-1, 1, -1, 1)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(width, height)
    glutCreateWindow(b"OpenGL Rectangle")
    glClearColor(0.0, 0.0, 0.0, 1.0)
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()

if __name__ == "__main__":
    main()
