from tkinter import *

# CREATE A FUNCTION FOR THE SUBMIT BUTTON

def submit() -> None: 
    username = entry.get()
    print(username)

# CREATE A FUNCTION FOR THE DELETE BUTTON

def delete() -> None:
    entry.delete(0, END)

# CREATE A FUNCTION FOR THE BACKSPACE BUTTON

def backspace() -> None:
    entry.delete(len(entry.get())-1, END) # deletes last character of a string

# CREATE ROOT

root = Tk()
root.geometry("700x100")
root.title("User Inputs")

#CREATE SUBMIT BUTTON

submit = Button(root, text="Submit", command=submit)
submit.pack(side = RIGHT)

# CREATE DELETE BUTTON

delete = Button(root, text="Delete", command=delete)
delete.pack(side = RIGHT)

# CREATE BACKSPACE BUTTON

backspace = Button(root, text="Backspace", command=backspace)
backspace.pack(side = RIGHT)

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