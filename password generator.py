import tkinter as tk
import random
import string

class PasswordGenerator:
    def __init__(own, master):
        own.master = master
        master.title("Password Generator")

        own.password_length_label = tk.Label(master, text="Password Length:")
        own.password_length_label.pack()

        own.password_length_entry = tk.Entry(master, width=20)
        own.password_length_entry.pack()

        own.generate_password_button = tk.Button(master, text="Generate Password", command=own.generate_password)
        own.generate_password_button.pack()

        own.password_display_text = tk.Text(master, height=1, width=40)
        own.password_display_text.pack()
   
    def generate_password(own):
        password_length = int(own.password_length_entry.get())
        password = own.generate_random_password(password_length)
        own.password_display_text.delete(1.0, tk.END)
        own.password_display_text.insert(tk.END, password)
        

    def generate_random_password(own, length):
        characters = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        return password

root = tk.Tk()
my_gui = PasswordGenerator(root)
root.mainloop()
