# Name: Richa
# Date: January 10, 2022
# File Name: games.py
# Description: In one tab you are able to play a rock paper scissors game against
# a computer. You get 5 points for each win. All the wins and losses are displayed
# in the bottom left corner. On another tab you can play a color game where the
# text displays one color name but has a different color for the text. You are
# supposed to enter the color of the text and you have 60 minutes to create a highscore.
# Both the score and highscore are displayed in the bottom left corner. To reset
# the highscore you must go to the file called "highscore.txt" within the same
# folder as this file and you must change the contents to contain only '0'.

#import libraries and functions
import random
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#create main window
window = Tk()
window.title('Games!')
window.geometry ('1000x1000')

#create different tabs
tab_control = ttk.Notebook(window) #create a control tab in window
tab1 = Frame(tab_control) #add a frame to the control tab
tab2 = Frame(tab_control) #add a frame to the control tab
tab_control.add(tab1, text='Rock Paper Scissors!')
tab_control.add(tab2, text='The Color Game!')
tab_control.pack(expand=1, fill='both')

# tab 1: a Rock Paper Scissors game
#message pop-up that reads rules/instructions
def clicked():
    messagebox.showinfo('Rock Paper Scissors: Rules/Instructions', ('In this game') +
    (' you will click one of the 3 buttons to choose your choice. You will get 5') +
    (' points for every win! The scores, wins and losses will be displayed in the') +
    (' bottom left corner.'))

#label that displays message pop-up
rpsmessage_label = Label(tab1, command=clicked())
rpsmessage_label.grid(row=0 , column=0)
# the 2 sides (labelled)
lbl_player = Label(tab1, text='You')
lbl_player.grid(row=0, column=2)
lbl_computer = Label(tab1, text='Computer')
lbl_computer.grid(row=0, column=8)

#upload choice images
rock_image = PhotoImage(file="rock.png")
paper_image = PhotoImage(file="paper.png")
scissors_image = PhotoImage(file="scissors.png")

# global variables:
rps_player_score = 0
rps_computer_score = 0
rps_score = 0
rps_player_choice = ''
rps_computer_choice = ''

# generate a random computer choice
def random_choice():
    global rps_computer_choice
    rps_computer_choice = random.choice(['rock', 'paper', 'scissors'])
    if rps_computer_choice == 'rock':
        random_lbl1 = Label(tab1, image=rock_image)
        random_lbl1.grid(row=3, column=8, sticky=S+E)
    elif rps_computer_choice == 'paper':
        random_lbl2 = Label(tab1, image=paper_image)
        random_lbl2.grid(row=3, column=8, sticky=S+E)
    elif rps_computer_choice == 'scissors':
        random_lbl3 = Label(tab1, image=scissors_image)
        random_lbl3.grid(row=3, column=8, sticky=S+E)
    return rps_computer_choice

#check to see if the player or computer wins and then calculate all the scores
def winner():
    global rps_player_score
    global rps_computer_score
    global rps_score
    if rps_player_choice == 'rock' and rps_computer_choice == 'scissors':
        rps_player_score += 1
        player_lbl = Label(tab1, text='You win!')
        player_lbl.grid(row=0, column=5, sticky=W+E)
    elif rps_player_choice == 'paper' and rps_computer_choice == 'rock':
        rps_player_score += 1
        rps_player_lbl = Label(tab1, text='You win!')
        rps_player_lbl.grid(row=0, column=5, sticky=W+E)
    elif rps_player_choice == 'scissors' and rps_computer_choice == 'paper':
        rps_player_score += 1
        rps_player_lbl = Label(tab1, text='You win!')
        rps_player_lbl.grid(row=0, column=5, sticky=W+E)
    elif rps_player_choice == 'paper' and rps_computer_choice == 'scissors':
        rps_computer_score+=1
        rps_computer_lbl = Label(tab1, text='You lose!')
        rps_computer_lbl.grid(row=0, column=5, sticky=W+E)
    elif rps_player_choice == 'rock' and rps_computer_choice == 'paper':
        rps_computer_score += 1
        rps_computer_lbl = Label(tab1, text='You lose!')
        rps_computer_lbl.grid(row=0, column=5, sticky=W+E)   
    elif rps_player_choice == 'scissors' and rps_computer_choice == 'rock':
        rps_computer_score+=1
        rps_computer_lbl = Label(tab1, text='You lose!')
        rps_computer_lbl.grid(row=0, column=5, sticky=W+E)        
    else:
        tie_lbl = Label(tab1, text='It\'s a tie!')
        tie_lbl.grid(row=0, column=5, sticky=W+E)
    
    rps_score = rps_player_score * 5
    win_lbl = Label(tab1, text=f'Win(s): {rps_player_score}')
    loss_lbl = Label(tab1, text=f'Loss(es): {rps_computer_score}')
    rps_score_lbl = Label(tab1, text=f'Score: {rps_score}')
    # for the 3 labels above you can concatenate them without using formatted
    # strings in this format:
    # win_lbl = Label(tab1, text='Win(s): ' + str(rps_player_score))
    win_lbl.grid(row=10, column=0, sticky=W)
    loss_lbl.grid(row=11, column=0, sticky=W)
    rps_score_lbl.grid(row=12, column=0, sticky=W)

#if the player chooses rock
def clicked_rock():
    global rps_player_choice
    random_choice()
    rps_player_choice = 'rock'
    winner()
    rock_lbl = Label(tab1, image=rock_image)
    rock_lbl.grid(row=3, column=2, sticky=S+W)

# if the player chooses paper
def clicked_paper():
    global rps_player_choice
    random_choice()
    rps_player_choice = 'paper'
    winner()
    paper_lbl = Label(tab1, image=paper_image)
    paper_lbl.grid(row=3, column=2, sticky=S+W)

# if the player chooses scissors
def clicked_scissors():
    global rps_player_choice
    random_choice()
    rps_player_choice = 'scissors'
    winner()
    scissors_lbl = Label(tab1, image=scissors_image)
    scissors_lbl.grid(row=3, column=2, sticky=S+W)

# rock, paper, scissor buttons
bttn1 = Button(tab1, text='rock', command=clicked_rock)
bttn1.grid(row=6, column=4, sticky=W+E)
bttn2 = Button(tab1, text='paper', command=clicked_paper)
bttn2.grid(row=6, column=5, sticky=W+E)
bttn3 = Button(tab1, text='scissors', command=clicked_scissors)
bttn3.grid(row=6, column=6, sticky=W+E)

# tab 2: the Color Game
#message pop-up box wtih rules/instructions
def message():
    messagebox.showinfo('Color Game: Rules/Instructions', ('You have to type the') +
                        (' color of the text, not the word. For every correct') +
                        (' answer you will get 1 point. The scores will be ') +
                        ('displayed in the bottom left corner. You will have a') +
                        (' total of 1 minute to create a highscore. Once the ') +
                        ('time is up, press the start game button once again.'))

#label with message pop-up and instructions
color_message_lbl = Label(tab2, command=message())
color_message_lbl.grid(row=0, column=0)
color_rule = Label(tab2, text='To start the game press the \'Start Game\' button!')
color_rule.grid(row=0, column=0)
color_rule_2 = Label(tab2, text='Don\'t add spaces when writing the name!')
color_rule_2.grid(row=1, column=0, sticky=W)

# list of possible colours
colors = ['red','blue','green','purple','black','yellow','orange','pink', 'cyan','brown']

#color game global variables (scores, colors, timeleft and if game is over)
text_color = ''
font_color_name = ''
color_player_score = 0
highscore = 0
timeleft = 60
gameover = False

#open & save highscore (uses encoding utf-8 because my device has some issues
# with decoding)
with open('highscore.txt', 'r') as f:
    fileData = f.read()
hscore = fileData.encode('utf-8').strip()
if hscore.strip():
    hscore = int(hscore)
highscore = int(hscore)

#create a 60 second timer 
def startCountdown():
    global timeleft
    global gameover
    if timeleft > 0:
        timeleft -= 1
        timelabel.config(text=f'Time left: {timeleft}')
        timelabel.after(1000, startCountdown)
    else:
        gameover = True
        color_bttn_start.config(text='Start Game')

#generate the colors for the text (color name and color of text)
def generate_colors():
    global text_color
    global font_color_name
    global colors
    text_color = random.choice(colors)
    while font_color_name == text_color:
        text_color = random.choice(colors) #repeats a continous loop until
        # text_color is different from font_color_name
    font_color_name = random.choice(colors)
    while text_color == font_color_name:
        font_color_name = random.choice(colors) #repeats a continous loop until
        # font_color_name is different from text_color
    color_text_lbl.config(fg=text_color)
    color_text_lbl.config(text=font_color_name.upper())

#check if the color entered is right, print scores/highscores and generate new colors
def color_entered():
    global text_color
    global color_player_score
    global highscore
    global timeleft
    global gameover
    user_font_color_name = txt.get().lower()
    if timeleft < 1:
        gameover = True
    if user_font_color_name == text_color and timeleft > 0:
        color_player_score += 1
        txt.delete(0, END)
        if highscore < color_player_score:
            highscore = color_player_score
            f = open('highscore.txt', 'w')
            f.write(str(highscore))
            f.close()
        generate_colors()
    elif timeleft > 0:
        generate_colors()
        color_bttn_start.config(text='Start Game')
    color_player_score_lbl.config(text=f'Score: {color_player_score}')
    highscore_lbl.config(text=f'Highscore: {highscore}')

#start the color game
def startgame():
    global text_color
    global color_player_score
    global highscore
    global timeleft
    global gameover
    color_player_score = 0
    timeleft = 60
    gameover = False
    color_player_score_lbl.config(text=f'Score: {color_player_score}')
    generate_colors()
    startCountdown()
    color_bttn_start.config(text='Restart Game')


#create color label
color_text_lbl = Label(tab2, text='', font=('Helvetica', 30), fg='#ff0')
color_text_lbl.grid(row=4, column=5)

#entry textbox to enter answer
txt = Entry(tab2, width=10)
txt.grid(row=5, column=5, sticky=W+E)

#create a time label
timelabel = Label(tab2, text='')
timelabel.grid(row=9, column=0, sticky=W)

#create a button to check entered text in textbox
color_bttn = Button(tab2, text='Enter!', command=color_entered)
color_bttn.grid(row=5, column=6, sticky=W+E)

#display scores (score and highscore)
color_player_score_lbl = Label(tab2, text=f'Score: {color_player_score}')
color_player_score_lbl.grid(row=10, column=0, sticky=W)
highscore_lbl = Label(tab2, text=f'Highscore: {highscore}')
highscore_lbl.grid(row=11, column=0, sticky=W)

#create a button with the option to replay or restart a game
color_bttn_start = Button(tab2, text='Start Game', command=startgame)
color_bttn_start.grid(row=0, column=6, sticky=W+E)

#focus the cursor in the textbox
txt.focus()

# view actual program
window.mainloop()