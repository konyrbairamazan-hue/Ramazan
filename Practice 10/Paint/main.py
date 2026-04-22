import pygame  # Import library for game creation
import sys     # For system-specific parameters and functions (exit)
import math    # For mathematical calculations (required for triangles)

pygame.init()  # Initialize all imported pygame modules

WIDTH = 1000   # Window width
HEIGHT = 700   # Window height
screen = pygame.display.set_mode((WIDTH, HEIGHT))  # Initialize a window for display
pygame.display.set_caption("Paint")  # Set the current window caption
clock = pygame.time.Clock()  # Create an object to help track time (control FPS)

# Define Color constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 180, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GRAY = (180, 180, 180)  # Color for the UI panel

screen.fill(WHITE)  # Fill the background with white

# State variables
current_color = BLACK   # Default drawing color
tool = "brush"          # Default tool
drawing = False         # Drawing flag (True when mouse is pressed)
start_pos = None        # Starting point for shapes
last_pos = None         # Last point for brush/line drawing
brush_size = 5          # Brush thickness
eraser_size = 20        # Eraser thickness

font = pygame.font.SysFont("Verdana", 20)  # Font for UI text


def draw_ui():
    """Draw the top control panel and usage tips"""
    pygame.draw.rect(screen, GRAY, (0, 0, WIDTH, 50))  # Draw top panel background

    # Tip string
    info = (
        f"Tool: {tool} | Colors: 1-Black 2-Red 3-Green 4-Blue 5-Yellow | "
        f"B-Brush R-Rect C-Circle E-Eraser S-Square T-RightTriangle U-Equilateral H-Rhombus"
    )

    text = font.render(info, True, BLACK)  # Render text to surface
    screen.blit(text, (10, 12))  # Draw text on screen


canvas = pygame.Surface((WIDTH, HEIGHT))  # Create a surface for persistent drawing
canvas.fill(WHITE)  # Fill canvas with white


while True:  # Main game loop
    clock.tick(60)  # Limit frame rate to 60 FPS

    for event in pygame.event.get():  # Event handling loop
        if event.type == pygame.QUIT:  # If user clicks the close button
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:  # Key press events

            # Tool selection keys
            if event.key == pygame.K_b:
                tool = "brush"
            elif event.key == pygame.K_r:
                tool = "rect"
            elif event.key == pygame.K_c:
                tool = "circle"
            elif event.key == pygame.K_e:
                tool = "eraser"
            elif event.key == pygame.K_s:
                tool = "square"
            elif event.key == pygame.K_t:
                tool = "right_triangle"
            elif event.key == pygame.K_u:
                tool = "equilateral_triangle"
            elif event.key == pygame.K_h:
                tool = "rhombus"

            # Color selection keys
            elif event.key == pygame.K_1:
                current_color = BLACK
            elif event.key == pygame.K_2:
                current_color = RED
            elif event.key == pygame.K_3:
                current_color = GREEN
            elif event.key == pygame.K_4:
                current_color = BLUE
            elif event.key == pygame.K_5:
                current_color = YELLOW

            # Clear canvas key
            elif event.key == pygame.K_DELETE:
                canvas.fill(WHITE)

        if event.type == pygame.MOUSEBUTTONDOWN:  # Mouse button pressed
            if event.pos[1] > 50:  # Check if click is below the UI panel
                drawing = True
                start_pos = event.pos  # Record starting coordinates
                last_pos = event.pos   # Record last point for continuous lines

        if event.type == pygame.MOUSEBUTTONUP:  # Mouse button released
            if drawing and start_pos and event.pos[1] > 50:
                end_pos = event.pos  # Record ending coordinates

                # Draw Rectangle
                if tool == "rect":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    rect = pygame.Rect(min(x1, x2), min(y1, y2),
                                       abs(x2 - x1), abs(y2 - y1))
                    pygame.draw.rect(canvas, current_color, rect, 2)

                # Draw Circle
                elif tool == "circle":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    radius = int(((x2 - x1)**2 + (y2 - y1)**2)**0.5)
                    pygame.draw.circle(canvas, current_color, start_pos, radius, 2)

                # Draw Square
                elif tool == "square":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    side = min(abs(x2 - x1), abs(y2 - y1))
                    square = pygame.Rect(x1, y1, side, side)
                    pygame.draw.rect(canvas, current_color, square, 2)

                # Draw Right Triangle
                elif tool == "right_triangle":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    points = [(x1, y1), (x1, y2), (x2, y2)]
                    pygame.draw.polygon(canvas, current_color, points, 2)

                # Draw Equilateral Triangle
                elif tool == "equilateral_triangle":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    side = abs(x2 - x1)
                    height = int((math.sqrt(3)/2) * side)
                    points = [(x1, y1 + height), (x1 + side, y1 + height), (x1 + side//2, y1)]
                    pygame.draw.polygon(canvas, current_color, points, 2)

                # Draw Rhombus
                elif tool == "rhombus":
                    x1, y1 = start_pos
                    x2, y2 = end_pos
                    cx = (x1 + x2) // 2
                    cy = (y1 + y2) // 2
                    points = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
                    pygame.draw.polygon(canvas, current_color, points, 2)

            drawing = False  # Reset drawing state
            start_pos = None
            last_pos = None

        if event.type == pygame.MOUSEMOTION and drawing:  # Continuous drawing logic
            if event.pos[1] > 50:
                if tool == "brush":
                    pygame.draw.line(canvas, current_color, last_pos, event.pos, brush_size)
                    last_pos = event.pos

                elif tool == "eraser":
                    pygame.draw.line(canvas, WHITE, last_pos, event.pos, eraser_size)
                    last_pos = event.pos

    # Screen refresh logic
    screen.fill(WHITE)        # Clear screen
    screen.blit(canvas, (0, 0))  # Copy drawing surface to screen
    draw_ui()                 # Draw UI elements on top

    pygame.display.flip()  # Update the full display Surface to the screen