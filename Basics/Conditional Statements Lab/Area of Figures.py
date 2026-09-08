import math

type_of_figure = str(input())

if type_of_figure == "square":
    side = float(input())
    result = side * side
elif type_of_figure == "rectangle":
    side1 = float(input())
    side2 = float(input())
    result = side1 * side2
elif type_of_figure == "circle":
    radius = float(input())
    result = math.pi * radius * radius
elif type_of_figure == "triangle":
    side = float(input())
    height = float(input())
    result = side * height / 2

print(f'{result:.3f}')
