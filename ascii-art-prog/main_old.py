brightness = list(
    R"""$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,"^`'."""[::-1]
)

# for _, v in brightness_list:
#     brightness.append(v)


def get_char(v):
    # lerp function
    i = round(v / 255 * (len(brightness) - 1))
    return brightness[i]


def contrastify(n):
    if n < 128:
        return 0
    else:
        return 255


from PIL import Image, ImageDraw, ImageFont

inp_im = Image.open("target.png")
""" Input image """

downscale = 5
""" Lower the downscale, less resize => better """

wid = inp_im.width
hei = inp_im.height
pixels = inp_im.load()

new_hei = hei // downscale
new_wid = wid // downscale

FONT_SIZE = 20

font = ImageFont.truetype(font=R"""C:\Windows\Fonts\consola.ttf""", size=FONT_SIZE)

# font spacing etc
XK = FONT_SIZE  # x values duplicate because text is intrinsically 1x2
YK = FONT_SIZE

new_wid *= XK
new_hei *= YK


output_image = Image.new(mode="RGB", size=(new_wid, new_hei))
ctx = ImageDraw.Draw(output_image)
# opxs = output_image.load()

for y_idx in range(0, hei // downscale):
    for x_idx in range(0, wid // downscale):
        y, x = y_idx * downscale, x_idx * downscale

        # color = tuple([contrastify(p) for p in pixels[x, y]])
        color = pixels[x, y]
        avg = round(sum([contrastify(p) for p in pixels[x, y]]) / 3)
        char = get_char(avg)

        ctx.text((x_idx * XK, y_idx * YK), char * 2, fill=color, font=font)


output_image.save("output.png")

""" use this to actually get text output """
# out = ""

# for y_idx in range(0, hei // downscale):
#     for x_idx in range(0, wid // downscale):
#         y, x = y_idx * downscale, x_idx * downscale

#         avg = round(sum([contrastify(p) for p in pixels[x, y]]) / 3)
#         closest = get_char(avg)

#         out += closest * 2
#     out += "\n"

# print(out)
