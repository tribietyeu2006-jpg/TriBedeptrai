import tkinter as tk
from tkinter import messagebox

def process_string():
    try:
        # Lấy dữ liệu từ các ô nhập
        original_str = entry_s.get()
        p = int(entry_p.get())
        n = int(entry_n.get())

        # Kiểm tra độ dài tối đa theo yêu cầu bài toán
        if len(original_str) > 80:
            messagebox.showwarning("Chú ý", "Chuỗi dài quá 80 ký tự, nhưng hệ thống vẫn sẽ xử lý.")

        # Logic xóa ký tự:
        # Trong Python, vị trí (index) bắt đầu từ 0. 
        # Nếu bài toán coi vị trí đầu tiên là 0:
        result_str = original_str[:p] + original_str[p+n:]

        # Hiển thị kết quả
        lbl_result.config(text=f"Chuỗi kết quả: {result_str}", fg="#D32F2F")
        
    except ValueError:
        messagebox.showerror("Lỗi", "Vị trí p và số lượng n phải là số nguyên!")

# Khởi tạo giao diện
root = tk.Tk()
root.title("Xử lý Chuỗi - Bài 121")
root.geometry("500x300")

# Thành phần giao diện
tk.Label(root, text="Nhập chuỗi ký tự (tối đa 80):", font=("Arial", 10, "bold")).pack(pady=5)
entry_s = tk.Entry(root, width=60)
entry_s.pack(pady=5)
entry_s.insert(0, "Con dieu roi cho vuc tham buon theo") # Ví dụ mẫu

frame_inputs = tk.Frame(root)
frame_inputs.pack(pady=10)

tk.Label(frame_inputs, text="Vị trí bắt đầu (p):").grid(row=0, column=0, padx=5)
entry_p = tk.Entry(frame_inputs, width=10)
entry_p.grid(row=0, column=1, padx=5)
entry_p.insert(0, "9")

tk.Label(frame_inputs, text="Số ký tự xóa (n):").grid(row=0, column=2, padx=5)
entry_n = tk.Entry(frame_inputs, width=10)
entry_n.grid(row=0, column=3, padx=5)
entry_n.insert(0, "17")

btn_process = tk.Button(root, text="Thực hiện xóa", command=process_string, bg="#FF9800", fg="white", font=("Arial", 10, "bold"))
btn_process.pack(pady=15)

lbl_result = tk.Label(root, text="Chuỗi kết quả: ", font=("Arial", 11, "italic"))
lbl_result.pack(pady=10)

root.mainloop()
