import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("500x630")

def function():
    try:
        method = entry.get()
        if method != "":
            method = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END,method)
            print(method)
        else:
            print("[ERROR] Enter Numbers Please!")
    except NameError:
        entry.delete(0, tk.END)
        print("[ERROR] Enter Numbers Please!")
    except SyntaxError:
        print("[ERROR]")
    except ZeroDivisionError:
        print("[ERROR] Zero Division Error")

def delete():
    entry.delete(0, tk.END)

def add_letter1():
    entry.insert(tk.END, "1")

def add_letter2():
    entry.insert(tk.END, "2")

def add_letter3():
    entry.insert(tk.END, "3")

def add_letter4():
    entry.insert(tk.END, "4")

def add_letter5():
    entry.insert(tk.END, "5")

def add_letter6():
    entry.insert(tk.END, "6")

def add_letter7():
    entry.insert(tk.END, "7")

def add_letter8():
    entry.insert(tk.END, "8")

def add_letter9():
    entry.insert(tk.END, "9")

def add_letter0():
    entry.insert(tk.END, "0")

def add_letter_plus():
    kop_total = entry.get()
    variable = kop_total.count("+")
    if variable > 0:
        print("[INVALID INPUT]")
    elif kop_total == "":
        print("[ERROR] Пожалуйста Напишите Какуюто Цифру!")
    else:
        entry.insert(tk.END, "+")

def add_letter_minus():
        kop_total = entry.get()
        variable = kop_total.count("-")
        if variable > 0:
            print("[INVALID INPUT]")
        elif kop_total == "":
            print("[ERROR] Пожалуйста Напишите Какуюто Цифру!")
        else:
            entry.insert(tk.END, "-")

def add_letter_kop():
    kop_total = entry.get()
    variable = kop_total.count("*")
    if variable > 1:
        print("[INVALID INPUT]")
    elif kop_total == "":
        print("[ERROR] Пожалуйста Напишите Какуюто Цифру!")
    else:
        entry.insert(tk.END, "*")

def add_letter_bol():
    kop_total = entry.get()
    variable = kop_total.count("/")
    if variable > 0:
        print("[INVALID INPUT]")
    elif kop_total == "":
        print("[ERROR] Пожалуйста Напишите Какуюто Цифру!")
    else:
        entry.insert(tk.END, "/")

entry = tk.Entry(root, font=("Arial", 36, "bold"))
entry.place(x=8, y=5, height=70, width=480)

text = tk.Label(root, text="Baysahedow Corparation", font=("Arial", 4, "bold"), fg="Black")
text.place(x=620, y=580)

button1 = tk.Button(root, text="1", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter1)
button1.place(x=15, y=100)

button2 = tk.Button(root, text="2", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter2)
button2.place(x=135, y=100)

button3 = tk.Button(root, text="3", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter3)
button3.place(x=255, y=100)

button4 = tk.Button(root, text="4", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter4)
button4.place(x=15, y=220)

button5 = tk.Button(root, text="5", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter5)
button5.place(x=135, y=220)

button6 = tk.Button(root, text="6", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter6)
button6.place(x=255, y=220)

button7 = tk.Button(root, text="7", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter7)
button7.place(x=15, y=340)

button8 = tk.Button(root, text="8", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter8)
button8.place(x=135, y=340)

button9 = tk.Button(root, text="9", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter9)
button9.place(x=255, y=340)

button0 = tk.Button(root, text="0", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter0)
button0.place(x=135, y=460)

button_plus = tk.Button(root, text="+", font=("Arial", 16, "bold"), width=8, height=4, fg="White", bg="Black", command=add_letter_plus)
button_plus.place(x=375, y=100)

button_kop = tk.Button(root, text="*", font=("Arial", 16, "bold"), width=8, height=4, fg="White", bg="Black", command=add_letter_kop)
button_kop.place(x=375, y=340)

button_bol = tk.Button(root, text="/", font=("Arial", 16, "bold"), width=8, height=4, fg="White", bg="Black", command=add_letter_bol)
button_bol.place(x=375, y=460)

button_minus = tk.Button(root, text="-", font=("Arial", 16, "bold"), width=8, height=4, fg="White", bg="Black", command=add_letter_minus)
button_minus.place(x=375, y=220)

delete_button = tk.Button(root, text="DEL", font=("Arial", 16, "bold"), width=8, height=4, fg="White", bg="Black", command=delete)
delete_button.place(x=15, y=460)

entry_button = tk.Button(root, text="Enter", font=("Arial", 16, "bold"), width=8, height=4, fg="White", bg="Black", command=function)
entry_button.place(x=255, y=460)

root.mainloop()