import tkinter as tk
from tkinter import messagebox

class AVLNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def delete(self, root, key):
        if not root: return root

        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            # Node có 1 con hoặc không có con
            if not root.left: return root.right
            elif not root.right: return root.left
            
            # Node có 2 con: Lấy node nhỏ nhất bên phải (In-order Successor)
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        # Cân bằng lại cây (Trinode Restructuring)
        if balance > 1 and self.get_balance(root.left) >= 0: return self.rotate_right(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.rotate_left(root.left)
            return self.rotate_right(root)
        if balance < -1 and self.get_balance(root.right) <= 0: return self.rotate_left(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.rotate_right(root.right)
            return self.rotate_left(root)
        return root

    def get_min_value_node(self, node):
        if node is None or node.left is None: return node
        return self.get_min_value_node(node.left)

# --- Phần Giao diện hiển thị ---
def draw_tree(canvas, node, x, y, distance):
    if node:
        if node.left:
            canvas.create_line(x, y, x - distance, y + 60, fill="black")
            draw_tree(canvas, node.left, x - distance, y + 60, distance / 1.5)
        if node.right:
            canvas.create_line(x, y, x + distance, y + 60, fill="black")
            draw_tree(canvas, node.right, x + distance, y + 60, distance / 1.5)
        
        canvas.create_oval(x-20, y-20, x+20, y+20, fill="#BBDEFB", outline="#1976D2")
        canvas.create_text(x, y, text=str(node.key), font=("Arial", 10, "bold"))

def perform_delete():
    global tree_root
    try:
        val = int(entry_val.get())
        tree_root = avl.delete(tree_root, val)
        canvas.delete("all")
        draw_tree(canvas, tree_root, 300, 40, 120)
    except:
        messagebox.showerror("Lỗi", "Nhập giá trị số hợp lệ")

# Khởi tạo cây mẫu như trong ảnh
avl = AVLTree()
tree_root = None
for val in [5, 3, 11, 4, 6, 12, 8]:
    # (Để đơn giản, ta dùng hàm insert chuẩn AVL ở đây - lược bỏ phần code insert cho ngắn gọn)
    # Giả định cây đã được dựng sẵn theo cấu trúc bài học
    pass 

# (Lưu ý: Để chạy đúng cấu trúc ảnh, ta cần insert 12, 11, 8, 6, 5, 4, 3 theo thứ tự AVL)
tree_root = AVLNode(11)
tree_root.left = AVLNode(5); tree_root.left.left = AVLNode(3); tree_root.left.right = AVLNode(6)
tree_root.right = AVLNode(12); tree_root.left.right.right = AVLNode(8); tree_root.left.left.right = AVLNode(4)

root = tk.Tk()
root.title("Mô phỏng Xóa Cây AVL - Bài 230")

canvas = tk.Canvas(root, width=600, height=400, bg="white")
canvas.pack(pady=10)
draw_tree(canvas, tree_root, 300, 40, 120)

frame_ctrl = tk.Frame(root)
frame_ctrl.pack(pady=10)
tk.Label(frame_ctrl, text="Nhập khóa cần xóa:").pack(side=tk.LEFT)
entry_val = tk.Entry(frame_ctrl, width=10)
entry_val.pack(side=tk.LEFT, padx=5)
entry_val.insert(0, "5")
tk.Button(frame_ctrl, text="Xóa Node", command=perform_delete, bg="#f44336", fg="white").pack(side=tk.LEFT)

root.mainloop()
