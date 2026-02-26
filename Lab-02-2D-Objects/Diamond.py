def draw_diamond():
    size = 5

    for i in range(size):
        print(" " * (size - i - 1) + "* " * (i + 1))

    for i in range(size - 1):
        print(" " * (i + 1) + "* " * (size - i - 1))

draw_diamond()
