import tkinter as tk
from tkinter import messagebox

# Hàm kiểm tra số hoàn hảo
def is_perfect(n):
    if n < 2:
        return False
    s = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            s += i
            if i != n // i:
                s += n // i
    return s == n

# Hàm xử lý khi bấm nút
def find_perfect():
    try:
        n = int(entry.get())
        result = []
        for i in range(2, n):
            if is_perfect(i):
                result.append(i)
        output.config(text="Các số hoàn hảo: " + " ".join(map(str, result)))
    except:
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên hợp lệ!")

# Tạo cửa sổ
root = tk.Tk()
root.title("Tìm số hoàn hảo")
root.geometry("400x200")

# Giao diện
label = tk.Label(root, text="Nhập n:")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Tìm", command=find_perfect)
button.pack()

output = tk.Label(root, text="")
output.pack()

# Chạy chương trình
root.mainloop()
