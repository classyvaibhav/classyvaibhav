#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []

        self.task_var = tk.StringVar()

        self.task_entry = tk.Entry(root, textvariable=self.task_var, width=40)
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
        self.add_button.grid(row=0, column=1, padx=5, pady=10)

        self.task_listbox = tk.Listbox(root, width=50)
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        self.edit_button = tk.Button(root, text="Edit", command=self.edit_task)
        self.edit_button.grid(row=2, column=0, padx=5, pady=10)

        self.delete_button = tk.Button(root, text="Delete", command=self.delete_task)
        self.delete_button.grid(row=2, column=1, padx=5, pady=10)

    def add_task(self):
        task = self.task_var.get()
        if task:
            self.tasks.append(task)
            self.update_task_listbox()
            self.task_var.set("")

    def edit_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            new_task = self.task_var.get()
            if new_task:
                self.tasks[selected_index] = new_task
                self.update_task_listbox()
                self.task_var.set("")
            else:
                messagebox.showwarning("Warning", "Task cannot be empty!")

    def delete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            selected_index = selected_index[0]
            del self.tasks[selected_index]
            self.update_task_listbox()

    def update_task_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoListApp(root)
    root.mainloop()


# In[ ]:



