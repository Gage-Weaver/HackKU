### Hackathon Project
### Blackjack game with powerups, multiplayer pvp or single vs dealer:
import tkinter as tk
from tkinter import messagebox
import random 
numbercardlist = [2,3,4,5,6,7,8,9,10]
facecardlist = ['j','q','k']
deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'a','a','a','a','j','j','j','j','q','q','q','q','k','k','k','k']
handvalue = 0
stillplaying = True
class card:
    def __init__(self, denom):
        if denom in numbercardlist:
            self.value = denom
        elif denom in facecardlist:
            self.value = 10
        else:
            self.value = 11
while stillplaying == True:
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
        print("Your hand value is", handvalue)
        print("You lost lmao")
        stillplaying = False
    while handvalue < 21 and stillplaying == True:
        print("Your hand value is", handvalue)
        userchoice = input("Would you like to hit: ")
        userchoice.lower
        if userchoice == 'yes':
            userhand.append(random.choice(deck))
            lastcard = userhand.pop()
            print("You drew a", lastcard)
            currentcard = card(lastcard)
            handvalue += currentcard.value
            if handvalue == 21:
                print("21!!!")
            elif handvalue > 21:
                print('You Lost lol')
            else:
                pass
        elif userchoice == 'no':
            print("Your ending total was", handvalue )
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
        standbutton = tk.Button(frame, text='stand', font=('Arial', 18))
        standbutton.grid(row=1, column=1, sticky = 's')
        frame.pack(fill='x')
        self.root.mainloop()
mygui()
    

    


