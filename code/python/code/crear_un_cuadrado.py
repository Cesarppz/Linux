import turtle 

def run():
    window = turtle.Screen()
    colors=['red','purple','blue','green','yellow','orange']
    t = turtle.Pen()
    t.speed(0)
    
    for x in range(360):
        t.pencolor(colors[x%6])
        t.width(x/100+1)
        t.forward(x)
        t.left(59)

    turtle.mainloop()
    
    
    # window= turtle.Screen()
    # line  = turtle.Turtle()
    # line.forward(90)
    # line.left(90)
    # line.forward(90)
    # line.left(90)
    # line.forward(90)
    # line.left(90)
    # line.forward(90)
    # line.left(90)
    # turtle.mainloop()


if __name__ == '__main__':
    run()