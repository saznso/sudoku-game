# holy moly this took way too long
# this is a sudoku game with multiple functions
# fill function fills the board with sudoku grid the base difficulty is easy
# solve function solves the sudoku
# clear function clears the board
# check function checks if what you entered is correct and displays a colour change accordingly
# then gamemode change function is self explanatory as with most of these tbh
# this game uses some API that i found to generate sudoku becuase if wouldve be too hard otherwise

import requests
import tkinter as tk
from tkinter import messagebox

mode = ['easy'] # using a list because lists are global


def hard_mode(): 

    mode[0] = 'hard'

    messagebox.showinfo('hard', 'gamemode set to hard')

def medium_mode():

    mode[0] = 'medium'

    messagebox.showinfo('medium', 'gamemode set to medium')

def easy_mode():

    mode[0] = 'easy'

    messagebox.showinfo('easy', 'gamemode set to easy')


def gen_board(): # generates the board using this API

    response = requests.get('https://sugoku.herokuapp.com/board?difficulty='+mode[0])
    grid = response.json()['board']

    return grid

def clear_board(): 

    # row 1
    
    one1.config(state = 'normal', fg = 'blue', bg = 'lavender') 
    one1.delete(0, tk.END)
    one2.config(state = 'normal', fg = 'blue', bg = 'lavender')
    one2.delete(0, tk.END)
    one3.config(state = 'normal', fg = 'blue', bg = 'lavender')
    one3.delete(0, tk.END)
    one4.config(state = 'normal', fg = 'blue', bg = 'lavender')
    one4.delete(0, tk.END)
    one5.config(state = 'normal', fg = 'blue', bg = 'lavender')
    one5.delete(0, tk.END)
    one6.config(state = 'normal', fg = 'blue', bg = 'lavender')
    one6.delete(0, tk.END)
    one7.config(state = 'normal', fg = 'blue', bg = 'lavender')
    one7.delete(0, tk.END)
    one8.config(state = 'normal', fg = 'blue', bg = 'lavender')
    one8.delete(0, tk.END)
    one9.config(state = 'normal', fg = 'blue', bg = 'lavender')
    one9.delete(0, tk.END)

    # row 2

    two1.config(state = 'normal', fg = 'blue', bg = 'lavender')
    two1.delete(0, tk.END)
    two2.config(state = 'normal', fg = 'blue', bg = 'lavender')
    two2.delete(0, tk.END)
    two3.config(state = 'normal', fg = 'blue', bg = 'lavender')
    two3.delete(0, tk.END)
    two4.config(state = 'normal', fg = 'blue', bg = 'lavender')
    two4.delete(0, tk.END)
    two5.config(state = 'normal', fg = 'blue', bg = 'lavender')
    two5.delete(0, tk.END)
    two6.config(state = 'normal', fg = 'blue', bg = 'lavender')
    two6.delete(0, tk.END)
    two7.config(state = 'normal', fg = 'blue', bg = 'lavender')
    two7.delete(0, tk.END)
    two8.config(state = 'normal', fg = 'blue', bg = 'lavender')
    two8.delete(0, tk.END)
    two9.config(state = 'normal', fg = 'blue', bg = 'lavender')
    two9.delete(0, tk.END)

    # row 3

    three1.config(state = 'normal', fg = 'blue', bg = 'lavender')
    three1.delete(0, tk.END)
    three2.config(state = 'normal', fg = 'blue', bg = 'lavender')
    three2.delete(0, tk.END)
    three3.config(state = 'normal', fg = 'blue', bg = 'lavender')
    three3.delete(0, tk.END)
    three4.config(state = 'normal', fg = 'blue', bg = 'lavender')
    three4.delete(0, tk.END)
    three5.config(state = 'normal', fg = 'blue', bg = 'lavender')
    three5.delete(0, tk.END)
    three6.config(state = 'normal', fg = 'blue', bg = 'lavender')
    three6.delete(0, tk.END)
    three7.config(state = 'normal', fg = 'blue', bg = 'lavender')
    three7.delete(0, tk.END)
    three8.config(state = 'normal', fg = 'blue', bg = 'lavender')
    three8.delete(0, tk.END)
    three9.config(state = 'normal', fg = 'blue', bg = 'lavender')
    three9.delete(0, tk.END)

    # row 4

    four1.config(state = 'normal', fg = 'blue', bg = 'lavender')
    four1.delete(0, tk.END)
    four2.config(state = 'normal', fg = 'blue', bg = 'lavender')
    four2.delete(0, tk.END)
    four3.config(state = 'normal', fg = 'blue', bg = 'lavender')
    four3.delete(0, tk.END)
    four4.config(state = 'normal', fg = 'blue', bg = 'lavender')
    four4.delete(0, tk.END)
    four5.config(state = 'normal', fg = 'blue', bg = 'lavender')
    four5.delete(0, tk.END)
    four6.config(state = 'normal', fg = 'blue', bg = 'lavender')
    four6.delete(0, tk.END)
    four7.config(state = 'normal', fg = 'blue', bg = 'lavender')
    four7.delete(0, tk.END)
    four8.config(state = 'normal', fg = 'blue', bg = 'lavender')
    four8.delete(0, tk.END)
    four9.config(state = 'normal', fg = 'blue', bg = 'lavender')
    four9.delete(0, tk.END)

    # row 5

    five1.config(state = 'normal', fg = 'blue', bg = 'lavender')
    five1.delete(0, tk.END)
    five2.config(state = 'normal', fg = 'blue', bg = 'lavender')
    five2.delete(0, tk.END)
    five3.config(state = 'normal', fg = 'blue', bg = 'lavender')
    five3.delete(0, tk.END)
    five4.config(state = 'normal', fg = 'blue', bg = 'lavender')
    five4.delete(0, tk.END)
    five5.config(state = 'normal', fg = 'blue', bg = 'lavender')
    five5.delete(0, tk.END)
    five6.config(state = 'normal', fg = 'blue', bg = 'lavender')
    five6.delete(0, tk.END)
    five7.config(state = 'normal', fg = 'blue', bg = 'lavender')
    five7.delete(0, tk.END)
    five8.config(state = 'normal', fg = 'blue', bg = 'lavender')
    five8.delete(0, tk.END)
    five9.config(state = 'normal', fg = 'blue', bg = 'lavender')
    five9.delete(0, tk.END)

    # row 6

    six1.config(state = 'normal', fg = 'blue', bg = 'lavender')
    six1.delete(0, tk.END)
    six2.config(state = 'normal', fg = 'blue', bg = 'lavender')
    six2.delete(0, tk.END)
    six3.config(state = 'normal', fg = 'blue', bg = 'lavender')
    six3.delete(0, tk.END)
    six4.config(state = 'normal', fg = 'blue', bg = 'lavender')
    six4.delete(0, tk.END)
    six5.config(state = 'normal', fg = 'blue', bg = 'lavender')
    six5.delete(0, tk.END)
    six6.config(state = 'normal', fg = 'blue', bg = 'lavender')
    six6.delete(0, tk.END)
    six7.config(state = 'normal', fg = 'blue', bg = 'lavender')
    six7.delete(0, tk.END)
    six8.config(state = 'normal', fg = 'blue', bg = 'lavender')
    six8.delete(0, tk.END)
    six9.config(state = 'normal', fg = 'blue', bg = 'lavender')
    six9.delete(0, tk.END)

    # row 7

    seven1.config(state = 'normal', fg = 'blue', bg = 'lavender')
    seven1.delete(0, tk.END)
    seven2.config(state = 'normal', fg = 'blue', bg = 'lavender')
    seven2.delete(0, tk.END)
    seven3.config(state = 'normal', fg = 'blue', bg = 'lavender')
    seven3.delete(0, tk.END)
    seven4.config(state = 'normal', fg = 'blue', bg = 'lavender')
    seven4.delete(0, tk.END)
    seven5.config(state = 'normal', fg = 'blue', bg = 'lavender')
    seven5.delete(0, tk.END)
    seven6.config(state = 'normal', fg = 'blue', bg = 'lavender')
    seven6.delete(0, tk.END)
    seven7.config(state = 'normal', fg = 'blue', bg = 'lavender')
    seven7.delete(0, tk.END)
    seven8.config(state = 'normal', fg = 'blue', bg = 'lavender')
    seven8.delete(0, tk.END)
    seven9.config(state = 'normal', fg = 'blue', bg = 'lavender')
    seven9.delete(0, tk.END)

    # row 8

    eight1.config(state = 'normal', fg = 'blue', bg = 'lavender')
    eight1.delete(0, tk.END)
    eight2.config(state = 'normal', fg = 'blue', bg = 'lavender')
    eight2.delete(0, tk.END)
    eight3.config(state = 'normal', fg = 'blue', bg = 'lavender')
    eight3.delete(0, tk.END)
    eight4.config(state = 'normal', fg = 'blue', bg = 'lavender')
    eight4.delete(0, tk.END)
    eight5.config(state = 'normal', fg = 'blue', bg = 'lavender')
    eight5.delete(0, tk.END)
    eight6.config(state = 'normal', fg = 'blue', bg = 'lavender')
    eight6.delete(0, tk.END)
    eight7.config(state = 'normal', fg = 'blue', bg = 'lavender')
    eight7.delete(0, tk.END)
    eight8.config(state = 'normal', fg = 'blue', bg = 'lavender')
    eight8.delete(0, tk.END)
    eight9.config(state = 'normal', fg = 'blue', bg = 'lavender')
    eight9.delete(0, tk.END)

    # row 9

    nine1.config(state = 'normal', fg = 'blue', bg = 'lavender')
    nine1.delete(0, tk.END)
    nine2.config(state = 'normal', fg = 'blue', bg = 'lavender')
    nine2.delete(0, tk.END)
    nine3.config(state = 'normal', fg = 'blue', bg = 'lavender')
    nine3.delete(0, tk.END)
    nine4.config(state = 'normal', fg = 'blue', bg = 'lavender')
    nine4.delete(0, tk.END)
    nine5.config(state = 'normal', fg = 'blue', bg = 'lavender')
    nine5.delete(0, tk.END)
    nine6.config(state = 'normal', fg = 'blue', bg = 'lavender')
    nine6.delete(0, tk.END)
    nine7.config(state = 'normal', fg = 'blue', bg = 'lavender')
    nine7.delete(0, tk.END)
    nine8.config(state = 'normal', fg = 'blue', bg = 'lavender')
    nine8.delete(0, tk.END)
    nine9.config(state = 'normal', fg = 'blue', bg = 'lavender')
    nine9.delete(0, tk.END)
    
def fill_board():

    board = gen_board()
    clear_board()

    # row 1

    if board[0][0] != 0:

        one1.insert(0, board[0][0])
        one1.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        one1.config(bg = 'lavender')

    if board[0][1] != 0:

        one2.insert(0, board[0][1])
        one2.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        one2.config(bg = 'lavender')

    if board[0][2] != 0:

        one3.insert(0, board[0][2])
        one3.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        one3.config(bg = 'lavender')

    if board[0][3] != 0:

        one4.insert(0, board[0][3])
        one4.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        one4.config(bg = 'lavender')

    if board[0][4] != 0:

        one5.insert(0, board[0][4])
        one5.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        one5.config(bg = 'lavender')

    if board[0][5] != 0:

        one6.insert(0, board[0][5])
        one6.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        one6.config(bg = 'lavender')

    if board[0][6] != 0:

        one7.insert(0, board[0][6])
        one7.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        one7.config(bg = 'lavender')

    if board[0][7] != 0:

        one8.insert(0, board[0][7])
        one8.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        one8.config(bg = 'lavender')

    if board[0][8] != 0:

        one9.insert(0, board[0][8])
        one9.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        one9.config(bg = 'lavender')

    # row 2

    if board[1][0] != 0:

        two1.insert(0, board[1][0])
        two1.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        two1.config(bg = 'lavender')

    if board[1][1] != 0:

        two2.insert(0, board[1][1])
        two2.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        two2.config(bg = 'lavender')

    if board[1][2] != 0:

        two3.insert(0, board[1][2])
        two3.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        two3.config(bg = 'lavender')

    if board[1][3] != 0:

        two4.insert(0, board[1][3])
        two4.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        two4.config(bg = 'lavender')

    if board[1][4] != 0:

        two5.insert(0, board[1][4])
        two5.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        two5.config(bg = 'lavender')

    if board[1][5] != 0:

        two6.insert(0, board[1][5])
        two6.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        two6.config(bg = 'lavender')

    if board[1][6] != 0:

        two7.insert(0, board[1][6])
        two7.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        two7.config(bg = 'lavender')

    if board[1][7] != 0:

        two8.insert(0, board[1][7])
        two8.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        two8.config(bg = 'lavender')

    if board[1][8] != 0:

        two9.insert(0, board[1][8])
        two9.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        two9.config(bg = 'lavender')

    # row 3

    if board[2][0] != 0:

        three1.insert(0, board[2][0])
        three1.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        three1.config(bg = 'lavender')

    if board[2][1] != 0:

        three2.insert(0, board[2][1])
        three2.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        three2.config(bg = 'lavender')

    if board[2][2] != 0:

        three3.insert(0, board[2][2])
        three3.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        three3.config(bg = 'lavender')

    if board[2][3] != 0:

        three4.insert(0, board[2][3])
        three4.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        three4.config(bg = 'lavender')

    if board[2][4] != 0:

        three5.insert(0, board[2][4])
        three5.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        three5.config(bg = 'lavender')

    if board[2][5] != 0:

        three6.insert(0, board[2][5])
        three6.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        three6.config(bg = 'lavender')

    if board[2][6] != 0:

        three7.insert(0, board[2][6])
        three7.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        three7.config(bg = 'lavender')

    if board[2][7] != 0:

        three8.insert(0, board[2][7])
        three8.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        three8.config(bg = 'lavender')

    if board[2][8] != 0:

        three9.insert(0, board[2][8])
        three9.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        three9.config(bg = 'lavender')

    # row 4

    if board[3][0] != 0:

        four1.insert(0, board[3][0])
        four1.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        four1.config(bg = 'lavender')

    if board[3][1] != 0:

        four2.insert(0, board[3][1])
        four2.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        four2.config(bg = 'lavender')

    if board[3][2] != 0:

        four3.insert(0, board[3][2])
        four3.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        four3.config(bg = 'lavender')

    if board[3][3] != 0:

        four4.insert(0, board[3][3])
        four4.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        four4.config(bg = 'lavender')

    if board[3][4] != 0:

        four5.insert(0, board[3][4])
        four5.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        four5.config(bg = 'lavender')

    if board[3][5] != 0:

        four6.insert(0, board[3][5])
        four6.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        four6.config(bg = 'lavender')

    if board[3][6] != 0:

        four7.insert(0, board[3][6])
        four7.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        four7.config(bg = 'lavender')

    if board[3][7] != 0:

        four8.insert(0, board[3][7])
        four8.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        four8.config(bg = 'lavender')

    if board[3][8] != 0:

        four9.insert(0, board[3][8])
        four9.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        four9.config(bg = 'lavender')

    # row 5

    if board[4][0] != 0:

        five1.insert(0, board[4][0])
        five1.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        five1.config(bg = 'lavender')

    if board[4][1] != 0:

        five2.insert(0, board[4][1])
        five2.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        five2.config(bg = 'lavender')

    if board[4][2] != 0:

        five3.insert(0, board[4][2])
        five3.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        five3.config(bg = 'lavender')

    if board[4][3] != 0:

        five4.insert(0, board[4][3])
        five4.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        five4.config(bg = 'lavender')

    if board[4][4] != 0:

        five5.insert(0, board[4][4])
        five5.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        five5.config(bg = 'lavender')

    if board[4][5] != 0:

        five6.insert(0, board[4][5])
        five6.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        five6.config(bg = 'lavender')
        
    if board[4][6] != 0:

        five7.insert(0, board[4][6])
        five7.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        five7.config(bg = 'lavender')

    if board[4][7] != 0:

        five8.insert(0, board[4][7])
        five8.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        five8.config(bg = 'lavender')

    if board[4][8] != 0:

        five9.insert(0, board[4][8])
        five9.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        five9.config(bg = 'lavender')

    # row 6

    if board[5][0] != 0:

        six1.insert(0, board[5][0])
        six1.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        six1.config(bg = 'lavender')

    if board[5][1] != 0:

        six2.insert(0, board[5][1])
        six2.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        six2.config(bg = 'lavender')

    if board[5][2] != 0:

        six3.insert(0, board[5][2])
        six3.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        six3.config(bg = 'lavender')

    if board[5][3] != 0:

        six4.insert(0, board[5][3])
        six4.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        six4.config(bg = 'lavender')

    if board[5][4] != 0:

        six5.insert(0, board[5][4])
        six5.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        six5.config(bg = 'lavender')

    if board[5][5] != 0:

        six6.insert(0, board[5][5])
        six6.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        six6.config(bg = 'lavender')
        
    if board[5][6] != 0:

        six7.insert(0, board[5][6])
        six7.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        six7.config(bg = 'lavender')

    if board[5][7] != 0:

        six8.insert(0, board[5][7])
        six8.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        six8.config(bg = 'lavender')

    if board[5][8] != 0:

        six9.insert(0, board[5][8])
        six9.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        six9.config(bg = 'lavender')

    # row 7

    if board[6][0] != 0:

        seven1.insert(0, board[6][0])
        seven1.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        seven1.config(bg = 'lavender')

    if board[6][1] != 0:

        seven2.insert(0, board[6][1])
        seven2.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        seven2.config(bg = 'lavender')

    if board[6][2] != 0:
        seven3.insert(0, board[6][2])
        seven3.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        seven3.config(bg = 'lavender')

    if board[6][3] != 0:

        seven4.insert(0, board[6][3])
        seven4.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        seven4.config(bg = 'lavender')

    if board[6][4] != 0:

        seven5.insert(0, board[6][4])
        seven5.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        seven5.config(bg = 'lavender')

    if board[6][5] != 0:

        seven6.insert(0, board[6][5])
        seven6.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        seven6.config(bg = 'lavender')
        
    if board[6][6] != 0:

        seven7.insert(0, board[6][6])
        seven7.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        seven7.config(bg = 'lavender')

    if board[6][7] != 0:

        seven8.insert(0, board[6][7])
        seven8.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        seven8.config(bg = 'lavender')
        
    if board[6][8] != 0:

        seven9.insert(0, board[6][8])
        seven9.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        seven9.config(bg = 'lavender')

    # row 8

    if board[7][0] != 0:

        eight1.insert(0, board[7][0])
        eight1.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        eight1.config(bg = 'lavender')

    if board[7][1] != 0:

        eight2.insert(0, board[7][1])
        eight2.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        eight2.config(bg = 'lavender')

    if board[7][2] != 0:
        
        eight3.insert(0, board[7][2])
        eight3.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        eight3.config(bg = 'lavender')

    if board[7][3] != 0:

        eight4.insert(0, board[7][3])
        eight4.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        eight4.config(bg = 'lavender')

    if board[7][4] != 0:

        eight5.insert(0, board[7][4])
        eight5.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        eight5.config(bg = 'lavender')

    if board[7][5] != 0:

        eight6.insert(0, board[7][5])
        eight6.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        eight6.config(bg = 'lavender')
        
    if board[7][6] != 0:

        eight7.insert(0, board[7][6])
        eight7.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        eight7.config(bg = 'lavender')

    if board[7][7] != 0:

        eight8.insert(0, board[7][7])
        eight8.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        eight8.config(bg = 'lavender')

    if board[7][8] != 0:

        eight9.insert(0, board[7][8])
        eight9.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        eight9.config(bg = 'lavender')

    # row 9

    if board[8][0] != 0:

        nine1.insert(0, board[8][0])
        nine1.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        nine1.config(bg = 'lavender')

    if board[8][1] != 0:

        nine2.insert(0, board[8][1])
        nine2.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        nine2.config(bg = 'lavender')

    if board[8][2] != 0:
        
        nine3.insert(0, board[8][2])
        nine3.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        nine3.config(bg = 'lavender')

    if board[8][3] != 0:

        nine4.insert(0, board[8][3])
        nine4.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        nine4.config(bg = 'lavender')

    if board[8][4] != 0:

        nine5.insert(0, board[8][4])
        nine5.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        nine5.config(bg = 'lavender')

    if board[8][5] != 0:

        nine6.insert(0, board[8][5])
        nine6.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        nine6.config(bg = 'lavender')
        
    if board[8][6] != 0:

        nine7.insert(0, board[8][6])
        nine7.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        nine7.config(bg = 'lavender')

    if board[8][7] != 0:

        nine8.insert(0, board[8][7])
        nine8.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        nine8.config(bg = 'lavender')

    if board[8][8] != 0:

        nine9.insert(0, board[8][8])
        nine9.config(state = 'readonly', readonlybackground = 'lavender', fg = 'black')

    else:

        nine9.config(bg = 'lavender')

    return board


##board = []
##
##def enter_board():
##
##    print('enter numbers of sudoku board from left to right')
##
##    for i in range(9):
##
##        sub_board = []
##
##        print('row ' + str(i + 1))
##
##        for j in range(9):
##            
##            num = int(input(str(j + 1) + ': '))
##            
##            sub_board.append(num)
##
##        board.append(sub_board)
##
##    return board
##
##board = enter_board()

def solve(board):

    find = find_empty(board)

    if not find:

        return True

    else: # find empty function returned a value indicating there is an  empty space

        row, col = find

    for i in range(1,10):

        if valid(board, i, (row, col)):

            board[row][col] = i
        
            if solve(board): 

                return True

            board[row][col] = 0 # if number we just tested doesnt work remove from board then go back try again with a different value

    return False

def valid(board, num, pos):

    # row

    for i in range(len(board[0])):

        if board[pos[0]][i] == num and pos[1] != i:

            return False

    # column

    for i in range(len(board)):

        if board[i][pos[1]] == num and pos[0] != 1:

            return False

    # 3 x 30

    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y * 3, box_y * 3 + 3):

        for j in range(box_x * 3, box_x * 3 + 3):

            if board[i][j] == num and (i, j) != pos:

                return False

    return True

def print_board():

    for i in range(len(board)):
        
        if i % 3 == 0 and i != 0:

            print('- - - - - - - - - - - -') 

        for j in range(len(board[0])):

            if j % 3 == 0 and j != 0:

                print(' | ', end = '') 

            if j == 8:

                print(board[i][j]) 

            else:

                print(str(board[i][j]) + ' ', end = '')

def find_empty(board):

    for i in range(len(board)):

        for j in range(len(board[0])):

            if board[i][j] == 0:

                return (i, j) # row, column

    return None

#solve()

def fill_solved():

    board = []
    sub_board = []

    # taking the current board

    # row 1

    if one1['state'] == 'readonly':

        sub_board.append(int(one1.get()))

    else:

        sub_board.append(0)

    if one2['state'] == 'readonly':

        sub_board.append(int(one2.get()))

    else:

        sub_board.append(0)

    if one3['state'] == 'readonly':

        sub_board.append(int(one3.get()))

    else:

        sub_board.append(0)

    if one4['state'] == 'readonly':

        sub_board.append(int(one4.get()))

    else:

        sub_board.append(0)

    if one5['state'] == 'readonly':

        sub_board.append(int(one5.get()))

    else:

        sub_board.append(0)

    if one6['state'] == 'readonly':

        sub_board.append(int(one6.get()))

    else:

        sub_board.append(0)

    if one7['state'] == 'readonly':

        sub_board.append(int(one7.get()))

    else:

        sub_board.append(0)

    if one8['state'] == 'readonly':

        sub_board.append(int(one8.get()))

    else:

        sub_board.append(0)

    if one9['state'] == 'readonly':

        sub_board.append(int(one9.get()))

    else:

        sub_board.append(0)

    board.append(sub_board)
    sub_board = []

    # row 2

    if two1['state'] == 'readonly':

        sub_board.append(int(two1.get()))

    else:

        sub_board.append(0)

    if two2['state'] == 'readonly':

        sub_board.append(int(two2.get()))

    else:

        sub_board.append(0)

    if two3['state'] == 'readonly':

        sub_board.append(int(two3.get()))

    else:

        sub_board.append(0)

    if two4['state'] == 'readonly':

        sub_board.append(int(two4.get()))

    else:

        sub_board.append(0)

    if two5['state'] == 'readonly':

        sub_board.append(int(two5.get()))

    else:

        sub_board.append(0)

    if two6['state'] == 'readonly':

        sub_board.append(int(two6.get()))

    else:

        sub_board.append(0)

    if two7['state'] == 'readonly':

        sub_board.append(int(two7.get()))

    else:

        sub_board.append(0)

    if two8['state'] == 'readonly':

        sub_board.append(int(two8.get()))

    else:

        sub_board.append(0)

    if two9['state'] == 'readonly':

        sub_board.append(int(two9.get()))

    else:

        sub_board.append(0)

    board.append(sub_board)
    sub_board = []

    # row 3

    if three1['state'] == 'readonly':

        sub_board.append(int(three1.get()))

    else:

        sub_board.append(0)

    if three2['state'] == 'readonly':

        sub_board.append(int(three2.get()))

    else:

        sub_board.append(0)

    if three3['state'] == 'readonly':

        sub_board.append(int(three3.get()))

    else:

        sub_board.append(0)

    if three4['state'] == 'readonly':

        sub_board.append(int(three4.get()))

    else:

        sub_board.append(0)

    if three5['state'] == 'readonly':

        sub_board.append(int(three5.get()))

    else:

        sub_board.append(0)

    if three6['state'] == 'readonly':

        sub_board.append(int(three6.get()))

    else:

        sub_board.append(0)

    if three7['state'] == 'readonly':

        sub_board.append(int(three7.get()))

    else:

        sub_board.append(0)

    if three8['state'] == 'readonly':

        sub_board.append(int(three8.get()))

    else:

        sub_board.append(0)

    if three9['state'] == 'readonly':

        sub_board.append(int(three9.get()))

    else:

        sub_board.append(0)

    board.append(sub_board)
    sub_board = []

    # row 4

    if four1['state'] == 'readonly':

        sub_board.append(int(four1.get()))

    else:

        sub_board.append(0)

    if four2['state'] == 'readonly':

        sub_board.append(int(four2.get()))

    else:

        sub_board.append(0)

    if four3['state'] == 'readonly':

        sub_board.append(int(four3.get()))

    else:

        sub_board.append(0)

    if four4['state'] == 'readonly':

        sub_board.append(int(four4.get()))

    else:

        sub_board.append(0)

    if four5['state'] == 'readonly':

        sub_board.append(int(four5.get()))

    else:

        sub_board.append(0)

    if four6['state'] == 'readonly':

        sub_board.append(int(four6.get()))

    else:

        sub_board.append(0)

    if four7['state'] == 'readonly':

        sub_board.append(int(four7.get()))

    else:

        sub_board.append(0)

    if four8['state'] == 'readonly':

        sub_board.append(int(four8.get()))

    else:

        sub_board.append(0)

    if four9['state'] == 'readonly':

        sub_board.append(int(four9.get()))

    else:

        sub_board.append(0)

    board.append(sub_board)
    sub_board = []

    # row 5

    if five1['state'] == 'readonly':

        sub_board.append(int(five1.get()))

    else:

        sub_board.append(0)

    if five2['state'] == 'readonly':

        sub_board.append(int(five2.get()))

    else:

        sub_board.append(0)

    if five3['state'] == 'readonly':

        sub_board.append(int(five3.get()))

    else:

        sub_board.append(0)

    if five4['state'] == 'readonly':

        sub_board.append(int(five4.get()))

    else:

        sub_board.append(0)

    if five5['state'] == 'readonly':

        sub_board.append(int(five5.get()))

    else:

        sub_board.append(0)

    if five6['state'] == 'readonly':

        sub_board.append(int(five6.get()))

    else:

        sub_board.append(0)

    if five7['state'] == 'readonly':

        sub_board.append(int(five7.get()))

    else:

        sub_board.append(0)

    if five8['state'] == 'readonly':

        sub_board.append(int(five8.get()))

    else:

        sub_board.append(0)

    if five9['state'] == 'readonly':

        sub_board.append(int(five9.get()))

    else:

        sub_board.append(0)

    board.append(sub_board)
    sub_board = []

    # row 6

    if six1['state'] == 'readonly':

        sub_board.append(int(six1.get()))

    else:

        sub_board.append(0)

    if six2['state'] == 'readonly':

        sub_board.append(int(six2.get()))

    else:

        sub_board.append(0)

    if six3['state'] == 'readonly':

        sub_board.append(int(six3.get()))

    else:

        sub_board.append(0)

    if six4['state'] == 'readonly':

        sub_board.append(int(six4.get()))

    else:

        sub_board.append(0)

    if six5['state'] == 'readonly':

        sub_board.append(int(six5.get()))

    else:

        sub_board.append(0)

    if six6['state'] == 'readonly':

        sub_board.append(int(six6.get()))

    else:

        sub_board.append(0)

    if six7['state'] == 'readonly':

        sub_board.append(int(six7.get()))

    else:

        sub_board.append(0)

    if six8['state'] == 'readonly':

        sub_board.append(int(six8.get()))

    else:

        sub_board.append(0)

    if six9['state'] == 'readonly':

        sub_board.append(int(six9.get()))

    else:

        sub_board.append(0)

    board.append(sub_board)
    sub_board = []

    # row 7

    if seven1['state'] == 'readonly':

        sub_board.append(int(seven1.get()))

    else:

        sub_board.append(0)

    if seven2['state'] == 'readonly':

        sub_board.append(int(seven2.get()))

    else:

        sub_board.append(0)

    if seven3['state'] == 'readonly':

        sub_board.append(int(seven3.get()))

    else:

        sub_board.append(0)

    if seven4['state'] == 'readonly':

        sub_board.append(int(seven4.get()))

    else:

        sub_board.append(0)

    if seven5['state'] == 'readonly':

        sub_board.append(int(seven5.get()))

    else:

        sub_board.append(0)

    if seven6['state'] == 'readonly':

        sub_board.append(int(seven6.get()))

    else:

        sub_board.append(0)

    if seven7['state'] == 'readonly':

        sub_board.append(int(seven7.get()))

    else:

        sub_board.append(0)

    if seven8['state'] == 'readonly':

        sub_board.append(int(seven8.get()))

    else:

        sub_board.append(0)

    if seven9['state'] == 'readonly':

        sub_board.append(int(seven9.get()))

    else:

        sub_board.append(0)

    board.append(sub_board)
    sub_board = []

    # row 8

    if eight1['state'] == 'readonly':

        sub_board.append(int(eight1.get()))

    else:

        sub_board.append(0)

    if eight2['state'] == 'readonly':

        sub_board.append(int(eight2.get()))

    else:

        sub_board.append(0)

    if eight3['state'] == 'readonly':

        sub_board.append(int(eight3.get()))

    else:

        sub_board.append(0)

    if eight4['state'] == 'readonly':

        sub_board.append(int(eight4.get()))

    else:

        sub_board.append(0)

    if eight5['state'] == 'readonly':

        sub_board.append(int(eight5.get()))

    else:

        sub_board.append(0)

    if eight6['state'] == 'readonly':

        sub_board.append(int(eight6.get()))

    else:

        sub_board.append(0)

    if eight7['state'] == 'readonly':

        sub_board.append(int(eight7.get()))

    else:

        sub_board.append(0)

    if eight8['state'] == 'readonly':

        sub_board.append(int(eight8.get()))

    else:

        sub_board.append(0)

    if eight9['state'] == 'readonly':

        sub_board.append(int(eight9.get()))

    else:

        sub_board.append(0)

    board.append(sub_board)
    sub_board = []

    # row 9

    if nine1['state'] == 'readonly':

        sub_board.append(int(nine1.get()))

    else:

        sub_board.append(0)

    if nine2['state'] == 'readonly':

        sub_board.append(int(nine2.get()))

    else:

        sub_board.append(0)

    if nine3['state'] == 'readonly':

        sub_board.append(int(nine3.get()))

    else:

        sub_board.append(0)

    if nine4['state'] == 'readonly':

        sub_board.append(int(nine4.get()))

    else:

        sub_board.append(0)

    if nine5['state'] == 'readonly':

        sub_board.append(int(nine5.get()))

    else:

        sub_board.append(0)

    if nine6['state'] == 'readonly':

        sub_board.append(int(nine6.get()))

    else:

        sub_board.append(0)

    if nine7['state'] == 'readonly':

        sub_board.append(int(nine7.get()))

    else:

        sub_board.append(0)

    if nine8['state'] == 'readonly':

        sub_board.append(int(nine8.get()))

    else:

        sub_board.append(0)

    if nine9['state'] == 'readonly':

        sub_board.append(int(nine9.get()))

    else:

        sub_board.append(0)

    board.append(sub_board)
    
    solve(board)

    # inserting the solved board into the free spaces

    # row 1

    if one1['state'] == 'normal':

        one1.delete(0, tk.END)
        one1.insert(0, board[0][0])
        one1.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if one2['state'] == 'normal':

        one2.delete(0, tk.END)
        one2.insert(0, board[0][1])
        one2.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if one3['state'] == 'normal':

        one3.delete(0, tk.END)
        one3.insert(0, board[0][2])
        one3.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if one4['state'] == 'normal':

        one4.delete(0, tk.END)
        one4.insert(0, board[0][3])
        one4.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if one5['state'] == 'normal':

        one5.delete(0, tk.END)
        one5.insert(0, board[0][4])
        one5.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if one6['state'] == 'normal':
        
        one6.delete(0, tk.END)
        one6.insert(0, board[0][5])
        one6.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if one7['state'] == 'normal':

        one7.delete(0, tk.END)
        one7.insert(0, board[0][6])
        one7.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if one8['state'] == 'normal':

        one8.delete(0, tk.END)
        one8.insert(0, board[0][7])
        one8.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if one9['state'] == 'normal':

        one9.delete(0, tk.END)
        one9.insert(0, board[0][8])
        one9.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    # row 2

    if two1['state'] == 'normal':

        two1.delete(0, tk.END)
        two1.insert(0, board[1][0])
        two1.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if two2['state'] == 'normal':

        two2.delete(0, tk.END)
        two2.insert(0, board[1][1])
        two2.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if two3['state'] == 'normal':

        two3.delete(0, tk.END)
        two3.insert(0, board[1][2])
        two3.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if two4['state'] == 'normal':

        two4.delete(0, tk.END)
        two4.insert(0, board[1][3])
        two4.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if two5['state'] == 'normal':

        two5.delete(0, tk.END)
        two5.insert(0, board[1][4])
        two5.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if two6['state'] == 'normal':

        two6.delete(0, tk.END)
        two6.insert(0, board[1][5])
        two6.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if two7['state'] == 'normal':

        two7.delete(0, tk.END)
        two7.insert(0, board[1][6])
        two7.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if two8['state'] == 'normal':

        two8.delete(0, tk.END)
        two8.insert(0, board[1][7])
        two8.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if two9['state'] == 'normal':

        two9.delete(0, tk.END)
        two9.insert(0, board[1][8])
        two9.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    # row 3

    if three1['state'] == 'normal':

        three1.delete(0, tk.END)
        three1.insert(0, board[2][0])
        three1.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if three2['state'] == 'normal':

        three2.delete(0, tk.END)
        three2.insert(0, board[2][1])
        three2.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if three3['state'] == 'normal':

        three3.delete(0, tk.END)
        three3.insert(0, board[2][2])
        three3.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if three4['state'] == 'normal':

        three4.delete(0, tk.END)
        three4.insert(0, board[2][3])
        three4.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if three5['state'] == 'normal':

        three5.delete(0, tk.END)
        three5.insert(0, board[2][4])
        three5.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if three6['state'] == 'normal':

        three6.delete(0, tk.END)
        three6.insert(0, board[2][5])
        three6.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if three7['state'] == 'normal':

        three7.delete(0, tk.END)
        three7.insert(0, board[2][6])
        three7.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if three8['state'] == 'normal':

        three8.delete(0, tk.END)
        three8.insert(0, board[2][7])
        three8.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if three9['state'] == 'normal':

        three9.delete(0, tk.END)
        three9.insert(0, board[2][8])
        three9.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    # row 4

    if four1['state'] == 'normal':

        four1.delete(0, tk.END)
        four1.insert(0, board[3][0])
        four1.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if four2['state'] == 'normal':

        four2.delete(0, tk.END)
        four2.insert(0, board[3][1])
        four2.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if four3['state'] == 'normal':

        four3.delete(0, tk.END)
        four3.insert(0, board[3][2])
        four3.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if four4['state'] == 'normal':

        four4.delete(0, tk.END)
        four4.insert(0, board[3][3])
        four4.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if four5['state'] == 'normal':

        four5.delete(0, tk.END)
        four5.insert(0, board[3][4])
        four5.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if four6['state'] == 'normal':

        four6.delete(0, tk.END)
        four6.insert(0, board[3][5])
        four6.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if four7['state'] == 'normal':

        four7.delete(0, tk.END)
        four7.insert(0, board[3][6])
        four7.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if four8['state'] == 'normal':

        four8.delete(0, tk.END)
        four8.insert(0, board[3][7])
        four8.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if four9['state'] == 'normal':

        four9.delete(0, tk.END)
        four9.insert(0, board[3][8])
        four9.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    # row 5

    if five1['state'] == 'normal':

        five1.delete(0, tk.END)
        five1.insert(0, board[4][0])
        five1.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if five2['state'] == 'normal':

        five2.delete(0, tk.END)
        five2.insert(0, board[4][1])
        five2.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if five3['state'] == 'normal':

        five3.delete(0, tk.END)
        five3.insert(0, board[4][2])
        five3.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if five4['state'] == 'normal':

        five4.delete(0, tk.END)
        five4.insert(0, board[4][3])
        five4.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if five5['state'] == 'normal':

        five5.delete(0, tk.END)
        five5.insert(0, board[4][4])
        five5.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if five6['state'] == 'normal':

        five6.delete(0, tk.END)
        five6.insert(0, board[4][5])
        five6.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')
        
    if five7['state'] == 'normal':

        five7.delete(0, tk.END)
        five7.insert(0, board[4][6])
        five7.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if five8['state'] == 'normal':

        five8.delete(0, tk.END)
        five8.insert(0, board[4][7])
        five8.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if five9['state'] == 'normal':

        five9.delete(0, tk.END)
        five9.insert(0, board[4][8])
        five9.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    # row 6

    if six1['state'] == 'normal':

        six1.delete(0, tk.END)
        six1.insert(0, board[5][0])
        six1.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if six2['state'] == 'normal':

        six2.delete(0, tk.END)
        six2.insert(0, board[5][1])
        six2.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if six3['state'] == 'normal':

        six3.delete(0, tk.END)
        six3.insert(0, board[5][2])
        six3.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if six4['state'] == 'normal':

        six4.delete(0, tk.END)
        six4.insert(0, board[5][3])
        six4.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if six5['state'] == 'normal':

        six5.delete(0, tk.END)
        six5.insert(0, board[5][4])
        six5.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if six6['state'] == 'normal':

        six6.delete(0, tk.END)
        six6.insert(0, board[5][5])
        six6.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')
        
    if six7['state'] == 'normal':

        six7.delete(0, tk.END)
        six7.insert(0, board[5][6])
        six7.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if six8['state'] == 'normal':

        six8.delete(0, tk.END)
        six8.insert(0, board[5][7])
        six8.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if six9['state'] == 'normal':

        six9.delete(0, tk.END)
        six9.insert(0, board[5][8])
        six9.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    # row 7

    if seven1['state'] == 'normal':

        seven1.delete(0, tk.END)
        seven1.insert(0, board[6][0])
        seven1.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if seven2['state'] == 'normal':

        seven2.delete(0, tk.END)
        seven2.insert(0, board[6][1])
        seven2.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if seven3['state'] == 'normal':

        seven3.delete(0, tk.END)        
        seven3.insert(0, board[6][2])
        seven3.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if seven4['state'] == 'normal':

        seven4.delete(0, tk.END)
        seven4.insert(0, board[6][3])
        seven4.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if seven5['state'] == 'normal':

        seven5.delete(0, tk.END)
        seven5.insert(0, board[6][4])
        seven5.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if seven6['state'] == 'normal':

        seven6.delete(0, tk.END)
        seven6.insert(0, board[6][5])
        seven6.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')
        
    if seven7['state'] == 'normal':

        seven7.delete(0, tk.END)
        seven7.insert(0, board[6][6])
        seven7.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if seven8['state'] == 'normal':

        seven8.delete(0, tk.END)
        seven8.insert(0, board[6][7])
        seven8.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if seven9['state'] == 'normal':

        seven9.delete(0, tk.END)
        seven9.insert(0, board[6][8])
        seven9.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    # row 8

    if eight1['state'] == 'normal':

        eight1.delete(0, tk.END)
        eight1.insert(0, board[7][0])
        eight1.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if eight2['state'] == 'normal':

        eight2.delete(0, tk.END)
        eight2.insert(0, board[7][1])
        eight2.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if eight3['state'] == 'normal':

        eight3.delete(0, tk.END)        
        eight3.insert(0, board[7][2])
        eight3.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if eight4['state'] == 'normal':

        eight4.delete(0, tk.END)
        eight4.insert(0, board[7][3])
        eight4.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if eight5['state'] == 'normal':

        eight5.delete(0, tk.END)
        eight5.insert(0, board[7][4])
        eight5.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if eight6['state'] == 'normal':
        
        eight6.delete(0, tk.END)
        eight6.insert(0, board[7][5])
        eight6.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')
        
    if eight7['state'] == 'normal':

        eight7.delete(0, tk.END)
        eight7.insert(0, board[7][6])
        eight7.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if eight8['state'] == 'normal':

        eight8.delete(0, tk.END)
        eight8.insert(0, board[7][7])
        eight8.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if eight9['state'] == 'normal':

        eight9.delete(0, tk.END)
        eight9.insert(0, board[7][8])
        eight9.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    # row 9

    if nine1['state'] == 'normal':

        nine1.delete(0, tk.END)
        nine1.insert(0, board[8][0])
        nine1.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if nine2['state'] == 'normal':

        nine2.delete(0, tk.END)
        nine2.insert(0, board[8][1])
        nine2.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if nine3['state'] == 'normal':

        nine3.delete(0, tk.END)        
        nine3.insert(0, board[8][2])
        nine3.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if nine4['state'] == 'normal':

        nine4.delete(0, tk.END)
        nine4.insert(0, board[8][3])
        nine4.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if nine5['state'] == 'normal':

        nine5.delete(0, tk.END)
        nine5.insert(0, board[8][4])
        nine5.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if nine6['state'] == 'normal':

        nine6.delete(0, tk.END)
        nine6.insert(0, board[8][5])
        nine6.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')
        
    if nine7['state'] == 'normal':

        nine7.delete(0, tk.END)
        nine7.insert(0, board[8][6])
        nine7.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if nine8['state'] == 'normal':

        nine8.delete(0, tk.END)
        nine8.insert(0, board[8][7])
        nine8.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

    if nine9['state'] == 'normal':

        nine9.delete(0, tk.END)
        nine9.insert(0, board[8][8])
        nine9.config(state = 'readonly', readonlybackground = 'lavender', fg = 'red')

def check_board():

    board = []
    sub_board = []

    # create the solved board

    # row 1

    if one1['state'] == 'readonly':

        sub_board.append(int(one1.get()))

    else:

        sub_board.append(0)

    if one2['state'] == 'readonly':

        sub_board.append(int(one2.get()))

    else:

        sub_board.append(0)

    if one3['state'] == 'readonly':

        sub_board.append(int(one3.get()))

    else:

        sub_board.append(0)

    if one4['state'] == 'readonly':

        sub_board.append(int(one4.get()))

    else:

        sub_board.append(0)

    if one5['state'] == 'readonly':

        sub_board.append(int(one5.get()))

    else:

        sub_board.append(0)

    if one6['state'] == 'readonly':

        sub_board.append(int(one6.get()))

    else:

        sub_board.append(0)

    if one7['state'] == 'readonly':

        sub_board.append(int(one7.get()))

    else:

        sub_board.append(0)

    if one8['state'] == 'readonly':

        sub_board.append(int(one8.get()))

    else:

        sub_board.append(0)

    if one9['state'] == 'readonly':

        sub_board.append(int(one9.get()))

    else:

        sub_board.append(0)

    board.append(sub_board)
    sub_board = []

    # row 2

    if two1['state'] == 'readonly':

        sub_board.append(int(two1.get()))

    else:

        sub_board.append(0)

    if two2['state'] == 'readonly':

        sub_board.append(int(two2.get()))

    else:

        sub_board.append(0)

    if two3['state'] == 'readonly':

        sub_board.append(int(two3.get()))

    else:

        sub_board.append(0)

    if two4['state'] == 'readonly':

        sub_board.append(int(two4.get()))

    else:

        sub_board.append(0)

    if two5['state'] == 'readonly':

        sub_board.append(int(two5.get()))

    else:

        sub_board.append(0)

    if two6['state'] == 'readonly':

        sub_board.append(int(two6.get()))

    else:

        sub_board.append(0)

    if two7['state'] == 'readonly':

        sub_board.append(int(two7.get()))

    else:

        sub_board.append(0)

    if two8['state'] == 'readonly':

        sub_board.append(int(two8.get()))

    else:

        sub_board.append(0)

    if two9['state'] == 'readonly':

        sub_board.append(int(two9.get()))

    else:

        sub_board.append(0)

    board.append(sub_board)
    sub_board = []

    # row 3

    if three1['state'] == 'readonly':

        sub_board.append(int(three1.get()))

    else:

        sub_board.append(0)

    if three2['state'] == 'readonly':

        sub_board.append(int(three2.get()))

    else:

        sub_board.append(0)

    if three3['state'] == 'readonly':

        sub_board.append(int(three3.get()))

    else:

        sub_board.append(0)

    if three4['state'] == 'readonly':

        sub_board.append(int(three4.get()))

    else:

        sub_board.append(0)

    if three5['state'] == 'readonly':

        sub_board.append(int(three5.get()))

    else:

        sub_board.append(0)

    if three6['state'] == 'readonly':

        sub_board.append(int(three6.get()))

    else:

        sub_board.append(0)

    if three7['state'] == 'readonly':

        sub_board.append(int(three7.get()))

    else:

        sub_board.append(0)

    if three8['state'] == 'readonly':

        sub_board.append(int(three8.get()))

    else:

        sub_board.append(0)

    if three9['state'] == 'readonly':

        sub_board.append(int(three9.get()))

    else:

        sub_board.append(0)

    board.append(sub_board)
    sub_board = []

    # row 4

    if four1['state'] == 'readonly':

        sub_board.append(int(four1.get()))

    else:

        sub_board.append(0)

    if four2['state'] == 'readonly':

        sub_board.append(int(four2.get()))

    else:

        sub_board.append(0)

    if four3['state'] == 'readonly':

        sub_board.append(int(four3.get()))

    else:

        sub_board.append(0)

    if four4['state'] == 'readonly':

        sub_board.append(int(four4.get()))

    else:

        sub_board.append(0)

    if four5['state'] == 'readonly':

        sub_board.append(int(four5.get()))

    else:

        sub_board.append(0)

    if four6['state'] == 'readonly':

        sub_board.append(int(four6.get()))

    else:

        sub_board.append(0)

    if four7['state'] == 'readonly':

        sub_board.append(int(four7.get()))

    else:

        sub_board.append(0)

    if four8['state'] == 'readonly':

        sub_board.append(int(four8.get()))

    else:

        sub_board.append(0)

    if four9['state'] == 'readonly':

        sub_board.append(int(four9.get()))

    else:

        sub_board.append(0)

    board.append(sub_board)
    sub_board = []

    # row 5

    if five1['state'] == 'readonly':

        sub_board.append(int(five1.get()))

    else:

        sub_board.append(0)

    if five2['state'] == 'readonly':

        sub_board.append(int(five2.get()))

    else:

        sub_board.append(0)

    if five3['state'] == 'readonly':

        sub_board.append(int(five3.get()))

    else:

        sub_board.append(0)

    if five4['state'] == 'readonly':

        sub_board.append(int(five4.get()))

    else:

        sub_board.append(0)

    if five5['state'] == 'readonly':

        sub_board.append(int(five5.get()))

    else:

        sub_board.append(0)

    if five6['state'] == 'readonly':

        sub_board.append(int(five6.get()))

    else:

        sub_board.append(0)

    if five7['state'] == 'readonly':

        sub_board.append(int(five7.get()))

    else:

        sub_board.append(0)

    if five8['state'] == 'readonly':

        sub_board.append(int(five8.get()))

    else:

        sub_board.append(0)

    if five9['state'] == 'readonly':

        sub_board.append(int(five9.get()))

    else:

        sub_board.append(0)

    board.append(sub_board)
    sub_board = []

    # row 6

    if six1['state'] == 'readonly':

        sub_board.append(int(six1.get()))

    else:

        sub_board.append(0)

    if six2['state'] == 'readonly':

        sub_board.append(int(six2.get()))

    else:

        sub_board.append(0)

    if six3['state'] == 'readonly':

        sub_board.append(int(six3.get()))

    else:

        sub_board.append(0)

    if six4['state'] == 'readonly':

        sub_board.append(int(six4.get()))

    else:

        sub_board.append(0)

    if six5['state'] == 'readonly':

        sub_board.append(int(six5.get()))

    else:

        sub_board.append(0)

    if six6['state'] == 'readonly':

        sub_board.append(int(six6.get()))

    else:

        sub_board.append(0)

    if six7['state'] == 'readonly':

        sub_board.append(int(six7.get()))

    else:

        sub_board.append(0)

    if six8['state'] == 'readonly':

        sub_board.append(int(six8.get()))

    else:

        sub_board.append(0)

    if six9['state'] == 'readonly':

        sub_board.append(int(six9.get()))

    else:

        sub_board.append(0)

    board.append(sub_board)
    sub_board = []

    # row 7

    if seven1['state'] == 'readonly':

        sub_board.append(int(seven1.get()))

    else:

        sub_board.append(0)

    if seven2['state'] == 'readonly':

        sub_board.append(int(seven2.get()))

    else:

        sub_board.append(0)

    if seven3['state'] == 'readonly':

        sub_board.append(int(seven3.get()))

    else:

        sub_board.append(0)

    if seven4['state'] == 'readonly':

        sub_board.append(int(seven4.get()))

    else:

        sub_board.append(0)

    if seven5['state'] == 'readonly':

        sub_board.append(int(seven5.get()))

    else:

        sub_board.append(0)

    if seven6['state'] == 'readonly':

        sub_board.append(int(seven6.get()))

    else:

        sub_board.append(0)

    if seven7['state'] == 'readonly':

        sub_board.append(int(seven7.get()))

    else:

        sub_board.append(0)

    if seven8['state'] == 'readonly':

        sub_board.append(int(seven8.get()))

    else:

        sub_board.append(0)

    if seven9['state'] == 'readonly':

        sub_board.append(int(seven9.get()))

    else:

        sub_board.append(0)

    board.append(sub_board)
    sub_board = []

    # row 8

    if eight1['state'] == 'readonly':

        sub_board.append(int(eight1.get()))

    else:

        sub_board.append(0)

    if eight2['state'] == 'readonly':

        sub_board.append(int(eight2.get()))

    else:

        sub_board.append(0)

    if eight3['state'] == 'readonly':

        sub_board.append(int(eight3.get()))

    else:

        sub_board.append(0)

    if eight4['state'] == 'readonly':

        sub_board.append(int(eight4.get()))

    else:

        sub_board.append(0)

    if eight5['state'] == 'readonly':

        sub_board.append(int(eight5.get()))

    else:

        sub_board.append(0)

    if eight6['state'] == 'readonly':

        sub_board.append(int(eight6.get()))

    else:

        sub_board.append(0)

    if eight7['state'] == 'readonly':

        sub_board.append(int(eight7.get()))

    else:

        sub_board.append(0)

    if eight8['state'] == 'readonly':

        sub_board.append(int(eight8.get()))

    else:

        sub_board.append(0)

    if eight9['state'] == 'readonly':

        sub_board.append(int(eight9.get()))

    else:

        sub_board.append(0)

    board.append(sub_board)
    sub_board = []

    # row 9

    if nine1['state'] == 'readonly':

        sub_board.append(int(nine1.get()))

    else:

        sub_board.append(0)

    if nine2['state'] == 'readonly':

        sub_board.append(int(nine2.get()))

    else:

        sub_board.append(0)

    if nine3['state'] == 'readonly':

        sub_board.append(int(nine3.get()))

    else:

        sub_board.append(0)

    if nine4['state'] == 'readonly':

        sub_board.append(int(nine4.get()))

    else:

        sub_board.append(0)

    if nine5['state'] == 'readonly':

        sub_board.append(int(nine5.get()))

    else:

        sub_board.append(0)

    if nine6['state'] == 'readonly':

        sub_board.append(int(nine6.get()))

    else:

        sub_board.append(0)

    if nine7['state'] == 'readonly':

        sub_board.append(int(nine7.get()))

    else:

        sub_board.append(0)

    if nine8['state'] == 'readonly':

        sub_board.append(int(nine8.get()))

    else:

        sub_board.append(0)

    if nine9['state'] == 'readonly':

        sub_board.append(int(nine9.get()))

    else:

        sub_board.append(0)

    board.append(sub_board)
    
    solve(board)

    error = 0

    # this is getting really hard to see so
    # i am adding a bunhc of comments

    # row 1 column 1

    if one1.get().isnumeric() == True:

        if int(one1.get()) == board[0][0]:

            one1.config(bg = 'lightgreen')

        else:

            one1.config(bg = 'red')

    else:

        if one1.get() == '':

            one1.config(bg = 'red')

        else:

            error += 1

    # row 1 column 2

    if one2.get().isnumeric() == True:

        if int(one2.get()) == board[0][1]:

            one2.config(bg = 'lightgreen')

        else:

            one2.config(bg = 'red')

    else:

        if one2.get() == '':

            one2.config(bg = 'red')

        else:

            error += 1

    # row 1 column 3

    if one3.get().isnumeric() == True:

        if int(one3.get()) == board[0][2]:

            one3.config(bg = 'lightgreen')

        else:

            one3.config(bg = 'red')

    else:

        if one3.get() == '':

            one3.config(bg = 'red')

        else:

            error += 1

    # row 1 column 4

    if one4.get().isnumeric() == True:

        if int(one4.get()) == board[0][3]:

            one4.config(bg = 'lightgreen')

        else:

            one4.config(bg = 'red')

    else:

        if one4.get() == '':

            one4.config(bg = 'red')

        else:

            error += 1

    # row 1 column 5

    if one5.get().isnumeric() == True:

        if int(one5.get()) == board[0][4]:

            one5.config(bg = 'lightgreen')

        else:

            one5.config(bg = 'red')

    else:

        if one5.get() == '':

            one5.config(bg = 'red')

        else:

            error += 1

    # row 1 column 6

    if one6.get().isnumeric() == True: # isnumeric() checks if an a string can be turned into an int

        if int(one6.get()) == board[0][5]:

            one6.config(bg = 'lightgreen')

        else:

            one6.config(bg = 'red')

    else:

        if one6.get() == '':

            one6.config(bg = 'red')

        else:

            error += 1

    # row 1 column 7

    if one7.get().isnumeric() == True:

        if int(one7.get()) == board[0][6]:

            one7.config(bg = 'lightgreen')

        else:

            one7.config(bg = 'red')

    else:

        if one7.get() == '':

            one7.config(bg = 'red')

        else:

            error += 1

    # row 1 column 8

    if one8.get().isnumeric() == True:

        if int(one8.get()) == board[0][7]:

            one8.config(bg = 'lightgreen')

        else:

            one8.config(bg = 'red')

    else:

        if one8.get() == '':

            one8.config(bg = 'red')

        else:

            error += 1

    # row 1 column 9

    if one9.get().isnumeric() == True:

        if int(one9.get()) == board[0][8]:

            one9.config(bg = 'lightgreen')

        else:

            one9.config(bg = 'red')

    else:

        if one9.get() == '':

            one9.config(bg = 'red')

        else:

            error += 1

    # row 2 column 1

    if two1.get().isnumeric() == True:

        if int(two1.get()) == board[1][0]:

            two1.config(bg = 'lightgreen')

        else:

            two1.config(bg = 'red')

    else:

        if two1.get() == '':

            two1.config(bg = 'red')

        else:

            error += 1

    # row 2 column 2

    if two2.get().isnumeric() == True:

        if int(two2.get()) == board[1][1]:

            two2.config(bg = 'lightgreen')

        else:

            two2.config(bg = 'red')

    else:

        if two2.get() == '':

            two2.config(bg = 'red')

        else:

            error += 1

    # row 2 column 3

    if two3.get().isnumeric() == True:

        if int(two3.get()) == board[1][2]:

            two3.config(bg = 'lightgreen')

        else:

            two3.config(bg = 'red')

    else:

        if two3.get() == '':

            two3.config(bg = 'red')

        else:

            error += 1

    # row 2 column 4

    if two4.get().isnumeric() == True:

        if int(two4.get()) == board[1][3]:

            two4.config(bg = 'lightgreen')

        else:

            two4.config(bg = 'red')

    else:

        if two4.get() == '':

            two4.config(bg = 'red')

        else:

            error += 1

    # row 2 column 5

    if two5.get().isnumeric() == True:

        if int(two5.get()) == board[1][4]:

            two5.config(bg = 'lightgreen')

        else:

            two5.config(bg = 'red')

    else:

        if two5.get() == '':

            two5.config(bg = 'red')

        else:

            error += 1

    # row 2 column 6

    if two6.get().isnumeric() == True:

        if int(two6.get()) == board[1][5]:

            two6.config(bg = 'lightgreen')

        else:

            two6.config(bg = 'red')

    else:

        if two6.get() == '':

            two6.config(bg = 'red')

        else:

            error += 1

    # row 2 column 7

    if two7.get().isnumeric() == True:

        if int(two7.get()) == board[1][6]:

            two7.config(bg = 'lightgreen')

        else:

            two7.config(bg = 'red')

    else:

        if two7.get() == '':

            two7.config(bg = 'red')

        else:

            error += 1

    # row 2 column 8

    if two8.get().isnumeric() == True:

        if int(two8.get()) == board[1][7]:

            two8.config(bg = 'lightgreen')

        else:

            two8.config(bg = 'red')

    else:

        if two8.get() == '':

            two8.config(bg = 'red')

        else:

            error += 1

    # row 2 column 9

    if two9.get().isnumeric() == True:

        if int(two9.get()) == board[1][8]:

            two9.config(bg = 'lightgreen')

        else:

            two9.config(bg = 'red')

    else:

        if two9.get() == '':

            two9.config(bg = 'red')

        else:

            error += 1

    # row 3 column 1

    if three1.get().isnumeric() == True:

        if int(three1.get()) == board[2][0]:

            three1.config(bg = 'lightgreen')

        else:

            three1.config(bg = 'red')

    else:

        if three1.get() == '':

            three1.config(bg = 'red')

        else:

            error += 1

    # row 3 column 2

    if three2.get().isnumeric() == True:

        if int(three2.get()) == board[2][1]:

            three2.config(bg = 'lightgreen')

        else:

            three2.config(bg = 'red')

    else:

        if three2.get() == '':

            three2.config(bg = 'red')

        else:

            error += 1

    # row 3 column 3

    if three3.get().isnumeric() == True:

        if int(three3.get()) == board[2][2]:

            three3.config(bg = 'lightgreen')

        else:

            three3.config(bg = 'red')

    else:

        if three3.get() == '':

            three3.config(bg = 'red')

        else:

            error += 1

    # row 3 column 4

    if three4.get().isnumeric() == True:

        if int(three4.get()) == board[2][3]:

            three4.config(bg = 'lightgreen')

        else:

            three4.config(bg = 'red')

    else:

        if three4.get() == '':

            three4.config(bg = 'red')

        else:

            error += 1

    # row 3 column 5

    if three5.get().isnumeric() == True:

        if int(three5.get()) == board[2][4]:

            three5.config(bg = 'lightgreen')

        else:

            three5.config(bg = 'red')

    else:

        if three5.get() == '':

            three5.config(bg = 'red')

        else:

            error += 1

    # row 3 column 6

    if three6.get().isnumeric() == True:

        if int(three6.get()) == board[2][5]:

            three6.config(bg = 'lightgreen')

        else:

            three6.config(bg = 'red')

    else:

        if three6.get() == '':

            three6.config(bg = 'red')

        else:

            error += 1

    # row 3 column 7

    if three7.get().isnumeric() == True:

        if int(three7.get()) == board[2][6]:

            three7.config(bg = 'lightgreen')

        else:

            three7.config(bg = 'red')

    else:

        if three7.get() == '':

            three7.config(bg = 'red')

        else:

            error += 1

    # row 3 column 8

    if three8.get().isnumeric() == True:

        if int(three8.get()) == board[2][7]:

            three8.config(bg = 'lightgreen')

        else:

            three8.config(bg = 'red')

    else:

        if three8.get() == '':

            three8.config(bg = 'red')

        else:

            error += 1

    # row 3 column 9

    if three9.get().isnumeric() == True:

        if int(three9.get()) == board[2][8]:

            three9.config(bg = 'lightgreen')

        else:

            three9.config(bg = 'red')

    else:

        if three9.get() == '':

            three9.config(bg = 'red')

        else:

            error += 1

    # row 4 column 1

    if four1.get().isnumeric() == True:

        if int(four1.get()) == board[3][0]:

            four1.config(bg = 'lightgreen')

        else:

            four1.config(bg = 'red')

    else:

        if four1.get() == '':

            four1.config(bg = 'red')

        else:

            error += 1

    # row 4 column 2

    if four2.get().isnumeric() == True:

        if int(four2.get()) == board[3][1]:

            four2.config(bg = 'lightgreen')

        else:

            four2.config(bg = 'red')

    else:

        if four2.get() == '':

            four2.config(bg = 'red')

        else:

            error += 1

    # row 4 column 3

    if four3.get().isnumeric() == True:

        if int(four3.get()) == board[3][2]:

            four3.config(bg = 'lightgreen')

        else:

            four3.config(bg = 'red')

    else:

        if four3.get() == '':

            four3.config(bg = 'red')

        else:

            error += 1

    # row 4 column 4

    if four4.get().isnumeric() == True:

        if int(four4.get()) == board[3][3]:

            four4.config(bg = 'lightgreen')

        else:

            four4.config(bg = 'red')

    else:

        if four4.get() == '':

            four4.config(bg = 'red')

        else:

            error += 1

    # row 4 column 5

    if four5.get().isnumeric() == True:

        if int(four5.get()) == board[3][4]:

            four5.config(bg = 'lightgreen')

        else:

            four5.config(bg = 'red')

    else:

        if four5.get() == '':

            four5.config(bg = 'red')

        else:

            error += 1

    # row 4 column 6

    if four6.get().isnumeric() == True:

        if int(four6.get()) == board[3][5]:

            four6.config(bg = 'lightgreen')

        else:

            four6.config(bg = 'red')

    else:

        if four6.get() == '':

            four6.config(bg = 'red')

        else:

            error += 1

    # row 4 column 7

    if four7.get().isnumeric() == True:

        if int(four7.get()) == board[3][6]:

            four7.config(bg = 'lightgreen')

        else:

            four7.config(bg = 'red')

    else:

        if four7.get() == '':

            four7.config(bg = 'red')

        else:

            error += 1

    # row 4 column 8

    if four8.get().isnumeric() == True:

        if int(four8.get()) == board[3][7]:

            four8.config(bg = 'lightgreen')

        else:

            four8.config(bg = 'red')

    else:

        if four8.get() == '':

            four8.config(bg = 'red')

        else:

            error += 1

    # row 4 column 9

    if four9.get().isnumeric() == True:

        if int(four9.get()) == board[3][8]:

            four9.config(bg = 'lightgreen')

        else:

            four9.config(bg = 'red')

    else:

        if four9.get() == '':

            four9.config(bg = 'red')

        else:

            error += 1

    # row 5 column 1

    if five1.get().isnumeric() == True:

        if int(five1.get()) == board[4][0]:

            five1.config(bg = 'lightgreen')

        else:

            five1.config(bg = 'red')

    else:

        if five1.get() == '':

            five1.config(bg = 'red')

        else:

            error += 1
            
    # row 5 column 2

    if five2.get().isnumeric() == True:

        if int(five2.get()) == board[4][1]:

            five2.config(bg = 'lightgreen')

        else:

            five2.config(bg = 'red')

    else:

        if five2.get() == '':

            five2.config(bg = 'red')

        else:

            error += 1

    # row 5 column 3

    if five3.get().isnumeric() == True:

        if int(five3.get()) == board[4][2]:

            five3.config(bg = 'lightgreen')

        else:

            five3.config(bg = 'red')

    else:

        if five3.get() == '':

            five3.config(bg = 'red')

        else:

            error += 1

    # row 5 column 4

    if five4.get().isnumeric() == True:

        if int(five4.get()) == board[4][3]:

            five4.config(bg = 'lightgreen')

        else:

            five4.config(bg = 'red')

    else:

        if five4.get() == '':

            five4.config(bg = 'red')

        else:

            error += 1

    # row 5 column 5

    if five5.get().isnumeric() == True:

        if int(five5.get()) == board[4][4]:

            five5.config(bg = 'lightgreen')

        else:

            five5.config(bg = 'red')

    else:

        if five5.get() == '':

            five5.config(bg = 'red')

        else:

            error += 1

    # row 5 column 6

    if five6.get().isnumeric() == True:

        if int(five6.get()) == board[4][5]:

            five6.config(bg = 'lightgreen')

        else:

            five6.config(bg = 'red')

    else:

        if five6.get() == '':

            five6.config(bg = 'red')

        else:

            error += 1

    # row 5 column 7

    if five7.get().isnumeric() == True:

        if int(five7.get()) == board[4][6]:

            five7.config(bg = 'lightgreen')

        else:

            five7.config(bg = 'red')

    else:

        if five7.get() == '':

            five7.config(bg = 'red')

        else:

            error += 1

    # row 5 column 8

    if five8.get().isnumeric() == True:

        if int(five8.get()) == board[4][7]:

            five8.config(bg = 'lightgreen')

        else:

            five8.config(bg = 'red')

    else:

        if five8.get() == '':

            five8.config(bg = 'red')

        else:

            error += 1

    # row 5 column 9

    if five9.get().isnumeric() == True:

        if int(five9.get()) == board[4][8]:

            five9.config(bg = 'lightgreen')

        else:

            five9.config(bg = 'red')

    else:

        if five9.get() == '':

            five9.config(bg = 'red')

        else:

            error += 1

    # row 6 column 1

    if six1.get().isnumeric() == True:

        if int(six1.get()) == board[5][0]:

            six1.config(bg = 'lightgreen')

        else:

            six1.config(bg = 'red')

    else:

        if six1.get() == '':

            six1.config(bg = 'red')

        else:

            error += 1

    # row 6 column 2

    if six2.get().isnumeric() == True:

        if int(six2.get()) == board[5][1]:

            six2.config(bg = 'lightgreen')

        else:

            six2.config(bg = 'red')

    else:

        if six2.get() == '':

            six2.config(bg = 'red')

        else:

            error += 1

    # row 6 column 3

    if six3.get().isnumeric() == True:

        if int(six3.get()) == board[5][2]:

            six3.config(bg = 'lightgreen')

        else:

            six3.config(bg = 'red')

    else:

        if six3.get() == '':

            six3.config(bg = 'red')

        else:

            error += 1

    # row 6 column 4

    if six4.get().isnumeric() == True:

        if int(six4.get()) == board[5][3]:

            six4.config(bg = 'lightgreen')

        else:

            six4.config(bg = 'red')

    else:

        if six4.get() == '':

            six4.config(bg = 'red')

        else:

            error += 1

    # row 6 column 5

    if six5.get().isnumeric() == True:

        if int(six5.get()) == board[5][4]:

            six5.config(bg = 'lightgreen')

        else:

            six5.config(bg = 'red')

    else:

        if six5.get() == '':

            six5.config(bg = 'red')

        else:

            error += 1

    # row 6 column 6

    if six6.get().isnumeric() == True:

        if int(six6.get()) == board[5][5]:

            six6.config(bg = 'lightgreen')

        else:

            six6.config(bg = 'red')

    else:

        if six6.get() == '':

            six6.config(bg = 'red')

        else:

            error += 1

    # row 6 column 7

    if six7.get().isnumeric() == True:

        if int(six7.get()) == board[5][6]:

            six7.config(bg = 'lightgreen')

        else:

            six7.config(bg = 'red')

    else:

        if six7.get() == '':

            six7.config(bg = 'red')

        else:

            error += 1

    # row 6 column 8

    if six8.get().isnumeric() == True:

        if int(six8.get()) == board[5][7]:

            six8.config(bg = 'lightgreen')

        else:

            six8.config(bg = 'red')

    else:

        if six8.get() == '':

            six8.config(bg = 'red')

        else:

            error += 1

    # row 6 column 9

    if six9.get().isnumeric() == True:

        if int(six9.get()) == board[5][8]:

            six9.config(bg = 'lightgreen')

        else:

            six9.config(bg = 'red')

    else:

        if six9.get() == '':

            six9.config(bg = 'red')

        else:

            error += 1

    # row 7 column 1

    if seven1.get().isnumeric() == True:

        if int(seven1.get()) == board[6][0]:

            seven1.config(bg = 'lightgreen')

        else:

            seven1.config(bg = 'red')

    else:

        if seven1.get() == '':

            seven1.config(bg = 'red')

        else:

            error += 1

    # row 7 column 2

    if seven2.get().isnumeric() == True:

        if int(seven2.get()) == board[6][1]:

            seven2.config(bg = 'lightgreen')

        else:

            seven2.config(bg = 'red')

    else:

        if seven2.get() == '':

            seven2.config(bg = 'red')

        else:

            error += 1

    # row 7 column 3

    if seven3.get().isnumeric() == True:

        if int(seven3.get()) == board[6][2]:

            seven3.config(bg = 'lightgreen')

        else:

            seven3.config(bg = 'red')

    else:

        if seven3.get() == '':

            seven3.config(bg = 'red')

        else:

            error += 1

    # row 7 column 4

    if seven4.get().isnumeric() == True:

        if int(seven4.get()) == board[6][3]:

            seven4.config(bg = 'lightgreen')

        else:

            seven4.config(bg = 'red')

    else:

        if seven4.get() == '':

            seven4.config(bg = 'red')

        else:

            error += 1

    # row 7 column 5

    if seven5.get().isnumeric() == True:

        if int(seven5.get()) == board[6][4]:

            seven5.config(bg = 'lightgreen')

        else:

            seven5.config(bg = 'red')

    else:

        if seven5.get() == '':

            seven5.config(bg = 'red')

        else:

            error += 1

    # row 7 column 6

    if seven6.get().isnumeric() == True:

        if int(seven6.get()) == board[6][5]:

            seven6.config(bg = 'lightgreen')

        else:

            seven6.config(bg = 'red')

    else:

        if seven6.get() == '':

            seven6.config(bg = 'red')

        else:

            error += 1

    # row 7 column 7

    if seven7.get().isnumeric() == True:

        if int(seven7.get()) == board[6][6]:

            seven7.config(bg = 'lightgreen')

        else:

            seven7.config(bg = 'red')

    else:

        if seven7.get() == '':

            seven7.config(bg = 'red')

        else:

            error += 1

    # row 7 column 8

    if seven8.get().isnumeric() == True:

        if int(seven8.get()) == board[6][7]:

            seven8.config(bg = 'lightgreen')

        else:

            seven8.config(bg = 'red')

    else:

        if seven8.get() == '':

            seven8.config(bg = 'red')

        else:

            error += 1

    # row 7 column 9

    if seven9.get().isnumeric() == True:

        if int(seven9.get()) == board[6][8]:

            seven9.config(bg = 'lightgreen')

        else:

            seven9.config(bg = 'red')

    else:

        if seven9.get() == '':

            seven9.config(bg = 'red')

        else:

            error += 1

    # row 8 column 1

    if eight1.get().isnumeric() == True:

        if int(eight1.get()) == board[7][0]:

            eight1.config(bg = 'lightgreen')

        else:

            eight1.config(bg = 'red')

    else:

        if eight1.get() == '':

            eight1.config(bg = 'red')

        else:

            error += 1

    # row 8 column 2

    if eight2.get().isnumeric() == True:

        if int(eight2.get()) == board[7][1]:

            eight2.config(bg = 'lightgreen')

        else:

            eight2.config(bg = 'red')

    else:

        if eight2.get() == '':

            eight2.config(bg = 'red')

        else:

            error += 1

    # row 8 column 3

    if eight3.get().isnumeric() == True:

        if int(eight3.get()) == board[7][2]:

            eight3.config(bg = 'lightgreen')

        else:

            eight3.config(bg = 'red')

    else:

        if eight3.get() == '':

            eight3.config(bg = 'red')

        else:

            error += 1

    # row 8 column 4

    if eight4.get().isnumeric() == True:

        if int(eight4.get()) == board[7][3]:

            eight4.config(bg = 'lightgreen')

        else:

            eight4.config(bg = 'red')

    else:

        if eight4.get() == '':

            eight4.config(bg = 'red')

        else:

            error += 1

    # row 8 column 5

    if eight5.get().isnumeric() == True:

        if int(eight5.get()) == board[7][4]:

            eight5.config(bg = 'lightgreen')

        else:

            eight5.config(bg = 'red')

    else:

        if eight5.get() == '':

            eight5.config(bg = 'red')

        else:

            error += 1

    # row 8 column 6

    if eight6.get().isnumeric() == True:

        if int(eight6.get()) == board[7][5]:

            eight6.config(bg = 'lightgreen')

        else:

            eight6.config(bg = 'red')

    else:

        if eight6.get() == '':

            eight6.config(bg = 'red')

        else:

            error += 1

    # row 8 column 7

    if eight7.get().isnumeric() == True:

        if int(eight7.get()) == board[7][6]:

            eight7.config(bg = 'lightgreen')

        else:

            eight7.config(bg = 'red')

    else:

        if eight7.get() == '':

            eight7.config(bg = 'red')

        else:

            error += 1

    # row 8 column 8

    if eight8.get().isnumeric() == True:

        if int(eight8.get()) == board[7][7]:

            eight8.config(bg = 'lightgreen')

        else:

            eight8.config(bg = 'red')

    else:

        if eight8.get() == '':

            eight8.config(bg = 'red')

        else:

            error += 1

    # row 8 column 9

    if eight9.get().isnumeric() == True:

        if int(eight9.get()) == board[7][8]:

            eight9.config(bg = 'lightgreen')

        else:

            eight9.config(bg = 'red')

    else:

        if eight9.get() == '':

            eight9.config(bg = 'red')

        else:

            error += 1

    # row 9 column 1

    if nine1.get().isnumeric() == True:

        if int(nine1.get()) == board[8][0]:

            nine1.config(bg = 'lightgreen')

        else:

            nine1.config(bg = 'red')

    else:

        if nine1.get() == '':

            nine1.config(bg = 'red')

        else:

            error += 1

    # row 9 column 2

    if nine2.get().isnumeric() == True:

        if int(nine2.get()) == board[8][1]:

            nine2.config(bg = 'lightgreen')

        else:

            nine2.config(bg = 'red')

    else:

        if nine2.get() == '':

            nine2.config(bg = 'red')

        else:

            error += 1

    # row 9 column 3

    if nine3.get().isnumeric() == True:

        if int(nine3.get()) == board[8][2]:

            nine3.config(bg = 'lightgreen')

        else:

            nine3.config(bg = 'red')

    else:

        if nine3.get() == '':

            nine3.config(bg = 'red')

        else:

            error += 1

    # row 9 column 4

    if nine4.get().isnumeric() == True:

        if int(nine4.get()) == board[8][3]:

            nine4.config(bg = 'lightgreen')

        else:

            nine4.config(bg = 'red')

    else:

        if nine4.get() == '':

            nine4.config(bg = 'red')

        else:

            error += 1

    # row 9 column 5

    if nine5.get().isnumeric() == True:

        if int(nine5.get()) == board[8][4]:

            nine5.config(bg = 'lightgreen')

        else:

            nine5.config(bg = 'red')

    else:

        if nine5.get() == '':

            nine5.config(bg = 'red')

        else:

            error += 1

    # row 9 column 6

    if nine6.get().isnumeric() == True:

        if int(nine6.get()) == board[8][5]:

            nine6.config(bg = 'lightgreen')

        else:

            nine6.config(bg = 'red')

    else:

        if nine6.get() == '':

            nine6.config(bg = 'red')

        else:

            error += 1

    # row 9 column 7

    if nine7.get().isnumeric() == True:

        if int(nine7.get()) == board[8][6]:

            nine7.config(bg = 'lightgreen')

        else:

            nine7.config(bg = 'red')

    else:

        if nine7.get() == '':

            nine7.config(bg = 'red')

        else:

            error += 1

    # row 9 column 8

    if nine8.get().isnumeric() == True:

        if int(nine8.get()) == board[8][7]:

            nine8.config(bg = 'lightgreen')

        else:

            nine8.config(bg = 'red')

    else:

        if nine8.get() == '':

            nine8.config(bg = 'red')

        else:

            error += 1

    # row 9 column 9

    if nine9.get().isnumeric() == True:

        if int(nine9.get()) == board[8][8]:

            nine9.config(bg = 'lightgreen')

        else:

            nine9.config(bg = 'red')

    else:

        if nine9.get() == '':

            nine9.config(bg = 'red')

        else:

            error += 1

    # if any of the boxes have something that isnt a number
    # it will display an error message

    if error > 1:

        messagebox.showerror('error', 'all values must be numbers')

    
    # check their entries one by one to see if it matches
    # if yes highlight green
    # if no highlight red
    # make sure it is int before checking with solved list  

window = tk.Tk()
window.title('sudoku')
window.config(bg = 'white')

frame = tk.Frame(window)
frame.config(bg = 'white')
frame.grid(column = 0, row = 0, padx = 20, pady = 20)

title = tk.Label(frame, text = 'sudoku')
title.config(fg = 'black', bg = 'lavender', font = ('calibri bold', 24))
title.grid(column = 0, row = 0, columnspan = 9, pady = (0, 20), sticky = 'ew')

# row 1

one1 = tk.Entry(frame)
one1.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
one1.grid(column = 0, row = 1, columnspan = 1)

one2 = tk.Entry(frame)
one2.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
one2.grid(column = 1, row = 1, columnspan = 1)

one3 = tk.Entry(frame)
one3.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
one3.grid(column = 2, row = 1, columnspan = 1, padx = (0,5))

one4 = tk.Entry(frame)
one4.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
one4.grid(column = 3, row = 1, columnspan = 1, padx = (5,0))

one5 = tk.Entry(frame)
one5.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
one5.grid(column = 4, row = 1, columnspan = 1)

one6 = tk.Entry(frame)
one6.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
one6.grid(column = 5, row = 1, columnspan = 1, padx = (0,5))

one7 = tk.Entry(frame)
one7.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
one7.grid(column = 6, row = 1, columnspan = 1, padx = (5,0))

one8 = tk.Entry(frame)
one8.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
one8.grid(column = 7, row = 1, columnspan = 1)

one9 = tk.Entry(frame)
one9.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
one9.grid(column = 8, row = 1, columnspan = 1)

# row 2

two1 = tk.Entry(frame)
two1.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
two1.grid(column = 0, row = 2, columnspan = 1)

two2 = tk.Entry(frame)
two2.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
two2.grid(column = 1, row = 2, columnspan = 1)

two3 = tk.Entry(frame)
two3.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
two3.grid(column = 2, row = 2, columnspan = 1, padx = (0,5))

two4 = tk.Entry(frame)
two4.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
two4.grid(column = 3, row = 2, columnspan = 1, padx = (5,0))

two5 = tk.Entry(frame)
two5.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
two5.grid(column = 4, row = 2, columnspan = 1)

two6 = tk.Entry(frame)
two6.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
two6.grid(column = 5, row = 2, columnspan = 1, padx = (0,5))

two7 = tk.Entry(frame)
two7.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
two7.grid(column = 6, row = 2, columnspan = 1, padx = (5,0))

two8 = tk.Entry(frame)
two8.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
two8.grid(column = 7, row = 2, columnspan = 1)

two9 = tk.Entry(frame)
two9.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
two9.grid(column = 8, row = 2, columnspan = 1)

# row 3

three1 = tk.Entry(frame)
three1.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
three1.grid(column = 0, row = 3, columnspan = 1)

three2 = tk.Entry(frame)
three2.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
three2.grid(column = 1, row = 3, columnspan = 1)

three3 = tk.Entry(frame)
three3.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
three3.grid(column = 2, row = 3, columnspan = 1, padx = (0,5))

three4 = tk.Entry(frame)
three4.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
three4.grid(column = 3, row = 3, columnspan = 1, padx = (5,0))

three5 = tk.Entry(frame)
three5.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
three5.grid(column = 4, row = 3, columnspan = 1)

three6 = tk.Entry(frame)
three6.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
three6.grid(column = 5, row = 3, columnspan = 1, padx = (0,5))

three7 = tk.Entry(frame)
three7.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
three7.grid(column = 6, row = 3, columnspan = 1, padx = (5,0))

three8 = tk.Entry(frame)
three8.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
three8.grid(column = 7, row = 3, columnspan = 1)

three9 = tk.Entry(frame)
three9.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
three9.grid(column = 8, row = 3, columnspan = 1)

# row 4

four1 = tk.Entry(frame)
four1.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
four1.grid(column = 0, row = 4, columnspan = 1, pady =(10,0))

four2 = tk.Entry(frame)
four2.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
four2.grid(column = 1, row = 4, columnspan = 1, pady =(10,0))

four3 = tk.Entry(frame)
four3.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
four3.grid(column = 2, row = 4, columnspan = 1, padx = (0,5), pady =(10,0))

four4 = tk.Entry(frame)
four4.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
four4.grid(column = 3, row = 4, columnspan = 1, pady =(10,0), padx = (5,0))

four5 = tk.Entry(frame)
four5.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
four5.grid(column = 4, row = 4, columnspan = 1, pady =(10,0))

four6 = tk.Entry(frame)
four6.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
four6.grid(column = 5, row = 4, columnspan = 1, padx = (0,5), pady =(10,0))

four7 = tk.Entry(frame)
four7.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
four7.grid(column = 6, row = 4, columnspan = 1, pady =(10,0), padx = (5,0))

four8 = tk.Entry(frame)
four8.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
four8.grid(column = 7, row = 4, columnspan = 1, pady =(10,0))

four9 = tk.Entry(frame)
four9.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
four9.grid(column = 8, row = 4, columnspan = 1, pady =(10,0))

# row 5

five1 = tk.Entry(frame)
five1.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
five1.grid(column = 0, row = 5, columnspan = 1)

five2 = tk.Entry(frame)
five2.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
five2.grid(column = 1, row = 5, columnspan = 1)

five3 = tk.Entry(frame)
five3.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
five3.grid(column = 2, row = 5, columnspan = 1, padx = (0,5))

five4 = tk.Entry(frame)
five4.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
five4.grid(column = 3, row = 5, columnspan = 1, padx = (5,0))

five5 = tk.Entry(frame)
five5.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
five5.grid(column = 4, row = 5, columnspan = 1)

five6 = tk.Entry(frame)
five6.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
five6.grid(column = 5, row = 5, columnspan = 1, padx = (0,5))

five7 = tk.Entry(frame)
five7.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
five7.grid(column = 6, row = 5, columnspan = 1, padx = (5,0))

five8 = tk.Entry(frame)
five8.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
five8.grid(column = 7, row = 5, columnspan = 1)

five9 = tk.Entry(frame)
five9.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
five9.grid(column = 8, row = 5, columnspan = 1)

# row 6

six1 = tk.Entry(frame)
six1.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
six1.grid(column = 0, row = 6, columnspan = 1)

six2 = tk.Entry(frame)
six2.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
six2.grid(column = 1, row = 6, columnspan = 1)

six3 = tk.Entry(frame)
six3.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
six3.grid(column = 2, row = 6, columnspan = 1, padx = (0,5))

six4 = tk.Entry(frame)
six4.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
six4.grid(column = 3, row = 6, columnspan = 1, padx = (5,0))

six5 = tk.Entry(frame)
six5.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
six5.grid(column = 4, row = 6, columnspan = 1)

six6 = tk.Entry(frame)
six6.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
six6.grid(column = 5, row = 6, columnspan = 1, padx = (0,5))

six7 = tk.Entry(frame)
six7.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
six7.grid(column = 6, row = 6, columnspan = 1, padx = (5,0))

six8 = tk.Entry(frame)
six8.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
six8.grid(column = 7, row = 6, columnspan = 1)

six9 = tk.Entry(frame)
six9.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
six9.grid(column = 8, row = 6, columnspan = 1)

# row 7

seven1 = tk.Entry(frame)
seven1.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
seven1.grid(column = 0, row = 7, columnspan = 1, pady =(10,0))

seven2 = tk.Entry(frame)
seven2.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
seven2.grid(column = 1, row = 7, columnspan = 1, pady =(10,0))

seven3 = tk.Entry(frame)
seven3.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
seven3.grid(column = 2, row = 7, columnspan = 1, padx = (0,5), pady =(10,0))

seven4 = tk.Entry(frame)
seven4.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
seven4.grid(column = 3, row = 7, columnspan = 1, pady =(10,0), padx = (5,0))

seven5 = tk.Entry(frame)
seven5.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
seven5.grid(column = 4, row = 7, columnspan = 1, pady =(10,0))

seven6 = tk.Entry(frame)
seven6.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
seven6.grid(column = 5, row = 7, columnspan = 1, padx = (0,5), pady =(10,0))

seven7 = tk.Entry(frame)
seven7.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
seven7.grid(column = 6, row = 7, columnspan = 1, pady =(10,0), padx = (5,0))

seven8 = tk.Entry(frame)
seven8.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
seven8.grid(column = 7, row = 7, columnspan = 1, pady =(10,0))

seven9 = tk.Entry(frame)
seven9.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
seven9.grid(column = 8, row = 7, columnspan = 1, pady =(10,0))

# row 8

eight1 = tk.Entry(frame)
eight1.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
eight1.grid(column = 0, row = 8, columnspan = 1)

eight2 = tk.Entry(frame)
eight2.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
eight2.grid(column = 1, row = 8, columnspan = 1)

eight3 = tk.Entry(frame)
eight3.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
eight3.grid(column = 2, row = 8, columnspan = 1, padx = (0,5))

eight4 = tk.Entry(frame)
eight4.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
eight4.grid(column = 3, row = 8, columnspan = 1, padx = (5,0))

eight5 = tk.Entry(frame)
eight5.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
eight5.grid(column = 4, row = 8, columnspan = 1)

eight6 = tk.Entry(frame)
eight6.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
eight6.grid(column = 5, row = 8, columnspan = 1, padx = (0,5))

eight7 = tk.Entry(frame)
eight7.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
eight7.grid(column = 6, row = 8, columnspan = 1, padx = (5,0))

eight8 = tk.Entry(frame)
eight8.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
eight8.grid(column = 7, row = 8, columnspan = 1)

eight9 = tk.Entry(frame)
eight9.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
eight9.grid(column = 8, row = 8, columnspan = 1)

# row 9

nine1 = tk.Entry(frame)
nine1.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
nine1.grid(column = 0, row = 9, columnspan = 1)

nine2 = tk.Entry(frame)
nine2.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
nine2.grid(column = 1, row = 9, columnspan = 1)

nine3 = tk.Entry(frame)
nine3.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
nine3.grid(column = 2, row = 9, columnspan = 1, padx = (0,5))

nine4 = tk.Entry(frame)
nine4.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
nine4.grid(column = 3, row = 9, columnspan = 1, padx = (5,0))

nine5 = tk.Entry(frame)
nine5.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
nine5.grid(column = 4, row = 9, columnspan = 1)

nine6 = tk.Entry(frame)
nine6.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
nine6.grid(column = 5, row = 9, columnspan = 1, padx = (0,5))

nine7 = tk.Entry(frame)
nine7.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
nine7.grid(column = 6, row = 9, columnspan = 1, padx = (5,0))

nine8 = tk.Entry(frame)
nine8.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
nine8.grid(column = 7, row = 9, columnspan = 1)

nine9 = tk.Entry(frame)
nine9.config(fg = 'blue', bg = 'lavender', font = ('calibri bold', 24), width = 2, justify = 'center', highlightthickness = 0)
nine9.grid(column = 8, row = 9, columnspan = 1)

# fill board button

fill_board_button = tk.Button(frame, text = 'fill', command = fill_board)
fill_board_button.config(fg = 'black', highlightbackground = 'lavender', font = ('calibri bold', 24), width = 4)
fill_board_button.grid(column = 0, row = 10, sticky = 'ew', columnspan = 3, pady =(15,0), padx = (0,5))

# solve board button

solve_board_button = tk.Button(frame, text = 'solve', command = fill_solved)
solve_board_button.config(fg = 'black', highlightbackground = 'lavender', font = ('calibri bold', 24), width = 4)
solve_board_button.grid(column = 3, row = 10, sticky = 'ew', columnspan = 3, pady =(15,0), padx = 5)

# clear board button

clear_board_button = tk.Button(frame, text = 'clear', command = clear_board)
clear_board_button.config(fg = 'black', highlightbackground = 'lavender', font = ('calibri bold', 24), width = 4)
clear_board_button.grid(column = 6, row = 10, sticky = 'ew', columnspan = 3, pady =(15,0), padx = (5,0))

# check board button

check_board_button = tk.Button(frame, text = 'check', command = check_board)
check_board_button.config(fg = 'black', highlightbackground = 'lavender', font = ('calibri bold', 24), width = 4)
check_board_button.grid(column = 0, row = 11, sticky = 'ew', columnspan = 3, pady =(15,0), padx = (0,5))

# easy button

easy_button = tk.Button(frame, text = 'easy', command = easy_mode)
easy_button.config(fg = 'black', highlightbackground = 'lavender', font = ('calibri bold', 24), width = 2)
easy_button.grid(column = 3, row = 11, sticky = 'ew', columnspan = 2, pady =(15,0), padx = (5,0))

# medium button

medium_button = tk.Button(frame, text = 'med', command = medium_mode)
medium_button.config(fg = 'black', highlightbackground = 'lavender', font = ('calibri bold', 24), width = 2)
medium_button.grid(column = 5, row = 11, sticky = 'ew', columnspan = 2, pady =(15,0), padx = (5,0))

# hard button

hard_button = tk.Button(frame, text = 'hard', command = hard_mode)
hard_button.config(fg = 'black', highlightbackground = 'lavender', font = ('calibri bold', 24), width = 2)
hard_button.grid(column = 7, row = 11, sticky = 'ew', columnspan = 2, pady =(15,0), padx = (5,0))

