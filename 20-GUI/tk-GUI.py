# creating a window in Tkinter

# import tkinter
# window = tkinter.Tk()
# window.mainloop()

# Opening image using pillow module
# from PIL import Image
# img = Image.open('Python-Image.png')
# img.show()

# Creating button widget, label widget, entry widget
# from tkinter import*
# from PIL import Image, ImageTk

# window  = Tk()
# name = Label(window, text='PythonX - Learn Python',bg='Light grey',fg='Blue',font=('Serif',16),underline=-1)
# img = Image.open('Python-Image.png')
# logo = ImageTk.PhotoImage(img)
# image = Label(window,image=logo)
# button = Button(window,text="Let's Start")
# username = Label(window,text='Username',font=('Serif',12))
# inputBox = Entry(window)

# name.pack()
# image.pack()
# username.pack(side=LEFT)
# inputBox.pack(side=RIGHT)
# button.place(x=100,y=500)
# window.mainloop()

# creating a Frame widget
# from tkinter import*
# window  = Tk()
# frame = Frame(window)
# lbl = Label(frame,text="Inside the frame")
# btn = Button(frame,text="Inside the frame")
# frame.pack()
# lbl.pack(side=TOP)
# btn.pack(side=BOTTOM)
# window.mainloop()

# creating a Checkbutton widget
# from tkinter import*

# window = Tk()
# lbl = Label(window,text="Choose your favourite programming languages:")
# frame = Frame(window)
# python = Checkbutton(frame,text='Python')
# java = Checkbutton(frame,text='Java')
# js = Checkbutton(frame,text='Javascript')
# cpp = Checkbutton(frame,text='C++')

# lbl.pack()
# frame.pack()
# python.pack()
# java.pack()
# js.pack()
# cpp.pack()
# window.mainloop()

# Creating a Radiobutton widget
from tkinter import*

window = Tk()
lbl = Label(window,text="Select your gender:")
frame = Frame(window)
var = StringVar()
male = Radiobutton(frame,text='Male',variable=var,value='M')
female = Radiobutton(frame,text='Female',variable=var,value='F')

lbl.pack()
frame.pack()
male.pack()
female.pack()
window.mainloop()

