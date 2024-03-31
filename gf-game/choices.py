from typing import Callable
import os
import time
from sys import exit


def options(
    topic: str, choices: list[tuple[str, Callable[[], None]]], name="Kitty-chan"
):
    print(f"{name}:", topic)
    print()

    for i, (choice, _) in enumerate(choices):
        print(f"{i}: {choice}")

    num = None
    while num == None:
        try:
            num = int(input("Your choice: "))
            if num < 0 or num >= len(choices):
                num = None
        except KeyboardInterrupt:
            exit()
        except:
            pass

    print("You:", choices[num][0])
    time.sleep(1)
    clear()
    choices[num][1]()


def clear():
    os.system("cls" if os.name == "nt" else "clear")


def pause():
    """Pause and clear terminal"""
    input("Press enter to continue: ")
    clear()
