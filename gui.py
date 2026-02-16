import tkinter as tk
from tkinter import filedialog, messagebox
from algorithm import process_decimation, process_vigenere

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
        messagebox.showwarning("Внимание", "Поле итогового текста пусто!")
        return
    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
    )
    
    if path:
        try:
            with open(path, 'w', encoding='utf-8') as f:
                f.write(final_text)
            messagebox.showinfo("Успех", "Файл успешно сохранен!")
        except Exception as e:
            messagebox.showerror("Ошибка", f"Не удалось сохранить файл: {e}")


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

def clear_all():
    key_var.set("")
    text_var.set("")
    on_content_changed()

root = tk.Tk()
root.title("Шифратор и дешифратор")
root.geometry("800x500+450+100")
root.resizable(False, False)


method = tk.StringVar(value="decimation")
key_var = tk.StringVar()
text_var = tk.StringVar()

key_var.trace_add("write", on_content_changed)
text_var.trace_add("write", on_content_changed)

tk.Radiobutton(root, text="Метод децимаций (eng)", variable=method, value="decimation", font=("Arial", 16)).place(x=80, y=20)
tk.Radiobutton(root, text="Виженера, прямой ключ (rus)", variable=method, value="vigenere", font=("Arial", 16)).place(x=380, y=20) 

tk.Label(root, text="Введите ключ:", font=("Arial", 16)).place(x=40, y=100)  
entry1 = tk.Entry(root, font=("Arial", 16), width=30, textvariable=key_var)
entry1.place(x=195, y=100)  
tk.Button(root, text="Открыть файл", font=("Arial", 16), command=open_file).place(x=590, y=95) 

tk.Label(root, text="Исходный текст:", font=("Arial", 16)).place(x=40, y=180)  
entry2 = tk.Entry(root, font=("Arial", 16), width=59, textvariable=text_var)
entry2.place(x=40, y=220) 

tk.Label(root, text="Итоговый текст:", font=("Arial", 16)).place(x=40, y=260)  
entry3 = tk.Entry(root, font=("Arial", 16), state="readonly", width=59)
entry3.place(x=40, y=300)

button_save = tk.Button(root, text="Сохранить файл", font=("Arial", 16), command=save_file).place(x=320, y=350)

tk.Button(root, text="Шифровать", font=("Arial", 16), command=lambda: run_cipher('encrypt')).place(x=150, y=420)  
tk.Button(root, text="Дешифровать", font=("Arial", 16), command=lambda: run_cipher('decrypt')).place(x=335, y=420)  
tk.Button(root, text="Очистить", font=("Arial", 16), command=clear_all).place(x=545, y=420)
  

root.mainloop()
