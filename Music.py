from tkinter import Button 

from requires import * 
from utils import * 

root.title("Music Player App") 
root.geometry("270x270") 


def main():
    Button(text = " Play ", width=WIDTH, font=FONT, fg=WHITE, bg=RED, command=Load).grid(row=1, column=1, padx=5, pady=4) 
    Button(text = " Mute ", width=WIDTH, font=FONT, fg=WHITE, bg=GREEN, command=Mute).grid(row=2, column=1, padx=5, pady=4) 
    Button(text = " Queue", width=WIDTH, font=FONT, fg=WHITE, bg="yellow", command=Queue).grid( row=3, column=1, padx=5, pady=4) 
    Button(text = " Again", width=WIDTH, font=FONT, fg=WHITE, bg=BLUE, command=Replay).grid(row=4, column=1, padx=5, pady=4) 
    Button(text = " Exit ", width=WIDTH, font=FONT, fg=WHITE, bg=PINK, command=Quit).grid(row=5, column=1, padx=5, pady=4) 


if __name__ == '__main__':
    time()
    main()
    root.mainloop() 

