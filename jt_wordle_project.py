def score_guess(target, guess):
    score = [0,0,0,0,0]

    if target == guess:
        score = [2,2,2,2,2]
    print(score)

# Main
target = "hello"
guess = "world"
score_guess(target,guess)

test commit from pycharm