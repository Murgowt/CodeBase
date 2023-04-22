import turtle

def sierpinski(points, depth, my_turtle):
    colors = ["blue", "red", "green", "white", "yellow", 
              "violet", "orange"]
    draw_triangle(points, colors[depth], my_turtle)
    if depth > 0:
        sierpinski([points[0], 
                    get_mid(points[0], points[1]), 
                    get_mid(points[0], points[2])],
                   depth-1, my_turtle)
        sierpinski([points[1], 
                    get_mid(points[0], points[1]), 
                    get_mid(points[1], points[2])],
                   depth-1, my_turtle)
        sierpinski([points[2], 
                    get_mid(points[2], points[1]), 
                    get_mid(points[0], points[2])],
                   depth-1, my_turtle)

def draw_triangle(points, color, my_turtle):
    my_turtle.fillcolor(color)
    my_turtle.up()
    my_turtle.goto(points[0][0],points[0][1])
    my_turtle.down()
    my_turtle.begin_fill()
    my_turtle.goto(points[1][0],points[1][1])
    my_turtle.goto(points[2][0],points[2][1])
    my_turtle.goto(points[0][0],points[0][1])
    my_turtle.end_fill()

def get_mid(p1, p2):
    return ((p1[0]+p2[0])/2, (p1[1]+p2[1])/2)

my_turtle = turtle.Turtle()
my_win = turtle.Screen()
my_points = [[-200,-100],[0,200],[200,-100]]
sierpinski(my_points, 3, my_turtle)
my_win.exitonclick()