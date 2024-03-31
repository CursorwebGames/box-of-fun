IMAGE_NAME = "duo.png"
""" from inputs/... """

DOWNSCALE = 5
""" Lower the downscale, less resize => better, recommend 5 """

STEPS_OF_COLOR = 3
""" more steps of color = less contrast in characters, but more in color"""


brightness = list(
    R"""$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'."""[::-1]
)


def get_char(v):
    # lerp function
    i = round(v / 255 * (len(brightness) - 1))
    return brightness[i]


def contrastify(n):
    """create a contrast for a better result"""
    i = round(n / 255 * STEPS_OF_COLOR)
    return round(i / STEPS_OF_COLOR * 255)


from PIL import Image, ImageDraw, ImageFont

inp_im = Image.open(f"inputs/{IMAGE_NAME}")
""" Input image """


wid = inp_im.width
hei = inp_im.height
pixels = inp_im.load()

new_hei = hei // DOWNSCALE
new_wid = wid // DOWNSCALE

FONT_SIZE = 20

font = ImageFont.truetype(font=R"""C:\Windows\Fonts\consola.ttf""", size=FONT_SIZE)

# font spacing etc
XK = FONT_SIZE  # x values duplicate because text is intrinsically 1x2
YK = FONT_SIZE

new_wid *= XK
new_hei *= YK


output_image = Image.new(mode="RGB", size=(new_wid, new_hei))
ctx = ImageDraw.Draw(output_image)

for y_idx in range(0, hei // DOWNSCALE):
    for x_idx in range(0, wid // DOWNSCALE):
        y, x = y_idx * DOWNSCALE, x_idx * DOWNSCALE

        # color = tuple([contrastify(p) for p in pixels[x, y]])
        color = pixels[x, y]
        avg = round(sum([contrastify(p) for p in pixels[x, y]]) / 3)
        char = get_char(avg)

        # ctx.text(
        #     (x_idx * XK + XK / 2, y_idx * YK + YK / 2), char * 2, fill=color, font=font
        # )
        ctx.text((x_idx * XK, y_idx * YK), char * 2, fill=color, font=font)
        # ctx.text((x_idx * XK, y_idx * YK), char * 2, fill=(255, 255, 255), font=font)


output_image.save(f"outputs/{IMAGE_NAME}")

# out = ""

# for y_idx in range(0, hei // downscale):
#     for x_idx in range(0, wid // downscale):
#         y, x = y_idx * downscale, x_idx * downscale

#         avg = round(sum([contrastify(p) for p in pixels[x, y]]) / 3)
#         closest = get_char(avg)

#         out += closest * 2
#     out += "\n"

# print(out)
