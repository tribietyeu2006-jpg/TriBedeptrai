import tkinter as tk
from tkinter import messagebox

can = ["Giáp","Ất","Bính","Đinh","Mậu","Kỷ","Canh","Tân","Nhâm","Quý"]
chi = ["Tý","Sửu","Dần","Mão","Thìn","Tỵ","Ngọ","Mùi","Thân","Dậu","Tuất","Hợi"]

def get_can_chi(year):
    c = can[(year + 6) % 10]
    ch = chi[(year + 8) % 12]
    return f"{c} {ch}"

def calculate():
    try:
        n = int(entry.get())
        name1 = get_can_chi(n)
        name2 = get_can_chi(n + 60)

        result.config(
            text=f"{n} - {name1}\n{n+60} - {name2}"
        )
    except:
        messagebox.showerror("Lỗi", "Nhập năm hợp lệ!")

# GUI
root = tk.Tk()
root.title("Tính năm Can Chi")
root.geometry("400x200")

tk.Label(root, text="Nhập năm dương lịch:").pack()

entry = tk.Entry(root)
entry.pack()

tk.Button(root, text="Tính", command=calculate).pack()

result = tk.Label(root, text="", fg="blue")
result.pack()

root.mainloop()
\
