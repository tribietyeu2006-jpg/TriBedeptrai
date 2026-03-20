import tkinter as tk
from ctypes import Structure, Union, c_ubyte, c_uint8

# Định nghĩa Bit Field (mô phỏng cách làm trong C)
class Bits(Structure):
    _fields_ = [
        ("b7", c_uint8, 1), ("b6", c_uint8, 1), ("b5", c_uint8, 1), ("b4", c_uint8, 1),
        ("b3", c_uint8, 1), ("b2", c_uint8, 1), ("b1", c_uint8, 1), ("b0", c_uint8, 1),
    ]

# Định nghĩa Union để "ánh xạ" ký tự và bit field vào cùng một vùng nhớ
class CharToBit(Union):
    _fields_ = [("char_val", c_ubyte), ("bits", Bits)]

def convert_to_binary():
    char_input = entry_char.get()
    if len(char_input) != 1:
        lbl_result.config(text="Vui lòng chỉ nhập 1 ký tự!")
        return

    # Chuyển ký tự thành mã ASCII và đưa vào union
    data = CharToBit()
    data.char_val = ord(char_input)

    # Truy xuất từng bit từ bit field mà không cần toán tử bit hay phép chia
    binary_str = f"{data.bits.b0} {data.bits.b1} {data.bits.b2} {data.bits.b3} " \
                 f"{data.bits.b4} {data.bits.b5} {data.bits.b6} {data.bits.b7}"
    
    lbl_result.config(text=f"Mã nhị phân: {binary_str}")

# Giao diện đồ họa
root = tk.Tk()
root.title("Bit Field & Union - Bài 171")
root.geometry("400x250")

tk.Label(root, text="Nhập một ký tự:", font=("Arial", 10, "bold")).pack(pady=10)
entry_char = tk.Entry(root, width=10, justify='center', font=("Arial", 14))
entry_char.pack(pady=5)
entry_char.insert(0, "Z")

btn_convert = tk.Button(root, text="Hiển thị Nhị phân", command=convert_to_binary, 
                        bg="#009688", fg="white", font=("Arial", 10, "bold"))
btn_convert.pack(pady=20)

lbl_result = tk.Label(root, text="Mã nhị phân: ", font=("Courier", 14, "bold"), fg="#333")
lbl_result.pack(pady=10)

root.mainloop()
