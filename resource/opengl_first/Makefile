
CXX 			:= g++
CXX_FLAG 		:= -Wall -Wextra
OPENGL_FLAGS 	:= -lglfw3 -lglew32 -lglu32 -lfreeglut -lopengl32 -lgdi32 -mwindows
default-target: all

all: window.exe

%.exe: %.c
	$(CXX) $< -o $@ $(CXX_FLAG) $(OPENGL_FLAGS)


