import tkinter as tk
from tkinter import messagebox

def odd_sum_recursive(arr, n):
    # Điều kiện dừng: Nếu mảng rỗng (n == 0)
    if n == 0:
        return 0
    
    # Lấy phần tử cuối cùng của mảng hiện tại
    last_element = arr[n-1]
    
    # Kiểm tra nếu là số lẻ thì cộng vào, ngược lại cộng 0
    current_value = last_element if last_element % 2 != 0 else 0
    
    # Đệ quy gọi lại chính nó với n-1 phần tử còn lại
    return current_value + odd_sum_recursive(arr, n - 1)

def handle_calculate():
    try:
        # Lấy dữ liệu từ ô nhập và chuyển thành list số nguyên
        data = entry_input.get().replace(',', ' ').split()
        arr = [int(x) for x in data]
        
        # Gọi hàm đệ quy
        result = odd_sum_recursive(arr, len(arr))
        
        # Hiển thị kết quả
        lbl_result.config(text=f"Tổng các phần tử lẻ: {result}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng chỉ nhập các số nguyên cách nhau bằng khoảng trắng!")

# Thiết lập giao diện
root = tk.Tk()
root.title("Tính Tổng Lẻ Đệ Quy - Bài 150")
root.geometry("400x250")

tk.Label(root, text="Nhập mảng số nguyên:", font=("Arial", 10, "bold")).pack(pady=10)
entry_input = tk.Entry(root, width=40, justify='center')
entry_input.pack(pady=5)
entry_input.insert(0, "2 3 4 5 6 7") # Ví dụ từ ảnh

btn_calc = tk.Button(root, text="Tính Tổng Lẻ", command=handle_calculate, 
                     bg="#673AB7", fg="white", font=("Arial", 10, "bold"))
btn_calc.pack(pady=20)

lbl_result = tk.Label(root, text="Tổng các phần tử lẻ: ", font=("Arial", 12), fg="#E91E63")
lbl_result.pack(pady=10)

root.mainloop()
