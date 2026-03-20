import tkinter as tk
from tkinter import ttk
import calendar

names = ["A", "B", "C", "D", "E"]

def tao_lich():
    year = int(entry_year.get())
    start_day = int(entry_start.get())
    month = int(entry_month.get())

    cal = calendar.monthcalendar(year, month)
    result = "Sun Mon Tue Wed Thu Fri Sat\n"
    duty_index = 0

    # Tính offset từ ngày đầu năm
    day_of_year = sum(calendar.monthrange(year, m)[1] for m in range(1, month)) + 1
    duty_index = (day_of_year - 1) % len(names)

    for week in cal:
        for i, day in enumerate(week):
            if day == 0:
                result += "    "
            elif i == 0:  # Chủ nhật
                result += f"{day:2}   "
            else:
                result += f"{day:2}[{names[duty_index]}] "
                duty_index = (duty_index + 1) % len(names)
        result += "\n"

    text_output.delete("1.0", tk.END)
    text_output.insert(tk.END, result)

root = tk.Tk()
root.title("Lịch trực")

tk.Label(root, text="Năm:").grid(row=0, column=0)
entry_year = tk.Entry(root)
entry_year.grid(row=0, column=1)

tk.Label(root, text="Thứ ngày đầu năm (0=CN):").grid(row=1, column=0)
entry_start = tk.Entry(root)
entry_start.grid(row=1, column=1)

tk.Label(root, text="Tháng:").grid(row=2, column=0)
entry_month = tk.Entry(root)
entry_month.grid(row=2, column=1)

btn = tk.Button(root, text="Tạo lịch trực", command=tao_lich)
btn.grid(row=3, column=0, columnspan=2)

text_output = tk.Text(root, width=50, height=15)
text_output.grid(row=4, column=0, columnspan=2)

root.mainloop()
