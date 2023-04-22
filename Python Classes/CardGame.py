import random

#Function to display the menu and get the choice from player
def gameMenu():
    print("Welcome to the Card Game, you have the following options: ")
    print("1.Start Game")
    print("2.Pick a Card")
    print("3.Shuffle Deck")
    print("4.Show my Cards")
    print("5.Check Win or Lose")
    print("6.Exit")
    choice = input("Please enter your selection: ")

    #Covering the case when the user selects option1 and a suite; default is suite1
    inputs = choice.split(" ")
    if(len(inputs)==1):
        return [int(choice),1]
    else:
        if(inputs[0]!='1'):
            return [int(inputs[0]),1]
        else:
            return [int(inputs[0]),int(inputs[1])]
        
#Function to create a deck with the selected suite
def createDeck(suites):
    numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = []
    #For loop for forming all the combinations between the suite values and the values
    for suite in suites:
        for value in numbers:
            deck.append(value+suite)
    return(deck)

#Function to randomly pick a card for both player and robot
def pickCard(playerCards,robotCards,deck):
    #Randomly picking a card for player and removing the card from deck
    length = len(deck)
    player_pick = random.randint(0, length-1)
    playerCards.append(deck[player_pick])
    deck.pop(player_pick)

    #Adding False at end of the deck to cover the case when the robot doesn't pick a card in a round
    deck.append(False)
    length = len(deck)
    robot_pick = random.randint(0, length-1)
    deck.pop()
    if(robot_pick !=False):
        robotCards.append(deck[robot_pick])
        deck.pop(robot_pick)
    
    return [playerCards,robotCards,deck]

#Function to shuffle the deck
def shuffleDeck(deck,suites):
    #Shuffle
    random.shuffle(deck)
    
    #Calculatig the middle index
    middle = int(round((len(deck)+1)/2,0))

    # storing the values of the cards and their positions
    firstSuiteA = "A"+suites[0]
    cardAtIndex0 = deck[0]

    secondSuitQ = "Q"+suites[1]
    cardAtMiddleIndex = deck[middle-1]

    lastSuiteK = "K"+suites[-1]
    cardAtLastIndex = deck[-1]

    #Swapping the first suite's A card to first position in deck
    for i in range(len(deck)):
        if(deck[i]==firstSuiteA):
            temp = deck[0]
            deck[0]=firstSuiteA
            deck[i]= temp

    #Swapping the second suite's Q card to middle position in deck
    for i in range(len(deck)):
        if(deck[i]==secondSuitQ):
            temp = deck[middle-1]
            deck[middle-1]= secondSuitQ
            deck[i]=temp
    
    #Swapping the filastrst suite's K card to last position in deck
    for i in range(len(deck)):
        if(deck[i]==lastSuiteK):
            temp = deck[-1]
            deck[-1] = lastSuiteK
            deck[i] = temp
    return deck

#Function to display the player's cards
def showCards(playerCards):
    print("Your Cards are: ")
    for card in playerCards:
        print(card)

#Function to determine the winner
def CheckWinOrLose(playerCards,robotCards,suites,deck):
    #Displaying the final cards of the player and robot
    print("Player Cards: ",playerCards)
    print("Robot Cards: ",robotCards)

    print(len(playerCards),len(robotCards))
    playerCardValues = []
    robotCardValues = []
    #Retrieving the values of the cards of both player and robot
    for card in playerCards:
        playerCardValues.append(card[0])
    for card in robotCards:
        robotCardValues.append(card[0])
    
    #RULE-1
    playerRuleFlag = Rule1(playerCards,suites,playerCardValues)
    robotRuleFlag = Rule1(robotCards,suites,robotCardValues)
    if(playerRuleFlag and not robotRuleFlag):
        print("PLAYER WINS by Rule 1!!!")
        return True
    elif(robotRuleFlag and not playerRuleFlag):
        print("ROBOT WIN by Rule 1!!!")
        return False
    
    #RULE-2
    playerRuleFlag = Rule2(playerCards,suites,playerCardValues)
    robotRuleFlag = Rule2(robotCards,suites,robotCardValues)
    if(playerRuleFlag and not robotRuleFlag):
        print("PLAYER WINS by Rule 2!!!")
        return True
    elif(robotRuleFlag and not playerRuleFlag):
        print("ROBOT WINS by Rule 2!!!2")
        return False

    #RULE-3
    playerRuleCount = Rule3(playerCards,suites)
    robotRuleCount = Rule3(robotCards,suites)
    if(playerRuleCount > robotRuleCount):
        print("PLAYER WINS by Rule 3!!!")
        return True
    elif(playerRuleCount < robotRuleCount):
        print("ROBOT WINS by Rule 3!!!")
        return False

    #RULE-4
    playerRuleCount = Rule4(playerCards,playerCardValues)
    robotRuleCount = Rule4(robotCards,robotCardValues)
    if(playerRuleCount > robotRuleCount):
        print("PLAYER WINS by Rule 4!!!")
        return True
    elif(playerRuleCount < robotRuleCount):
        print("ROBOT WINS by Rule 4!!!")
        return False

    #IF none of the rules are succeded, then its declared a TIE
    print("Robot Wins!!")
    return False

#Function to check if there are one value card from each sutie 
def Rule1(cards,suites,cardValues):
    check = False
    for value in cardValues:
        allValueCardsInAllSuites = []
        for suite in suites:
            allValueCardsInAllSuites.append(value+suite)
        check =  all(item in cards for item in allValueCardsInAllSuites)
        if(check):
            return check
    return check

#Function to check if there are one value card from atleast total Number of suites minues one
def Rule2(cards,suites,cardValues):
    for value in cardValues:
        count=0
        for suite in suites:
            card = value+suite
            if(card in cards):
                count+=1
        if(count>=len(suites)-1):
            return True
    return False

#Function to count the number of cards from second suite
def Rule3(cards,suites):
    secondSuite = suites[1]
    count =0
    for card in cards:
        if(secondSuite in card):
            count+=1
    return count

#Function to calculate the average of the values of the cards
def Rule4(cards,cardValues):
    avg = 0
    for value in cardValues:
        if(value =='A'):
            avg+=1
        elif(value=='J'):
            avg+=11
        elif(value=='Q'):
            avg+=12
        elif(value=="K"):
            avg+=13
        else:
            avg+=int(value)
    avg = avg/len(cards)
    return avg

#The manager function which maintains the state of the game, stores the cards player and robot have at every stage of the game
def playGame():
    flag = True
    suits1 = ["♥", "♦", "♣", "♠"]
    suits2 = ["😃", "😈", "😵", "🤢", "😨"]
    suits3 = ["🤡", "👹", "👺", "👻", "👽", "👾", "🤖"]
    suite = suits1
    deck = createDeck(suite)
    playerCards=[]
    robotCards=[]
    print("Available suites: ")
    print(suits1)
    print(suits2)
    print(suits3)    
    while(flag):
        [choice,suitChoice] = gameMenu()
        if(choice == 1):
            if(suitChoice is None):
                suite = suits1
            if(suitChoice>3 or suitChoice<1):
                print("Invalid number of suites")
            else:
                if(suitChoice==1):
                    deck = createDeck(suits1)
                    suite = suits1
                elif(suitChoice==2):
                    deck = createDeck(suits2)
                    suite = suits2
                else:
                    deck = createDeck(suits3)
                    suite = suits3
            playerCards=[]
            robotCards=[]
            print("suite: ",suite)
            print("deck: ",deck)
        
        elif(choice == 2):
            [playerCards,robotCards,deck]=pickCard(playerCards,robotCards,deck)
            if(len(playerCards)>=6 or len(robotCards)>=6):
                result = CheckWinOrLose(playerCards,robotCards,suite,deck)
                print(result)
                flag=False
        elif(choice ==3):
            deck = shuffleDeck(deck,suite)
        elif(choice ==4):
            showCards(playerCards)
        elif(choice == 5):
            # playerCards=['Q😈','Q😈','K😵','K🤢','K😨']
            # robotCards = ['K😈','Q😈','K😵','K🤢','K😨']
            result = CheckWinOrLose(playerCards,robotCards,suite,deck)
            print(result)
            flag=False
        elif(choice ==6):
            flag = False
        else:
            print("Please enter a valid selection.")
    
    print("Thank you for playing!")
            

#Main Function
if __name__ == "__main__":
    playGame()
