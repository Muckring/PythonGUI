from tkinter import *

def submit() -> None:
    username = entry.get()
    print(username)

root = Tk()
root.geometry("1400x1200")
root.title("User Inputs")

submit = Button(root, text="Submit", command=submit)
submit.pack()

entry = Entry()
entry.config(font=("TImes New Roman", 50, 'bold'))
entry.config(bg="black")
entry.config(fg='#00FF00')

# entry.config(state=DISABLED) ACTIVE/DISABLED
# entry.config(width="10") width attribute sets max width
# entry.config(show="*") show replaces text with specified symbol

entry.pack()

picture = PhotoImage(file="bonfire.gif")
root.iconphoto(True, picture)
root.config(background="red")

root.mainloop()