from tkinter import *

# CREATE A FUNCTION FOR THE SUBMIT BUTTON

def submit() -> None: 
    username = entry.get()
    print(username)

# CREATE ROOT

root = Tk()
root.geometry("1400x1200")
root.title("User Inputs")

#CREATE SUBMIT BUTTON

submit = Button(root, text="Submit", command=submit)
submit.pack()

# CREATE USER INPUT ENTRY(FIELD)
entry = Entry()
entry.config(font=("TImes New Roman", 50, 'bold'))
entry.config(bg="black")
entry.config(fg='#00FF00')

# entry.config(state=DISABLED) ACTIVE/DISABLED
# entry.config(width="10") width attribute sets max width
# entry.config(show="*") show replaces text with specified symbol

entry.pack()

# CONVERT GIF FILE TO PHOTOIMAGE
# CHANGE ROOT ICON

picture = PhotoImage(file="bonfire.gif")
root.iconphoto(True, picture)
root.config(background="red")

root.mainloop()