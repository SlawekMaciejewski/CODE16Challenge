import colorgram

# def extract_colors_picture(picture_jpg, number_of_colors):
#     colors = colorgram.extract(picture_jpg, number_of_colors)
#     rgb_colors = []
#     for i in range(number_of_colors):
#         rgb_colors.append((colors[i].rgb.r, colors[i].rgb.g, colors[i].rgb.b))
#     # first 3 tuples are like white, delete them
#     rgb_colors = rgb_colors[3:]
#     return rgb_colors


def extract_colors_picture2(picture_jpg, number_of_colors):
    colors = colorgram.extract(picture_jpg, number_of_colors)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    # first 3 tuples are like white, delete them
    rgb_colors = rgb_colors[3:]
    return rgb_colors


picture = 'spots.jpg'
COLOR_PALETTE = extract_colors_picture2(picture, 30)
print(COLOR_PALETTE)