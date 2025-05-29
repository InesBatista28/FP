# Exercise 5 on "How to think like a computer scientist", ch. 11.

import turtle

def main():
    screen = turtle.Screen()
    t = turtle.Turtle()

    # Use t.up(), t.down() and t.goto(x, y)

    # Put your code here
    file = open("drawing.txt", "r")
    for line in file:
        linha = line.rstrip()
        if linha == "UP":
            t.up()
        elif linha == "DOWN":
            t.down()
        else:
            x, y = linha.split()
            t.goto(int(x), int(y))

    # Wait until window is closed
    screen.mainloop()


if __name__ == "__main__":
    main()

