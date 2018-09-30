# Python implementation of perudo https://en.wikipedia.org/wiki/Dudo

import random as rdm

def perudo():

    # initialise game
    p1DiceN = 5
    p2DiceN = 5
    gameDone = False
    round = 0

    print("Welcome to perudo.\n"
          "To see the rules visit: https://en.wikipedia.org/wiki/Dudo\n"
          "To call the previous bet type 'call'\n"
          "To bet four twos type 'bet 4 2'\n")

    while gameDone == False:

        # initialise round
        turnDone = False

        d1 = rdm.randint(1, 6)
        d2 = rdm.randint(1, 6)
        d3 = rdm.randint(1, 6)
        d4 = rdm.randint(1, 6)
        d5 = rdm.randint(1, 6)
        c1 = rdm.randint(1, 6)
        c2 = rdm.randint(1, 6)
        c3 = rdm.randint(1, 6)
        c4 = rdm.randint(1, 6)
        c5 = rdm.randint(1, 6)

        p1Dice = [d1, d2, d3, d4, d5]
        p2Dice = [c1, c2, c3, c4, c5]

        for i in range(p1DiceN,5):
            p1Dice.pop(0)

        for i in range(p2DiceN,5):
            p2Dice.pop(0)

        round += 1
        print('Round {0}. Your dice are:\n{1}\n'.format(round,p1Dice))

        while turnDone == False:

            whatDo = input('What do you want to do?')

            if whatDo == 'call':
                print('You called, all dice are revealed')
                print('Your dice are:\n{0}'.format(p1Dice))
                print('Opponent''s dice are:\n{0}'.format(p2Dice))
                num = 0
                point = 0
                for i in range(0, p1DiceN):
                    if (p1Dice[point] == currBet[1] or p1Dice[point] == 1):
                        num += 1
                    point += 1

                point = 0
                for i in range(0, p2DiceN):
                    if (p2Dice[point] == currBet[1] or p2Dice[point] == 1):
                        num += 1
                    point += 1
                
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
                    print('Your dice are:\n{0}'.format(p1Dice))
                    print('Opponent''s dice are:\n{0}'.format(p2Dice))
                    num = 0
                    point = 0
                    for i in range(0, p1DiceN):
                        if (p1Dice[point] == currBet[1] or p1Dice[point] == 1):
                            num += 1
                        point += 1

                    point = 0
                    for i in range(0, p2DiceN):
                        if (p2Dice[point] == currBet[1] or p2Dice[point] == 1):
                            num += 1
                        point += 1
                    print('There are {0} {1}s!'.format(num,currBet[1]))
                    if num < currBet[0]:
                        print('You lose a die')
                        p1DiceN -= 1
                    else:
                        print('Computer loses a dice')
                        p2DiceN -= 1
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




