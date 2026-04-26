# Define clipping window (xmin, ymin) to (xmax, ymax)
clip_window = {
"xmin": 100,
"ymin": 100,
"xmax": 300,
"ymax": 300
}

# Function to check if a point is inside the clipping window
def is_point_inside(x, y, clip_win):
    return (clip_win["xmin"] <= x <= clip_win["xmax"]) and \
        (clip_win["ymin"] <= y <= clip_win["ymax"])

# Sample points
points = [
(150, 150),
(90, 120),
(250, 310),
(100, 100), # Boundary point
(305, 299)
]

# Clip the points
print("Clipping result:")
for (x, y) in points:
    if is_point_inside(x, y, clip_window):
        print(f"Point ({x}, {y}) is INSIDE the clipping window.")
    else:
        print(f"Point ({x}, {y}) is OUTSIDE the clipping window.")