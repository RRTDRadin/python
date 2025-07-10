from tkinter import *

window = Tk()
window.title('Tkinter Sample Window')
window.geometry('300x300')

greeting = Label(text="Hello User", fg='black', bg='white')
button = Button(text="Click me", fg='black', bg='white')
entry = Entry(fg='yellow', bg='blue', width=50)
greeting.pack()
button.pack()
entry.pack()

frame = Frame(master=window, relief=RAISED, borderwith=5)
frame.pack()
lable = Label(master=frame, text='Sample Frame')

textbox = Text(fg='green',bg='yellow')
textbox.pack()