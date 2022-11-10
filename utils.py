from time import strftime
from tkinter import filedialog, Label
from pygame import mixer
from requires import root
mixer.init()

label1 = Label(root, font=("Old-English", 15), width=10, bg="black", fg="cyan")
label1.grid(row=0, column=1)


def Load():
    mixer.music.load(filedialog.askopenfile())  # type: ignore 
    mixer.music.play()
    #  mixer.music.play(int(input("\nEnter Number of Loops for Play: ")))


def Mute():
    global Number
    if (Number%2 == 0):
        mixer.music.pause()
    if (Number%2 != 0):
        mixer.music.unpause()
    Number += 1


def Queue():
    mixer.music.load(filedialog.askopenfile())  # type: ignore 
    mixer.music.queue(filedialog.askopenfile())  # type: ignore 
    mixer.music.play()
    #  mixer.music.play(int(input("\nEnter Number of Loops for Queue: ")))


def Replay():
    mixer.music.play()


def Quit():
    mixer.music.stop()
    exit()


def time():
    label1.config(text=strftime("%I:%M %p")) 
    label1.after(1000, time)