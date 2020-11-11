from tkinter import *

cal=Tk()
cal.title("Simple Calculator")
cal.geometry("400x400")

def key_press(a):
    global exp
    exp+=str(a)
    input.set(exp)

def key_clear():
    global exp
    exp=""
    input.set("")

def key_equal():
    global exp
    try:
        j=str(eval(input.get()))
        input.set(j)
        exp=j
    except:
        input.set("Bad expression")
        exp=""
exp=""
input=StringVar()


entry=Entry(cal,bd=8,font=('arial',20,'bold'),bg="powder blue",textvariable=input,insertwidth=4).grid(columnspan=4)
clear=Button(cal,bd=3,text="Clear",command=lambda:key_clear(),padx=15,pady=10).grid(row=1,column=0)
open_bracket=Button(cal,command=lambda:key_press("("),text="(",padx=15,pady=10).grid(row=1,column=1)
close_bracket=Button(cal,bd=3,text=")",command=lambda:key_press(")"),padx=15,pady=10).grid(row=1,column=2)
button_power=Button(cal,bd=3,text="^",command=lambda:key_press("^"),padx=15,pady=10).grid(row=1,column=3)

button_7=Button(cal,bd=3,text="7",command=lambda:key_press("7"),padx=15,pady=10).grid(row=2,column=0)
button_8=Button(cal,bd=3,text="8",command=lambda:key_press("8"),padx=15,pady=10).grid(row=2,column=1)
button_9=Button(cal,bd=3,text="9",command=lambda:key_press("9"),padx=15,pady=10).grid(row=2,column=2)
button_add=Button(cal,bd=3,text="+",command=lambda:key_press("+"),padx=15,pady=10).grid(row=2,column=3)

button_4=Button(cal,bd=3,text="4",command=lambda:key_press("4"),padx=15,pady=10).grid(row=3,column=0)
button_5=Button(cal,bd=3,text="5",command=lambda:key_press("5"),padx=15,pady=10).grid(row=3,column=1)
button_6=Button(cal,bd=3,text="6",command=lambda:key_press("6"),padx=15,pady=10).grid(row=3,column=2)
button_sub=Button(cal,bd=3,text="-",command=lambda:key_press("-"),padx=15,pady=10).grid(row=3,column=3)

button_3=Button(cal,bd=3,text="3",command=lambda:key_press("3"),padx=15,pady=10).grid(row=4,column=0)
button_2=Button(cal,bd=3,text="2",command=lambda:key_press("2"),padx=15,pady=10).grid(row=4,column=1)
button_1=Button(cal,bd=3,text="1",command=lambda:key_press("1"),padx=15,pady=10).grid(row=4,column=2)
button_mul=Button(cal,bd=3,text="*",command=lambda:key_press("*"),padx=15,pady=10).grid(row=4,column=3)

button_0=Button(cal,bd=3,text="0",command=lambda:key_press("0"),padx=15,pady=10).grid(row=5,column=0)
button_dec=Button(cal,bd=3,text=".",command=lambda:key_press("."),padx=15,pady=10).grid(row=5,column=1)
button_div=Button(cal,bd=3,text="/",command=lambda:key_press("/"),padx=15,pady=10).grid(row=5,column=2)
button_equal=Button(cal,bd=3,text="=",command=lambda:key_equal(),padx=15,pady=10).grid(row=5,column=3)


cal.mainloop()