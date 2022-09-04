import turtle
    
def graph(max_y, max_x):

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
