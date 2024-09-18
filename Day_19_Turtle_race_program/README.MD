
### Extract colors using colorgram
```python

import colorgram

colors = colorgram.extract('image.jpg', 30)

rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.g
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

```

### Draw Color Dots 
```python

t.colormode(255)
color_list = [(247, 246, 246), (195, 149, 149), (230, 213, 213), (246, 253, 253), (253, 249, 249), (200, 231, 231), (90, 179, 179), (32, 176, 176), (232, 106, 106), (69, 80, 80), (162, 101, 101), (215, 86, 86), (212, 104, 104), (38, 48, 48), (176, 200, 200), (17, 151, 151), (160, 209, 209), (128, 190, 190), (93, 103, 103), (232, 166, 166), (153, 214, 214), (179, 184, 184), (205, 219, 219), (55, 159, 159), (238, 177, 177), (22, 31, 31), (161, 81, 81)]
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 101

for dot_count in range(1, number_of_dots):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

```