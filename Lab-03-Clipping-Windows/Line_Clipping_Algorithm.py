# Region codes
INSIDE = 0  # 0000
LEFT   = 1  # 0001
RIGHT  = 2  # 0010
BOTTOM = 4  # 0100
TOP    = 8  # 1000

# Define clipping window (xmin, ymin) to (xmax, ymax)
x_min = 100
y_min = 100
x_max = 300
y_max = 300

# Function to compute region code for a point (x, y)
def compute_code(x, y):
    code = INSIDE
    if x < x_min:
        code |= LEFT
    elif x > x_max:
        code |= RIGHT
    if y < y_min:
        code |= BOTTOM
    elif y > y_max:
        code |= TOP
    return code

# Cohen-Sutherland clipping algorithm
def cohen_sutherland_clip(x1, y1, x2, y2):
    code1 = compute_code(x1, y1)
    code2 = compute_code(x2, y2)
    accept = False

    while True:
        # Both endpoints inside
        if code1 == 0 and code2 == 0:
            accept = True
            break
        # Logical AND is not 0, both endpoints share an outside zone
        elif code1 & code2 != 0:
            break
        else:
            # At least one endpoint is outside the clip window
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            # Find intersection point
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

            # Replace point outside the window with the intersection point
            if code_out == code1:
                x1, y1 = x, y
                code1 = compute_code(x1, y1)
            else:
                x2, y2 = x, y
                code2 = compute_code(x2, y2)

    if accept:
        print(f"Line accepted from ({x1:.1f}, {y1:.1f}) to ({x2:.1f}, {y2:.1f})")
    else:
        print("Line rejected")

# Example lines to clip
cohen_sutherland_clip(50, 150, 350, 250)      # Partially inside
cohen_sutherland_clip(120, 120, 180, 280)     # Fully inside
cohen_sutherland_clip(90, 90, 95, 95)         # Fully outside
