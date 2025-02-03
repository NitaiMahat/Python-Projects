"""
 Name: Nitai Mahat
 Date: 10/5/2024
 Course: CSC 201
 Assignment: Project 2

 Description: This program begins with a gif image and creates a text file storing
              data for a "pointillistic" version of the image. The user can choose
              whether the background will be either white or black.

 Document Assistance: (who and what  OR  declare that you gave or received no assistance): I gave Yasser assistance to create the final file name where / had to be located.
"""
from graphics2 import *
import random
import tkinter as tk
from tkinter import filedialog
import sys


NUM_CIRCLES = 7500
   
def main():
    #allows you to choose a file 
    root = tk.Tk()
    root.withdraw()
    filenameWithPath = filedialog.askopenfilename()
#    filenameWithPath = 'gallery/fall_retangular_scene.gif' # use this code if the file chooser doesn't work

    #add your code here
    dotDigit = filenameWithPath.find('.')
    fileExtension = filenameWithPath[dotDigit + 1:]
    
    if fileExtension.lower() != 'gif':
        print("Invalid file format. Must choose a 'gif' file.\nEnding execution.")
        sys.exit(-1)   
    
    imgObject = Image(Point(0, 0), filenameWithPath)
    imgWidth = imgObject.getWidth()
    imgHeight = imgObject.getHeight()
    
    artExtension = filenameWithPath[:dotDigit] + '.art'
    
    backgroundColor = int(input("Color for background? (1 white, 2 black) "))
    
    if backgroundColor != 1 and backgroundColor != 2:
        print("Invalid color choice. Using black.")
        backgroundColor = 2
    
    # Open the .art file to write image data
    artFile = open(artExtension, 'w')
    artFile.write(f"{imgWidth} {imgHeight}\n")
    artFile.write(f"{backgroundColor}\n")
    
    for _ in range(NUM_CIRCLES): 
        xCord = random.randrange(imgWidth)
        yCord = random.randrange(imgHeight)
        colorNums = imgObject.getPixel(xCord, yCord)
        red = colorNums[0]
        green = colorNums[1]
        blue = colorNums[2]
        radius = random.randrange(1, 8)
        artFile.write(f"{xCord} {yCord} {radius} {red} {green} {blue}\n")
        
    # Print file name (excluding path)
    slashFind = filenameWithPath.rfind('/')     
    print(f"File created: {artExtension[slashFind + 1:]}")
    print("Program ending.")
    
    artFile.close()

main()
