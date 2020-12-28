from tkinter import *
import tkinter.messagebox as tmb

# & All functions


def click(event):
    global scvalue
    text = event.widget.cget("text")
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            try:
                value = eval(screen.get())

            except Exception as e:
                print(e)
                err = tmb.showerror(
                    "ERROR ENCOUNTERED", "SORRY, An Error Occured,\n Please Check Your Input.")
        scvalue.set(value)
        screen.update()

    elif text == "C":
        scvalue.set("")
        screen.update()

    else:
        scvalue.set(scvalue.get() + text)
        screen.update()  # @ to update the screen with the widgets pressed


root = Tk()
root.geometry("390x498")
root.minsize(390, 498)
root.maxsize(390, 498)
root.title("GUI Calculator -By Deepraj")
root.wm_iconbitmap("calculator_14445.ico")


# $ Moving to Screen
scvalue = StringVar()
scvalue.set("")
screen = Entry(root, textvar=scvalue, font="Comicsansms 30",
               bg="#B5BABA", relief=SUNKEN)
screen.pack(pady=10, padx=4)

# ^ BAsic
f1 = Frame(root, bg="#EE5537", height=20, width=30)
b = Button(f1, text="C", font="consolas 19", bg="#E8F2E6", width=8)
b.pack(side=LEFT, padx=3, pady=2, anchor=W)
b.bind("<Button-1>", click)
b = Button(f1, text="/", font="consolas 19", bg="#E8F2E6", width=8)
b.pack(side=LEFT, padx=3, pady=2, anchor=E)
b.bind("<Button-1>", click)
b = Button(f1, text="-", font="consolas 19", bg="#E8F2E6", width=8)
b.pack(side=LEFT, padx=3, pady=2, anchor=E)
b.bind("<Button-1>", click)

f1.pack(anchor=NW)

f1 = Frame(root, bg="#EE5537", height=20, width=30)

b = Button(f1, text="+", font="consolas 19", bg="#E8F2E6", width=8)
b.pack(side=LEFT, padx=3, pady=2, anchor=E)
b.bind("<Button-1>", click)
b = Button(f1, text="*", font="consolas 19", bg="#E8F2E6", width=8)
b.pack(side=LEFT, padx=3, pady=2, anchor=W)
b.bind("<Button-1>", click)
b = Button(f1, text="=", font="consolas 19", bg="#E8F2E6", width=8)
b.pack(side=LEFT, padx=3, pady=2, anchor=W)
b.bind("<Button-1>", click)
f1.pack(anchor=NW)


#! First Row Buttons
f1 = Frame(root, bg="#EE5537", height=20, width=30)
b = Button(f1, text="7", font="consolas 19", bg="#E8F2E6", width=8)
b.pack(side=LEFT, padx=3, pady=2, anchor=W)
b.bind("<Button-1>", click)
b = Button(f1, text="8", font="consolas 19", bg="#E8F2E6", width=8)
b.pack(side=LEFT, padx=3, pady=2, anchor=W)
b.bind("<Button-1>", click)
b = Button(f1, text="9", font="consolas 19", bg="#E8F2E6", width=8)
b.pack(side=LEFT, padx=3, pady=2, anchor=W)
b.bind("<Button-1>", click)
f1.pack(anchor=NW)

# ^ Second row Buttons

f1 = Frame(root, bg="#EE5537", height=20, width=30)
b = Button(f1, text="4", font="consolas 19", bg="#E8F2E6", width=8)
b.pack(side=LEFT, padx=3, pady=2, anchor=W)
b.bind("<Button-1>", click)
b = Button(f1, text="5", font="consolas 19", bg="#E8F2E6", width=8)
b.pack(side=LEFT, padx=3, pady=2, anchor=W)
b.bind("<Button-1>", click)
b = Button(f1, text="6", font="consolas 19", bg="#E8F2E6", width=8)
b.pack(side=LEFT, padx=3, pady=2, anchor=W)
b.bind("<Button-1>", click)
f1.pack(anchor=NW)

# * Third row Buttons
f1 = Frame(root, bg="#EE5537", padx=0, height=20, width=30)
b = Button(f1, text="1", font="consolas 19", bg="#E8F2E6", width=8)
b.pack(side=LEFT, padx=3, pady=2, anchor=W)
b.bind("<Button-1>", click)
b = Button(f1, text="2", font="consolas 19", bg="#E8F2E6", width=8)
b.pack(side=LEFT, padx=3, pady=2, anchor=W)
b.bind("<Button-1>", click)
b = Button(f1, text="3", font="consolas 19", bg="#E8F2E6", width=8)
b.pack(side=LEFT, padx=3, pady=2, anchor=W)
b.bind("<Button-1>", click)
f1.pack(anchor=NW)

# @ Fourth row Buttons
f1 = Frame(root, bg="#EE5537", height=20, width=20)
b = Button(f1, text="00", font="consolas 19", bg="#E8F2E6", width=8)
b.pack(side=LEFT, padx=3, pady=2, anchor=W)
b.bind("<Button-1>", click)
b = Button(f1, text="0", font="consolas 19", bg="#E8F2E6", width=8)
b.pack(side=LEFT, padx=3, pady=2, anchor=W)
b.bind("<Button-1>", click)
b = Button(f1, text=".", font="consolas 19", bg="#E8F2E6", width=8)
b.pack(side=LEFT, padx=3, pady=2, anchor=W)
b.bind("<Button-1>", click)
f1.pack(anchor=NW)

# % Thanks Func


def thanks():
    tmb.showinfo("Feedback-Window",
                 "Would you like to give us a 5⭐\n Enjoy Your day....")


# $ Thanks Note
f1 = Frame(root, bg="#EE5537", height=10, width=15)
b = Button(f1, text="Share your\nExperience⭐", font="consolas 19",
           bg="#E8F2E6", width=12, command=thanks)
b.pack(side=BOTTOM, padx=3, pady=4, anchor=W)
f1.pack(anchor=S)

root.mainloop()
