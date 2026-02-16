import tkinter as tk
from tkinter import filedialog, messagebox
from algorithm import process_decimation, process_vigenere

BG_COLOR = "#FFC0CB"      
BTN_COLOR = "#FF738b"     
ENTRY_COLOR = "#FFD7DE"

def on_content_changed(*args):
    entry3.config(state="normal")
    entry3.delete(0, tk.END)
    entry3.config(state="readonly")

def open_file():
    path = filedialog.askopenfilename()
    if path:
        with open(path, 'r', encoding='utf-8') as f:
            text_var.set(f.read())

def save_file():
    final_text = entry3.get()
    if not final_text:
        messagebox.showwarning("Внимание", "Поле итога пусто!")
        return
    path = filedialog.asksaveasfilename(defaultextension=".txt")
    if path:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(final_text)

def run_cipher(mode):
    raw_text = text_var.get()
    key = key_var.get()
    if method.get() == "decimation":
        res = process_decimation(raw_text, key, mode)
    else:
        res = process_vigenere(raw_text, key, mode)
    entry3.config(state="normal")
    entry3.delete(0, tk.END)
    entry3.insert(0, res)
    entry3.config(state="readonly")

root = tk.Tk()
root.title("Шифратор и Дешифратор")
root.geometry("630x360+500+200")
root.resizable(False, False)
root.configure(bg=BG_COLOR)

method = tk.StringVar(value="decimation")
key_var = tk.StringVar()
text_var = tk.StringVar()
key_var.trace_add("write", on_content_changed)
text_var.trace_add("write", on_content_changed)

FNT = ("Arial", 12)

tk.Radiobutton(root, text="Метод децимаций (eng)", variable=method, value="decimation", 
               font=FNT, bg=BG_COLOR).place(x=80, y=15)
tk.Radiobutton(root, text="Виженера, прямой ключ (rus)", variable=method, value="vigenere", 
               font=FNT, bg=BG_COLOR).place(x=310, y=15) 

tk.Label(root, text="Ключ:", font=FNT, bg=BG_COLOR).place(x=40, y=70)  
entry1 = tk.Entry(root, font=FNT, width=40, textvariable=key_var, bg=ENTRY_COLOR)
entry1.place(x=100, y=70)  
tk.Button(root, text="Открыть файл", font=FNT, command=open_file, bg=BTN_COLOR).place(x=470, y=65) 

tk.Label(root, text="Исходный текст:", font=FNT, bg=BG_COLOR).place(x=40, y=120)  
entry2 = tk.Entry(root, font=FNT, width=60, textvariable=text_var, bg=ENTRY_COLOR)
entry2.place(x=40, y=150) 

tk.Label(root, text="Итоговый текст:", font=FNT, bg=BG_COLOR).place(x=40, y=200)  
entry3 = tk.Entry(root, font=FNT, state="readonly", width=60, readonlybackground=ENTRY_COLOR)
entry3.place(x=40, y=230)

tk.Button(root, text="Сохранить результат", font=FNT, command=save_file, bg=BTN_COLOR).place(x=312, y=280)
tk.Button(root, text="Шифровать", font=FNT, command=lambda: run_cipher('encrypt'), bg=BTN_COLOR).place(x=40, y=280)  
tk.Button(root, text="Дешифровать", font=FNT, command=lambda: run_cipher('decrypt'), bg=BTN_COLOR).place(x=167, y=280)  
tk.Button(root, text="Очистить", font=FNT, command=lambda: [key_var.set(""), text_var.set("")], bg=BTN_COLOR).place(x=500, y=280)

root.mainloop()
