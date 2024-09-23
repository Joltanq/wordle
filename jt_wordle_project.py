import random

def decrease_and_pop(guess_dict,item_to_remove):
    for key, value in guess_dict.items():
        if key == item_to_remove:
            guess_dict[item_to_remove] = guess_dict[item_to_remove] - 1
    # creates a smaller dictionary, only bringing across items that do not have value = 0
    filtered_dict = {k :v for k,v in guess_dict.items() if v != 0}
    return filtered_dict


def score_guess(target, guess):
    # scores the guess of a user against the target word.
    # takes the target word and the guess word as parameters
    # functions returns the score as a list which represents if the letter is in the right place, in the word,or cant be found at all
    score = []
    position_of_character = 0
    guess_character_count = {}
    # creates a dictionary with letters in the target word
    # then creates a placeholder list with As
    # first remove the characters which are a given
    # then if they're in the wrong place, or there aren't any more "allocations" like t = hello, g = world
    for character in target:
        guess_character_count[character] = guess_character_count.get(character,0) +1

    for characters in range(len(target)):
        score.append("a")

    for guess_character in guess:
        if guess_character not in target:
            score[position_of_character] = 0
        elif guess_character == target[position_of_character]:
            score[position_of_character] = 2
            guess_character_count = decrease_and_pop(guess_character_count, guess_character)
        position_of_character += 1


    position = 0
    for score_position in score:
        if score_position != "a":
            pass
        elif str(guess[position]) in guess_character_count.keys():
            score[position] = 1
        else:
            score[position] = 0
        position += 1
    return score

print(score_guess("world","hello"))
print(score_guess("cheek","erred"))
#
# def read_file(FILE_NAME,list_name):
#     file = open(FILE_NAME,'r')
#     for line in file:
#         list_name.append(line.strip())
#     file.close()
#     return list_name
#
# def help_message():
# # when called, gives the user some helpful tips like what the 0, 1 and 2 means
# # explains what the rules are
#     print("This is a game of Wordle")
#     print("The aim of the game is to guess the word we've selected")
#     print("They have to be valid English words, and of the same length as the target word to count as an attempt")
#     print("Each individual character is scored as a 0,1 or 2")
#     print("0 means it does not exist in the word")
#     print("1 means it's in the word, but in the wrong spot")
#     print("2 means it's in the right spot")
#     print("Type HELP at any time to bring back this message")
#
# def check_validty(guess,target_list):
#     while True:
#         if guess in target_list:
#             return guess
#         elif guess == "help":
#             help_message()
#             guess = input("What's your best guess: ")
#         else:
#             print("That does not look like an English word")
#             guess = input("What's your best guess: ")
#
# def remaining_words(target,guess):
#     guess_character_count = {}
#     for character in guess:
#         guess_character_count[character] = guess_character_count.get(character,0) +1
#
#     for key in guess_character_count:
#         if key not in target:
#             try:
#                 ALPHABETS.remove(key)
#             except:
#                 pass
#     return ALPHABETS
#
# # Main
# ALPHABETS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# target_words = []
# all_words = []
# target_words = read_file("target_words.txt",target_words)
# all_words = read_file("all_words.txt",all_words)
# target = random.choice(target_words)
# number_of_attempts = 0
# print(target)
#
# help_message()
# print("\n")
# while number_of_attempts < 3:
#     valid_guess = check_validty(input("What's your best guess: "),all_words)
#     if len(valid_guess) != len(target):
#         print("Your guess doesn't seem to be the right length")
#     elif (target == valid_guess):
#         print("Congratulations! You won!")
#         break
#     else:
#         print(score_guess(target,valid_guess))
#         print("Try with these letters")
#         print(remaining_words(target,valid_guess))
#         print("\n")
#         number_of_attempts += 1
# else:
#     print("You ran out of attempts")
#     print("The word you were looking for was " + target)
