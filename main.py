from tkinter import Button 
from requires import WIDTH, FONT, root 
from requires import GREEN, BLACK, PINK, YELLOW, CYAN, RED 
from utils import Load, Mute, Queue, Replay, Stop, time 
from symbols import Psymbol, Msymbol, Qsymbol, Esymbol, Rsymbol 


root.title("Music Player App") 
root.geometry("270x270") 


def main():
    Button(root, text = " Play ", width=WIDTH, font=FONT, fg=BLACK, bg=GREEN, command=Load).grid(row=1, column=1, padx=5, pady=4) 
    Button(root, text = " Mute ", width=WIDTH, font=FONT, fg=BLACK, bg=PINK, command=Mute).grid(row=2, column=1, padx=5, pady=4) 
    Button(root, text = " Queue", width=WIDTH, font=FONT, fg=BLACK, bg=YELLOW, command=Queue).grid( row=3, column=1, padx=5, pady=4) 
    Button(root, text = "RePlay", width=WIDTH, font=FONT, fg=BLACK, bg=CYAN, command=Replay).grid(row=4, column=1, padx=5, pady=4) 
    Button(root, text = " Stop ", width=WIDTH, font=FONT, fg=BLACK, bg=RED, command=Stop).grid(row=5, column=1, padx=5, pady=4)  


if __name__ == '__main__':
    time()
    main()
    root.mainloop() 

