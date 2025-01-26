# importing stuff
import turtle
import random
import time

# here is where colors are defined, using RGB values
def choose_color_theme():
    themes = {
        'Rainbow': [(255, 0, 0), (255, 165, 0), (255, 255, 0), (0, 128, 0), (0, 0, 255), (128, 0, 128)],
        'Pastel': [(255, 192, 203), (0, 255, 255), (255, 0, 255), (255, 215, 0), (192, 192, 192), (0, 255, 0)],
        'Forest': [(22, 92, 8), (8, 35, 92), (12, 5, 59), (75, 85, 37), (104, 83, 56), (106, 67, 45)],
        'Grey': [(178, 190, 181), (132, 136, 132), (129, 133, 137), (54, 69, 79), (137, 148, 153), (229, 228, 226)]
    }

    print("Choose a color theme:") # User input, asks for what theme user wants
    for theme_name, colors in themes.items():
        color_names = ', '.join([f"RGB({r}, {g}, {b})" for r, g, b in colors])
        print(f"{theme_name}: {color_names}")

    while True:
        theme_choice = input("Enter the name of your chosen theme: ")
        if theme_choice in themes:
            return themes[theme_choice]
        else:
            print("Invalid theme name. Please choose from the provided options.")


# Defines what shapes are to be used, for Turtle
def draw_shape(t, shape, colors):
    t.fillcolor(random.choice(colors))
    t.begin_fill()
    if shape == 'rectangle':
        width = random.randint(50, 150)
        height = random.randint(50, 150)
      
        for _ in range(2):
            t.forward(width)
            t.right(90)
            t.forward(height)
            t.right(90)
   
    elif shape == 'square':
        side = random.randint(50, 150)
        for _ in range(4):
            t.forward(side)
            t.right(90)
   
    elif shape == 'triangle':
        side = random.randint(50, 150)
        for _ in range(3):
            t.forward(side)
            t.right(120)
  
    elif shape == 'trapezoid':
        base = random.randint(80, 150)
        top = random.randint(50, 100)
        height = random.randint(50, 150)
        t.forward(base)
        t.right(60)
        t.forward(top)
        t.right(120)
        t.forward(height)
        t.right(120)
        t.forward(top)
        t.right(60)
   
    elif shape == 'circle':
        radius = random.randint(30, 100)
        t.circle(radius)
 
    elif shape == 'hexagon':
        side = random.randint(40, 100)
        for _ in range(6):
            t.forward(side)
            t.right(60)
   
    elif shape == 'octagon':
        side = random.randint(40, 100)
        for _ in range(8):
            t.forward(side)
            t.right(45)
   
    elif shape == 'rhombus':
        side = random.randint(50, 150)
        for _ in range(2):
            t.forward(side)
            t.right(60)
            t.forward(side)
            t.right(120)
   
    elif shape == 'pentagon':
        side = random.randint(50, 150)
        for _ in range(5):
            t.forward(side)
            t.right(72)
   
    elif shape == 'kite':
        side = random.randint(50, 150)
        long_diag = random.randint(60, 150)
        short_diag = random.randint(40, 100)
        t.forward(side)
        t.right(70)
        t.forward(long_diag)
        t.right(100)
        t.forward(short_diag)
        t.right(80)
        t.forward(long_diag)
        t.right(100)
        t.forward(short_diag)
   
    elif shape == 'oval':
        radius1 = random.randint(50, 100)
        radius2 = random.randint(30, 80)
        t.left(45)
        for _ in range(2):
            t.circle(radius1, 90)
            t.circle(radius2, 90)
   
    elif shape == 'heptagon':
        side = random.randint(50, 150)
        for _ in range(7):
            t.forward(side)
            t.right(51.43)
    t.end_fill()


# Heres how the popup should act, and how Turtle should act as well
def main():
    screen = turtle.Screen()
    screen.setup(1200, 1200)
    screen.tracer(0)

    t = turtle.Turtle()
    turtle.colormode(255)
    screen_width = screen.window_width() // 2
    screen_height = screen.window_height() // 2

    shapes = ['rectangle', 'square', 'triangle', 'trapezoid', 'circle', 'hexagon', 'octagon', 'rhombus', 'pentagon',
              'kite', 'oval', 'heptagon']

    colors = choose_color_theme()
    # User input for how long Turtle should draw, with a minimum of 5 second duration
    user_input = input("How long should Turtle draw for? (minimum 5 seconds): ")
    seconds = max(5, int(user_input))

    start_time = time.time()

    t.penup()
    t.goto(0, 0)  # Start at the center
    t.pendown()

    step = 10
    while True:
        current_time = time.time()
        elapsed_time = current_time - start_time

        if elapsed_time >= seconds:
            break

        shape = random.choice(shapes)
        draw_shape(t, shape, colors)

        x_bias = random.randint(-5, 5)
        y_bias = random.randint(-5, 5)

        new_x = t.xcor() + x_bias
        new_y = t.ycor() + y_bias

        if abs(new_x) > screen_width:
            x_direction = -1 if new_x > 0 else 1
            t.setx(screen_width - x_direction * step / 2)
        else:
            t.setx(new_x)

        if abs(new_y) > screen_height:
            y_direction = -1 if new_y > 0 else 1
            t.sety(screen_height - y_direction * step / 2)
        else:
            t.sety(new_y)

        t.right(random.randint(0, 360))
        screen.update()

    turtle.done()


if __name__ == "__main__":
    main()
