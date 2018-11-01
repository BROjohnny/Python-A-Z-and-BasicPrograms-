import random

cash = 2000
def get_winning_numbers():
    winningNumbersset = set()
    while len(winningNumbersset) < 5 :
        winningNumbersset.add(random.randint(1, 99))
    return winningNumbersset

def customerTicketNumbers() :
    global cash
    cash -= 50
    customerNumbersSet = set()
    customerNumbers = input("Enther your lucky tickt numbers here [separate using commas & 5 numbers only]")
    customerNumbersList = customerNumbers.split(',')
    for i in customerNumbersList:
        customerNumbersSet.add(int(i))
    return customerNumbersSet

def getresult(winningNumbersset, customerNumbersSet) :
    numbersMached = customerNumbersSet.intersection(winningNumbersset)
    print("winning numbers are {}".format(winningNumbersset))
    prizeset = [0, 0, 0, 400, 2000, 40000, 100000000]
    prize = prizeset[len(numbersMached)]
    if prize > 0:
        global cash
        cash += prize
        return 'you won {} much prize and you mached {} numbers'.format(prize , len(numbersMached))
    else:
        return 'May be you win next time, TRY AGAIN!'

def runthagame():
    while True:
        print("Welcome to the online lottery app,Lest start the game! \n")
        getresponse = input("do you want [c]heck balance , [s]tart the game or [q]uite ?")
        if getresponse == 'c' :
            global cash
            print(cash)
        elif getresponse == 's' :
            a = get_winning_numbers()
            b = customerTicketNumbers()
            print(getresult(a, b))

        elif getresponse == 'q' :
            break
        else :
            print("Invalied response.")

runthagame()