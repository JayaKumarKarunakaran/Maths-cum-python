import math
import turtle

from turtle import *
def hearta(k):
    return 15*math.sin(k)**3
def heartb(k):
    return 12*math.cos(k)- 5*\
        math.cos(2*k)-2*\
        math.cos(3*k)- \
        math.cos(4*k)
speed(900000000097946475889388)
bgcolor("black")
print("hey are you want to tel anything to me....after you watching it" )
for i in range(450):
    goto (hearta(i)*20,heartb(i)*20)
    
    for j in range(5):
        color("pink")
        
    goto(0,0)

done()
