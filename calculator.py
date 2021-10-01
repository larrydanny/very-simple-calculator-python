from tkinter import *

window = Tk()

window.title("Simple Calculator")
window.configure(background="#333333")
dotClicked = False


def buttonClick(number):
    fieldValue = entry.get()
    entry.delete(0, END)
    entry.insert(0, fieldValue + number)


def buttonDot():
    global dotClicked
    if not dotClicked:
        fieldValue = entry.get()
        entry.delete(0, END)
        entry.insert(0, fieldValue + ".")


def buttonCancel():
    entry.delete(0, END)


def buttonPlus():
    global first_number, sign
    first_number = entry.get()
    entry.delete(0, END)
    sign = "+"


def buttonMinus():
    global first_number, sign
    first_number = entry.get()
    entry.delete(0, END)
    sign = "-"


def buttonMultiply():
    global first_number, sign
    first_number = entry.get()
    entry.delete(0, END)
    sign = "*"


def buttonDivide():
    global first_number, sign
    first_number = entry.get()
    entry.delete(0, END)
    sign = "/"


def buttonEqual():
    secondNumber = entry.get()
    entry.delete(0, END)

    if sign == "+":
        entry.insert(0, float(first_number) + float(secondNumber))

    if sign == "-":
        entry.insert(0, float(first_number) - float(secondNumber))

    if sign == "*":
        entry.insert(0, float(first_number) * float(secondNumber))

    if sign == "/":
        entry.insert(0, float(float(first_number) / float(secondNumber)))


entry = Entry(window)
entry.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

button1 = Button(window,
                 command=lambda: buttonClick("1"),
                 highlightbackground="#333333",
                 text="1",
                 pady=10)
button1.grid(row=1, column=0)

button2 = Button(window,
                 command=lambda: buttonClick("2"),
                 highlightbackground="#333333",
                 text="2",
                 pady=10)
button2.grid(row=1, column=1)

button3 = Button(window,
                 command=lambda: buttonClick("3"),
                 highlightbackground="#333333",
                 text="3",
                 pady=10)
button3.grid(row=1, column=2)

button4 = Button(window,
                 command=lambda: buttonClick("4"),
                 highlightbackground="#333333",
                 text="4",
                 pady=10)
button4.grid(row=2, column=0)

button5 = Button(window,
                 command=lambda: buttonClick("5"),
                 highlightbackground="#333333",
                 text="5",
                 pady=10)
button5.grid(row=2, column=1)

button6 = Button(window,
                 command=lambda: buttonClick("6"),
                 highlightbackground="#333333",
                 text="6",
                 pady=10)
button6.grid(row=2, column=2)

button7 = Button(window,
                 command=lambda: buttonClick("7"),
                 highlightbackground="#333333",
                 text="7",
                 pady=10)
button7.grid(row=3, column=0)

button8 = Button(window,
                 command=lambda: buttonClick("8"),
                 highlightbackground="#333333",
                 text="8",
                 pady=10)
button8.grid(row=3, column=1)

button9 = Button(window,
                 command=lambda: buttonClick("9"),
                 highlightbackground="#333333",
                 text="9",
                 pady=10)
button9.grid(row=3, column=2)

button0 = Button(window,
                 command=lambda: buttonClick("0"),
                 highlightbackground="#333333",
                 text="0",
                 pady=10)
button0.grid(row=4, column=0)

buttonPlus = Button(window,
                    command=buttonPlus,
                    highlightbackground="#333333",
                    text="+",
                    pady=10)
buttonPlus.grid(row=4, column=1)

buttonMinus = Button(window,
                     command=buttonMinus,
                     highlightbackground="#333333",
                     text="-",
                     pady=10)
buttonMinus.grid(row=4, column=2)

buttonMultiply = Button(window,
                        command=buttonMultiply,
                        highlightbackground="#333333",
                        text="*",
                        pady=10)
buttonMultiply.grid(row=5, column=0)

buttonDivide = Button(window,
                      command=buttonDivide,
                      highlightbackground="#333333",
                      text="/",
                      pady=10)
buttonDivide.grid(row=5, column=1)

buttonEqual = Button(window,
                     command=buttonEqual,
                     highlightbackground="#333333",
                     text="=",
                     pady=10)
buttonEqual.grid(row=5, column=2)

buttonCancel = Button(window,
                      command=buttonCancel,
                      highlightbackground="#333333",
                      text="C",
                      pady=10)
buttonCancel.grid(row=6, column=0)

buttonDot = Button(window,
                   command=buttonDot,
                   highlightbackground="#333333",
                   text=".",
                   pady=10)
buttonDot.grid(row=6, column=1)


window.mainloop()
