/**
 * tutorial-05: Uniform Variables
 * see at: http://ogldev.atspace.co.uk/www/tutorial05/tutorial05.html
 */

#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
using namespace std;

#include <GL/glew.h>
#include <GL/freeglut.h>

#include <opengl_util.h>

GLuint VBO;
GLuint gScaleLocation;

// const char* pVSFileName = "05_uniform_variables/shader.vs";
// const char* pFSFileName = "05_uniform_variables/shader.fs";

static void RenderScene()
{
    glClear(GL_COLOR_BUFFER_BIT);
    glEnableVertexAttribArray(0);
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 0, 0);
    glDrawArrays(GL_TRIANGLES, 0, 3);
    glDisableVertexAttribArray(0);
    glutSwapBuffers();
}

static void IdleCB()
{
    static float Scale = 0.0f;
    Scale += 0.01f;
    glUniform1f(gScaleLocation, sinf(Scale));
    sleep(10);
    glutPostRedisplay();
}

static void CreateVertexBuffer()
{
    vec3f Vertices[3];
    Vertices[0] = vec3f(0.0f, 0.0f, 0.0f);
    Vertices[1] = vec3f(0.5f, 0.5f, 0.5f);
    Vertices[2] = vec3f(0.5f, -0.5f, 0.5f);

    glGenBuffers(1, &VBO);
    glBindBuffer(GL_ARRAY_BUFFER, VBO);
    glBufferData(GL_ARRAY_BUFFER, sizeof(Vertices), Vertices, GL_STATIC_DRAW);
}

static void AddShader(GLuint ShaderProg, const char *pShaderText, GLenum ShaderType)
{
    GLuint ShaderObj = glCreateShader(ShaderType);
    const GLchar *p[1];
    p[0] = pShaderText;
    GLint Lengths[1];
    Lengths[0] = strlen(pShaderText);
    glShaderSource(ShaderObj, 1, p, Lengths);
    glCompileShader(ShaderObj);

    GLint success = 0;
    glGetShaderiv(ShaderObj, GL_COMPILE_STATUS, &success);
    CHECK_NULL(success);
    
    glAttachShader(ShaderProg, ShaderObj);
}

static void CompileShaders()
{
    GLuint ShaderProg = glCreateProgram();

    string vs, fs;
    // ReadFile(pVSFileName, vs);
    // ReadFile(pFSFileName, fs);
    vs = "#version 400\n"
"layout (location = 0) in vec3 Position;"
"uniform float gScale;"
"void main() {"
"    gl_Position = vec4(gScale * Position.x, gScale * Position.y, Position.z, 1.0);"
"}";
    fs = "#version 400\n"
"out vec4 FragColor;"
"void main() {"
"    FragColor = vec4(1.0, 0.0, 0.0, 1.0);"
"}";

    AddShader(ShaderProg, vs.c_str(), GL_VERTEX_SHADER);
    AddShader(ShaderProg, fs.c_str(), GL_FRAGMENT_SHADER);

    GLint success = 0;

    glLinkProgram(ShaderProg);
    glGetProgramiv(ShaderProg, GL_LINK_STATUS, &success);
    CHECK_NULL(success);
    
    glValidateProgram(ShaderProg);
    glGetProgramiv(ShaderProg, GL_VALIDATE_STATUS, &success);
    CHECK_NULL(success);
    
    glUseProgram(ShaderProg);
    gScaleLocation = glGetUniformLocation(ShaderProg, "gScale");
}

int main(int argc, char **argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA); // GLUT_DOUBLE enables double buffering
    
    glutInitWindowSize(400, 400);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("tutorial-05: Uniform Variables");

    glutDisplayFunc(RenderScene); // register GLUT callback function.
    glutIdleFunc(IdleCB);

    // must be done after glut is initialized.
    GLenum res = glewInit();
    if(res != GLEW_OK) {
        fprintf(stdout, "Error: '%s'\n", glewGetErrorString(res));
        return EXIT_FAILURE;
    }

    glClearColor(0.0f, 0.0f, 0.0f, 0.0f);

    CreateVertexBuffer();

    CompileShaders();

    glutMainLoop();

    return EXIT_SUCCESS;
}

