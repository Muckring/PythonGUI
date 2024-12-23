from tkinter import *

count: int = 0
def click() -> None:
    global count
    count +=1
    label.config(text=count)
    if count==10:
        label.config(font=('Verdana', 50, 'italic'))
        label.config(text="You run out of clicks!!!!")

root = Tk()
root.geometry("1000x1200")

button = Button(root, text="Click me now!!!!")
button.config(command=click)
button.config(font=("Ink Free", 50, 'bold'))
button.config(relief=SUNKEN)
button.config(fg="yellow")
button.config(bg='red')
button.config(padx='40')
button.config(pady='40')
button.config(bd='5')
button.config(activebackground='black')
button.config(activeforeground='white')
pict = PhotoImage(file="click-gif-3.gif")
button.config(image=pict)
button.config(compound='top')
# button.config(state=DISABLED) ACTIVE - BUTTON ON, DISABLED -BUTTON OFF
button.pack()
label = Label(root, text=count)
label.config(font=("Arial", 100, 'bold'))
label.pack()

root.mainloop()