from tkinter import *

window = Tk()
window.geometry("600x800")
window.title('Labels')


label = Label(window, text="Hello World!",
                       font=("Verdana", 60, "bold"),
                       fg="white", bg="black")
label.pack()
window.mainloop() 

