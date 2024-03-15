from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic-Tac-Toe')
root.iconbitmap('c:/gui/codemy.ico')

# X starts so true
clicked = True
count = 0


# Disable all the buttons
def disable_all_buttons():
    for button in buttons:
        button.config(state=DISABLED)


# Check to see if someone won
def check_if_won():
    global winner
    winner = False
    for combination in winning_combinations:
        if buttons[combination[0]]["text"] == buttons[combination[1]]["text"] == buttons[combination[2]]["text"] != " ":
            winner = True
            for index in combination:
                buttons[index].config(bg="red")
            messagebox.showinfo("Tic Tac Toe", f"CONGRATULATIONS! {buttons[combination[0]]['text']} Wins!!")
            disable_all_buttons()

    # Check if tie
    if count == 9 and not winner:
        messagebox.showinfo("Tic Tac Toe", "It's A Tie!\nNo One Wins!")
        disable_all_buttons()


# Button clicked function
def button_click(b):
    global clicked, count

    if b["text"] == " " and clicked:
        b["text"] = "X"
        clicked = False
        count += 1
        check_if_won()
    elif b["text"] == " " and not clicked:
        b["text"] = "O"
        clicked = True
        count += 1
        check_if_won()
    else:
        messagebox.showerror("Tic Tac Toe", "Hey! That box has already been selected.\nPick Another Box...")


# Create buttons
buttons = []
for i in range(9):
    button = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                    command=lambda current_button=i: button_click(buttons[current_button]))
    buttons.append(button)

# Grid buttons to the screen
for i in range(3):
    for j in range(3):
        buttons[i * 3 + j].grid(row=i, column=j)

# Define winning combinations
winning_combinations = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]


# Reset the game
def reset_game():
    global clicked, count
    clicked = True
    count = 0
    for button in buttons:
        button.config(text=" ", bg="SystemButtonFace", state=NORMAL)


# Create menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Create Options Menu
options_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset_game)

root.mainloop()
