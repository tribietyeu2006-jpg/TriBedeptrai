import tkinter as tk
from tkinter import filedialog, messagebox
import os

def split_file():
    file_path = entry_file.get()
    try:
        # Chuyển KB sang Byte (1 KB = 1024 Bytes)
        max_kb = int(entry_size.get())
        max_bytes = max_kb * 1024
        
        if not os.path.exists(file_path):
            messagebox.showerror("Lỗi", "Tập tin không tồn tại!")
            return

        file_size = os.path.getsize(file_path)
        base_name = os.path.basename(file_path)
        
        with open(file_path, 'rb') as f:
            part_num = 0
            while True:
                chunk = f.read(max_bytes)
                if not chunk:
                    break
                
                # Tạo tên file con theo định dạng: file.000, file.001...
                part_name = f"{file_path}.{part_num:03d}"
                with open(part_name, 'wb') as chunk_file:
                    chunk_file.write(chunk)
                
                log_txt.insert(tk.END, f"Đã tạo: {os.path.basename(part_name)} [{len(chunk)} bytes]\n")
                part_num += 1
        
        log_txt.insert(tk.END, f"--- Hoàn tất! Chia thành {part_num} file(s) ---\n")
        messagebox.showinfo("Thành công", f"Đã chia file thành {part_num} phần!")

    except ValueError:
        messagebox.showerror("Lỗi", "Kích thước n phải là số nguyên (KB)!")

def browse_file():
    filename = filedialog.askopenfilename()
    entry_file.delete(0, tk.END)
    entry_file.insert(0, filename)

# Giao diện đồ họa
root = tk.Tk()
root.title("Công cụ chia nhỏ File - Bài 189")
root.geometry("550x450")

# Chọn file
tk.Label(root, text="Chọn tập tin cần chia:", font=("Arial", 10, "bold")).pack(pady=5)
frame_f = tk.Frame(root)
frame_f.pack()
entry_file = tk.Entry(frame_f, width=50)
entry_file.pack(side=tk.LEFT, padx=5)
tk.Button(frame_f, text="Duyệt...", command=browse_file).pack(side=tk.LEFT)

# Nhập kích thước
tk.Label(root, text="Kích thước tối đa mỗi phần (KB):", font=("Arial", 10)).pack(pady=10)
entry_size = tk.Entry(root, width=20, justify='center')
entry_size.pack()
entry_size.insert(0, "20") # Mặc định 20KB như ví dụ

# Nút thực hiện
btn_split = tk.Button(root, text="BẮT ĐẦU CHIA FILE", command=split_file, 
                      bg="#f44336", fg="white", font=("Arial", 10, "bold"), pady=10)
btn_split.pack(pady=20)

# Khu vực Log
tk.Label(root, text="Nhật ký xử lý:").pack()
log_txt = tk.Text(root, height=10, width=60, bg="#212121", fg="#00FF00")
log_txt.pack(pady=5)

root.mainloop()
