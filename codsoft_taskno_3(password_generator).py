from tkinter import *
import string
import random
root = Tk()
root.title("password generator")
root.geometry('240x360')
root.resizable(False, False)
root.config(bg = '#003')
def generator():
 small_alpha = string.ascii_lowercase
 capital_alpha = string.ascii_uppercase
 numbers = string.digits
 special_char = string.punctuation
 all = small_alpha + capital_alpha + numbers + special_char
 password_length = int(length_box.get())
 #gen_password = random.sample(all, password_length)
 #passwordField.insert(0, gen_password)
 if choice.get() == 1:
    passwordField.insert(0, random.sample(small_alpha, password_length))
 elif choice.get() == 2:
    passwordField.insert(0, random.sample(small_alpha + capital_alpha, password_length))
  
 elif choice.get() == 3:
    passwordField.insert(0, random.sample(all, password_length))




choice = IntVar()
Font = ('Arial', 13, 'bold')
password_label = Label(root, text = 'password generator', font = ('times new roman', 20, 'bold'), bg = '#003', fg = 'white')
password_label.grid(pady = 5)
weak_btn = Radiobutton(root, text = 'Week', value = 1, variable = choice, font = Font)
weak_btn.grid(pady = 5)

Medium_btn = Radiobutton(root, text = 'Medium', value = 2, variable = choice, font = Font)
Medium_btn.grid(pady = 5)

strong_btn = Radiobutton(root, text = 'Strong', value = 3, variable = choice, font = Font)
strong_btn.grid(pady = 5)

length_label = Label(root, text = 'password Length', font = Font, bg = '#003', fg = 'white')
length_label.grid(pady = 5)

length_box = Spinbox(root, from_=5, to_=18, width = 5, font = Font)
length_box.grid(pady = 5)

generate_button = Button(root, text = 'Generate', font  = Font, command = generator)
generate_button.grid(pady = 5)

passwordField = Entry(root, width = 25, bd = 2, font = Font)
passwordField.grid(pady = 10)


root.mainloop()
