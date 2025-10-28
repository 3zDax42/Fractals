import pygame
import math
import cmath

pygame.init()

pygame.display.set_caption("Mandelbrot")
screen = pygame.display.set_mode((800, 800))
screen.fill((200, 200, 200))
Width = 800; Hight = 800

def Mandelbrot(c = 0, z=complex(0,0), counter=0):
    while (abs(z) < 2) and (counter < 80):
        z = z*z + c
        counter += 1
    else:
        return counter

t = -1
while t < 1: # upper bound for real (horizontal) axis
    t += .001
    m = -1 #lower bound for imaginary axis
    while m < 1: #upper bound for imaginary (vertical) axis
        m += .001 # Make smaller to increase resolution
        c = complex(t, m)
        num = Mandelbrot(c)
        if num < 40:
            screen.set_at((int(t*400 + 400), int(m*400 + 400)), (num*2, num, num*5))
        elif num < 80:
            screen.set_at((int(t*400 + 400), int(m*400 + 400)), (num*3, num, num*2))
        elif num == 80:
            screen.set_at((int(t*400 + 400), int(m*400 + 400)), (200, 200, 200))
        else:
            screen.set_at((int(t*400 + 400), int(m*400 + 400)), (0, 0, 0))
        #print("num is ", num, " at ", t*100+400, m*100+400)
    
    

    pygame.display.flip()
pygame.time.wait(1000)
pygame.quit()
