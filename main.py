import os
from sys import exit


def clear():
    os.system("cls" if os.name == "nt" else "clear")


programs = [
    (
        "ascii art",
        "ascii-art-prog",
    ),
    ("gf game", "gf-game"),
    ("parametric gif generator", "parametric"),
    ("shooter game", "shooter-game"),
]

while True:
    print("=== FUN BOX ===")
    print("What would you like to try?")
    for i, (name, _) in enumerate(programs):
        print(f"{i}. {name}")
    print(f"{len(programs)}. exit")

    idx = None
    while idx == None:
        try:
            idx = int(input(">> "))
            if idx < 0 or idx > len(programs):
                idx = None
        except KeyboardInterrupt:
            exit()
        except:
            pass

    if idx == len(programs):
        exit()

    clear()
    prog = programs[idx]
    os.chdir(prog[1])
    os.system("py main.py")
    os.chdir("..")

    print(f"\n\n=== END OF '{prog[0]}' ==")
    input("Press enter to continue: ")
    clear()
