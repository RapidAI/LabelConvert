/**
 * tutorial-05: Uniform Variables
 * see at: http://ogldev.atspace.co.uk/www/tutorial05/tutorial05.html
 */

#include <cstdio>
#include <cmath>
#include <cstring>
#include <string>
#include <chrono>
#include <thread>
using namespace std;

#include <GL/glew.h>
#include <GL/freeglut.h>

// #include <opengl_util.h>

GLuint VBO;
GLuint gWorldLocation;

// const char* pVSFileName = "shader.vs";
// const char* pFSFileName = "shader.fs";

typedef float mat4x4f[4][4];
struct vec3f {
    float x, y, z;
    vec3f() { }
    vec3f(float _x, float _y, float _z) {
        x = _x; y = _y; z = _z;
    }
};

static void sleep(int milliseconds) {
    std::chrono::milliseconds dura(milliseconds);
    std::this_thread::sleep_for(dura);
}

static void mulmatf(const void * a, const void * b, void *result, 
        const int x, const int y, const int z)
{
    const float (*pa)[y] = (const float (*)[y])a;
    const float (*pb)[z] = (const float (*)[z])b;
    float pans[x][z] = {0};
    for(int i = 0; i < x; ++i) {
        for(int j = 0; j < z; ++j) {
            float num = 0.0f;
            for(int k = 0; k < y; ++k) {
                num += pa[i][k]*pb[k][j];
            }
            pans[i][j] = num;
        }
    }
    memcpy(result, pans, sizeof(float) * x * z);
}

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

    mat4x4f World;

    mat4x4f translation = {
        1.0f, 0.0f, 0.0f, sinf(Scale),
        0.0f, 1.0f, 0.0f, 0.0f,
        0.0f, 0.0f, 1.0f, 0.0f,
        0.0f, 0.0f, 0.0f, 1.0f };
    mat4x4f rotation = {
        cosf(Scale), -sinf(Scale), 0.0f, 0.0f, 
        sinf(Scale), cosf(Scale) , 0.0f, 0.0f, 
        0.0f       , 0.0f        , 1.0f, 0.0f, 
        0.0f       , 0.0f        , 0.0f, 1.0f };
    mat4x4f scaling = {
        sinf(Scale), 0.0f        , 0.0f, 0.0f,
        0.0f       , sinf(Scale) , 0.0f, 0.0f,  
        0.0f       , 0.0f        , sinf(Scale), 0.0f,  
        0.0f       , 0.0f        , 0.0f, 1.0f };

    mulmatf(rotation, scaling, World, 4, 4, 4);
    mulmatf(translation, World, World, 4, 4, 4);

    glUniformMatrix4fv(gWorldLocation, 1, GL_TRUE, &World[0][0]);
    
    sleep(10);
    glutPostRedisplay();
}

static void CreateVertexBuffer()
{
    vec3f Vertices[3];
    Vertices[0] = vec3f(-0.25f, 0.0f, 0.0f);
    Vertices[1] = vec3f(0.25f, 0.25f, 0.0f);
    Vertices[2] = vec3f(0.25f, -0.25f, 0.0f);

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
"uniform mat4 gWorld;"
"void main()"
"{"
"    gl_Position = gWorld * vec4(Position, 1.0);"
"}";
    fs = "#version 400\n"
"out vec4 FragColor;"
"void main() {"
"    FragColor = vec4(1.0, 0.0, 0.0, 1.0);"
"}";

    AddShader(ShaderProg, vs.c_str(), GL_VERTEX_SHADER);
    AddShader(ShaderProg, fs.c_str(), GL_FRAGMENT_SHADER);
    glLinkProgram(ShaderProg);
    glValidateProgram(ShaderProg);
    glUseProgram(ShaderProg);

    gWorldLocation = glGetUniformLocation(ShaderProg, "gWorld");
}

int main(int argc, char **argv)
{
    glutInit(&argc, argv);
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGBA); // GLUT_DOUBLE enables double buffering
    
    glutInitWindowSize(400, 400);
    glutInitWindowPosition(100, 100);
    glutCreateWindow("Transformation");

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

