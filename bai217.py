import tkinter as tk
from tkinter import messagebox

# Định nghĩa cấu trúc 1 Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.append_node = last.next = new_node

    def swap_nodes_with_value_k(self, k):
        # Tạo một node giả (dummy) đứng trước head để xử lý trường hợp k nằm ở đầu
        dummy = Node(0)
        dummy.next = self.head
        prev = dummy
        current = self.head

        while current and current.next:
            if current.data == k:
                # Thực hiện hoán đổi: prev -> current -> next_node -> ...
                next_node = current.next
                
                # Cập nhật liên kết
                current.next = next_node.next
                next_node.next = current
                prev.next = next_node
                
                # Sau khi swap, 'current' giờ đứng sau 'next_node'
                # Chuẩn bị cho lần lặp tiếp theo
                prev = next_node
            else:
                prev = current
                current = current.next
        
        self.head = dummy.next

    def to_string(self):
        nodes = []
        curr = self.head
        while curr:
            nodes.append(f"[{curr.data}]")
            curr = curr.next
        return "".join(nodes)

# --- Xử lý giao diện ---
def process_swap():
    try:
        data_input = entry_list.get().split()
        k = int(entry_k.get())
        
        llist = LinkedList()
        for x in data_input:
            if x == '0': break # Dừng nếu gặp 0 như đề bài
            llist.append(int(x))
        
        # Lưu trạng thái trước khi swap
        lbl_old.config(text=f"List gốc: {llist.to_string()}")
        
        # Thực hiện swap
        llist.swap_nodes_with_value_k(k)
        
        # Hiển thị kết quả mới
        lbl_new.config(text=f"List mới: {llist.to_string()}")
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên!")

# Tạo GUI
root = tk.Tk()
root.title("Hoán đổi Node - Bài 217")
root.geometry("500x350")

tk.Label(root, text="Nhập dãy số (cách nhau bởi dấu cách, kết thúc bằng 0):").pack(pady=5)
entry_list = tk.Entry(root, width=50)
entry_list.pack(pady=5)
entry_list.insert(0, "1 2 3 1 2 3 1 0")

tk.Label(root, text="Nhập giá trị k cần đảo:").pack(pady=5)
entry_k = tk.Entry(root, width=10)
entry_k.pack(pady=5)
entry_k.insert(0, "1")

btn_run = tk.Button(root, text="Thực hiện Hoán đổi Node", command=process_swap, 
                     bg="#2196F3", fg="white", font=("Arial", 10, "bold"))
btn_run.pack(pady=20)

lbl_old = tk.Label(root, text="List gốc: ", fg="grey")
lbl_old.pack()
lbl_new = tk.Label(root, text="List mới: ", font=("Arial", 11, "bold"), fg="green")
lbl_new.pack(pady=10)

root.mainloop()
