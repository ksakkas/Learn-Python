from tkinter import *

root = Tk()

minutes = Label(root, text="Λεπτά:")
minutes.pack(side=LEFT)

scale = Scale(root, from_=1, to=20, orient=HORIZONTAL, length=500)
scale.pack()

button = Button(root, text="Ξεκίνα τώρα", command=quit)
button.pack()

root.mainloop()