import colorgram

rgb_color = []

color = colorgram.extract('hirst_painting.jpg', 30)

for color in color:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_rgb_color = (r, g, b)
    rgb_color.append(new_rgb_color)

print(rgb_color)
