#18.10.2024 Yuna Antonenko
#Ülesanded 6
import turtle
import math


turtle.fd(100)
turtle.left(90)
kordaja = 10
a = math.radians(53)
h = 4.4
x = abs(h / math.tan(a))
c = math.sqrt(h**2 + x ** 2)


print(x)


turtle.fd(x*kordaja)
turtle.left(90)
turtle.fd(h*kordaja)
turtle.left(180-(180-90-53))
turtle.fd(c*kordaja)






turtle.done()
