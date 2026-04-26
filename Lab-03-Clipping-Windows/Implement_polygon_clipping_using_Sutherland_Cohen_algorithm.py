import matplotlib.pyplot as plt

# Clipping window
x_min, y_min = 100, 100
x_max, y_max = 300, 300

# Define polygon (example hexagon)
polygon = [
    (50, 150),
    (150, 50),
    (250, 80),
    (350, 150),
    (300, 300),
    (100, 350)
]

def inside(p, edge):
    x, y = p
    if edge == "LEFT":
        return x >= x_min
    elif edge == "RIGHT":
        return x <= x_max
    elif edge == "BOTTOM":
        return y >= y_min
    elif edge == "TOP":
        return y <= y_max

def intersect(p1, p2, edge):
    x1, y1 = p1
    x2, y2 = p2

    if edge == "LEFT":
        x = x_min
        y = y1 + (y2 - y1) * (x_min - x1) / (x2 - x1)
    elif edge == "RIGHT":
        x = x_max
        y = y1 + (y2 - y1) * (x_max - x1) / (x2 - x1)
    elif edge == "BOTTOM":
        y = y_min
        x = x1 + (x2 - x1) * (y_min - y1) / (y2 - y1)
    elif edge == "TOP":
        y = y_max
        x = x1 + (x2 - x1) * (y_max - y1) / (y2 - y1)

    return (x, y)

def sutherland_hodgman_clip(subject_polygon):
    edges = ["LEFT", "RIGHT", "BOTTOM", "TOP"]
    clipped_polygon = subject_polygon

    for edge in edges:
        new_polygon = []
        for i in range(len(clipped_polygon)):
            curr = clipped_polygon[i]
            prev = clipped_polygon[i - 1]

            if inside(curr, edge):
                if not inside(prev, edge):
                    new_polygon.append(intersect(prev, curr, edge))
                new_polygon.append(curr)
            elif inside(prev, edge):
                new_polygon.append(intersect(prev, curr, edge))

        clipped_polygon = new_polygon

    return clipped_polygon

# Perform clipping
clipped = sutherland_hodgman_clip(polygon)

# Plotting
def plot_polygon(poly, color, label):
    x = [p[0] for p in poly] + [poly[0][0]]
    y = [p[1] for p in poly] + [poly[0][1]]
    plt.plot(x, y, marker='o', label=label)

plt.figure()
plot_polygon(polygon, 'blue', "Original Polygon")
plot_polygon(clipped, 'red', "Clipped Polygon")

# Draw clipping window
plt.plot([x_min, x_max, x_max, x_min, x_min],
         [y_min, y_min, y_max, y_max, y_min],
         'green', label="Clipping Window")

plt.legend()
plt.title("Sutherland-Hodgman Polygon Clipping")
plt.grid()
plt.show()