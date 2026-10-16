import tkinter as tk

root = tk.Tk()
root.title("Calculator")
root.geometry("700x600")

def function():
    try:
        method = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END,method)
        print(method)
    except NameError:
        entry.delete(0, tk.END)
        print("Error")
    except SyntaxError:
        entry.delete(0, tk.END)
        print("Error")

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
    entry.insert(tk.END, "+")

def add_letter_minus():
    entry.insert(tk.END, "-")

def add_letter_kop():
    entry.insert(tk.END, "*")

def add_letter_bol():
    entry.insert(tk.END, "/")

entry = tk.Entry(root, font=("Arial", 36, "bold"))
entry.place(x=80, y=5)

text = tk.Label(root, text="Baysahedow Corparation", font=("Arial", 4, "bold"), fg="Black")
text.place(x=620, y=580)

button1 = tk.Button(root, text="1", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter1)
button1.place(x=30, y=100)

button2 = tk.Button(root, text="2", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter2)
button2.place(x=150, y=100)

button3 = tk.Button(root, text="3", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter3)
button3.place(x=270, y=100)

button4 = tk.Button(root, text="4", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter4)
button4.place(x=30, y=220)

button5 = tk.Button(root, text="5", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter5)
button5.place(x=150, y=220)

button6 = tk.Button(root, text="6", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter6)
button6.place(x=270, y=220)

button7 = tk.Button(root, text="7", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter7)
button7.place(x=30, y=340)

button8 = tk.Button(root, text="8", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter8)
button8.place(x=150, y=340)

button9 = tk.Button(root, text="9", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter9)
button9.place(x=270, y=340)

button0 = tk.Button(root, text="0", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter0)
button0.place(x=150, y=460)

button_plus = tk.Button(root, text="+", font=("Arial", 16, "bold"), width=8, height=3, fg="Black", command=add_letter_plus)
button_plus.place(x=460, y=220)

button_kop = tk.Button(root, text="*", font=("Arial", 16, "bold"), width=8, height=3, fg="Black", command=add_letter_kop)
button_kop.place(x=580, y=220)

button_bol = tk.Button(root, text="/", font=("Arial", 16, "bold"), width=8, height=3, fg="Black", command=add_letter_bol)
button_bol.place(x=580, y=315)

button_minus = tk.Button(root, text="-", font=("Arial", 16, "bold"), width=8, height=3, fg="Black", command=add_letter_minus)
button_minus.place(x=460, y=315)

delete_button = tk.Button(root, text="DEL", font=("Arial", 16, "bold"), width=8, height=4, fg="Black", command=delete)
delete_button.place(x=30, y=460)

entry_button = tk.Button(root, text="Enter", font=("Arial", 16, "bold"), width=17, height=4, fg="Black", command=function)
entry_button.place(x=460, y=100)

root.mainloop()