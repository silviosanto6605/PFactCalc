#!/usr/bin/python3

import random
import math
import os
import subprocess
import time

try:

    number = int(input("Inserici il numero da scomporre in fattori primi: "))

    fattore = str(number)+"=1"
    divisor=2


    while number>=divisor:
        if number % divisor == 0:
            fattore=fattore+'*'+str(divisor)
            number=number/divisor

        else:
            divisor=divisor+1


    if number <=divisor:
        print(fattore)
        input("Press enter to exit  ")
        exit()

except KeyboardInterrupt:
    print('Exiting...')
    exit()

except (SyntaxError, NameError,ValueError):
    print("Il valore inserito non e' corretto")
    exit()
