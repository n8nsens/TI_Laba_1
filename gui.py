import tkinter as tk
from tkinter import filedialog, messagebox
from algorithm import process_decimation

def open_file():
    path = filedialog.askopenfilename()
    if path:
        with open(path, 'r', encoding='utf-8') as f:
            entry2.delete(0, tk.END)
            entry2.insert(0, f.read())

def run_cipher(mode):
    raw_text = entry2.get()
    key = entry1.get()
    
    if method.get() == "decimation":
        res = process_decimation(raw_text, key, mode)
    else:
        res = "Виженер еще в разработке..."

    entry3.config(state="normal")
    entry3.delete(0, tk.END)
    entry3.insert(0, res)
    entry3.config(state="readonly")

def clear_all():
    entry1.delete(0, tk.END)
    entry2.delete(0, tk.END)
    entry3.config(state="normal")
    entry3.delete(0, tk.END)
    entry3.config(state="readonly")

root = tk.Tk()
root.title("Шифратор и дешифратор")
root.geometry("800x500+450+100")
root.resizable(False, False)

method = tk.StringVar(value="decimation")  

tk.Radiobutton(root, text="Метод децимаций (eng)", variable=method, value="decimation", font=("Arial", 16)).place(x=80, y=20)
tk.Radiobutton(root, text="Виженера, прямой ключ (rus)", variable=method, value="vigenere", font=("Arial", 16)).place(x=380, y=20) 

tk.Label(root, text="Введите ключ:", font=("Arial", 16)).place(x=40, y=100)  
entry1 = tk.Entry(root, font=("Arial", 16), width=30)
entry1.place(x=195, y=100)  
tk.Button(root, text="Открыть файл", font=("Arial", 16), command=open_file).place(x=590, y=95) 

tk.Label(root, text="Исходный текст:", font=("Arial", 16)).place(x=40, y=180)  
entry2 = tk.Entry(root, font=("Arial", 16), width=59)
entry2.place(x=40, y=220) 
tk.Label(root, text="Итоговый текст:", font=("Arial", 16)).place(x=40, y=260)  
entry3 = tk.Entry(root, font=("Arial", 16), state="readonly", width=59)
entry3.place(x=40, y=300)  

tk.Button(root, text="Шифровать", font=("Arial", 16), command=lambda: run_cipher('encrypt')).place(x=150, y=400)  
tk.Button(root, text="Дешифровать", font=("Arial", 16), command=lambda: run_cipher('decrypt')).place(x=335, y=400)  
tk.Button(root, text="Очистить", font=("Arial", 16), command=clear_all).place(x=545, y=400)  

root.mainloop()
