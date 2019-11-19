from graph import *

# HEAD
penColor('black')
brushColor('yellow')
circle(200, 200, 100)

# EYES
brushColor('red')
circle(160, 170, 20)
circle(240, 170, 10)

brushColor('black')
circle(160, 170, 10)
circle(240, 170, 5)

# MOUTH
rectangle(160, 240, 240, 250)

# EYEBROWS
polygon([
    (100, 100),
    (95, 105),
    (195, 170),
    (200, 165)
])
polygon([
    (300, 120),
    (305, 125),
    (235, 163),
    (230, 158)
])


# penColor(255,0,255)
# penSize(5)
# brushColor("blue")
# rectangle(100, 100, 300, 200)
# brushColor("yellow")
# polygon([(100,100), (200,50),
#          (300,100), (100,100)])
# penColor("white")
# brushColor("green")
# circle(200, 150, 50)
#
run()
