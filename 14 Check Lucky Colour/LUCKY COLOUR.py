import random

def guesscolor():
    colours = ['red' , 'blue' , 'yellow' , 'green' , 'orange' , 'purple' , 'white']
    luckyColor = random.choice(colours)

    for i in range(3):
        print("these are lucky colours {}".format(colours))
        guess = input("Enter lucky colour you think[you have 3 chance to guess]")

        if luckyColor != guess:
            colours.remove(guess)
            print("seems like {} is not a lucky colour[chance {}]".format(guess,i+1))
        else:
            break

    if luckyColor == guess:
        print("this is lucky day to you,thats why these colours match,do everything using this colour today")
    else:
        print("this is lucky colour {} , TRY AGAIN! MAY BE NEXT TIME YOU GOT LUCKY COLOUR".format(luckyColor))
guesscolor()