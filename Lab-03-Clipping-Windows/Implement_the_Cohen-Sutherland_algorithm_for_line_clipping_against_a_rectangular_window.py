import matplotlib.pyplot as plt

INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

# Clipping window
x_min, y_min = 100, 100
x_max, y_max = 300, 300

def compute_code(x, y):
    code = INSIDE
    if x < x_min: code |= LEFT
    elif x > x_max: code |= RIGHT
    if y < y_min: code |= BOTTOM
    elif y > y_max: code |= TOP
    return code

def cohen_sutherland_clip(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)
    accept = False

    while True:
        if code1 == 0 and code2 == 0:
            accept = True
            break
        elif code1 & code2 != 0:
            break
        else:
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            if code_out & TOP:
                x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)
                y = y_max
            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
                y = y_min
            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
                x = x_max
            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
                x = x_min

            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

    if accept:
        return (x1, y1, x2, y2)
    else:
        return None

# Test lines
lines = [
    (10, 20, 50, 70),
    (40, 80, 80, 20),
    (50, 150, 350, 250),
    (120, 120, 180, 280)
]

plt.figure()

# Draw clipping window
plt.plot([x_min, x_max, x_max, x_min, x_min],
         [y_min, y_min, y_max, y_max, y_min],
         'green', label="Clipping Window")

# Plot original lines (blue)
for line in lines:
    x1, y1, x2, y2 = line
    plt.plot([x1, x2], [y1, y2], 'blue')

# Plot clipped lines (red)
for line in lines:
    clipped = cohen_sutherland_clip(*line)
    if clipped:
        x1, y1, x2, y2 = clipped
        plt.plot([x1, x2], [y1, y2], 'red', linewidth=2)

plt.title("Cohen-Sutherland Line Clipping")
plt.grid()
plt.show()