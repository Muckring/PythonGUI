from tkinter import *

window = Tk()
window.geometry("600x800")
window.title('Labels')

photo =PhotoImage(file='bonfire.gif')




label = Label(window, text="Hello World!",
                       font=("Verdana", 60, "bold"),# font is an option
                       # which is equal to a tuple containing font family, size,
                       # font style
                       fg="white", bg="black",
                       # fg is font color, bg is background color
                       relief=RAISED, # relief is border
                       bd=20, # bd is border thickness
                       padx=40, # padx is paddijng on the right and on the left of the text
                       pady=30, # padY is padding at the top and bottom of the text
                       image=photo, # image is a property that helps add an image to a label
                       compound='bottom' #compound is a property that defines the position
                       # of an image in relation to the text(bottom, top, left,right)
                       )
label.pack()
window.mainloop() 

