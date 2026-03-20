import tkinter as tk
from tkinter import messagebox

def calculate():
    try:
        # Lấy dữ liệu từ ô nhập liệu và chuyển thành set
        set_a = set(map(int, entry_a.get().replace(',', ' ').split()))
        set_b = set(map(int, entry_b.get().replace(',', ' ').split()))

        # Thực hiện các phép toán tập hợp
        giao = sorted(list(set_a & set_b))
        hop = sorted(list(set_a | set_b))
        hieu = sorted(list(set_a - set_b))

        # Hiển thị kết quả lên giao diện
        lbl_giao.config(text=f"C = A * B (Giao): {giao}")
        lbl_hop.config(text=f"C = A + B (Hợp): {hop}")
        lbl_hieu.config(text=f"C = A \ B (Hiệu): {hieu}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng chỉ nhập số nguyên, cách nhau bởi dấu cách hoặc dấu phẩy.")

# Khởi tạo cửa sổ chính
root = tk.Tk()
root.title("Phép toán Tập hợp - Bài 83")
root.geometry("450x350")

# Thành phần giao diện
tk.Label(root, text="Nhập tập hợp A (VD: 1, 2, 3, 5):").pack(pady=5)
entry_a = tk.Entry(root, width=40)
entry_a.pack()

tk.Label(root, text="Nhập tập hợp B (VD: 1, 3, 6, 7):").pack(pady=5)
entry_b = tk.Entry(root, width=40)
entry_b.pack()

btn_calc = tk.Button(root, text="Tính toán", command=calculate, bg="#4CAF50", fg="white")
btn_calc.pack(pady=20)

# Khu vực hiển thị kết quả
frame_res = tk.LabelFrame(root, text="Kết quả", padx=10, pady=10)
frame_res.pack(padx=10, fill="both")

lbl_giao = tk.Label(frame_res, text="C = A * B (Giao): ", fg="blue")
lbl_giao.pack(anchor="w")

lbl_hop = tk.Label(frame_res, text="C = A + B (Hợp): ", fg="green")
lbl_hop.pack(anchor="w")

lbl_hieu = tk.Label(frame_res, text="C = A \ B (Hiệu): ", fg="red")
lbl_hieu.pack(anchor="w")

root.mainloop()
