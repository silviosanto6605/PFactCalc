#!/usr/bin/python3

import random
import math
import os
import subprocess
import time



number = int(input("Inserici il numero da scomporre in fattori primi: "))

fattore = str(number)+"=1"
divisor=2


while number>=divisor:
    if number % divisor == 0:
        fattore=fattore+'*'+str(divisor)
        number=number/divisor

    else:
        divisor=divisor+1

    print(fattore)
    time.sleep(2)
