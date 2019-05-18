from Tkinter import *
import time

bgColor = 'blue'
fgColor = 'white'

root = Tk()
root.title('Time Card')
root.configure(background=bgColor)

Label(root, text='Time Card', fg=fgColor, bg=bgColor).pack(fill=X)
lowerSection = Frame(root, bg=bgColor, highlightbackground='black', borderwidth=2)
lowerSection.pack(fill=X, side=BOTTOM, padx=10, pady=10)

buttons = []
labels = []

startTime = 0


def callback(val):
    global startTime
    if buttons[val]['text'] == 'stop':
        buttons[val].configure(text='start')
        time_lapse = round((time.time() - startTime) / 3600, 1)
        labels[val].configure(text=time_lapse)
        return
    for button in buttons:
        button.configure(text='start')
    buttons[val].configure(text='stop')
    startTime = time.time()


for x in range(5):
    temp = Entry(lowerSection, highlightbackground=bgColor)
    temp.grid(row=x, column=1, padx=10, pady=10)
    temp = Button(lowerSection, highlightbackground=bgColor, text='start', command=lambda val=x: callback(val), width = 10)
    temp.grid(row=x, column=2, padx=10, pady=10)
    buttons.append(temp)
    temp = Label(lowerSection, highlightbackground=bgColor, text='0.0')
    temp.grid(row=x, column=3, padx=10, pady=10)
    labels.append(temp)

root.mainloop()
