# AI-Snake-Game
CPSC 439 Project 1: Snake Game AI. 


Will make AI to beat the Snake Game (reach 100 score) based off video by Code Bullet https://www.youtube.com/watch?v=3bhP7zulFfY. 

We built the Snake game using python language. Python helped us implement the algorithm for the AI functionality of the game as well as provided with a user-friendly UI. Python libraries enabled our game to look user friendly and operate how we wanted it to. 
	In order to make the project we started by importing libraries. Python comes with multiple libraries that help in different sectors of application/code. Some of the libraries that we used were sys, math, random, pygame and tkinter. Here is a quick intro to what these libraries let us do for the games:

Sys- system-specific parameters and functions. This module gives user access to variables that can be used by the interpreter. This module helped us design the functions of the snake game where it helped snake / food and the grid set up.
Math- This module allowed us to use all the math operators. Common ones are addition, subtraction, multiplication and division. So for the game the grid was a big math platform that we were able to manipulate using the math module. The snake takes steps in numerical measures.
Random- This module helped us generate a random float uniformly. For the game purposes it helped the food block to randomly appear in the grid. 
Pygame- This is the most important module to build a game using python. It includes computer graphics and sound libraries designed for the game
Tkinter- This module is python’s standard GUI (Graphical User Interface) that helps with the game’s User Interface.

After importing all the necessary libraries, we set the rows and column for the grid. Then specified the functions for the snake’s moves like the directions. The next step was to add the cube’s (food) property. After we coded the basic game of snake, we tried implementing the greedy algorithm to the code. The purpose of the greedy algorithm implementation was that it would help the snake have human brains. It can detect it’s environment and go after the food block. At the same time it would avoid eating itself or running into the board grid. 


Files:
    snake.py                                                  Main File
    Readme.md                                                 Readme
    

Installation:
  
