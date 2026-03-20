import tkinter as tk
import random
from tkinter import messagebox

arr = []

def generate_array():
    global arr
    try:
        n = int(entry.get())
        if n <= 0:
            raise ValueError
        arr = [random.randint(-100, 100) for _ in range(n)]
        text_input.delete("1.0", tk.END)
        text_input.insert(tk.END, " ".join(map(str, arr)))
        result.config(text="")
    except:
        messagebox.showerror("Lỗi", "Nhập số nguyên dương hợp lệ!")

def process_array():
    if not arr:
        messagebox.showwarning("Cảnh báo", "Hãy tạo mảng trước!")
        return
    
    # a. đếm số chia hết 4 và tận cùng 6
    count = sum(1 for x in arr if x % 4 == 0 and abs(x) % 10 == 6)
    
    # b. nhân đôi phần tử lẻ
    new_arr = [x*2 if x % 2 != 0 else x for x in arr]
    
    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, " ".join(map(str, new_arr)))
    
    result.config(text=f"Số phần tử chia hết 4, tận cùng 6: {count}")

# GUI
root = tk.Tk()
root.title("Bài 63 - Xử lý mảng")
root.geometry("500x400")

tk.Label(root, text="Nhập số phần tử n:").pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Tạo mảng", command=generate_array).pack(pady=5)
tk.Button(root, text="Xử lý", command=process_array).pack(pady=5)

tk.Label(root, text="Mảng ban đầu:").pack()
text_input = tk.Text(root, height=5)
text_input.pack()

tk.Label(root, text="Mảng sau xử lý:").pack()
text_output = tk.Text(root, height=5)
text_output.pack()

result = tk.Label(root, text="", fg="blue")
result.pack()

root.mainloop()
