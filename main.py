# Python implementation of perudo https://en.wikipedia.org/wiki/Dudo

import random as rdm

def perudo():

    # initialise game
    gameDone = False
    p1DiceN = 5
    p2DiceN = 5
    round = 0

    print("Welcome to perudo.\n"
          "To see the rules visit: https://en.wikipedia.org/wiki/Dudo\n"
          "To call the previous bet type 'call'\n"
          "To bet four twos type 'bet 4 2'\n")

    while gameDone == False:

        # initialise round
        turnDone = False
        p1Dice = rdm.sample(range(1,6),p1DiceN)
        p2Dice = rdm.sample(range(1,6),p2DiceN)
        round += 1
        print('Round {0}. Your dice are:\n{1}\n'.format(round,p1Dice))

        while turnDone == False:

            whatDo = input('What do you want to do?')

            if whatDo == 'call':
                print('Your opponent''s dice are:\n{0}'.format(p2Dice))
                num = p1Dice.count(currBet[1]) + p2Dice.count(currBet[1])
                print('There are {0} {1}s!\n'.format(num, currBet[1]))
                if num < currBet[0]:
                    print('Your opponent loses a die')
                    p2DiceN -= 1
                else:
                    print('You lose a die')
                    p1DiceN -= 1
                turnDone = True

            if whatDo.startswith('bet'):
                tempLst = whatDo.split()
                currBet = [int(tempLst[1]),int(tempLst[2])]
                print('Your bet is {0} {1}\n'.format(currBet[0],currBet[1]))
                move = rdm.uniform(0,1)
                print(move)
                if move < 0.2:
                    print('Your opponent calls')
                    num = p1Dice.count(currBet[1]) + p2Dice.count(currBet[1])
                    print('There are {0} {1}s!'.format(num,currBet[1]))
                    if num < currBet[0]:
                        print('Your opponent loses a die')
                        p2DiceN -= 1
                    else:
                        print('You lose a die')
                        p1DiceN -= 1
                    turnDone = True
                else:
                    if currBet[1] != 6:
                        if rdm.randint(0,1):
                            currBet[1] += rdm.randint(1,6-currBet[1])
                        else:
                            currBet[0] += 1
                    else:
                        currBet[0] += 1
                    print('Your opponent bets {0} {1}'.format(currBet[0],currBet[1]))

                pass

        if p1DiceN == 0 or p2DiceN == 0:
            gameDone = True

if __name__ == "__main__":
    game = perudo()