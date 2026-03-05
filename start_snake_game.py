from turtle import Screen, Turtle
import time
snake = Turtle("square")
screen = Screen()
screen.setup(width=2000,height=1500)
screen.bgcolor("black")
screen.title("My snake game")
screen.listen()
snake.fillcolor("white")
snake.penup()


# snake_boxes_cor = []
snake_boxes = [snake]
def turn_left():
    snake.left(90)

def turn_right():
    snake.right(90)


def snake_grow():
    global snake_boxes
    snake_boxes.append(Turtle("square"))



def move_snake():
    screen.tracer(0)
    snake_boxes_cor = []
    for box in snake_boxes:
        new_dict = {"x_cor": box.xcor(),"y_cor": box.ycor()}
        box.color("white")
        box.penup()
        snake_boxes_cor.append(new_dict)
    pre = 1
    if not len(snake_boxes) == 1:
        for snake_cor in snake_boxes_cor:
            snake_boxes[pre].setposition(snake_cor["x_cor"],snake_cor["y_cor"])
            pre += 1
            if not len(snake_boxes) > pre:
                break
    snake.forward(20)
    time.sleep(0.1)
    screen.update()

screen.onkey(key="h",fun=snake_grow)
# screen.onkey(key="Up",fun=move_snake)
screen.onkey(key="Left",fun=turn_left)
screen.onkey(key="Right",fun=turn_right)

is_running = True

while is_running:
    move_snake()

screen.mainloop()
