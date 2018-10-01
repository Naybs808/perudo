# Python implementation of perudo https://en.wikipedia.org/wiki/Dudo

import random as rdm

def Basic_expected_strat(comp_dice, Unknown, amount_bet, face_value, Known):
    """This AI strategy follows a basic expected value estimation to determine if the computer should call or bet.
    It uses an estimation that 1/3 of the opponents dice are of the value being bet.
    Assume the human player starts the betting... and they bet that there are x dice of value y.

    Let K(y) be the number of dice in the computers hand with the value y, and U be the number of unknown dice.
    Then E(y), the expected number of dice with value y, is ~ K(y) + U/3
    Let S be the set of values taken by the computers hand.

    1. The AI calls if the expected value: E(y) < B, where B is the number of dice bet

    2. If E(y) > K(y) + U/3, the AI chooses to bet X of Y, such that

    i. Y is chosen by: Y = max(mode(S)), the most common value seen in the computers hand
        (Note: if |mode(S)| >1, choose the highest), and X is chosen to maximise E(Y),
        under the constraint that E(Y)< K(Y) + U/3

    iii. if no bet exists above the players bet, which the computer evaluates to have E(Y)< K(Y) + U/3,
    for some value Y, then the AI calls.
    """

    ones = 0
    twos = 0
    threes = 0
    fours = 0
    fives = 0
    sixes = 0

    for k in range(0,Known):
        if comp_dice[k]==1:
            ones+=1
            twos+=1
            threes+=1
            fours+=1
            fives+=1
            sixes+=1
        if comp_dice[k]==2:
            twos+=1
        if comp_dice[k]==3:
            threes+=1
        if comp_dice[k]==4:
            fours+=1
        if comp_dice[k]==5:
            fives+=1
        if comp_dice[k]==6:
            sixes+=1

    array = [ones, twos, threes, fours, fives, sixes]

    # AI thinks player expected value is E_y
    E_y = array[face_value-1]+(Unknown/3)

    if E_y < amount_bet:
        return False

    mode = 0
    value = 0
    for i in range(0,6):
        if array[i]>=mode:
            mode = array[i]
            value = i
    value +=1

    # AI thinks its highest expected value is  E_Y,
    E_Y = mode + (Unknown/3)


    X=0
    while (X+(Unknown/3)) < E_Y:
        X+=1

    X+=1

    if X>amount_bet or ((mode>face_value) and X==amount_bet):
        bet = [X, value]
        return bet
    else:
        return False



def perudo():

    # initialise game
    playerDiceN = 5
    compDiceN = 5

    gameDone = False
    round = 0

    print("Welcome to perudo.\n"
          "To see the rules visit: https://en.wikipedia.org/wiki/Dudo\n"
          "To call the previous bet type 'call'\n"
          "To bet four twos type 'bet 4 2'\n"
          )

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
        playerDice = [d1, d2, d3, d4, d5]
        compDice = [c1, c2, c3, c4, c5]

        for i in range(playerDiceN,5):
            playerDice.pop(0)

        for i in range(compDiceN,5):
            compDice.pop(0)

        round += 1
        print('Round {0}. Your dice are:\n{1}\n'.format(round,playerDice))

        while turnDone == False:

            whatDo = input('What do you want to do?')

            if whatDo == 'call':
                print('You called, all dice are revealed')
                print('Your dice are:\n{0}'.format(playerDice))
                print('Opponent''s dice are:\n{0}'.format(compDice))
                num = 0
                point = 0
                for i in range(0, playerDiceN):
                    if (playerDice[point] == currBet[1] or playerDice[point] == 1):
                        num += 1
                    point += 1

                point = 0
                for i in range(0, compDiceN):
                    if (compDice[point] == currBet[1] or compDice[point] == 1):
                        num += 1
                    point += 1
                
                print('There are {0} {1}s!\n'.format(num, currBet[1]))
                if num < currBet[0]:
                    print('Your opponent loses a die')
                    compDiceN -= 1
                else:
                    print('You lose a die')
                    playerDiceN -= 1
                turnDone = True

            if whatDo.startswith('bet'):
                tempLst = whatDo.split()
                currBet = [int(tempLst[1]),int(tempLst[2])]
                print('Your bet is {0} {1}\n'.format(currBet[0],currBet[1]))


                x = Basic_expected_strat(compDice, playerDiceN, currBet[0], currBet[1], compDiceN)

                if x == False:
                    print('Your opponent calls')
                    print('Your dice are:\n{0}'.format(playerDice))
                    print('Opponent''s dice are:\n{0}'.format(compDice))
                    num = 0
                    point = 0
                    for i in range(0, playerDiceN):
                        if (playerDice[point] == currBet[1] or playerDice[point] == 1):
                            num += 1
                        point += 1

                    point = 0
                    for i in range(0, compDiceN):
                        if (compDice[point] == currBet[1] or compDice[point] == 1):
                            num += 1
                        point += 1
                    print('There are {0} {1}s!'.format(num,currBet[1]))
                    if num < currBet[0]:
                        print('You lose a die')
                        playerDiceN -= 1
                    else:
                        print('Computer loses a dice')
                        compDiceN -= 1
                    turnDone = True

                else:
                    bet = Basic_expected_strat(compDice, playerDiceN, currBet[0], currBet[1], compDiceN)
                    currBet[0]=bet[0]
                    currBet[1]=bet[1]

                    print('Your opponent bets {0} {1}'.format(currBet[0],currBet[1]))

                pass

        if playerDiceN == 0 or compDiceN == 0:
            gameDone = True

if __name__ == "__main__":
    game = perudo()




