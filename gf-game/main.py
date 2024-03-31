# events
# if you get above 100 rizz you win the game
# start at 0 rizz
# if you get below -5 rizz you get a rizztraining order
# dialogue

# catgirl rizz personality
"""
insulting people
breaking things
causing chaos
watching anime
playing with toys (plushies and action figures)
giving headpats
"""

"""
Plot:
- first meeting
- go on a dinner date (dinner vocab)
- hangman game
- piano game (like a typing game)
- busting (code)
- shopping (inventory management money game)
- did you get a rizztraining order yet??
"""
from random import randint, choice
from sys import exit


class Catgirl:
    def __init__(self) -> None:
        self.rizz = 0
        self.inv = []

    def decr_rizz(self, amt=1):
        self.rizz -= amt
        if self.rizz <= -5:
            print("You got below 5 rizz! Rizztraining order for you\n\nYOU LOST")
            exit()

    def incr_rizz(self, amt=1):
        self.rizz += amt
        # if self.rizz >= 20:
        #     print(
        #         "You got above 20 rizz! Girlfriend ACQUIRED\n\nYOU WON\n\ncredits: Coder100 (thanks for playing)"
        #     )


from choices import options, pause, clear

print(
    """Welcome to dating simulator, meet your potential girlfriend Kitty-chan!
    If you get over  20 rizz you win!
    If you get under -5 rizz you will get a rizztraining order so be careful.
    If you don't get over 20 rizz at the end of the game you also lose (you get friendzoned)."""
)

input("Press enter to begin: ")
clear()


kc = Catgirl()


# --- first meeting ---
def meeting():
    print("You: Hi.")
    options(
        "Fuck off and die, you're an insufferable prick, you don't deserve my time or attention.",
        [
            (
                "Go fuck yourself, why would your mother give birth to such a pos like you?",
                pos_choice,
            ),
            ("I want to fuck you", horny_choice),
        ],
    )


def pos_choice():
    kc.incr_rizz()
    if randint(0, 1):
        options(
            "Go fuck yourself, your mother birthed you an ungrateful cunt",
            [
                ("Go on a date with me", end_meeting),
                ("Fuck you, I'll see you soon", end_meeting),
            ],
        )
    else:
        options(
            "How rude! Don't worry, I'll give you a headpat to make you feel better!",
            [("Go on a date with me", end_meeting)],
        )


def horny_choice():
    kc.decr_rizz()
    if randint(0, 1):
        options(
            "Go to horny jail you gooner",
            [
                ("How about a date first?", end_meeting),
                ("Please just give me a chance", end_meeting),
            ],
        )
    else:
        options("I'm just a catgirl nya...", [("Go on a date with me.", end_meeting)])


def end_meeting():
    if kc.rizz < 0:
        print("Kitty-chan: Nya fine I always wanted to eat an overpriced steak anyways")
    else:
        print("Kitty-chan: Well free food isn't bad I guess")
    print("End of first meeting, your rizz level:", kc.rizz)
    pause()


meeting()


# dinner date
def dinner_date():
    print("You have successfully obtained a date at big steak lugar")
    print("You must maximize rizz by ordering the correct items!")
    options(
        "¿En qué puede servirle usted?",
        [
            ("Quiero un vaso de agua, por favor", spanish_water),
            ("What are you saying", no_spanish_water),
        ],
        name="Waiter",
    )


def no_spanish_water():
    kc.decr_rizz()
    options(
        "He's clearly speaking Fr*nch how do you not know how to speak Fr*nch?? Baka",
        [
            ("Erm, actually, he's speaking in spanish", nerd_spanish),
            ("Fuck you then go talk to him yourself", rude_spanish),
        ],
    )


def nerd_spanish():
    kc.decr_rizz()
    options(
        "Nerd",
        [
            ("Erm, actually, I'm just a monolingual gigachad", nerd_reply),
            ("What do you want for dinner?", order_steak_pre),
        ],
    )


def nerd_reply():
    kc.decr_rizz()
    options(
        "I think you mean monolingual beta",
        [("Okay, well what do you want for dinner?", order_steak_pre)],
    )


def rude_spanish():
    kc.incr_rizz()
    options(
        "I would but I only know how to say je ne peux pas parler espagnol",
        [
            ("I didn't know you were a ployglot sigma!", nerd_reply),
            ("Well what do you want for dinner?", order_steak_pre),
        ],
    )


def spanish_water():
    kc.incr_rizz()
    options(
        "Wow I didn't know you spoke Fr*nch that's so hot",
        [
            ("はい、かっこいいヒトです！", ew_japanese),
            ("That's spanish you idiot", not_spanish),
        ],
    )


def ew_japanese():
    kc.decr_rizz()
    options(
        "Okay nevermind you are a baka just using google translate",
        [("Whatever, what do you want for dinner?", order_steak_pre)],
    )


def not_spanish():
    kc.incr_rizz()
    options(
        "Okay, well I can speak some spanish too: joder eres un pendejo",
        [("Fuck you. What do you want for dinner?", order_steak_pre)],
    )


def order_steak_pre():
    options(
        "(thinking for a while) I think want steak medium rare",
        [
            ("Finally you came to a decision", lambda: order_game(True)),
            ("I think I'll get a hamburger then", lambda: order_game(False)),
        ],
    )


def order_game(rizzed: bool = False):
    if rizzed:
        kc.incr_rizz()
    options(
        "¿Qué quieren comer?",
        [
            (
                "Un típo de carne muy ricísima porque ha quemado hasta no hay nada que nos queda",
                worst_food_opt,
            ),
            (
                "Un típo de fideo muy larga de italia que podemos comer con un tenedor",
                wrong_food_opt,
            ),
            (
                "Un típo de carne que está entre dos pedazos de pan y un típo de carne como un bistec",
                lambda: correct_food_opt(True),
            ),
            (
                "I want a steak and a hamburger please",
                lambda: correct_food_opt(False),
            ),
            ("I don't understand you.", recursive_rizz_removal),
        ],
        name="Waiter",
    )


def worst_food_opt():
    kc.decr_rizz()
    options(
        "Esta opción es muy asquerosa, ¿quién quiere comer ese? ¿Está burlándome? ¿Señorita, por qué decide estar contigo?",
        [
            ("Le odio a la señorita, por favor, démelo", worst_food_resp),
        ],
        name="Waiter",
    )


def wrong_food_opt():
    options(
        "Está bien. En seguida. Aquí tienen ustedes",
        [("Gracias", wrong_food_resp)],
        name="Waiter",
    )


def correct_food_opt(rizzed: bool):
    if rizzed:
        kc.incr_rizz()
    else:
        kc.decr_rizz()

    options(
        "Está bien señor. En seguida. Aquí lo tienen ustedes.",
        [
            ("Gracias", lambda: correct_food_resp(True)),
            ("Thank you!", lambda: correct_food_resp(False)),
        ],
        name="Waiter",
    )


def recursive_rizz_removal():
    kc.decr_rizz()
    options("No te puedo entender tampoco.", [("Okay", order_game)], name="Waiter")


def worst_food_resp():
    kc.decr_rizz()
    options(
        """What is this steak.
Well, I've had better.
This restaurant sucks why would they give you a burnt steak like this, I'm pretty sure this is like 60% percent ash. How nya~ty of them UwU
We're only going to tip them 60% you know this is unacceptable""",
        [("Huh, my translation app must have been broken", end_dinner_date)],
    )


def wrong_food_resp():
    kc.decr_rizz()
    options(
        """Why did you order spaghetti what the heck are you doing?
I wanted a steak because I'm allergic to spaghetti nya
Are you trying to kill me nya""",
        [
            ("Huh, my translation app must have been broken", end_dinner_date),
            ("I think this was for another table", lying_wrong_resp),
        ],
    )


def correct_food_resp(rizzed: bool):
    if rizzed:
        kc.incr_rizz()

    kc.incr_rizz()
    options("Wow this is an amazing steak! Good job!", [("Enjoy!", end_dinner_date)])


def lying_wrong_resp():
    kc.decr_rizz(2)
    options(
        "You idiot we are the only ones here how could they possibly have messed up the order",
        [("Oops", end_dinner_date)],
    )


def end_dinner_date():
    print("End of dinner date, your rizz level:", kc.rizz)
    pause()


dinner_date()


# hangman game
def hangman_game():
    print(
        "Kitty-chan wants to play hangman with you! You must maximize rizz by winning the game."
    )
    pause()

    words = [
        "cat",
        "kitty",
        "the quick brown fox jumps over the lazy dog",
        "rizz",
        "jason ding",
        "ap biology",
        "bloodbath jumpscare",
        "wordle",
        "baka",
    ]

    hangman_pic = [
        R" O  ",
        R"/|\ ",
        R" |  ",
        R"/ \ ",
    ]

    top = """
+------+
|      $""".strip()
    middle = """|     """
    bottom = """
+---------""".strip()

    word = choice(words)
    guessed = set()
    wrong = 0
    max_wrong = len(hangman_pic)

    def print_guess():
        won = True
        print("Word: ", end="")
        for c in word:
            if c == " ":
                print(" ", end="")
                continue

            if c in guessed:
                print(c, end="")
            else:
                won = False
                print("_", end="")
        print()
        return won

    def print_man():
        print(top)
        for i in hangman_pic[0:wrong]:
            print(middle + i)
        for i in range(2 + max_wrong - wrong):
            print(middle)
        print(bottom)
        print()

    def get_char():
        char = None
        while char == None:
            try:
                char = input("Enter a letter: ")
                if len(char) != 1 or not char.isalpha() or char in guessed:
                    char = None
            except KeyboardInterrupt:
                exit()
            except:
                pass
        return char

    while wrong <= max_wrong:
        clear()
        print_man()
        won = print_guess()

        if won:
            return True

        c = get_char()
        guessed.add(c)
        if c not in word:
            wrong += 1

    print("The word was", word)
    return False


def hangman_plot():
    won_hangman = hangman_game()
    if won_hangman:
        print("Kitty-chan: Good job!!")
        kc.incr_rizz(3)
    else:
        print("Kitty-chan: loser")
        kc.decr_rizz(3)

    print("End of hangman game. Your rizz level:", kc.rizz)
    pause()


hangman_plot()


# piano performance date
def piano_performance_date():
    print("Kitty-chan heard you can play piano!! She wants you to perform for her.")
    options(
        "Nya~ I heard you are really good with the fingers, you really know how to touch a piano",
        [
            ("What the fuck is wrong with you", piano_insult_resp),
            ("Yes I am really good at fingering passages", piano_horny_resp),
        ],
    )


def piano_insult_resp():
    kc.incr_rizz()
    options(
        "Nya~ I just want you to play piano for me UwU",
        [
            ("Okay", lambda: piano_pre(False)),
            ("Do not say that ever again", lambda: piano_pre(True)),
        ],
    )


def piano_horny_resp():
    kc.incr_rizz()
    options(
        "Nya~ I don't believe you, show me OwO",
        [
            ("I'll be sure to caress the piano", lambda: piano_pre(True)),
            ("Of course", lambda: piano_pre(True)),
        ],
    )


def piano_pre(rizzed: bool):
    if rizzed:
        kc.incr_rizz()

    num = randint(0, 2)
    if num == 0:
        text = "Play some Chopin for me nya~"
    elif num == 1:
        text = "Play rush E OwO"
    else:
        text = "Play some anime music I love アニメ!"

    options(
        text,
        [
            ("I don't know how to play that", piano_cantplay),
            ("I can play that", lambda: piano_game(num)),
        ],
    )


def piano_cantplay():
    kc.decr_rizz()
    options(
        "Kitty-chan: Then play heart and soul, everyone can play heart and soul",
        [("Okay, fine", lambda: piano_game(3))],
    )


def piano_game(idx):
    from difflib import SequenceMatcher

    # 0 == hanon (aka chopin)
    # 1 == rush E
    # 2 == anime
    # 3 == h&s
    chromatic = "awsedftgyhujk"
    songs = [
        ("'Chopin' aka Hanon", "adfghgfdsfghjhgfdghjkjhgk"),
        ("Rush E", "dddddddddfdedhklllllkjlkkkkkjhkjjjjtjg"),
        ("Attack on Titan", "jghtgdtsjghtgtds"),
        ("Heart and Soul", "kkkkjhjklkkkkjhjklkkkkjhjkl"),
    ]

    print("To play the piano, you must type on your keyboard.")
    print(
        "Obviously the best musicians are supposed to play it as accurately as possible."
    )
    print(
        "Try out a chromatic scale on your keyboard! Type the following (and then press enter):"
    )

    def judge_piece(piece):
        print(">>", piece)
        text = input(">> ")

        seq = SequenceMatcher(None, piece, text)
        ratio = seq.ratio()

        score = round(ratio * 10)
        print("Your score:", f"{score}/10")
        return score

    judge_piece(chromatic)

    pause()
    print("Kitty-chan: Please play", songs[idx][0], "nya~!")
    score = judge_piece(songs[idx][1])
    if score < 5:
        print(
            "Kitty-chan: That was",
            "absolutely terrible." if score < 3 else "listenable I guess.",
            "Please don't play again",
        )
        kc.decr_rizz()
    else:
        print("Yay!! Good job!!")
        kc.incr_rizz(3)

    pause()
    end_piano_performance_date()


def end_piano_performance_date():
    print("End of piano recital. Your rizz level:", kc.rizz)
    pause()


piano_performance_date()


# code busting
def code_busting():
    options(
        "I heard you like busting nya~",
        [
            ("Yeah, busting makes me feel good", busting_sus),
            ("What?", busting_confused),
        ],
    )


def busting_sus():
    options(
        "Well I have caesar cipher I bet you can't solve nya~",
        [
            ("I bet I can bust it", busting_game),
        ],
    )


def busting_confused():
    options(
        "Like code busters!! I have a caesar cipher I bet you can't solve nya~",
        [
            ("Please do not ever refer it as busting again", busting_game),
            ("I guess I am pretty good at busting", busting_game),
        ],
    )


def busting_game():
    texts = [
        "i hope you have a nice day",
        "the quick brown fox jumps over the lazy dog",
        "to be or not to be that is the question",
        "where have you been all this time",
        "i really like python python is a top language",
        "busting makes me feel good",
        "come get a hunny bun",
    ]

    def caesar(text: str, shift: int):
        result = ""

        for c in text:
            if c.isalpha():
                result += chr((ord(c) + shift - ord("a")) % 26 + ord("a"))
            else:
                result += c

        return result

    def get_num():
        num = None
        while num == None:
            try:
                num = int(input("Your guess: "))
                if num < 1 or num > 13:
                    num = None
            except KeyboardInterrupt:
                exit()
            except:
                pass

        return num

    print("You must guess how many shifts left it took to encrypt the cipher!")
    print("For example, 1 shift left turns A into B.")
    print("The number will be between 1-13.")

    text = choice(texts)
    shift = randint(1, 13)

    encrypted = caesar(text, shift)

    guesses = 0
    guess = -1
    while guess != shift:
        guesses += 1
        pause()
        print("Encoded text:")
        print(encrypted)
        guess = get_num()
        print()
        print("Your guess decodes to:")
        print(caesar(encrypted, 26 - guess))

    print()
    print("You got it in", guesses, "try/tries!")
    pause()

    if guesses < 3:
        kc.incr_rizz(2)
        options(
            "Kitty-chan: Wow you are so good at busting!",
            [
                (
                    "I'm quite the buster if I do say so myself",
                    lambda: end_code_busting(True),
                ),
                ("Thanks!", lambda: end_code_busting(False)),
            ],
        )
    else:
        kc.decr_rizz()
        options(
            "Kitty-chan: see told you you couldn't do it",
            [
                ("Who even made that cipher?", lambda: end_code_busting(False)),
                ("Yeah I think I'll stick to edging", lambda: end_code_busting(False)),
            ],
        )


def end_code_busting(rizzed: bool):
    if rizzed:
        kc.incr_rizz()
    print("End of code busting. Your rizz level:", kc.rizz)
    pause()


code_busting()


# shopping game
def shopping_start():
    options(
        "I want to go shopping nya~",
        [
            ("Okay, let's go", shopping_pos_resp),
            ("I'm so tired... I don't want to", shopping_neg_resp),
        ],
    )


def shopping_pos_resp():
    options("How about the clash royale gemshop nya~", [("Sounds good", shopping_game)])


def shopping_neg_resp():
    kc.decr_rizz()
    options("nya~ Pwease UwU", [("Okay fine", shopping_game)])


def shopping_game():
    print(
        """You are in the clash royale gemshop! You must buy the items that get you to more than 50 rizz with $100!
All items you choose are immediately purchased and cannot be returned."""
    )

    pause()

    # name, price, rizz
    items = [
        ("flaming bow", 5, 1),
        ("red dress", 50, 20),
        ("blue dress", 50, 20),
        ("princess yawn emote", 40, 17),
        ("heeheeheehaw emote", 40, 17),
        ("new laptop", 60, 30),
        ("new phone", 20, 15),
        ("rubik's cube", 15, 13),
        ("energy drink", 6, 2),
        ("bowtie", 11, 8),
        ("new suit", 45, 19),
        ("AP Psych prep book", 30, 7),
        ("TI-84 Calculator", 35, 13),
        ("new apple iphone", 25, 16),
    ]

    money = 100
    rizz = 0
    bought = set()

    # 2 extra padding between name and price
    padding = 2 + max([len(name) for name, _, _ in items])

    def print_shop():
        print(f"idx name{' ' * (padding - 4)}price  rizz")
        for i, (name, price, rizz) in enumerate(items):
            if i in bought:
                print()
                continue

            ## index
            # len('idx') == 3, -1 for '.'
            print(" " * (2 - len(str(i))), end="")
            print(i, end=". ")

            ## name
            print(name, end=" " * (padding - len(name)))

            ## price
            # len('price  ') == 7
            print(f"${price}", end=" " * (7 - len(f"${price}")))
            print(rizz)

    def can_buy():
        # global money
        return any(
            [
                price <= money and i not in bought
                for i, (_, price, _) in enumerate(items)
            ]
        )

    def get_idx():
        num = None
        while num == None:
            try:
                num = int(input("Enter idx you would like to buy: "))
                if (
                    num < 0
                    or num >= len(items)
                    or num in bought
                    or money < items[num][1]
                ):
                    num = None
            except KeyboardInterrupt:
                exit()
            except:
                pass
        return num

    while can_buy():
        print_shop()
        print(f"Your budget: ${money}", end="    ")
        print(f"Your rizz:", rizz)
        num = get_idx()
        bought.add(num)
        money -= items[num][1]
        rizz += items[num][2]

        clear()

        print(
            "Bought", items[num][0], f"(-${items[num][1]})", f"(+{items[num][2]} rizz)"
        )
        pause()

    print("final rizz:", rizz)
    print("remaining money:", money)

    if rizz < 50:
        kc.decr_rizz(2)
        print("You failed to get 50 items worth of rizz.")
        options(
            "Your tastes in shopping suck nya~",
            [
                ("Says you", shop_loss_bad_resp),
                ("That's too bad", shop_loss_ok_resp),
            ],
        )
    else:
        rizz_obt = round((rizz + money) / 15)
        print("You successfully bought 50 items worth of rizz!")
        print("score:", rizz_obt)
        kc.incr_rizz(rizz_obt)
        options(
            "Yay!! I love shopping with you! <3",
            [
                ("Me too!", shop_win_good_resp),
                ("That was so boring", shop_win_bad_resp),
            ],
        )


def shop_loss_bad_resp():
    kc.decr_rizz()
    options(
        "Rude",
        [
            ("Sorry", lambda: end_shopping(True)),
            (
                "I don't see you with any money to buy anything",
                lambda: end_shopping(False),
            ),
        ],
    )


def shop_loss_ok_resp():
    options(
        "I'm going to need to teach you how to properly be stylish nya~",
        [
            ("Yes please do", lambda: end_shopping(True)),
            (
                "No, I think my style is fine, it's a you problem",
                lambda: end_shopping(False),
            ),
        ],
    )


def shop_win_good_resp():
    kc.incr_rizz()
    options(
        "We should shop again sometime!!",
        [("Yes", lambda: end_shopping(True)), ("No", lambda: end_shopping(False))],
    )


def shop_win_bad_resp():
    kc.decr_rizz()
    options(
        "Nya~~ you are no fun",
        [
            ("Yeah, I know", lambda: end_shopping(False)),
            ("No I just don't like shopping with you", lambda: end_shopping(False)),
        ],
    )


def end_shopping(rizzed: bool):
    if rizzed:
        kc.incr_rizz()
    else:
        kc.decr_rizz()

    print("End of shopping game. Your rizz:", kc.rizz)

    if kc.rizz >= 20:
        print("You have obtained enough rizz! You got yourself a girlfriend! Yay!")
        print("YOU WON THE GAME!!")
    else:
        print("You did not get enough rizz.")
        print("Kitty-chan: Sowwy I just see you as a friend UwU")
        print("YOU LOST")

    print("  Thanks for playing!")
    print("    - Coder100")


shopping_start()
