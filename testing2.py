import turtle, random

def move(turt, x, y):
    # turt is a turtle
    # x is final x coordinte (destination)
    # y is final y coordinate
    turt.up()
    turt.goto(x,y)
    turt.down()
t = turtle.Turtle()
t.color('red', 'red')
t.turtlesize(2,2,2)
tx,ty = -300,0
move(t, tx,ty)


def route2(turt, tx, ty):
    t.left(90)
   
def route3(turt, tx, ty):
    t.left(90)

def route4(turt, tx, ty):
    t.left(90)

tfinished = False



while (not tfinished):
    if tfinished == False:
        step = random.randint(1, 10)
        tx = tx + step
        t.setx(tx)
    finishline = 100
    if tx >= finishline:
        tfinished = True

route2(t, -200, 0)
tfinished = False

while  (not tfinished):
    if tfinished == False:
        step = random.randint(1, 1)
        ty = ty + step
        t.sety(ty)
    finishline = 200
    if ty >= finishline:
        tfinished = True
            
route3(t, -200 , 200)
tfinished = False
finishline = -300

while (not tfinished):
    if tfinished == False:
        step = random.randint(-1,-1)
        tx =  tx + step
        t.setx(tx)
     
    if tx <= finishline:
        tfinished = True


route4(t, -300, 200)
tfinished = False
finishline = 0

while  (not tfinished):
    if tfinished == False:
        step = random.randint(-1, -1)
        ty = ty + step
        t.sety(ty)
    
    if ty <= finishline:
        tfinished = True

        
            
input()