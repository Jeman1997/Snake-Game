from turtle import Screen,Turtle
from food import Food
from snake import Snake
from scoreboard import Scorebd
import time
s=Screen()
s.setup(width=600,height=600)
s.bgcolor('black')
s.title('Snake Game')
s.tracer(0)
snake=Snake()
food=Food()
sbd=Scorebd()
s.listen()
s.onkey(key='w',fun=snake.upward)
s.onkey(key='s',fun=snake.downward)
s.onkey(key='a',fun=snake.leftward)
s.onkey(key='d',fun=snake.rightward)
is_on=True
while is_on:
    s.update()
    time.sleep(0.1)
    #for x in seg:
        #x.fd(20)
    #seg[0].lt(90)   
    snake.move()
#---Collision with food---------------#
    if snake.seg[0].distance(food) < 15:
        food.refresh()
        sbd.upd()
        snake.extend()
#---Collision with walls--------------#
    if snake.seg[0].xcor()>290 or snake.seg[0].xcor()<-290 or snake.seg[0].ycor()>290 or snake.seg[0].ycor()<-290:
        sbd.reset()
        snake.reset()
#---Snake trying to eat a part of itself------#
    for se in snake.seg:
        if se==snake.seg[0]:
            pass
        elif snake.seg[0].distance(se)<10:
            sbd.reset()
            snake.reset()
s.exitonclick()
