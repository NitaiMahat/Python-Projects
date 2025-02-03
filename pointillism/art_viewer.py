"""
 Name: Nitai Mahat
 Date: 10/11/2024
 Course: CSC 201
 Assignment: Project 2
 
 Description: This program reads a text file with an art extension and draws
              the "pointillistic" version of an image from the data in the file.
              The largest dimension is specified and the smaller dimension set
              proportionally.   
     
 Document Assistance: (who and what  OR  declare that you gave or received no assistance):I gave or received no assistance.
"""
from graphics2 import *
import tkinter as tk
from tkinter import filedialog
import sys
MAX_WINDOW_DIMENSION = 600

def main():
    #allows you to choose a file
    root = tk.Tk()
    root.withdraw()
    artFileName = filedialog.askopenfilename()
#    artFileName = 'gallery/fall_retangular_scene.art' # use this code if the file chooser doesn't work
    
    #add your code here
    dotDigit = artFileName.find('.')
    fileExtension = artFileName[dotDigit + 1:]
    
    
    if fileExtension.lower() != 'art':
        print("Invalid file format. Must choose an 'art' file.\nEnding execution.")
        sys.exit(-1)
    
    # Opens the art file to read data inside
    artFile = open(artFileName, 'r')
    value = artFile.readline().split()
    imgWidth = int(value[0])
    imgHeight = int(value[1])
    backgroundColor = int(artFile.readline())
  
    # Window dimensions based on the image aspect ratio
    if imgWidth >= imgHeight:
        windowWidth = MAX_WINDOW_DIMENSION
        windowHeight = int(MAX_WINDOW_DIMENSION * (imgHeight / imgWidth))
    else:
        windowWidth = int(MAX_WINDOW_DIMENSION * (imgWidth / imgHeight))
        windowHeight = MAX_WINDOW_DIMENSION
    
    # Window for displaying the image
    artWindow = GraphWin('Art Viewer', windowWidth, windowHeight)
    
    
    if backgroundColor == 1:
        artWindow.setBackground('white')
    else:
        artWindow.setBackground('black')
    
    # Draws the circles
    for line in artFile:
        circleData = line.strip().split()
        xCord = int(circleData[0])
        yCord = int(circleData[1])
        radius = int(circleData[2])
        red = int(circleData[3])
        green = int(circleData[4])
        blue = int(circleData[5])
        
        # Calculations to make it fit within the window dimensions
        scaledPointX = xCord * (windowWidth / imgWidth)
        scaledPointY = yCord * (windowHeight / imgHeight)
        circleColor = color_rgb(red, green, blue)
        
       
        drawCircle = Circle(Point(scaledPointX, scaledPointY), radius)
        drawCircle.setFill(circleColor)
        drawCircle.setOutline(circleColor)
        drawCircle.draw(artWindow)
    
    
    artFile.close()
    print("Picture completed.")

main()