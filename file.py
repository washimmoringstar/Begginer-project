import random
def game():
    print(" you are playing a game")
    score = random.randint(1, 100)
    print(f" your score is {score}")
    # fetch high score from file
    with open("highscore.txt", "r") as f:
        content = f.read()
        if content != "":
            highscore = int(content)
        else:
            highscore = 0
    if score > highscore:
        # write new high score to file
        print(" you have the highest score")
        with open("highscore.txt", "w") as f:
            f.write(str(score))
            return score

game()