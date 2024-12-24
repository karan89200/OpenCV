import cv2
import numpy as np
import os

# Initialize variables
drawing = False
tool = "pencil"
color = (0, 0, 255)  # Default red
thickness = 2
start_x, start_y = -1, -1
dropdown_open = False
selected_tool = "pencil"

# Path to the icons folder
icon_folder = "img"

# Load icons
def load_icon(filename):
    try:
        icon = cv2.imread(os.path.join(icon_folder, filename))
        if icon is None:
            raise FileNotFoundError(f"Icon {filename} not found.")
        return cv2.resize(icon, (40, 40))
    except Exception as e:
        print(e)
        return np.ones((40, 40, 3), dtype=np.uint8) * 255  # Placeholder white icon

icons = {
    "pencil": load_icon("pencil.png"),
    "eraser": load_icon("eraser.png"),
    "line": load_icon("line.png"),
    "rectangle": load_icon("rectangle.png"),
    "star": load_icon("star.png"),
    "thickness": load_icon("thickness.png"),
}

# Button positions (left toolbox)
toolbox_buttons = {
    "pencil": (10, 50),
    "eraser": (10, 110),
    "line": (10, 170),
    "rectangle": (10, 230),
    "star": (10, 290),
    "thickness": (10, 350),
}

# Create a blank canvas
canvas_height, canvas_width = 600, 800
img = np.ones((canvas_height, canvas_width - 100, 3), dtype=np.uint8) * 255

# Function to draw a star
def draw_star(img, center, size, color, thickness):
    points = []
    for i in range(10):
        angle = i * 2 * np.pi / 10
        r = size if i % 2 == 0 else size // 2
        x = int(center[0] + r * np.cos(angle))
        y = int(center[1] - r * np.sin(angle))
        points.append((x, y))
    for i in range(len(points)):
        cv2.line(img, points[i], points[(i + 1) % len(points)], color, thickness)

# Mouse callback function
def draw(event, x, y, flags, param):
    global drawing, start_x, start_y, tool, img, color, thickness, dropdown_open, selected_tool

    # Adjust x-coordinate for drawing
    adjusted_x = x - 100

    # Handle thickness dropdown click
    if dropdown_open:
        if event == cv2.EVENT_LBUTTONDOWN:
            bx, by = toolbox_buttons["thickness"]
            for i in range(7):
                if bx <= x <= bx + 80 and by + 40 + i * 20 <= y <= by + 60 + i * 20:
                    thickness = i + 1
                    dropdown_open = False
            return

    # Handle toolbox clicks
    for key, pos in toolbox_buttons.items():
        bx, by = pos
        if bx <= x <= bx + 40 and by <= y <= by + 40:
            if event == cv2.EVENT_LBUTTONDOWN:
                selected_tool = key
                if key == "thickness":
                    dropdown_open = not dropdown_open
                else:
                    tool = key
                return

    if adjusted_x < 0:  # Ignore clicks outside the canvas
        return

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        start_x, start_y = adjusted_x, y

    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        if tool == "pencil":
            cv2.line(img, (start_x, start_y), (adjusted_x, y), color, thickness)
            start_x, start_y = adjusted_x, y
        elif tool == "eraser":
            cv2.line(img, (start_x, start_y), (adjusted_x, y), (255, 255, 255), thickness)
            start_x, start_y = adjusted_x, y
        elif tool == "star":
            temp_img = img.copy()
            draw_star(temp_img, ((start_x + adjusted_x) // 2, (start_y + y) // 2), min(abs(adjusted_x - start_x), abs(y - start_y)) // 2, color, thickness)
            cv2.imshow("Paint", combined_canvas(temp_img))
        elif tool == "line":
            temp_img = img.copy()
            cv2.line(temp_img, (start_x, start_y), (adjusted_x, y), color, thickness)
            cv2.imshow("Paint", combined_canvas(temp_img))
        elif tool == "rectangle":
            temp_img = img.copy()
            cv2.rectangle(temp_img, (start_x, start_y), (adjusted_x, y), color, thickness)
            cv2.imshow("Paint", combined_canvas(temp_img))

    elif event == cv2.EVENT_LBUTTONUP and drawing:
        drawing = False
        if tool == "star":
            draw_star(img, ((start_x + adjusted_x) // 2, (start_y + y) // 2), min(abs(adjusted_x - start_x), abs(y - start_y)) // 2, color, thickness)
        elif tool == "line":
            cv2.line(img, (start_x, start_y), (adjusted_x, y), color, thickness)
        elif tool == "rectangle":
            cv2.rectangle(img, (start_x, start_y), (adjusted_x, y), color, thickness)

# Combine toolbox and canvas
def combined_canvas(temp_img=None):
    toolbox = np.ones((canvas_height, 100, 3), dtype=np.uint8) * 255  # White background for toolbox

    # Draw icons with white background
    for key, pos in toolbox_buttons.items():
        bx, by = pos
        toolbox[by:by+40, bx:bx+40] = icons[key]
        if key == selected_tool:
            cv2.rectangle(toolbox, (bx - 2, by - 2), (bx + 42, by + 42), (0, 255, 0), 2)

    # Draw thickness dropdown
    if dropdown_open:
        dropdown = toolbox.copy()
        bx, by = toolbox_buttons["thickness"]
        for i in range(7):
            y_start = by + 40 + i * 20
            cv2.rectangle(dropdown, (bx, y_start), (bx + 80, y_start + 20), (200 - i * 20, 200 - i * 20, 200 - i * 20), -1)
            cv2.putText(dropdown, f"{i + 1}", (bx + 5, y_start + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 1)
        toolbox = dropdown

    combined = np.hstack((toolbox, temp_img if temp_img is not None else img))
    return combined

# Set up the window and callback
cv2.namedWindow("Paint")
cv2.setMouseCallback("Paint", draw)

while True:
    cv2.imshow("Paint", combined_canvas())
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('c'):  # Clear canvas
        img = np.ones((canvas_height, canvas_width - 100, 3), dtype=np.uint8) * 255

cv2.destroyAllWindows()
