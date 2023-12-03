import random
from tkinter import *

#Dictionary and vars
schema = {
    "rock":{"rock":1,"paper":0,"scissors":2},
    "paper":{"rock":2,"paper":1,"scissors":1}, 
    "scissors":{"rock":0,"paper":2,"scissors":1}
}
comp_score = 0
player_score = 0

#Functions
def outcome_handler(user_choice):
    global comp_score
    global player_score
    outcomes = ["rock","paper","scissors"]
    random_number = random.randint(0,2)
    computer_choice = outcomes[random_number]
    result             = schema[user_choice][computer_choice]

    player_choice_label.config(fg="red",text="player choice : "+str(user_choice))
    computer_choice_label.config(fg="green",text="computer choice :"+str(computer_choice))
    if result == 2:
        player_score = player_score +2
        player_score_label.config(text="player : "+str(player_score))
        outcome_label.config(fg="blue",text="outcome : player won")
    elif result ==1:
        player_score = player_score +1
        comp_score = comp_score +1
        player_score_label.config(text="player : "+str(player_score))
        computer_score_label.config(text="computer : "+str(comp_score))
        outcome_label.config(fg="blue",text="outcome : Draw")
    elif result ==0:
        comp_score = comp_score +2
        computer_score_label.config(text="computer : "+str(comp_score))
        outcome_label.config(fg="blue",text="outcome : computer won")

                             
#Main screen
master = Tk()
master.title("RPS")

#labels
Label(master,text="Rock, Paper, Scissors",font=("Calibri",16)).grid(row=0,sticky=N,pady=10,padx=200)
Label(master,text="please select an option",font=("Calibri",14)).grid(row=1,sticky=N)
player_score_label = Label(master,text="player : 0",font=("calibri",14))
player_score_label.grid(row=2,sticky=W)
computer_score_label = Label(master,text="computer : 0",font=("calibri",14))
computer_score_label.grid(row=2,sticky=E)
player_choice_label = Label(master,font=("calibri",14))
player_choice_label.grid(row=3,sticky=W)
computer_choice_label = Label(master,font=("calibri",14))
computer_choice_label.grid(row=3,sticky=E)
outcome_label = Label(master,font=("calibri",14))
outcome_label.grid(row=3,sticky=N)
#Buttons
Button(master,text="Rock",width=15,command=lambda:outcome_handler("rock")).grid(row=4,sticky=W,padx=5,pady=5)
Button(master,text="Paper",width=15,command=lambda:outcome_handler("paper")).grid(row=4,sticky=N,pady=5)
Button(master,text="Scissors",width=15,command=lambda:outcome_handler("scissors")).grid(row=4,sticky=E,padx=5,pady=5)
#Dummy Label
Label(master).grid(row=5)
master.mainloop()
