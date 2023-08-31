/**
 * tutorial-01: Open a window.
 * see at: http://ogldev.atspace.co.uk/www/tutorial01/tutorial01.html
 */

#include <GL/freeglut.h>

static void InternalCB()
{
    // clear the framebuffer
    glClear(GL_COLOR_BUFFER_BIT);

    // tells GLUT to swap the roles of the backbuffer and the frontbuffer. 
    // In the next round through the render callback we will render into 
    // the current frames front buffer and the current backbuffer will be displayed.
    glutSwapBuffers();
}


// int WinMain(HINSTANCE hInstance, HINSTANCE hPrevInstance, LPSTR lpCmdLine, int nShowCmd)
int main(int argc, char **argv)
{
    // FreeConsole();
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA); // GLUT_DOUBLE enables double buffering
    
    glutInitWindowSize(400, 300);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("tutorial-01: Open a window.");
    
    glutSetWindowTitle((const char *)glGetString(GL_VERSION));

    glutDisplayFunc(InternalCB); // This function is continuously called by GLUT internal loop.

    // The color has four channels (RGBA) and it is specified as a normalized value between 0.0 and 1.0.
    glClearColor(0.0f, 1.0f, 1.0f, 0.0f);

    // This call passes control to GLUT which now begins its own internal loop. 
    // In our case GLUT will only call the function we registered as a display callback (InternalCB) 
    // to give us a chance to render the frame.
    glutMainLoop();

    return EXIT_SUCCESS;
}

