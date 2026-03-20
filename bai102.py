import tkinter as tk
from tkinter import messagebox
import random

def generate_and_transpose():
    try:
        # Lấy giá trị n và m từ giao diện
        n = int(entry_n.get())
        m = int(entry_m.get())
        
        if n <= 0 or m <= 0:
            raise ValueError

        # a. Tạo ma trận ngẫu nhiên n x m trong đoạn [-100, 100]
        matrix_a = [[random.randint(-100, 100) for _ in range(m)] for _ in range(n)]
        
        # b. Chuyển vị ma trận (Transpose)
        # Ma trận chuyển vị sẽ có kích thước m x n
        matrix_at = [[matrix_a[i][j] for i in range(n)] for j in range(m)]

        # Hàm hỗ trợ định dạng ma trận để hiển thị
        def format_matrix(matrix):
            return "\n".join(["\t".join(map(str, row)) for row in matrix])

        # Hiển thị lên giao diện
        txt_original.delete(1.0, tk.END)
        txt_original.insert(tk.END, format_matrix(matrix_a))
        
        txt_transpose.delete(1.0, tk.END)
        txt_transpose.insert(tk.END, format_matrix(matrix_at))
        
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên dương cho n và m!")

# Khởi tạo cửa sổ
root = tk.Tk()
root.title("Quản lý Ma trận - Bài 102")
root.geometry("500x500")

# Khu vực nhập liệu
frame_input = tk.Frame(root, pady=10)
frame_input.pack()

tk.Label(frame_input, text="Nhập n (hàng):").grid(row=0, column=0, padx=5)
entry_n = tk.Entry(frame_input, width=10)
entry_n.grid(row=0, column=1, padx=5)

tk.Label(frame_input, text="Nhập m (cột):").grid(row=0, column=2, padx=5)
entry_m = tk.Entry(frame_input, width=10)
entry_m.grid(row=0, column=3, padx=5)

btn_run = tk.Button(root, text="Tạo & Chuyển vị", command=generate_and_transpose, bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
btn_run.pack(pady=10)

# Khu vực hiển thị kết quả
tk.Label(root, text="Ma trận gốc A (n x m):", font=("Arial", 9, "italic")).pack()
txt_original = tk.Text(root, height=8, width=50, bg="#f0f0f0")
txt_original.pack(pady=5)

tk.Label(root, text="Ma trận chuyển vị Aᵀ (m x n):", font=("Arial", 9, "italic")).pack()
txt_transpose = tk.Text(root, height=8, width=50, bg="#e8f5e9")
txt_transpose.pack(pady=5)

root.mainloop()
