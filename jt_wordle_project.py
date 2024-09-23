import random

def score_guess(target, guess):
    # scores the guess of a user against the target word.
    # takes the target word and the guess word as parameters
    # functions returns the score as a list which represents if the letter is in the right place, in the word,or cant be found at all
    score = []
    position_of_character = 0

    for character in guess:
        if character not in target:
            score.append(0)
        elif character == target[position_of_character]:
            score.append(2)
        else:
            score.append(1)
        position_of_character += 1
    return score

def read_file(FILE_NAME,list_name):
    file = open(FILE_NAME,'r')
    for line in file:
        list_name.append(line.strip())
    file.close()
    return list_name

def help_message():
# when called, gives the user some helpful tips like what the 0, 1 and 2 means
# explains what the rules are
    print("This is a game of Wordle")
    print("The aim of the game is to guess the word we've selected")
    print("They have to be valid English words, and of the same length as the target word to count as an attempt")
    print("Each individual character is scored as a 0,1 or 2")
    print("0 means it does not exist in the word")
    print("1 means it's in the word, but in the wrong spot")
    print("2 means it's in the right spot")
    print("Type HELP at any time to bring back this message")

def check_validty(guess,target_list):
    while True:
        if guess in target_list:
            return guess
        elif guess == "help":
            help_message()
            guess = input("What's your best guess: ")
        else:
            print("That does not look like an English word")
            guess = input("What's your best guess: ")

# Main
target_words = []
all_words = []
target_words = read_file("target_words.txt",target_words)
all_words = read_file("all_words.txt",all_words)
target = random.choice(target_words)
number_of_attempts = 0
print(target)

help_message()
while number_of_attempts < 3:
    valid_guess = check_validty(input("What's your best guess: "),all_words)
    if len(valid_guess) != len(target):
        print("Your guess doesn't seem to be the right length")
    elif (target == valid_guess):
        print("Congratulations! You won!")
        break
    else:
        print(score_guess(target,valid_guess))
        number_of_attempts += 1
else:
    print("You ran out of attempts")
    print("The word you were looking for was " + target)
