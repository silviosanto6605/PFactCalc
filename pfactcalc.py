#!/usr/bin/python3

from tkinter import *
import random
import math
import os
import subprocess
import time



window = Tk()

window.title("PFactCalc 0.1.0")

window.geometry('350x200')

labeltitle = Label(window, text="PFactCalc 0.1.0", font=("Impact",30), justify=CENTER)
labeltitle.configure(background='white')
labeltitle.grid(column=2, row=1) #titolo 

txt = Entry(window,width=15)
txt.grid(column=2, row=5) #input

def outputtext(fattore):
    output = Label(window, text=fattore, font=("Arial",12), justify=RIGHT, width=30)
    output.grid(column=2, row=6) #output
    output.configure(background='white')    

def start_factorization():
    number = int(txt.get())

    fattore = str(number)+"=1"
    divisor=2



    while number>=divisor:
        if number % divisor == 0:
            fattore=fattore+'*'+str(divisor)
            number=number/divisor

        else:
            divisor=divisor+1


    if number <=divisor:
        outputtext(fattore)

        
        



btn = Button(window, text="Calculate", font=("Calibri",15), command=start_factorization)
btn.configure(background='white')
btn.grid(column=2, row=3)

window.configure(background='white')
#window.wm_iconbitmap('pfactcalc.png')


window.mainloop()
