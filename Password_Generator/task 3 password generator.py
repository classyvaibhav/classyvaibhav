#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import random
from tkinter import messagebox

root = Tk()
root.geometry("550x600")

passstr = StringVar()
passlen = IntVar()
passlen.set(0)

def generate_password():
    pass1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 
            'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
            'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
            'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 
            'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', 
            '9', '0', ' ', '!', '@', '#', '$', '%', '^', '&', 
            '*', '(', ')']

    password = ""

    for x in range(passlen.get()):
        password = password + random.choice(pass1)

    passstr.set(password)

def accept_password():
    accepted_password = passstr.get()
    messagebox.showinfo("Accepted Password", f"The accepted password is:\n{accepted_password}")

def reset_password():
    passstr.set("")
    passlen.set(0)

result_label = Label(root, text='Password Generator', bg='Darkblue', fg='white', width=31, height=2)
result_label.grid(row=0, column=0, columnspan=5, pady=(30, 25))
result_label.config(font=('Algerian', 20, 'bold'))

result_label = Label(root, text='Enter User Name:', fg='black', width=15, height=1)
result_label.grid(row=2, column=0, columnspan=5, pady=(25, 13), sticky='w')
result_label.config(font=('Arial Black', 11))

user_name_entry = Entry(root, text='', width=35)
user_name_entry.grid(row=2, column=3, ipady=1)

result_label = Label(root, text='Enter Password Length:', fg='black', width=19, height=1)
result_label.grid(row=3, column=0, columnspan=5, pady=(5, 15), sticky='w')
result_label.config(font=('Arial Black', 11))

pass_len_entry = Entry(root, textvariable=passlen, width=35)
pass_len_entry.grid(row=3, column=3, ipady=1)

result_label = Label(root, text='Generated Password:', fg='black', width=17, height=1)
result_label.grid(row=4, column=0, columnspan=5, pady=(5, 15), sticky='w')
result_label.config(font=('Arial Black', 11))

result_entry = Entry(root, textvariable=passstr, width=35)
result_entry.grid(row=4, column=3, ipady=1)

Button(root, text="Generate Password", command=generate_password).grid(row=5, column=0, columnspan=5, pady=(5, 10), ipady=11)

Button(root, text="Accept Password", command=accept_password).grid(row=6, column=0, columnspan=5, pady=(5, 15), ipady=11)

Button(root, text="Reset Password", command=reset_password).grid(row=7, column=0, columnspan=5, pady=(5, 15), ipady=11)

root.mainloop()


# In[ ]:



