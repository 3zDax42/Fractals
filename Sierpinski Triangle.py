import pygame
import random

pygame.init()
Game_Screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Sierpinski Triangle")
Clock = pygame.time.Clock()
Game_On = True

def Mid(Point1, Point2):
    Mid_Point = Point1 - Point2
    Mid_Point = Mid_Point / 2 + Point2
    return Mid_Point
def Recursive_Sierpinski_Function(X_1, Y_1, X_2, Y_2, X_3, Y_3, i = 0, Is_Even = 1):
    i += 1
    if i > 8:
        return 0
    pygame.draw.polygon(Game_Screen, (i*50%255, i*2%255, i*20%255), ((X_1, Y_1), (X_2, Y_2), (X_3, Y_3)))

    if Is_Even:
        pygame.draw.polygon(Game_Screen, (i*50%255, i*2%255, i*20%255), ((X_1, Y_1), (X_2, Y_2), (X_3, Y_3)))
        Is_Even *= -1
    else:
        pygame.draw.polygon(Game_Screen, (0, 0, 0), ((X_1, Y_1), (X_2, Y_2), (X_3, Y_3)))
        Is_Even *= -1
    Recursive_Sierpinski_Function(X_1, Y_1, Mid(X_1, X_2), Mid(Y_1, Y_2), Mid(X_3, X_1), Mid(Y_3, Y_1), i, Is_Even) # Top
    Recursive_Sierpinski_Function(Mid(X_1, X_2), Mid(Y_1, Y_2), X_2, Y_2, Mid(X_3, X_2), Mid(Y_3, Y_2), i, Is_Even) # Left
    Recursive_Sierpinski_Function(Mid(X_1, X_3), Mid(Y_1, Y_3), Mid(X_2, X_3), Mid(Y_2, Y_3), X_3, Y_3, i, Is_Even) # Right

Recursive_Sierpinski_Function(500, 0, 0, 1000, 1000, 1000)

while Game_On:
    Clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            Game_On = False

    
    #Game_Screen.fill((0, 0, 0))
    

    pygame.display.flip()
pygame.quit()
