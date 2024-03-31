from PIL import Image, ImageDraw, ImageFont

alphabet = "abcdefghijklmnopqrstuvwxyz"
caps = alphabet.upper()

nums = "1234567890"

special = R"""~!@#$%^&*()_+-=[]\|{}:"'<>? /█▓▒░"""

chars = list(alphabet + caps + nums + special)

print("chars:", len(chars))

font = ImageFont.truetype(font=R"""C:\Windows\Fonts\consola.ttf""", size=20)

XK = 12
YK = 22

WID = XK * 10  # 120
HEI = YK * 10  # 220
im = Image.new(mode="RGB", size=(WID, HEI))

ctx = ImageDraw.Draw(im)
for y in range(0, 10):
    for x in range(0, 10):
        index = y * 10 + x
        if index >= len(chars):
            break
        ctx.text((x * XK, y * YK), chars[index], fill=(255, 255, 255), font=font)


pixels = im.load()

# max x = 119
# max y = 219

# xk = 12
# yk = 22

pixel_count = YK * XK

brightness_values = []

for yi in range(0, HEI // YK):
    for xj in range(0, WID // XK):
        sx = xj * XK
        sy = yi * YK

        idx = yi * 10 + xj

        if idx >= len(chars):
            break

        total_sum = 0

        for y in range(sy, sy + YK):
            for x in range(sx, sx + XK):
                total_sum += (pixels[x, y][0] + pixels[x, y][1] + pixels[x, y][2]) // 3

        avg = round(total_sum / pixel_count)
        # brightness_values[avg] = chars[idx]
        brightness_values.append((avg, chars[idx]))

brightness_values = sorted(brightness_values, key=lambda x: x[0])
print([v for _, v in brightness_values])

im.save("char-out.png")
