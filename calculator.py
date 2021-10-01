from tkinter import *
calculator = Tk()
calculator.title("Calculator Isaiahekundayo17@gmail.com")
calculator.geometry('450x350')
calculator['bg']= "grey"

num = ""
num1 = 0
num2 = None


def btnPushed(text):
    inputOutput.insert(END,text)


def addbtnPushed():
    global num1
    storeNum = inputOutput.get()
    num1 = float(num1)
    num1 += float(inputOutput.get())
    num1 = str(num1)
    hidden.config(text=f"{hidden.cget('text')}+{storeNum} = {num1}")
    inputOutput.delete(0, END)



def subbtnPushed():
    global num1
    storeNum = inputOutput.get()
    num1 = float(num1)
    num1 -= float(inputOutput.get())
    num1 = str(num1)
    hidden.config(text=f"{hidden.cget('text')}-{storeNum} = {num1}")
    inputOutput.delete(0, END)



def divbtnPushed():
    global num1
    storeNum = inputOutput.get()
    num1 = float(num1)
    num1 /= float(inputOutput.get())
    num1 = str(num1)
    hidden.config(text=f"{hidden.cget('text')}/{storeNum} = {num1}")
    inputOutput.delete(0, END)

    


def mulbtnPushed():
    global num1
    storeNum = inputOutput.get()
    num1 = float(num1)
    num1 *= float(inputOutput.get())
    num1 = str(num1)
    hidden.config(text=f"{hidden.cget('text')}+{storeNum} = {num1}")
    inputOutput.delete(0, END)


def cbtnPushed():
    global num1
    inputOutput.delete(0, END)
    hidden.config(text=0)
    num1 = 0
    
def equalbtnPushed():
    global num1
    num1 = inputOutput.get()
    if num1 == "":
        num1 = "0"
        hidden.config(text=num1)
    else:
        hidden.config(text=num1)
    
inputOutput = Entry(calculator , text=0, width=50,font=19)
hidden = Label(calculator, text=0, width=50, height=2, bg="grey",border=0, font=20)
button9 = Button(calculator, text="9", command=lambda:btnPushed("9"), width=15, height=3)
button8 = Button(calculator, text="8", command=lambda:btnPushed("8"), width=15, height=3)
button7 = Button(calculator, text="7", command=lambda:btnPushed("7"), width=15, height=3)
button6 = Button(calculator, text="6", command=lambda:btnPushed("6"), width=15, height=3)
button5 = Button(calculator, text="5", command=lambda:btnPushed("5"), width=15, height=3)
button4 = Button(calculator, text="4", command=lambda:btnPushed("4"), width=15, height=3)
button3 = Button(calculator, text="3", command=lambda:btnPushed("3"), width=15, height=3)
button2 = Button(calculator, text="2", command=lambda:btnPushed("2"), width=15, height=3)
button1 = Button(calculator, text="1", command=lambda:btnPushed("1"), width=15, height=3)
button0 = Button(calculator, text="0", command=lambda:btnPushed("0"), width=15, height=3)

addBtn = Button(calculator, text="+", command=lambda:addbtnPushed(), width=15, height=3)
subBtn = Button(calculator, text="-", command=lambda:subbtnPushed(), width=15, height=3)
divBtn = Button(calculator, text="/", command=lambda:divbtnPushed(), width=15, height=3)
mulBtn = Button(calculator, text="*", command=lambda:mulbtnPushed(), width=15, height=3)
equalBtn = Button(calculator, text="=", command=lambda:equalbtnPushed(), width=15, height=3)
clear = Button(calculator, text="clear", command=lambda:cbtnPushed(), width=15, height=3)


inputOutput.grid(row=0, column=0, columnspan=4, ipady=35)
hidden.grid(row=1,column=0,columnspan= 4)
button9.grid(row=2, column=0)
button8.grid(row=2, column=1)
button7.grid(row=2, column=2)
button6.grid(row=3, column=0)
button5.grid(row=3, column=1)
button4.grid(row=3, column=2)
button3.grid(row=4, column=0)
button2.grid(row=4, column=1)
button1.grid(row=4, column=2)
button0.grid(row=5, column=0)

addBtn.grid(row=2, column=3)
subBtn.grid(row=3, column=3)
divBtn.grid(row=4, column=3)
mulBtn.grid(row=5, column=1)
equalBtn.grid(row=5, column=2)
clear.grid(row=5, column=3)



calculator.mainloop()
