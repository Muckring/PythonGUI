from tkinter import *

root = Tk()
root.geometry("1400x1200")
root.title("User Inputs")

entry = Entry()
entry.config(font=("TImes New Roman", 50, 'bold'))
entry.pack()

picture = PhotoImage(file="bonfire.gif")
root.iconphoto(True, picture)
root.config(background="black")

root.mainloop()