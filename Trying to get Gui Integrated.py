### Trying to get Gui Integrated
import tkinter as tk
from tkinter import messagebox
from tkinter import *
import random 
numbercardlist = [2,3,4,5,6,7,8,9,10]
facecardlist = ['j','q','k']
deck = [2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,6,6,6,6,7,7,7,7,8,8,8,8,9,9,9,9,10,10,10,10,'a','a','a','a','j','j','j','j','q','q','q','q','k','k','k','k']
handvalue = 0
stillplaying = True
userelement = ['']
userchoice = ['']
class card:
    def __init__(self, denom):
        if denom in numbercardlist:
            self.value = denom
        elif denom in facecardlist:
            self.value = 10
        else:
            self.value = 11
class gui:
    def __init__(self):
        ###Basic Stuff
        self.root = tk.Tk()
        self.root.geometry("1920x1080")
        self.root['bg'] = 'green'
        self.root.title("BlackJack Game")
        frame = tk.Frame(self.root)
        label1 = tk.Label(self.root, text="Hello, This is Elemental Blackjack, the age old game of Blackjack with a Twist", font=('Arial', 25))
        label1.pack(padx=20, pady=20)
        label1['bg'] = 'green'
        label2 = tk.Label(self.root, text="Choose a team, and starting value below, team Fire allows you to take score from the dealer and team Ice allows you to add score to your own hand", font=('Arial', 13))
        label2.pack(padx=20, pady=20)
        label2['bg'] = 'green'
        label1 = tk.Label(self.root, text="Standard Black Jack rules, dealer hits 16 and below", font=('Arial', 25))
        label1.pack(padx=20, pady=20)
        label1['bg'] = 'green'
        ###Frame Column Config
        frame.columnconfigure(0, weight=1)
        frame.columnconfigure(1, weight=1)
        frame.columnconfigure(2, weight=1)
        frame['bg'] = 'green'
        ###Button Definitions
        def fireclick():
            print('You chose Fire')
            userelement[0] = 'fire'
            buttonfire.destroy()
            buttonice.destroy()
            buttonnone.destroy()
            return userelement
        def noneclick():
            print('You chose No Powerup')
            userelement[0] = ''
            buttonfire.destroy()
            buttonice.destroy()
            buttonnone.destroy()
            return userelement
        def iceclick():
            print('You chose Ice')
            userelement[0] = 'ice'
            buttonfire.destroy()
            buttonice.destroy()
            buttonnone.destroy()
            return userelement
        def startgame():
            stillplaying = True
            buttonstart.destroy()
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
                    label = Label(self.root, text= ("BlackJack, you Win!!"), font=('Arial', 18))
                    label['bg'] = 'green'
                    label.pack()
                    messagebox.showinfo("Message", "BaclkJack You Win!!")
                    stillplaying = False
                elif handvalue >21:
                    handvalue -= 10
                    userhand[0][0] = 'Ace'
                
                while stillplaying == True:
                    label = Label(self.root, text= ("Your cards", userhand ), font=('Arial', 18))
                    label['bg'] = 'green'
                    label.pack()
                    label = Label(self.root, text= ("hand value", handvalue), font = ('Arial', 18))
                    label['bg'] = 'green'
                    label.pack()
                    label = Label(self.root, text= ("up card is: ", dealerhand[0][0]), font = ('Arial', 18))
                    label['bg'] = 'green'
                    label.pack()
                    userchoicepopup = messagebox.askyesno('Would you like to Hit?')
                    if userchoicepopup == True:
                        userhand.append(random.choice(deck))
                        lastcard = userhand[(len(userhand)-1)]
                        label = Label(self.root, text= ("You Drew", lastcard), font=('Arial', 18))
                        label['bg'] = 'green'
                        label.pack()
                        currentcard = card(lastcard)
                        handvalue += currentcard.value
                        if handvalue > 21 and (('a' in userhand) or ('a' in userhand[0])):
                            handvalue -= 10
                            if 'a' in userhand[0]:
                                for i in range(len(userhand[0])):
                                    if userhand[0][(i-1)] == 'a':
                                        userhand[0][(i-1)] = 'Ace'
                            if 'a' in userhand:
                                for i in range(len(userhand)):
                                    if userhand[(i-1)] =='a':
                                        userhand[(i-1)] = 'Ace'
                        if handvalue == 21:
                            label = Label(self.root, text= ("You Drew 21!!"), font=('Arial', 18))
                            label['bg'] = 'green'
                            label.pack()
                            label = Label(self.root, text= ("Down Card is", dealerhand[0][1]), font=('Arial', 18))
                            label['bg'] = 'green'
                            label.pack()
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
                                label = Label(self.root, text= ("Dealer Draws a", lastcard), font=('Arial', 18))
                                label['bg'] = 'green'
                                label.pack()
                                currentcard = card(lastcard)
                                dealerhandvalue += currentcard.value
                            if dealerhandvalue < 21 and dealerhandvalue > 16:
                                if userelement[0] == 'fire':
                                    dealerhandvalue -= 3
                                    label = Label(self.root, text= ("You Activate Fire Reducing dealer score by 3"), font=('Arial', 18))
                                    label['bg'] = 'green'
                                    label.pack()
                                if dealerhandvalue < handvalue:
                                    label = Label(self.root, text= ("You had", handvalue, "Dealer Had", dealerhandvalue, "You Win"), font=('Arial', 18))
                                    label['bg'] = 'green'
                                    label.pack()
                                    messagebox.showinfo("Message", "You Win")
                                    stillplaying = False
                                elif dealerhandvalue > handvalue:
                                    label = Label(self.root, text= ("You had", handvalue, "Dealer had", dealerhandvalue, "You Lose"), font=('Arial', 18))
                                    label['bg'] = 'green'
                                    label.pack()
                                    messagebox.showinfo("Message", "Dealer Wins")
                                    stillplaying = False
                                else:
                                    label = Label(self.root, text= ("You had", handvalue, "Dealer had", dealerhandvalue, "Its a Push"), font=('Arial', 18))
                                    label['bg'] = 'green'
                                    label.pack()
                                    messagebox.showinfo("Message", "Push")
                                    stillplaying = False
                            if dealerhandvalue > 21:
                                label = Label(self.root, text= ("Dealer Busted"), font=('Arial', 18))
                                label['bg'] = 'green'
                                label.pack()
                                stillplaying = False
                            elif dealerhandvalue == 21:
                                label = Label(self.root, text= ("Down card is", dealerhand[0][1]), font=('Arial', 18))
                                label['bg'] = 'green'
                                label.pack()
                                if userelement[0] == 'fire':
                                    dealerhandvalue -= 3
                                    label = Label(self.root, text= ("You Activate Fire Reducing dealer score by 3"), font=('Arial', 18))
                                    label['bg'] = 'green'
                                    label.pack()
                                    if dealerhandvalue < handvalue:
                                        label = Label(self.root, text= ("You had", handvalue, "Dealer had", dealerhandvalue, "You Win"), font=('Arial', 18))
                                        label['bg'] = 'green'
                                        label.pack()
                                        messagebox.showinfo("Message", "You Win")
                                        stillplaying = False
                                    elif dealerhandvalue > handvalue:
                                        label = Label(self.root, text= ("You had", handvalue, "Dealer had", dealerhandvalue, "You Lose"), font=('Arial', 18))
                                        label['bg'] = 'green'
                                        label.pack()
                                        messagebox.showinfo("Message", "Dealer Wins")
                                        stillplaying = False
                                    else:
                                        label = Label(self.root, text= ("You had", handvalue, "Dealer had", dealerhandvalue, "Its a Push"), font=('Arial', 18))
                                        label['bg'] = 'green'
                                        label.pack()
                                        messagebox.showinfo("Message", "Push")
                                        stillplaying = False
                                else:
                                    label = Label(self.root, text= ("You had", handvalue, "Dealer had", dealerhandvalue, "Its a Push"), font=('Arial', 18))
                                    label['bg'] = 'green'
                                    label.pack()
                                    messagebox.showinfo("Message", "Push")
                                stillplaying = False
                        elif handvalue > 21:
                            label = Label(self.root, text= ("You busted"), font=('Arial', 18))
                            label['bg'] = 'green'
                            label.pack()
                            messagebox.showinfo("Message", "You Bust")
                            stillplaying = False
                    elif userchoicepopup == False:
                        if userelement[0] == 'ice' and handvalue < 19:
                            handvalue += 3
                            label = Label(self.root, text= ("You activate Ice increasing your score by 3"), font=('Arial', 18))
                            label['bg'] = 'green'
                            label.pack()
                        label = Label(self.root, text= ("Your Hand Value", handvalue), font=('Arial', 18))
                        label['bg'] = 'green'
                        label.pack()
                        label = Label(self.root, text= ("Down Card", dealerhand[0][1]), font=('Arial', 18))
                        label['bg'] = 'green'
                        label.pack()
                        label = Label(self.root, text= ("Dealer Hand Value", dealerhandvalue), font=('Arial', 18))
                        label['bg'] = 'green'
                        label.pack()
                        while stillplaying == True:
                            if dealerhandvalue <= 16:
                                dealerhand.append(random.choice(deck))
                                lastcard = dealerhand[(len(dealerhand)-1)]
                                label = Label(self.root, text= ("Dealer Draws", lastcard), font=('Arial', 18))
                                label['bg'] = 'green'
                                label.pack()
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
                                if userelement[0] == 'fire':
                                    dealerhandvalue -=3
                                    label = Label(self.root, text= ("You activate Fire Reducing dealer score by 3"), font=('Arial', 18))
                                    label['bg'] = 'green'
                                    label.pack()
                                if dealerhandvalue > handvalue:
                                    label = Label(self.root, text= ("You had", handvalue, "Dealer had", dealerhandvalue, "Dealer Wins"), font=('Arial', 18))
                                    label['bg'] = 'green'
                                    label.pack()
                                    messagebox.showinfo("Message", "Dealer Wins")
                                    stillplaying = False
                                elif dealerhandvalue < handvalue:
                                    label = Label(self.root, text= ("You had", handvalue, "Dealer had", dealerhandvalue, "You Win"), font=('Arial', 18))
                                    label['bg'] = 'green'
                                    label.pack()
                                    messagebox.showinfo("Message", "You Win")
                                    stillplaying = False
                                else:
                                    label = Label(self.root, text= ("You had", handvalue, "Dealer had", dealerhandvalue, "Its a Push"), font=('Arial', 18))
                                    label['bg'] = 'green'
                                    label.pack()
                                    messagebox.showinfo("Message", "Push")
                                    stillplaying = False
                            if dealerhandvalue > 21:
                                label = Label(self.root, text= ("Dealer Busts"), font=('Arial', 18))
                                label['bg'] = 'green'
                                label.pack()
                                messagebox.showinfo("Message", "Dealer Busts")
                                stillplaying = False
                            if dealerhandvalue == 21 and userelement[0] == 'fire':
                                dealerhandvalue -= 3
                                label = Label(self.root, text= ("You Activate fire reducing dealer score by 3"), font=('Arial', 18))
                                label['bg'] = 'green'
                                label.pack()
                                if dealerhandvalue > handvalue:
                                    label = Label(self.root, text= ("You had", handvalue, "Dealer had", dealerhandvalue, "Dealer Wins"), font=('Arial', 18))
                                    label['bg'] = 'green'
                                    label.pack()
                                    messagebox.showinfo("Message", "Dealer Wins")
                                    stillplaying = False
                                elif dealerhandvalue < handvalue:
                                    label = Label(self.root, text= ("You had", handvalue, "Dealer had", dealerhandvalue, "You Win"), font=('Arial', 18))
                                    label['bg'] = 'green'
                                    label.pack()
                                    messagebox.showinfo("Message", "You Win!")
                                    stillplaying = False
                                else:
                                    label = Label(self.root, text= ("You had", handvalue, "Dealer had", dealerhandvalue, "Its a Push"), font=('Arial', 18))
                                    label['bg'] = 'green'
                                    label.pack()
                                    messagebox.showinfo("Message", "Push")
                                    stillplaying = False
                            if dealerhandvalue == 21:
                                label = Label(self.root, text= ("You had", handvalue, "Dealer had", dealerhandvalue, "Dealer Wins"), font=('Arial', 18))
                                label['bg'] = 'green'
                                label.pack()
                                messagebox.showinfo("Message", "Dealer Wins")
                                stillplaying = False
                for widgets in self.root.winfo_children():
                    widgets.destroy()
                playagainpopup = messagebox.askyesno('Would you like to Play again?')
                if playagainpopup == True:
                    startgame()
                else:
                    stillplaying = False
        ##### BUTTONS
        buttonfire = tk.Button(frame, text='Fire', font=('arial', 16), command=fireclick)
        buttonfire.grid(row=0, column=0, sticky='we')
        buttonfire['bg'] = 'red'
        buttonnone = tk.Button(frame, text='No Powerups', font=('arial', 16), command=noneclick)
        buttonnone.grid(row=0, column=1, sticky='we')
        buttonnone['bg'] = 'grey'
        buttonice = tk.Button(frame, text='Ice', font=('arial', 16), command=iceclick)
        buttonice.grid(row=0, column=2, sticky='we')
        buttonice['bg'] = 'blue'
        buttonstart = tk.Button(frame, text='Start Game', font=('arial', 16), command=startgame)
        buttonstart.grid(row=3, column=1, sticky='we')
        buttonstart['bg'] = 'grey'












        frame.pack(fill='x')
        self.root.mainloop()
gui()











