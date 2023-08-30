import random
import time
num_cards=['Red 0','Red 1','Red 1','Red 2','Red 2','Red 3','Red 3','Red 4','Red 4','Red 5','Red 5','Red 6','Red 6','Red 7','Red 7','Red 8','Red 9','Red 9',
                     'Blue 0','Blue 1','Blue 1','Blue 2','Blue 2','Blue 3','Blue 3','Blue 4','Blue 4','Blue 5','Blue 5','Blue 6','Blue 6','Blue 7','Blue 7','Blue 8','Blue 8','Blue 9','Blue 9',
                     'Green 0','Green 1','Green 1','Green 2','Green 2','Green 3','Green 3','Green 4','Green 4','Green 5','Green 5','Green 6','Green 6','Green 7','Green 7','Green 8','Green 8','Green 9','Green 9',
                     'Yellow 0','Yellow 1','Yellow 1','Yellow 2','Yellow 2','Yellow 3','Yellow 3','Yellow 4','Yellow 4','Yellow 5','Yellow 5','Yellow 6','Yellow 6','Yellow 7','Yellow 7','Yellow 8','Yellow 8','Yellow 9','Yellow 9']
special_cards=['Red Reverse','Red Reverse','Blue Reverse','Blue Reverse','Green Reverse','Green Reverse','Yellow Reverse','Yellow Reverse',
                         'Red Skip','Red Skip','Blue Skip','Blue Skip','Green Skip','Green Skip','Yellow Skip','Yellow Skip',
                         'Red Draw Two','Red Draw Two','Blue Draw Two','Blue Draw Two','Green Draw Two','Green Draw Two','Yellow Draw Two','Yellow Draw Two',
                         'Wild','Wild','Wild','Wild','Wild Draw Four','Wild Draw Four','Wild Draw Four','Wild Draw Four']
cards=num_cards+special_cards
check=[]
player=[]
comp=[]
Len=len(cards)

print ("Welcome to UNO")
print ("The rules are simple and are as follows:")
print ("• Both you and your opponent start with 7 cards each.")
print ("• To play a card, enter the name of the card keeping in mind the case(uppercase and lowercase) of each character.")
print ("• To draw a card, enter '+1'.")
print ("• If you don't have any cards that can be played, enter 'Pass'.")
print ("• None can only be entered after you've drawn a card.")
print ("• The first one to get rid of all their cards win the game.")


def Jhalak(List,limit):                                                   #Function to add cards to a list from the main list randomly

    global cards
    global check
    global player
    global comp
    
    count=0
    while (count<limit):
        if (len(cards)==len(check)):
            check.clear()
            check1=player+comp+list(prev_card)
            check2=[]
            for i in check1:
                checkindex=0
                if (i not in check2):
                    for j in range (check1.count(i)):
                        check.append(cards.index(i)+checkindex)
                        checkindex+=1
                    check2.append(i)
        tempindex=random.randint(0,Len-1)
        if (tempindex not in check):
            List.append(cards[tempindex])
            check.append(tempindex)
            count+=1

Jhalak(player,7)
Jhalak(comp,7)

while (1):                                                                    #Choosing the starting card
    temp=random.randint(0,len(num_cards)-1)
    if (temp not in check):
        check.append(temp)
        prev_card=cards[temp]
        break
    
def Colours():                                      #Function to choose the colour if a wild card is played
    
    global prev_card
    
    while (1):
        prev_card=input("Choose the colour:")
        if (prev_card in ['Red','Blue','Green','Yellow']):
            break
        else:
            print ("Invalid colour.")    

def Banzal():                                                                              #Functions for when its the player's turn
    
    global prev_card
    global player
    global comp

    flag=0
    while (1):                                                                              #While loop forces the user to choose a card
        time.sleep(1)
        print ("\n"*2)
        print ("Previous card:",prev_card)
        print ("Your cards:",player)
        card=input("Enter the card you want to play:")
        if (card=='Pass' and flag==1):                                        #If user has drawn a card and still doesn't have any playable cards
            return
        elif (card=='+1' and flag==0):                                          #If user wants to draw a card
            Jhalak(player,1)
            flag=1
        elif (card in player):                                                          #If user inputs a card from their deck
            break
        else:                                                                                   #If input is incompatible  
            print ("Invalid input.")
            print ("Check if spacing and character cases are correct.")
            
    temp=card.split()
    flag=0
    for i in temp:
        if (i in prev_card.split()):
            if ("Reverse" in temp or "Skip" in temp):
                time.sleep(1)
                print ("\n"*2)
                print ("It's your turn again.")
                prev_card=card
                player.remove(card)
                Banzal()
            elif ("Draw" in temp and "Two" in temp):
                time.sleep(1)
                Jhalak(comp,2)
                print ("\n"*2)
                print ("Your opponent drew 2 cards.")
                print ("It's your turn again.")
                prev_card=card
                player.remove(card)
                Banzal()
            elif ("Wild" in temp):
                pass
            else:
                prev_card=card
                player.remove(card)
            flag=1
            break
    if ("Wild" in temp):
        if ("Draw" in temp and "Four" in temp):
            time.sleep(1)
            Jhalak(comp,4)
            print ("\n"*2)
            print ("Your opponent drew 4 cards.")
            print ("\n"*2)
            time.sleep(1)
            Colours()
            player.remove(card)
            time.sleep(1)
            print ("\n"*2)
            print ("It's your turn again.")
            Banzal()
        else:
            Colours()
            player.remove(card)
        flag=1
    else:
        if (flag==0):
            time.sleep(1)
            print ("\n"*2)
            print ("Chosen card is not playable.")
            Banzal()

def comp_colours():                                              #Function to choose colour at random if wild card is played
    
    global prev_card

    tempindex=random.randint(0,3)
    Colour=['Red','Blue','Green','Yellow']
    prev_card=Colour[tempindex]

def comp_play():                                                    #Function for when it's the computer's turn

    global prev_card
    global comp
    global player
    global card                                                         #Identifier 'card' is the card to be played 

    ret=0
    for i in comp:                                                      #First for ... else looks for a playable card in the computer's deck
        temp=i.split()                                                          
        if ("Wild" in temp):
            card=i
            ret=1
            break
        flag=0
        for j in temp:
            if (j in prev_card.split()):
                card=i
                ret=1
                flag=1
                break
        if (flag==1):
            break
    else:                                                                    #If there is no playable card, it takes an extra card from the pile
        time.sleep(1)
        print ("\n"*2)
        print ("Your opponent drew a card.")
        Jhalak(comp,1)
        temp=comp[-1].split()
        if ("Wild" in temp):
            card=comp[-1]
            ret=1
        for j in temp:
            if (j in prev_card.split()):
                card=comp[-1]
                ret=1
                break

    if (ret==0):                                                                                           #Executes if no card is playable
        time.sleep(1)
        print ("\n"*2)
        print ("Your opponent has no playable cards.")
        print ("Your opponent has",len(comp),"cards left.")
    else:                                                                                                       #card has been played
        comp.remove(card)
        time.sleep(1)
        print ("\n"*2)
        print ("Your opponent played ",card,".",sep="")
        print ("Your opponent has",len(comp),"cards left.")
        temp=card.split()
        for i in temp:
            if (i in prev_card.split()):
                if("Reverse" in temp or "Skip" in temp):
                    time.sleep(1)
                    print ("\n"*2)
                    print ("It's your opponent's turn again.")
                    prev_card=card
                    comp_play()
                elif ("Draw" in temp and "Two" in temp):
                    time.sleep(1)
                    Jhalak(player,2)
                    print ("\n"*2)
                    print ("You drew 2 cards.")
                    print ("It's your opponent's turn again.")
                    prev_card=card
                    comp_play()
                elif ("Wild" in temp):
                    pass
                else:
                    prev_card=card
                break
        if ("Wild" in temp):
            if ("Draw" in temp and "Four" in temp):
                time.sleep(1)
                Jhalak(player,4)
                print ("\n"*2)
                print ("You drew 4 cards.")
                comp_colours()
                print ("It's your opponent's turn again.")
                comp_play()
            else:
                comp_colours()

while (len(player)!=0 and len(comp)!=0):                      #Loop executes as long as both players have cards
    Banzal()                                                                       #Player's turn
    if (len(player)==0):
        break
    comp_play()                                                                 #Computer's turn

time.sleep(1)    
print ("\n"*2)
if (len(player)==0):                                                          #If player wins
    print ("Congratulations, you've won!")
else:                                                                                  #If computer wins
    print ("You lost.")
    time.sleep(1)
    print ("Against a computer.")
    time.sleep(1)
    print ("That chooses cards at random.")
    time.sleep(1)
    print ("Wow.")
    time.sleep(1)
    print ("You suck.")
