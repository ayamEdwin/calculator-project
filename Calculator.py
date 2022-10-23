# Calculator App
from tkinter import *
win = Tk()
win.title("Calculator")
win.configure(bg="orange")
win.geometry('197x268')
win.resizable(False, False)
txt_box = Entry(win, width=8, borderwidth=2, font='Arial 30 roman bold', bg="grey")
txt_box.insert(0, '0')
txt_box.grid(row=0, column=0, columnspan=5, padx=10, pady=10)
dot = txt_box.get()


def prompt():
    txt_box.insert(0, 'NULL')


def on_click():
    txt_box.delete(0, END)
    win.after(200, prompt)


def erase():
    txt_box.delete(0, END)


def answer():
    s_num = txt_box.get()
    txt_box.delete(0, END)
    if operator == 'add':
        txt_box.insert(0, float(f_num) + float(s_num))
    elif operator == 'multiply':
        txt_box.insert(0, float(f_num) * float(s_num))
    elif operator == 'divide':
        txt_box.insert(0, float(f_num) / float(s_num))
    elif operator == 'subtract':
        txt_box.insert(0, float(f_num) - float(s_num))
    else:
        pass


def addition():
    global f_num
    global operator
    operator = 'add'
    f_num = txt_box.get()
    txt_box.delete(0, END)


def multi():
    global f_num
    global operator
    operator = 'multiply'
    f_num = txt_box.get()
    txt_box.delete(0, END)


def div():
    global f_num
    global operator
    operator = 'divide'
    f_num = txt_box.get()
    txt_box.delete(0, END)


def sub():
    global f_num
    global operator
    operator = 'subtract'
    f_num = txt_box.get()
    txt_box.delete(0, END)


def numbers(num):
    global  current
    current = txt_box.get()
    txt_box.delete(0, END)
    txt_box.insert(0, str(current) + str(num))


def pop_up():
    txt_box.insert(0, '.')


def period():
    txt_box.insert(0, current)
    txt_box.delete(0, END)
    win.after(200, pop_up)


# row_1 buttons
button_mc = Button(win, text="MC", padx=8, pady=1, font='Times 10 bold', bg="blue", command=on_click)
button_mr = Button(win, text="MR", padx=11, pady=1, font='Times 10 bold', bg="blue", command=on_click)
button_ms = Button(win, text="MS", padx=12, pady=1, font='Times 10 bold', bg="blue", command=on_click)
button_mp = Button(win, text="M+", padx=8, pady=1, font='Times 10 bold', bg="blue", command=on_click)

# row_2 buttons
button_clear = Button(win, text="←", padx=13, pady=5, bg="blue", command=erase)
button_ce = Button(win, text="CE", padx=14, pady=5, bg="blue", command=on_click)
button_c = Button(win, text="C", padx=17, pady=5, bg="blue", command=on_click)
button_add = Button(win, text="+", padx=13, pady=5, bg="blue", command=addition)

# row_3 buttons
button_7 = Button(win, text="7", padx=15, pady=5, bg="grey", command=lambda: numbers(7))
button_8 = Button(win, text="8", padx=18, pady=5, bg="grey", command=lambda: numbers(8))
button_9 = Button(win, text="9", padx=18, pady=5, bg="grey", command=lambda: numbers(9))
button_div = Button(win, text="/", padx=15, pady=5, bg="blue", command=div)

# row_4 buttons
button_4 = Button(win, text="4", padx=15, pady=5, bg="grey", command=lambda: numbers(4))
button_5 = Button(win, text="5", padx=18, pady=5, bg="grey", command=lambda: numbers(5))
button_6 = Button(win, text="6", padx=18, pady=5, bg="grey", command=lambda: numbers(6))
button_mul = Button(win, text="*", padx=15, pady=5, bg="blue", command=multi)

# row_5 buttons
button_1 = Button(win, text="1", padx=15, pady=5, bg="grey", command=lambda: numbers(1))
button_2 = Button(win, text="2", padx=18, pady=5, bg="grey", command=lambda: numbers(2))
button_3 = Button(win, text="3", padx=18, pady=5, bg="grey", command=lambda: numbers(3))
button_sub = Button(win, text="-", padx=15, pady=5, bg="blue", command=sub)

# row_6 buttons
button_0 = Button(win, text="0", padx=15, pady=5, bg="grey", command=lambda: numbers(0))
button_dot = Button(win, text=".", padx=20, pady=5, bg="grey", command=period)
button_equal = Button(win, text="=", padx=41, pady=5, bg="blue", command=answer)

# row_1
button_mc.grid(row=1, column=0)
button_mr.grid(row=1, column=1)
button_ms.grid(row=1, column=2)
button_mp.grid(row=1, column=3)

# row_2
button_clear.grid(row=2, column=0)
button_ce.grid(row=2, column=1)
button_c.grid(row=2, column=2)
button_add.grid(row=2, column=3)

# row_3
button_7.grid(row=3, column=0)
button_8.grid(row=3, column=1)
button_9.grid(row=3, column=2)
button_div.grid(row=3, column=3)

# row_4
button_4.grid(row=4, column=0)
button_5.grid(row=4, column=1)
button_6.grid(row=4, column=2)
button_mul.grid(row=4, column=3)

# row_5
button_1.grid(row=5, column=0)
button_2.grid(row=5, column=1)
button_3.grid(row=5, column=2)
button_sub.grid(row=5, column=3)

# row_6
button_0.grid(row=6, column=0)
button_dot.grid(row=6, column=1)
button_equal.grid(row=6, column=2, columnspan=2)

win.mainloop()
