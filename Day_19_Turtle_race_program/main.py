from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
  tim.forward(10)

def move_backwards():
  tim.backward(10)

def turn_left():
  new_heading = tim.heading() + 10
  tim.setheading(new_heading)

def turn_right():
  tim.right(-10)

def clear():
  tim.clear()
  tim.penup()
  tim.home()
  tim.pendown()

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(move_backwards, key="s")
screen.onkey(turn_left, key='a')
screen.onkey(turn_right, key='d')
screen.onkey(clear, key='c')

screen.exitonclick()