from random import randint
import tkinter as tk

def increase_balance():
        current_balance = int(balance_label["text"][:-1])
        new_balance = current_balance + randint(100,1000)
        balance_label.config(text=f"{new_balance}$")
window = tk.Tk()
window.title("bablo")

balance_label = tk.Label(window, text="0$", font=("Arial", 24))
balance_label.pack(pady=20)
increase_button = tk.Button(window, text="knopka bablo", command=increase_balance, font=("Arial", 18), bg="gold", fg="darkgreen")
increase_button.pack(pady=10)
window.mainloop()
