from Tkinter import *

bgColor = 'blue'
fgColor = 'white'

root = Tk()
root.title('Time Card')
root.configure(background=bgColor)

Label(root, text='Time Card', fg=fgColor, bg=bgColor).pack(fill=X)
lowerSection = Frame(root, bg=bgColor, highlightbackground='black', borderwidth=2)
lowerSection.pack(fill=X, side=BOTTOM, padx=10, pady=10)

entries = []
buttons = []

for x in range(5):
    temp = Entry(lowerSection, highlightbackground=bgColor)
    temp.grid(row=x, column=1, padx=10, pady=10)
    entries.append(temp)
    temp = Button(lowerSection, highlightbackground=bgColor, text='start')
    temp.grid(row=x, column=2, padx=10, pady=10)
    buttons.append(temp)



root.mainloop()