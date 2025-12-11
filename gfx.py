# author: Jesus Sisniega-Serrano
# version: 12-11-2025
# NO AI USED IN THE PROCESS OF CREATION. >:(
# Based on Umaur Tariq's 3D Cube Visualization Script: https://www.youtube.com/watch?v=Y3ee6z3Lz88

import pygame # Python graphics library
from math import * # Math functions library
import sys # System interactions library

# Simple matrix multiplication function.
def multiply_m(a,b):
    aRows = len(a)
    aCols = len(a[0])
    bRows = len(b)
    bCols = len(b[0])

    # Dot product matrix dimentions are the number of rows in matrix a by the number of columns in matrix b.
    product = [[0 for _ in range(bCols)] for _ in range(aRows)]
    if aCols == bRows:
        for i in range(aRows):
            for j in range(bCols):
                for k in range(bRows):
                    product[i][j] += a[i][k] * b[k][j] 
    else:
        print("Incompatible Matrix Size")
    return product

# def add_m(a,b):
#     a_rows = len(a)
#     a_cols = len(a[0])
#     b_rows = len(b)
#     b_cols = len(b[0])
#
#     product = [[0 for _ in range(a_cols)] for _ in range(a_rows)]
#     if (a_cols == b_cols) & (a_rows == b_rows):
#         for i in range(a_rows):
#             for j in range(a_cols):
#                     product[i][j] += a[i][j] + b[i][j]
#     else:
#         print("Incopmatible Matrix Size")
#     return product
#!!! Currently unused. No need to uncomment. !!!

# Defines window object.
windowSize = 800
rotSpeed = 0.02
window = pygame.display.set_mode((windowSize, windowSize))

# Necessary to run real-time graphics.
clock = pygame.time.Clock()

# Identity matrix for a 2D span. 
projection_matrix = [[1, 0, 0]
                    ,[0, 1, 0]
                    ,[0, 0, 0]]
        
# Draws a line of any color. 
def connect_points(i, j, points, isRed):
    color = (255,255,255) # White color vector.
    if isRed == True:
        color = (255, 0, 0) # Red color vector.

    pygame.draw.line(window, color, (points[i][0],points[i][1]), (points[j][0],points[j][1]))
        
scale = 20 # Individual cube scale.
# Future script modifications may include zoom functions!

aX = aY = aZ = 0 # Starting angle(s) degrees. x, y, z respectively.

# Where all the magic happens.
# Insert a 3D matrix of any size and watch as your computer renders sh*tty graphics! Not sure why I decided to do this...
def visualizeMatrix(xyzmatrix):
    z = len(xyzmatrix)
    y = len(xyzmatrix[z])
    x = len(xyzmatrix[z][y])

    # Creates the invitual points for each cube.

    # Generates height.
    cubesCUBED = [n for n in range(z)]
    for f in cubesCUBED:

        # Generates width.
        cubesGrid = [n for n in range(y)]
        for c in cubesGrid:
            # Array containing x and y coordinates coresponding to your screen.
            cubesLine = [n for n in range(x)]

            # Generates length.
            for r in cubesLine:

                cube = [n for n in range(8)]
                cube[0] = [[-1 + r*2], [-1 + c*2], [ 1 + f*2]]
                cube[1] = [[ 1 + r*2], [-1 + c*2], [ 1 + f*2]]
                cube[2] = [[ 1 + r*2], [ 1 + c*2], [ 1 + f*2]]
                cube[3] = [[-1 + r*2], [ 1 + c*2], [ 1 + f*2]]
                cube[4] = [[-1 + r*2], [-1 + c*2], [-1 + f*2]]
                cube[5] = [[ 1 + r*2], [-1 + c*2], [-1 + f*2]]
                cube[6] = [[ 1 + r*2], [ 1 + c*2], [-1 + f*2]]
                cube[7] = [[-1 + r*2], [ 1 + c*2], [-1 + f*2]]

                cubesLine[r] = cube

            cubesGrid[c] = cubesLine

        cubesCUBED[f] = cubesGrid

    # PyGame main loop.
    # Allows a real-time interactable application to occur.
    while True:
        clock.tick(60) # Framerate
        window.fill((0,0,0))

        # Matrices necessary to complete the linear transformations to rotate points about a 3D space.
        rotX = [[       1,        0,        0]
               ,[       0,  cos(aX), -sin(aX)]
               ,[       0,  sin(aX),  cos(aX)]]

        rotY = [[ cos(aY),        0,  sin(aY)]
               ,[       1,        0,        0]
               ,[-sin(aY),        0,  cos(aY)]]

        rotZ = [[ cos(aZ), -sin(aZ),        0]
               ,[ sin(aZ),  cos(aZ),        0]
               ,[       0,        0,        1]]

        # Unpacks informtion.
        for f in range(len(cubesCUBED)):
            cubesGrid = cubesCUBED[f]

            # Unpacks information.
            for c in range(len(cubesGrid)):
                cubesLine = cubesGrid[c]

                # Unpacks information.
                for r in range(len(cubesLine)):
                    cube_points = cubesLine[r]
                    points = [0 for _ in range(len(cube_points))]
                    i = 0

                    # print(cube_points) # debug

                    # Multply original coordinates by all 3 rotational matrices, then finally "flatten" matrix into a 2D image.
                    for point in cube_points:
                        rotate_x = multiply_m(rotX,point)
                        rotate_y = multiply_m(rotY,rotate_x)
                        rotate_z = multiply_m(rotZ,rotate_y)
                        point_2d = multiply_m(projection_matrix,rotate_z)
                        
                        #print(point_2d) # debug

                        localX = (point_2d[0][0] * scale) + windowSize/2
                        localY = (point_2d[1][0] * scale) + windowSize/2
                        
                        points[i] = (localX, localY)
                        
                        i += 1
                        pygame.draw.circle(window,(100,100,100),(x,y),3)
                        
                    # PyGame's built-in vector simulation.
                    connect_points(0, 1, points)
                    connect_points(0, 3, points)
                    connect_points(0, 4, points)
                    connect_points(1, 2, points)
                    connect_points(1, 5, points)
                    connect_points(2, 6, points)
                    connect_points(2, 3, points)
                    connect_points(3, 7, points)
                    connect_points(4, 5, points)
                    connect_points(4, 7, points)
                    connect_points(6, 5, points)
                    connect_points(6, 7, points)
        
        # PyGame's keyboard input reader.
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                aX=aY=aZ=0
            if keys[pygame.K_a]:
                aY += rotSpeed
            if keys[pygame.K_d]:
                aY -= rotSpeed
            if keys[pygame.K_w]:
                aX += rotSpeed
            if keys[pygame.K_s]:
                aX -= rotSpeed
            if keys[pygame.K_q]:
                aZ -= rotSpeed
            if keys[pygame.K_e]:
                aZ += rotSpeed
        
        # Updates display by tick amount.
        pygame.display.update()
        