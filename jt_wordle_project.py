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


# Main
target_words = []
all_words = []
target_words = read_file("target_words.txt",target_words)
all_words = read_file("all_words.txt",all_words)
target = "world"
guess = "world"
print(score_guess(target,guess))