import tkinter as tk
import time

root = tk.Tk()
root.title("Calculator")
root.geometry("500x680")

root.resizable(False, False)

Console = True

Variable = True

def analyze_file_hystory():
    try:
        with open("history.txt", "r") as file:
            file.read()
    except FileNotFoundError:
        with open("history.txt", "a") as file:
            file.write(" * * * * * HYSTORY * * * * *\n")

def analyze_file_instructions():
    try:
        with open("instructions.txt", "r") as file:
            file.read()
    except FileNotFoundError:
        with open("instructions.txt", "a", encoding="utf-8") as file:
            file.write(f" * * * * * Instructions * * * * *\n\n- - - - - Русский - - - - -\n1. Нажмите Кнопку 'C' Чтобы Удалить По Одному и Удерживайте Кнопку 'C' Чтобы Удалить Все\n2. Введите Комбинацию '4973903.944' Чтобы Отключить Консоль или Введите Комбинацию '4973903.97' Чтобы Включить Консоль\n\n- - - - - English - - - - - \n1. Press the 'C' button to delete one by one and hold 'C' to delete all. \n2. Enter the combination '4973903.944' to disable the console or enter the combination '4973903.97' to enable the console.")

analyze_file_hystory()
analyze_file_instructions()

def function():
    global Console
    try:
        variable = entry.get()
        if variable == "4973903.944":
            Console = False
            entry.delete(0, tk.END)
        elif variable == "4973903.97":
            Console = True
            entry.delete(0, tk.END)
        elif variable != "":
            method = eval(entry.get())
            entry.delete(0, tk.END)
            entry.insert(tk.END,method)
            with open("history.txt", "a") as file:
                file.write(f"{variable} = {method}\n")
            if Console == True:
                print(f"{variable} = {method}")
        else:
            print("[ERROR] Enter Numbers Please!")
    except NameError:
        entry.delete(0, tk.END)
        if Console == True:
            print("[ERROR] Enter Numbers Please!")
    except SyntaxError:
        if Console == True:
            print("[ERROR]")
    except ZeroDivisionError:
        if Console == True:
            print("[ERROR] Zero Division Error")
    except TypeError:
        if Console == True:
            print()

press_time = 0

def on_press(event):
    global press_time
    press_time = time.time()

def on_release(event):
    global press_time
    duration = time.time() - press_time
    if duration > 0.5:
        delete()
    else:
        delete2()

def delete():
    entry.delete(0, tk.END)

def delete2():
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current[:-1])

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
        print("[ERROR]")
    else:
        entry.insert(tk.END, "+")

def add_letter_minus():
        kop_total = entry.get()
        variable = kop_total.count("-")
        if variable > 0:
            print("[INVALID INPUT]")
        elif kop_total == "":
            print("[ERROR]")
        else:
            entry.insert(tk.END, "-")

def add_letter_kop():
    kop_total = entry.get()
    variable = kop_total.count("*")
    if variable > 1:
        print("[INVALID INPUT]")
    elif kop_total == "":
        print("[ERROR]")
    else:
        entry.insert(tk.END, "*")

def add_letter_bol():
    kop_total = entry.get()
    variable = kop_total.count("/")
    if variable > 0:
        print("[INVALID INPUT]")
    elif kop_total == "":
        print("[ERROR]")
    else:
        entry.insert(tk.END, "/")

def add_letter_ostatok():
    kop_total = entry.get()
    variable = kop_total.count("%")
    if variable > 0:
        print("[INVALID INPUT]")
    elif kop_total == "":
        print("[ERROR]")
    else:
        entry.insert(tk.END, "%")

def add_letter_tocka():
    kop_total = entry.get()
    variable = kop_total.count(".")
    if variable > 0:
        print("[INVALID INPUT]")
    elif kop_total == "":
        print("[ERROR]")
    else:
        entry.insert(tk.END, ".")

entry = tk.Entry(root, font=("Arial", 36, "bold"))
entry.place(x=8, y=5, height=70, width=480)

button1 = tk.Button(root, text="1", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter1)
button1.place(x=15, y=200)

button2 = tk.Button(root, text="2", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter2)
button2.place(x=135, y=200)

button3 = tk.Button(root, text="3", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter3)
button3.place(x=255, y=200)

button4 = tk.Button(root, text="4", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter4)
button4.place(x=15, y=320)

button5 = tk.Button(root, text="5", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter5)
button5.place(x=135, y=320)

button6 = tk.Button(root, text="6", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter6)
button6.place(x=255, y=320)

button7 = tk.Button(root, text="7", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter7)
button7.place(x=15, y=440)

button8 = tk.Button(root, text="8", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter8)
button8.place(x=135, y=440)

button9 = tk.Button(root, text="9", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter9)
button9.place(x=255, y=440)

button0 = tk.Button(root, text="0", font=("Arial", 16, "bold"), width=8, height=4, bg="Orange", fg="Black", activebackground="darkred", command=add_letter0)
button0.place(x=135, y=560)

button_plus = tk.Button(root, text="+", font=("Arial", 16, "bold"), width=8, height=4, fg="White", bg="Black", command=add_letter_plus)
button_plus.place(x=373, y=440)

button_kop = tk.Button(root, text="*", font=("Arial", 16, "bold"), width=8, height=4, fg="White", bg="Black", command=add_letter_kop)
button_kop.place(x=373, y=200)

button_bol = tk.Button(root, text="/", font=("Arial", 16, "bold"), width=8, height=4, fg="White", bg="Black", command=add_letter_bol)
button_bol.place(x=373, y=80)

button_minus = tk.Button(root, text="-", font=("Arial", 16, "bold"), width=8, height=4, fg="White", bg="Black", command=add_letter_minus)
button_minus.place(x=373, y=320)

button_ostatok = tk.Button(root, text="%", font=("Arial", 16, "bold"), width=8, height=4, fg="White", bg="Black", command=add_letter_ostatok)
button_ostatok.place(x=255, y=80)

tocka_button = tk.Button(root, text=".", font=("Arial", 16, "bold"), width=8, height=4, fg="White", bg="Black", command=add_letter_tocka)
tocka_button.place(x=15, y=560)

delete_button = tk.Button(root, text="С", font=("Arial", 16, "bold"), width=8, height=4, fg="White", bg="red")
delete_button.place(x=15, y=80)

delete_button.bind("<ButtonPress-1>", on_press)
delete_button.bind("<ButtonRelease-1>", on_release)

entry_button = tk.Button(root, text="Enter", font=("Arial", 16, "bold"), width=17, height=4, fg="White", bg="Black", command=function)
entry_button.place(x=255, y=560)

def window2():
    window2 = tk.Toplevel()
    window2.title("Castom")
    window2.geometry("500x600")

    def function_text_on_or_off():
        variable = ""
        if Console == True:
            variable = "ON"
        else:
            variable = "OFF"
        win2_label_console_on_or_off = tk.Label(window2, text=f"Console: {variable}", font=("Arial", 16, "bold"), fg="Black")
        win2_label_console_on_or_off.place(x=65, y=120)

    def console_on():
        global Console
        Console = True
        function_text_on_or_off()

    def console_off():
        global Console
        Console = False
        function_text_on_or_off()

    win2_label = tk.Label(window2, text="Console", font=("Arial", 16, "bold"), fg="black")
    win2_label.place(x=90, y=10)

    win2_button_console_on = tk.Button(window2, text="On", font=("Arial", 16, "bold"), fg="White", bg="Green", width=6, height=2, command=console_on)
    win2_button_console_on.place(x=30, y=45)

    win2_button_console_off = tk.Button(window2, text="Off", font=("Arial", 16, "bold"), fg="White", bg="Red", width=6, height=2, command=console_off)
    win2_button_console_off.place(x=150, y=45)
        

icon = tk.PhotoImage(file="files-calculator/nastroyki.png")

nastroyki_button = tk.Button(root, image=icon, width=110, height=108, fg="White", command=window2)
nastroyki_button.place(x=135, y=79)

root.mainloop()