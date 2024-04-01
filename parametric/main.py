from rainbow_parametric_anim import anim
from rainbow_parametric import draw
from sys import exit
from math import sin, cos, pi
import math

print("Rainbow Parametric Image Generator")
print("Please enter in your parametric equation. It must be:")
print("  - A valid python tuple expression")
print("  - Use t as the parameter")
print("  - Available functions: sin, cos, pi")
print("      - You can also use more functions available with math. (e.g. math.sinh)")
print("  - For example: (sin(5 * t), cos(3 * t))")
print("==> For best results, coordinates should range from -1 to 1 on the xy axes. <==")

eq = None  # type: ignore
while eq == None:
    try:
        # DO NOT DUPLICATE THIS VAR
        # due to stupid python "magic"
        # updating the variable updates the lambda
        equation_expr = input("Enter your equation: ")
        eq = lambda t: eval(equation_expr)
        x, y = eq(0.5)
    except KeyboardInterrupt:
        exit()
    except:
        pass

size = int(input("Size of resulting image (empty for 250): ") or 250)

print(
    "\nDetail of image, how many steps should be made, more detail = slower, (500 recommended)"
)
detail = int(input("Detail (empty for default): ") or 500)

print("\nThickness of stroke")
thick = int(input("Thickness (empty for 2): ") or 2)

print(
    "\nImage step, how many frames should be generated (lower = more frames, slower) (10 recommended)"
)
image_step = int(input("Image step (empty for 10): ") or 10)

print(
    "\nPeriod of function (valid python expression) (usually is 2 * pi, but use desmos to check)"
)
period = None  # type: ignore
while period == None:
    try:
        s = input("Enter your equation (leave blank for 2 * pi): ") or "2 * pi"
        period = eval(s)
        if type(period) != float:
            period = None
    except KeyboardInterrupt:
        exit()
    except:
        pass

gen_still = input("\nGenerate still image as well? (y/n) ") == "y"
if gen_still:
    print("\nStill images take less time to generate, so size can be bigger (optional)")
    still_size = int(
        input("Optional still image size (leave blank to be twice as size): ")
        or 2 * size
    )

file_name = (
    input("\nFilename (w/o extension, e.g. output) (leave blank for output): ")
    or "output"
)

anim(eq, file_name, size, detail, thick, image_step, period)  # type: ignore
print(f"Saved gif to parametric/{file_name}.gif")

if gen_still:
    draw(eq, file_name, still_size, detail, thick, period)  # type: ignore
    print(f"Saved png to parametric/{file_name}.png")
