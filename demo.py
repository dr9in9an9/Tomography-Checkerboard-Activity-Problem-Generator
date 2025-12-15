# author: Jesus Sisniega-Serrano
# version: 12-15-2025
# NO AI USED IN THE PROCESS OF CREATION. >:(
# 
# THANK U FOR CHECKING OUT MY WORK!
####################

# public libraries #
import numpy
import time

# personal scripts #
import tomography2D
import gfx

####################

# demo 1: First-steps into tomography
tomography2D.demo(5, 3)

# demo 2: Understanding the cube
# gfx.visualizeMatrix([[[0]]], "")

# demo 3 part a: 2D arrays visualized in 3D, XRAYS
# temp = tomography2D.returnBoards(5, 3)
# xray = [temp[1]]
# print(temp[0])
# gfx.visualizeMatrix(xray, "xray")
##################################################
# demo 3 part b: 2D arrays visualized in 3D, MINES
# mine = [] # paste print inside here.
# gfx.visualizeMatrix(mine, "mine")

# demo 4: A 3D tomography solution
# mine = [n for n in range(4)]
# for r in mine:
#     mine[r] = tomography2D.returnBoards(5, 3)[0]
# gfx.visualizeMatrix(mine, "mine")

# demo 5: Future work: 3D tomography problem generator
# xray = [n for n in range(2)]
# for r in xray:
#     xray[r] = tomography2D.returnBoards(7, 1+2*r)[1]
# gfx.visualizeMatrix(xray, "xray")
