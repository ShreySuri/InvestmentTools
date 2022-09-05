import turtle
    
def graph(max_x, max_y):

    t = turtle.Pen()
    t.hideturtle()
    vert = turtle.Pen()
    vert.hideturtle()
    hori = turtle.Pen()
    hori.hideturtle()


    t.up()
    t.left(90)

    for i in range (1, 3):
        t.forward(375 * i)
        t.left(90)
        t.forward(750 * i)
        t.left(90)
        t.down()

    vert.up()
    hori.up()
    vert.right(90)
    hori.right(90)

    for i in range (1, 3):
        vert.forward(375 * i)
        hori.forward(375 * i)
        vert.right(90)
        hori.right(90)

    hori.right(90)
    vert.down()
    hori.down()

    vert_quotient = 750 / max_y
    if int(vert_quotient) == vert_quotient:
        vert_quotient = vert_quotient - 1
    else:
        toggle = True

    hori_quotient = 1500 / max_x
    if int(hori_quotient) == hori_quotient:
        hori_quotient = hori_quotient - 1
    else:
        toggle = True

    for i in range (0, max_y):
        vert.forward(vert_quotient)
        vert.right(90)
        vert.forward(10)
        vert.right(180)
        vert.forward(10)
        vert.right(90)

    for i in range (0, max_x):
        hori.forward(hori_quotient)
        hori.left(90)
        hori.forward(10)
        hori.left(180)
        hori.forward(10)
        hori.left(90)


  
