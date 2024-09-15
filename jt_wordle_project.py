def score_guess(target, guess):
    score = []

    for character in guess:
        if character in target:
            score.append("1")
        else:
            score.append("0")
    return score

# Main
target = "hello"
guess = "world"
print(score_guess(target,guess))


