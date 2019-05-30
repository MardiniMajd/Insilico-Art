#a program that convert DNA sequences into "drawing"
from tkinter import *
import tkinter
import  turtle
DNA_turtle = turtle.Turtle()
DNA_turtle.speed(100)

def turtlestep(angle, length):
    DNA_turtle.right(angle)
    DNA_turtle.fd(length)

import Bio
from Bio import SeqIO

seq = SeqIO.parse('Arabidopsis thaliana chlorophyll AB binding protein 1 - SNP (transform one nucliotide).fasta', 'fasta')

for i in seq:
     if i=="G":
         DNA_turtle.pensize(3)
         DNA_turtle.color('yellow')
         turtlestep(90, 10)
     if i=="C":
         DNA_turtle.pensize(3)
         DNA_turtle.color('red')
         turtlestep(-90, 10)
     if i=="T":
         DNA_turtle.pensize(3)
         DNA_turtle.color('green')
         turtlestep(80, 10)
     if i=="A":
         DNA_turtle.pensize(3)
         DNA_turtle.color('blue')
         turtlestep(-80, 10)

tkinter.mainloop()



