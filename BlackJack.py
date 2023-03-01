#create variables and list of cards#
import random
numbers = ["1", "2", "3", "4", "5", "6", "7"]
figures = ["j", "q", "k"]
cards = numbers + figures
player_cards = []
dealer_cards = []
totalPoints = 0
totalDealPoints = 0
turn_finished = False
dealer_turn = False
pick_number = 0
replay = True

while replay == True:
    print("\nWelcome to BlackJack!")
    print("\nLet's see your fortune!")
    print("\ntype enter to begin")
    input()

    def addValue(new_card):
        global totalPoints
        global numbers
        if new_card in numbers:
            totalPoints += int(new_card)
        else:
            totalPoints += 10

    def addValueD(newDealercard):
        global totalDealPoints
        global numbers
        if newDealercard in numbers:
            totalDealPoints += int(newDealercard)
        else:
            totalDealPoints += 10

    #player turn#
    new_card = random.choice(cards)
    player_cards.append(new_card)
    addValue(new_card)
    print("Your first card is ", player_cards, "!")

    while turn_finished == False:
        ans = input("\npick another card? y/n ")
        if ans == "y":
            new_card = random.choice(cards)
            player_cards.append(new_card)
            addValue(new_card)
            print("your hand is updated: ", player_cards)
            if totalPoints > 21:
                print("Burst!!!")
                turn_finished = True
                break
            elif totalPoints == 21:
                print("BlackJack!!!")
                turn_finished = True
                break
            else:
                continue
        else:
            print("\nhere's your hand ", player_cards)
            print("the sum is ", totalPoints)
            turn_finished = True

    #dealer turn#

    def randomic(par):
        global dealer_turn
        global pick_number
        pick_number = random.randrange(1, 10)
        if pick_number >= par:
            dealer_turn = True
        else:
            dealer_turn = False

    print("\nNow the dealer's turn!")
    print("\nPress enter to continue")
    input()

    turn_finished = False
    newDealercard = random.choice(cards)
    dealer_cards.append(newDealercard)
    addValueD(newDealercard)
    print("The first dealer card is ", dealer_cards, "!")

    print("\nPress enter to continue")
    input()

    newDealercard = random.choice(cards)
    dealer_cards.append(newDealercard)
    addValueD(newDealercard)
    print("The dealer draw another card: ", dealer_cards)

    print("\nPress enter to continue")
    input()

    while turn_finished == False:
        if totalDealPoints <= 10:
            newDealercard = random.choice(cards)
            dealer_cards.append(newDealercard)
            addValueD(newDealercard)
            print("The dealer draw another card: ", dealer_cards)
            print("\nPress enter to continue")
            input()
            if totalDealPoints > 21:
                print("Burst!!!")
                turn_finished = True
                break
            elif totalDealPoints == 21:
                print("BlackJack!!!")
                turn_finished = True
                break
            else:
                continue
        elif totalDealPoints >= 10 and totalDealPoints <= 15:
            randomic(8)
            if dealer_turn == False:
                newDealercard = random.choice(cards)
                dealer_cards.append(newDealercard)
                addValueD(newDealercard)
                print("The dealer draw another card: ", dealer_cards)
                print("\nPress enter to continue")
                input()
                if totalDealPoints > 21:
                    print("Burst!!!")
                    turn_finished = True
                    break
                elif totalDealPoints == 21:
                    print("BlackJack!!!")
                    turn_finished = True
                    break
                else:
                    continue
            else:
                print("The dealer end is turn!")
                print("the sum is ", totalDealPoints)
                dealer_turn = True
                break
        elif totalDealPoints > 15 and totalDealPoints <= 19:
            randomic(4)
            if dealer_turn == False:
                newDealercard = random.choice(cards)
                dealer_cards.append(newDealercard)
                addValueD(newDealercard)
                print("The dealer draw another card: ", dealer_cards)
                print("\nPress enter to continue")
                input()
                if totalDealPoints > 21:
                    print("\nBurst!!!")
                    turn_finished = True
                    break
                elif totalDealPoints == 21:
                    print("\nBlackJack!!!")
                    turn_finished = True
                    break
                else:
                    continue
            else:
                print("The dealer end is turn!")
                print("the sum is ", totalDealPoints)
                dealer_turn = True
                break
        else:
            print("The dealer end is turn!")
            print("The sum is: ", totalDealPoints)
            turn_finished = True

    # conditions of victory

    print("\nAnd the winner is...")
    print("\nPress enter to continue")
    input()

    if totalPoints > totalDealPoints and totalPoints <= 21:
        print("\n+++++++++++++++")
        print("You Win!!! :D")
        print("+++++++++++++++")
    elif totalPoints == totalDealPoints and len(player_cards) < len(dealer_cards):
        print("\n+++++++++++++++")
        print("You Win!!! :D")
        print("+++++++++++++++")
    elif totalDealPoints > 21 and totalPoints <= 21:
        print("\n+++++++++++++++")
        print("You Win!!! :D")
        print("+++++++++++++++")
    else:
        print("\n++++++++++++++++++++++++++++++")
        print("The dealer Wins! Too bad! :(")
        print("++++++++++++++++++++++++++++++")

    # replay

    re = input("\nPlay again? y/n ")
    if re == "y":
        replay = True
    else:
        print("Bye bye!!!")
        replay = False
