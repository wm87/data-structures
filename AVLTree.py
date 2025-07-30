import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# AVL-Baum-Knoten und -Logik (wie vorher definiert)
class Node:
    def __init__(self, key):
        self.key = key
        self.height = 1
        self.left = None
        self.right = None

class AVLTree:
    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, key):
        if not root:
            return root
        elif key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.right = self.delete(root.right, temp.key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1 and self.get_balance(root.left) >= 0:
            return self.right_rotate(root)
        if balance > 1 and self.get_balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)
        if balance < -1 and self.get_balance(root.right) <= 0:
            return self.left_rotate(root)
        if balance < -1 and self.get_balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def search(self, root, key):
        if root is None or root.key == key:
            return root
        if key < root.key:
            return self.search(root.left, key)
        else:
            return self.search(root.right, key)

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def right_rotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def get_min_value_node(self, node):
        while node.left:
            node = node.left
        return node

    # Für Visualisierung
    def find_path(self, root, key):
        path = []
        node = root
        while node:
            path.append(node)
            if key == node.key:
                return path
            elif key < node.key:
                node = node.left
            else:
                node = node.right
        return []

    def draw_tree(self, root, highlight_key=None):
        tree_height = self.get_height(root)
        fig_width = max(12, 2 ** (tree_height - 1))
        fig_height = tree_height * 1.5

        fig, ax = plt.subplots(figsize=(fig_width, fig_height))
        ax.axis("off")

        highlight_nodes = set()
        if highlight_key is not None:
            highlight_nodes = set(self.find_path(root, highlight_key))

        self._draw_node(ax, root, 0, 0, x_offset=fig_width, level=0, highlight_nodes=highlight_nodes)
        return fig

    def _draw_node(self, ax, node, x, y, x_offset, level, highlight_nodes):
        if not node:
            return

        key = node.key
        height = node.height
        balance = self.get_balance(node)
        label = f"{key}\nh={height}, b={balance}"

        is_highlighted = node in highlight_nodes
        node_color = "salmon" if is_highlighted else "lightblue"
        edge_color = "red" if is_highlighted else "black"

        ax.text(x, -y, label, ha="center", va="center",
                bbox=dict(boxstyle="round,pad=0.4", facecolor=node_color, edgecolor=edge_color, linewidth=2))

        gap = x_offset / (2 ** (level + 2))
        y_step = 1.5

        if node.left:
            x_left = x - gap
            y_left = y + y_step
            color = "red" if node.left in highlight_nodes else "gray"
            ax.plot([x, x_left], [-y, -y_left], color=color, linewidth=2 if color == "red" else 1)
            self._draw_node(ax, node.left, x_left, y_left, x_offset, level + 1, highlight_nodes)

        if node.right:
            x_right = x + gap
            y_right = y + y_step
            color = "red" if node.right in highlight_nodes else "gray"
            ax.plot([x, x_right], [-y, -y_right], color=color, linewidth=2 if color == "red" else 1)
            self._draw_node(ax, node.right, x_right, y_right, x_offset, level + 1, highlight_nodes)


# === GUI-Klasse ===
class AVLTreeGUI:
    def __init__(self, root):
        self.tree = AVLTree()
        self.root_node = None

        self.window = root
        self.window.title("AVL Baum GUI")
        self.window.geometry("900x700")

        # Eingabe
        self.entry = tk.Entry(self.window, font=("Arial", 14))
        self.entry.pack(pady=10)

        # Buttons
        frame = tk.Frame(self.window)
        frame.pack()

        self.insert_btn = tk.Button(frame, text="Einfügen", command=self.insert_key, width=12)
        self.insert_btn.grid(row=0, column=0, padx=5, pady=5)

        self.search_btn = tk.Button(frame, text="Suchen", command=self.search_key, width=12)
        self.search_btn.grid(row=0, column=1, padx=5, pady=5)

        self.delete_btn = tk.Button(frame, text="Löschen", command=self.delete_key, width=12)
        self.delete_btn.grid(row=0, column=2, padx=5, pady=5)

        self.draw_btn = tk.Button(frame, text="Baum zeichnen", command=self.draw_tree, width=12)
        self.draw_btn.grid(row=0, column=3, padx=5, pady=5)

        # Statusanzeige
        self.status_label = tk.Label(self.window, text="", font=("Arial", 12))
        self.status_label.pack(pady=10)

        # Matplotlib Figure in Tkinter
        self.fig_canvas = None

    def get_input_key(self):
        val = self.entry.get()
        if not val.isdigit():
            messagebox.showerror("Fehler", "Bitte eine gültige ganze Zahl eingeben!")
            return None
        return int(val)

    def insert_key(self):
        key = self.get_input_key()
        if key is None:
            return
        self.root_node = self.tree.insert(self.root_node, key)
        self.status_label.config(text=f"Knoten {key} eingefügt.")
        self.draw_tree(highlight_key=key)

    def search_key(self):
        key = self.get_input_key()
        if key is None:
            return
        found = self.tree.search(self.root_node, key)
        if found:
            self.status_label.config(text=f"Knoten {key} gefunden.")
        else:
            self.status_label.config(text=f"Knoten {key} nicht gefunden.")
        self.draw_tree(highlight_key=key if found else None)

    def delete_key(self):
        key = self.get_input_key()
        if key is None:
            return
        found = self.tree.search(self.root_node, key)
        if not found:
            self.status_label.config(text=f"Knoten {key} nicht gefunden, kann nicht gelöscht werden.")
            self.draw_tree()
            return
        self.root_node = self.tree.delete(self.root_node, key)
        self.status_label.config(text=f"Knoten {key} gelöscht.")
        self.draw_tree()

    def draw_tree(self, highlight_key=None):
        if self.fig_canvas:
            self.fig_canvas.get_tk_widget().destroy()

        if self.root_node is None:
            self.status_label.config(text="Der Baum ist leer.")
            return

        fig = self.tree.draw_tree(self.root_node, highlight_key=highlight_key)
        self.fig_canvas = FigureCanvasTkAgg(fig, master=self.window)
        self.fig_canvas.draw()
        self.fig_canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    app = AVLTreeGUI(root)
    root.mainloop()
