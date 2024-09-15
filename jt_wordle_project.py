def score_guess(target, guess):
    score = []
    i = 0

    for character in guess:
        if character not in target:
            score.append("0")
        elif character == target[i]:
            score.append("2")
        else:
            score.append("1")
        i += 1
    return score

# Main
target = "hello"
guess = "world"
print(score_guess(target,guess))


