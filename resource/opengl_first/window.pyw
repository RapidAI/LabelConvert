#! /usr/bin/env python3
# -*- encoding: utf-8 -*-

from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def plotfunc():
    glClear(GL_COLOR_BUFFER_BIT)
    glFlush();

def guimain():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)
    glutInitWindowPosition(100, 100)
    glutInitWindowSize(400, 300)
    glutCreateWindow(b"first window")
    glutDisplayFunc(plotfunc)
    glClearColor(0.0, 1.0, 1.0, 0.0)
    glutMainLoop()

if __name__ == '__main__':
    guimain()
