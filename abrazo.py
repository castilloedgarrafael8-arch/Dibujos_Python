import turtle

t = turtle.Turtle()
t.pensize(6)
t.shape("turtle")

def go(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def arco(direc, radio, ang):
    t.seth(direc)
    t.circle(radio, ang)

def linea(direc, longitud):
    t.seth(direc)
    t.forward(longitud)
    
t.pencolor("DarkSlateGray")
go(-221.06, -274.24)
arco(91.16, -396.99, 36.29)
arco(155.73, -122.98, 208.8)
arco(49.77, -115.22, 205.68)
arco(304.41, -437.54, 32.78)

go(0, 148.20)
linea(268.98, 132.52)

go(0, -126.32)
linea(269.11, 152.26)

go(57.30, 4.26)
arco(156.47, 137.59, 47.09)
arco(203.56, 28.29, 141.24)
arco(344.8, 110.58, 24.41)
arco(9.21, -90.12, 37.58)
arco(331.63, -26.73, 115.03)
arco(216.6, -92.24, 20.73)
arco(195.87, -180.73, 29.16)

t.pencolor("Black")
t.fillcolor("Black")

go(-97.77, 44.52)
t.begin_fill()
arco(292.24, 32.36, 43.96)
arco(336.2, 6.68, 98.41)
arco(74.61, 34.84, 42.72)
arco(187.89, 39.15, 39.4)
t.end_fill()

go(59.36, 88.98)
t.begin_fill()
arco(87.09, 9.99, 113.68)
arco(200.76, 18.84, 76.54)
arco(280.21, 10.20, 117.43)
arco(34.73, 22.37, 52.36)
t.end_fill()

go(129.61, 66.28)
t.begin_fill()
arco(79.94, 11.11, 131.91)
arco(211.84, 18.22, 82.94)
arco(294.79, 9.15, 97.25)
arco(32.04, 23.26, 47.9)
t.end_fill()

t.pensize(9)
go(61.70, 60.37)
arco(258.02, 16.20, 166.88)
go(-38.59, 79.55)
arco(97.1, 15.87, 205.46)
go(-113.31, 56.86)
arco(107.74, 17.51, 180)

t.pensize(4)
t.pencolor("DeepPink")
t.fillcolor("DeepPink")
go(132.79, 41.33)
linea(218.39, 14.68)
go(121.28, 44.75)
linea(225, 11.17)
go(33.16, 69.04)
linea(213.43, 11.83)
go(25.45, 74.01)
linea(219.29, 12.75)

t.pencolor("Red")
t.fillcolor("Red")
go(-1.05, 210.56)
t.begin_fill()
arco(45.17, 183.09, 18.97)
arco(64.14, 24.12, 89.38)
arco(160.7, 22.51, 90)
arco(110.84, 19.63, 90)
arco(211.58, 26.95, 90)
arco(305.31, 214.92, 15.27)
t.end_fill()

t.hideturtle()
turtle.done()