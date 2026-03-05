from turtle import Screen, Turtle
import time
snake = Turtle("turtle")
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.listen()
snake.fillcolor("white")
snake.pencolor("red")
snake.penup()

is_running = True

# snake_boxes_cor = []
snake_boxes = [snake]
def turn_left():
    snake.left(90)
    print("Turn_left")
def turn_right():
    snake.right(90)
    print("Turn_right")

def pause():
    global is_running
    is_running = False

def snake_grow():
    global snake_boxes
    snake_boxes.append(Turtle("square"))
    print(f"add extra box, overall:{len(snake_boxes)}")

def move_snake():
    screen.tracer(0)
    snake_boxes_cor = []
    for box in snake_boxes:
        new_dict = {"x_cor": box.xcor(),"y_cor": box.ycor()}
        box.fillcolor("white")
        box.pencolor("red")
        box.penup()
        snake_boxes_cor.append(new_dict)
    pre = 1
    if not len(snake_boxes) == 1:
        for snake_cor in snake_boxes_cor:
            snake_boxes[pre].setposition(snake_cor["x_cor"],snake_cor["y_cor"])
            pre += 1
            if not len(snake_boxes) > pre:
                print(f"position changed to forward box pre:{pre} box len:{len(snake_boxes)}")
                break
    snake.forward(20)
    screen.update()
    time.sleep(.1)

screen.onkey(key="h",fun=snake_grow)
# screen.onkey(key="Up",fun=move_snake)
screen.onkey(key="space", fun=pause)
screen.onkey(key="Left",fun=turn_left)
screen.onkey(key="Right",fun=turn_right)



while is_running:
    move_snake()

screen.mainloop()
