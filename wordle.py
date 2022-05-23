import random
from messages import messages
from config import config
from colorama import Fore


wordsFile = open("./words.txt")
words = wordsFile.read().split("\n")


tries = int(config["TRIES"])
print("You have", tries, "tries")

word = random.choice(words)

guesses = 0
if config["SHOW_ANSWER"] == True:
    print("Word:", word)


def Convert(string):
    list1 = []
    list1[:0] = string
    return list1


def promptUser():
    global userWord
    userWord = input("Place your guess (" + str(guesses + 1) + "/" + str(tries) + "): ").strip().lower()
    prAns(userWord)


def addGuess():
    global guesses
    guesses += 1


def prAns(input):
    if len(input) != 5:
        print(messages['INVALID_LENGTH'])
        promptUser()
        return
    userWord1 = Convert(input)

    contains0 = word.__contains__(userWord1[0])
    contains1 = word.__contains__(userWord1[1])
    contains2 = word.__contains__(userWord1[2])
    contains3 = word.__contains__(userWord1[3])
    contains4 = word.__contains__(userWord1[4])

    is0 = word[0] == userWord1[0]
    is1 = word[1] == userWord1[1]
    is2 = word[2] == userWord1[2]
    is3 = word[3] == userWord1[3]
    is4 = word[4] == userWord1[4]

    # print(contains0, contains1, contains2, contains3, contains4)
    # print(is0, is1, is2, is3, is4)

    # there has to be a better way of doing this lmao
    global color0
    global correct0
    correct0 = False
    if contains0 and is0:
        color0 = Fore.GREEN
        correct0 = True
    elif contains0 and not is0:
        color0 = Fore.YELLOW
    else:
        color0 = Fore.RED

    global color1
    global correct1
    correct1 = False
    if contains1 and is1:
        color1 = Fore.GREEN
        correct1 = True
    elif contains1 and not is1:
        color1 = Fore.YELLOW
    else:
        color1 = Fore.RED

    global color2
    global correct2
    correct2 = False
    if contains0 and is2:
        color2 = Fore.GREEN
        correct2 = True
    elif contains2 and not is2:
        color2 = Fore.YELLOW
    else:
        color2 = Fore.RED

    global color3
    global correct3
    correct3 = False
    if contains3 and is3:
        color3 = Fore.GREEN
        correct3 = True
    elif contains3 and not is3:
        color3 = Fore.YELLOW
    else:
        color3 = Fore.RED

    global color4
    global correct4
    correct4 = False
    if contains4 and is4:
        color4 = Fore.GREEN
        correct4 = True
    elif contains4 and not is4:
        color4 = Fore.YELLOW
    else:
        color4 = Fore.RED

    print(
        color0,
        userWord1[0],
        color1,
        userWord1[1],
        color2,
        userWord1[2],
        color3,
        userWord1[3],
        color4,
        userWord1[4],
        Fore.RESET,
    )
    global isCorrect
    isCorrect = correct0 and correct1 and correct2 and correct3 and correct4
    addGuess()
    if guesses == tries and input != word:
        print("You failed!")
        print("The word was", word)
        exit()


promptUser()

while isCorrect == False:
    promptUser()
else:
    print("You did it!")
