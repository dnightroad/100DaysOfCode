from turtle import Turtle,onkey
snake_position = [(0,0), (-20,0), (-40,0)]
class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in snake_position:

            self.add_segment(position)

    def add_segment(self, position):
        new_snake_part = Turtle("square")
        new_snake_part.color("white")
        new_snake_part.penup()
        new_snake_part.goto(position)
        self.segments.append(new_snake_part)

        def left_move():
            self.head.setheading(180)
        def right_move():
            self.head.setheading(0)
        def up_move():
            self.head.setheading(90)
        def down_move():
            self.head.setheading(270)
        onkey(up_move, "Up")
        onkey(down_move, "Down")
        onkey(left_move, "Left")
        onkey(right_move, "Right")

    def move(self):
        for seg_num in range((len(self.segments) - 1), 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(20)
        if self.head.xcor() >= 300  or self.head.ycor() >= 300\
                or self.head.xcor() <= -300 or self.head.ycor() <=-300:
            game_is_on = False
            return game_is_on


    def extend(self):
        self.add_segment(self.segments[-1].position())






