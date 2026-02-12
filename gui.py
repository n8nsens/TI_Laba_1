import tkinter as tk

root = tk.Tk()
root.title("Шифратор и дешифратор")
root.geometry("800x500+450+100")
root.resizable(False, False)

method = tk.StringVar(value="decimation")  

radio1 = tk.Radiobutton(
    root,
    text="Метод децимаций (eng)",
    variable=method,
    value="decimation",
    font=("Arial", 16),
)
radio1.place(x=80, y=20)  

radio2 = tk.Radiobutton(
    root,
    text="Виженера, прямой ключ (rus)",
    variable=method,
    value="vigenere",
    font=("Arial", 16),
)
radio2.place(x=380, y=20) 

label1 = tk.Label(root, text="Введите ключ:", font=("Arial", 16))
label1.place(x=40, y=100)  
entry1 = tk.Entry(root, font=("Arial", 16), width=30)
entry1.place(x=195, y=100)  
button1 = tk.Button(root, text="Открыть файл", font=("Arial", 16), command=lambda: print("OK"))
button1.place(x=590, y=95)  

label2 = tk.Label(root, text="Исходный текст:", font=("Arial", 16))
label2.place(x=40, y=180)  
entry2 = tk.Entry(root, font=("Arial", 16), width=59)
entry2.place(x=40, y=220) 

label3 = tk.Label(root, text="Итоговый текст:", font=("Arial", 16))
label3.place(x=40, y=260)  
entry3 = tk.Entry(root, font=("Arial", 16), state="readonly", width=59)
entry3.place(x=40, y=300)  

button2 = tk.Button(root, text="Шифровать", font=("Arial", 16), command=lambda: print("OK"))
button2.place(x=150, y=400)  
button3 = tk.Button(root, text="Дешифровать", font=("Arial", 16), command=lambda: print("OK"))
button3.place(x=335, y=400)  
button4 = tk.Button(root, text="Очистить", font=("Arial", 16), command=lambda: print("OK"))
button4.place(x=545, y=400)  

root.mainloop()