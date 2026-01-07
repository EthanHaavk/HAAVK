# # print('%10.2f'%(3.1415926))
# import turtle
# screen=turtle.Screen()
# pen=turtle.Turtle()
# pen.setheading(90)

# # 假设一格的长度为20像素，这里让画笔向上移动两格
# step_size = 55
# pen.forward(5 * step_size)

# # 保持窗口打开，直到用户关闭它
# turtle.done()


import turtle
screen=turtle.Screen()
pen=turtle.Turtle()
pen.setheading(90)

s=55
pen.forward(5*s)

pen.setheading(0)
pen.forward(5*s)
pen.setheading(-90)
pen.forward(5*s)
pen.setheading(-180)
pen.forward(5*s)
pen.setheading(0)
pen.forward(7*s)
pen.setheading(-90)
pen.forward(5*s)
pen.setheading(0)
pen.backward(7*s)
pen.setheading(90)
pen.forward(5*s)
pen.setheading(-180)
pen.forward(7*s)
pen.setheading(0)
pen.forward(2*s)
pen.setheading(-90)
pen.forward(1*s)
pen.setheading(0)
pen.backward(2*s)
pen.setheading(-90)
pen.forward(1*s)
pen.setheading (0)
pen.forward(2*s)
turtle.done()
