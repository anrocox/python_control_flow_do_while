#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 23, 2014

@author: anroco

In Python, how to simulate the do-while loop?

En Python, ¿Cómo simular el ciclo do-while?
'''

#the difference between while loop and do-while loop is in the minimum number
#of times it runs, the while loop runs minimum zero times and the do-while loop
#runs minimum one time

#create two integers
n = 1
c = 1

#defines an infinite loop using the statement "while True:"
while True:
    print('iteration {}, simulation of the do-while loop'.format(c))

    #increases by one the counter c
    c += 1
    #adds 2 to value n
    n += 2

    #condition that stops the cycle
    if n > 10:
        break

print('n = {} c = {}'.format(n, c))
