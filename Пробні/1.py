import turtle
import keyboard

keyboard.add_hotkey('w', lambda: turtle.forward(10))
keyboard.add_hotkey('s', lambda: turtle.backward(10))
keyboard.add_hotkey('a', lambda: turtle.left(10))
keyboard.add_hotkey('d', lambda: turtle.right(10))

turtle.exitonclick()
