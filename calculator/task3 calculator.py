#!/usr/bin/env python
# coding: utf-8

# In[1]:


import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")

        self.entry = tk.Entry(root, font=("Helvetica", 20), justify="right")
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        button_texts = [
            ("7", "8", "9", "/"),
            ("4", "5", "6", "*"),
            ("1", "2", "3", "-"),
            ("0", "=", "+", "C"),  # "=" replaces ".", "C" is Clear Button
        ]

        for i in range(len(button_texts)):
            for j in range(len(button_texts[i])):
                text = button_texts[i][j]
                button = tk.Button(root, text=text, font=("Helvetica", 16), command=lambda t=text: self.on_button_click(t))
                button.grid(row=i + 1, column=j, padx=5, pady=5, sticky="nsew")

        self.root.grid_rowconfigure(len(button_texts) + 1, weight=1)
        self.root.grid_columnconfigure(4, weight=1)

    def on_button_click(self, text):
        if text == "=":
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
        elif text == "C":
            self.entry.delete(0, tk.END)
        else:
            current_text = self.entry.get()
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, current_text + text)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()


# In[ ]:



