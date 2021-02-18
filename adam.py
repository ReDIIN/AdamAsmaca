import random

pics = ["""
    +---+
    |   |
        |
        |
        |
        |
        |
        |
==========""", """

    +---+
    |   |
    0   |
        |
        |
        |
        |
        |
==========""", """

    +---+
    |   |
    0   |
    |   |
        |
        |
        |
        |
==========""", """

    +---+
    |   |
    0   |
    |   |
   /|   |
        |
        |
        |
==========""", """

    +---+
    |   |
    0   |
    |   |
   /|\  |
        |
        |
        |
==========""", """

    +---+
    |   |
    0   |
    |   |
   /|\  |
   /    |
        |
        |
==========""", """

    +---+
    |   |
    0   |
    |   |
   /|\  |
   / \  |
        |
        |
=========="""]

while True:
    print(("-" * 30) + "\nÇocuk Adam\n" + ("-" * 30))

    word = random.choice(["adam", "python", "terminal", "mrrobot" "çocuk", "adam", "root", "hacker", ])
    step = 0
    letters = []

    while True:
        print(pics[step])

        for i, char in enumerate(word):
            print(char if i in letters else "_"),

        answer = input("\nCevap: ")

        if answer == word:
            print("Kazandınız!\n\n")
            break
        else:
            while True:
                rand = random.randint(0, len(word))
                if not rand in letters:
                    letters.append(rand)
                    break
            step += 1

        if step >= len(pics):
            print("Kaybettiniz!\n\n")
            break
