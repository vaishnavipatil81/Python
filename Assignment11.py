

from tkinter import *


root = Tk()
root.title("Simple GUI Application")
root.geometry("400x300")
root.configure(bg="#e3f2fd")


label = Label(root, text="Enter Your Name:", font=("Arial", 12), bg="#e3f2fd")
label.pack(pady=10)

entry = Entry(root, font=("Arial", 12), width=25)
entry.pack(pady=5)


def show_message():
    name = entry.get()
    if name:
        output_label.config(text=f"Hello, {name}! Welcome to Tkinter GUI.")
    else:
        output_label.config(text="Please enter your name!")


btn = Button(root, text="Submit", font=("Arial", 12), bg="#2196f3", fg="white",
             activebackground="#1976d2", command=show_message)
btn.pack(pady=10)

output_label = Label(root, text="", font=("Arial", 12), bg="#e3f2fd", fg="green")
output_label.pack(pady=10)


exit_btn = Button(root, text="Exit", font=("Arial", 12), bg="red", fg="white",
                  command=root.destroy)
exit_btn.pack(pady=10)


root.mainloop()
