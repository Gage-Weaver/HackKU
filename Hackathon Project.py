### Hackathon Project
### Blackjack game with powerups, multiplayer pvp or single vs dealer:
### Fix bug dealer draws ace doesnt revert to 1
import tkinter as tk
from tkinter import messagebox
import random 
numbercardlist = [2,3,4,5,6,7,8,9,10]
facecardlist = ['j','q','k']
deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'a','a','a','a','j','j','j','j','q','q','q','q','k','k','k','k']
handvalue = 0
stillplaying = True
print("This is elemental blackjack here is a rundown of the elements: ")
print("Team Fire allows you to take away 3 from the opponents final score")
print("Team Ice allows you to add 3 to your score if you are below 19")
userelement = input("Would you like to be Fire or Ice?: ")
userelement.lower()
class card:
    def __init__(self, denom):
        if denom in numbercardlist:
            self.value = denom
        elif denom in facecardlist:
            self.value = 10
        else:
            self.value = 11
while stillplaying == True:
    dealerhand = []
    dealerhand.append(random.choices(deck, k=2))
    dealerhandvalue = 0
    for ele in dealerhand[0]:
        currentcard = card(ele)
        dealerhandvalue += currentcard.value
    if dealerhandvalue >21:
        dealerhandvalue -= 10
        dealerhand[0][0] = 'Ace'
    userhand = []
    userhand.append(random.choices(deck, k=2))
    handvalue = 0
    for ele in userhand[0]:
        currentcard = card(ele)
        handvalue += currentcard.value
    if handvalue == 21:
        print("You won! Blackjack")
        stillplaying = False
    elif handvalue >21:
        handvalue -= 10
        userhand[0][0] = 'Ace'
    while stillplaying == True:
        print("Your cards are: ", userhand)
        print("Your hand value is", handvalue)
        print("The dealers up card is", dealerhand[0][0])
        userchoice = input("Would you like to hit: ")
        userchoice.lower
        if userchoice == 'yes':
            userhand.append(random.choice(deck))
            lastcard = userhand[(len(userhand)-1)]
            print("You drew a: ", lastcard)
            currentcard = card(lastcard)
            handvalue += currentcard.value
            if handvalue > 21 and (('a' in userhand) or ('a' in userhand[0])):
                if 'a' in userhand[0]:
                    for i in range(len(userhand[0])-1):
                        if userhand[0][i] == 'a':
                            userhand[0][i] = 'Ace'
                for i in range(len(userhand) -1):
                    if userhand[i] =='a':
                        userhand[i] = 'Ace'
                handvalue -= 10
            if handvalue == 21:
                print("You hit 21!")
                print("The dealers down card was a", dealerhand[0][1])
                if dealerhandvalue <=16:
                    dealerhand.append(random.choice(deck))
                    lastcard = dealerhand[(len(dealerhand)-1)]
                    if dealerhandvalue > 21 and (('a' in dealerhand) or ('a' in dealerhand[0])):
                        dealerhandvalue -= 10
                        if 'a' in dealerhand[0]:
                            for i in range(len(dealerhand[0])-1):
                                if dealerhand[0][i] == 'a':
                                    dealerhand[0][i] = 'Ace'
                                else: pass
                        for i in range(len(dealerhand) -1):
                            if dealerhand[i] =='a':
                                dealerhand[i] = 'Ace'
                            else:
                                pass
                    print("The dealer draws a", lastcard)
                    currentcard = card(lastcard)
                    dealerhandvalue += currentcard.value
                if dealerhandvalue < 21 and dealerhandvalue > 16:
                    if userelement == 'fire':
                        dealerhandvalue -= 3
                    if dealerhandvalue < handvalue:
                        print("The dealer ended with", dealerhandvalue, "You Win")
                        stillplaying = False
                    elif dealerhandvalue > handvalue:
                        print("The dealer ended with", dealerhandvalue, "You Lose")
                        stillplaying = False
                    else:
                        print("The dealer ended with", dealerhandvalue, "Its a Push")
                        stillplaying = False
                if dealerhandvalue > 21:
                    print("You won! the dealer busted")
                    stillplaying = False
                elif dealerhandvalue == 21:
                    if userelement == 'fire':
                        dealerhandvalue -= 3
                    print("The dealers down card was a", dealerhand[0][1])
                    print("The dealer hit 21, Its a Push")
                    stillplaying = False
            elif handvalue > 21:
                print('You Busted')
                stillplaying = False
        elif userchoice == 'no':
            if userelement == 'ice' and handvalue < 19:
                handvalue += 3
            print("Your ending total was", handvalue )
            print("The dealers down card was a", dealerhand[0][1])
            print("This puts the dealers total at", dealerhandvalue)
            while stillplaying == True:
                if dealerhandvalue <= 16:
                    dealerhand.append(random.choice(deck))
                    lastcard = dealerhand[(len(dealerhand)-1)]
                    print("The dealer draws a:", lastcard)
                    currentcard = card(lastcard)
                    dealerhandvalue += currentcard.value
                    if dealerhandvalue > 21 and (('a' in dealerhand) or ('a' in dealerhand[0])):
                        if 'a' in dealerhand[0]:
                            for i in range(len(dealerhand[0])):
                                if dealerhand[0][(i-1)] == 'a':
                                    dealerhand[0][(i-1)] = 'Ace'
                        if 'a' in dealerhand:
                            for i in range(len(dealerhand)):
                                if dealerhand[(i-1)] =='a':
                                    dealerhand[(i-1)] = 'Ace'
                        dealerhandvalue -= 10
                if dealerhandvalue < 21 and dealerhandvalue > 16:
                    if userelement == 'fire':
                        dealerhandvalue -=3
                        print('You use your fire powers to subtract 3 from the opponents score')
                    if dealerhandvalue > handvalue:
                        print("The dealer ended with", dealerhandvalue, "The dealer wins")
                        stillplaying = False
                    elif dealerhandvalue < handvalue:
                        print("The dealer ended with", dealerhandvalue, "You Win!")
                        stillplaying = False
                    else:
                        print("The dealer ended with", dealerhandvalue, "Its a Push")
                        stillplaying = False
                if dealerhandvalue > 21:
                    print("You won! the dealer busted")
                    stillplaying = False
                if dealerhandvalue == 21 and userelement == 'fire':
                    dealerhandvalue -= 3
                    print('You use your fire powers to subtract 3 from opponents score')
                    if dealerhandvalue > handvalue:
                        print("The dealer ended with", dealerhandvalue, "The dealer wins")
                        stillplaying = False
                    elif dealerhandvalue < handvalue:
                        print("The dealer ended with", dealerhandvalue, "You Win!")
                        stillplaying = False
                    else:
                        print("The dealer ended with", dealerhandvalue, "Its a Push")
                        stillplaying = False
                if dealerhandvalue == 21:
                    print("The dealer drew 21, Dealer Wins")
                    stillplaying = False
    playagain = input("Would you like to play again?: ")
    playagain.lower()
    if playagain == 'yes':
        stillplaying = True
    else:
        pass
class mygui:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("500x500")
        self.root.title("BlackJack Game")
        frame = tk.Frame(self.root)
        frame.columnconfigure(0, weight = 1)
        hitbutton = tk.Button(frame, text='Hit', font=('Arial', 18))
        hitbutton.grid(row=0, column=0, sticky = 's')
        standbutton = tk.Button(frame, text='Stand', font=('Arial', 18))
        standbutton.grid(row=1, column=1, sticky = 's')
        frame.pack(fill='x')
        self.root.mainloop()
mygui()