# creating a window in Tkinter

# import tkinter
# window = tkinter.Tk()
# window.mainloop()

# Opening image using pillow module
# from PIL import Image
# img = Image.open('Python-Image.png')
# img.show()

from tkinter import*
from PIL import Image, ImageTk

window  = Tk()
name = Label(window, text='PythonX - Learn Python',bg='Light grey',fg='Blue',font=('Serif',16),underline=-1)
img = Image.open('Python-Image.png')
logo = ImageTk.PhotoImage(img)
image = Label(window,image=logo)
button = Button(window,text="Let's Start")
username = Label(window,text='Username',font=('Serif',12))
inputBox = Entry(window)

name.pack()
image.pack()
username.pack(side=LEFT)
inputBox.pack(side=RIGHT)
button.place(x=100,y=500)
window.mainloop()

