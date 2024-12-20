import tkinter as tk
from tkinter import messagebox, simpledialog
import numpy as np
import sympy as sp
import subprocess


class MatrixCalculator:
    def __init__(self, window):
        self.window_width = "1200"
        self.window_height = "800"
        self.total_background_color = "#ffeed3"
        self.button_background_color = "#ffebbe"
        self.total_font_name = "DejaVu Sans Condensed"
        self.total_big_font_size = 24
        self.total_middle_font_size = 20
        self.total_small_font_size = 16
        self.window = window

        self.action_var = tk.StringVar(value="determinant")
        self.size_var = tk.IntVar(value=2)
        self.size_type = tk.StringVar(value="2x2")

        self.matrix = []
        self.latex_code = "Empty"

        # Внешний вид
        self.window.title("Matrix Calculator")
        self.window.geometry(self.window_width + "x" + self.window_height)
        icon = tk.PhotoImage(master=window, file="Matrix.png")
        window.iconphoto(False, icon)
        window.config(bg=self.total_background_color)

        # Выбор действия
        tk.Label(self.window, text="Выберите действие:", pady=4, bg=self.total_background_color,
                 font=(self.total_font_name, self.total_big_font_size)).pack()
        action_frame = tk.Frame(self.window, bg=self.total_background_color)
        tk.Radiobutton(action_frame, text="Найти определитель", padx=2, pady=4, bg=self.total_background_color,
                       font=(self.total_font_name, self.total_small_font_size), variable=self.action_var,
                       value="determinant").grid(row=0, column=0, stick="ew")
        tk.Radiobutton(action_frame, text="Найти обратную", padx=2, pady=4, bg=self.total_background_color,
                       font=(self.total_font_name, self.total_small_font_size), variable=self.action_var,
                       value="inverse").grid(row=0, column=1, stick="ew")
        action_frame.pack()

        # Выбор порядка матрицы
        tk.Label(self.window, text="Выберите порядок матрицы:", pady=2, bg=self.total_background_color,
                 font=(self.total_font_name, self.total_big_font_size)).pack()
        size_frame = tk.Frame(self.window, bg=self.total_background_color)
        tk.Radiobutton(size_frame, text="2x2", padx=2, pady=2, bg=self.total_background_color,
                       font=(self.total_font_name, self.total_small_font_size), variable=self.size_type, value="2x2",
                       command=self.update_ui).grid(row=0, column=0, stick="ew")
        tk.Radiobutton(size_frame, text="3x3", padx=2, pady=2, bg=self.total_background_color,
                       font=(self.total_font_name, self.total_small_font_size), variable=self.size_type, value="3x3",
                       command=self.update_ui).grid(row=0, column=1, stick="ew")
        tk.Radiobutton(size_frame, text="nxn", padx=2, pady=2, bg=self.total_background_color, variable=self.size_type,
                       value="nxn", font=(self.total_font_name, self.total_small_font_size),
                       command=self.get_matrix_size).grid(row=0, column=2, stick="ew")
        size_frame.pack()

        self.matrix_frame = tk.Frame(self.window)
        self.matrix_frame.pack()

        self.calculate_button = tk.Button(self.window, text="Вычислить", pady=4, bg=self.total_background_color,
                                          font=(self.total_font_name, self.total_middle_font_size),
                                          command=self.run_script_by_action)
        self.calculate_button.pack()

        self.result_text = tk.Text(self.window, padx=4, pady=4, height=15, width=60)
        self.result_text.pack()

        self.update_ui()

    def get_matrix_size(self):
        size = simpledialog.askinteger("Ввод размера матрицы.", "Введите размер матрицы n от 2 до 25:")
        if size is not None and 2 <= size <= 25:
            self.size_var.set(size)
            self.update_ui()
        elif size < 2 or size > 25:
            messagebox.showerror("Ошибка", "Неверный размер матрицы")

    def update_ui(self):
        if self.size_type.get() == "2x2":
            self.size_var.set(2)
        if self.size_type.get() == "3x3":
            self.size_var.set(3)
        for widget in self.matrix_frame.winfo_children():
            widget.destroy()

        self.matrix = []
        matrix_size = self.size_var.get()

        for i in range(matrix_size):
            row = []
            for j in range(matrix_size):
                entry = tk.Entry(self.matrix_frame, width=8)
                entry.grid(row=i, column=j)
                row.append(entry)
            self.matrix.append(row)

    def save_matrix_to_file(self):
        matrix_size = self.size_var.get()
        with open("input.txt", "w") as file:
            file.write(str(matrix_size) + ' ' + str(matrix_size) + '\n')
            for i in range(matrix_size):
                row = []
                for j in range(matrix_size):
                    value = self.matrix[i][j].get()
                    row.append(value if value else "0")
                file.write(" ".join(row) + "\n")

    def load_result_from_file(self):
        try:
            with open("output.txt", "r") as file:
                result = file.read()
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Результат:\n{result}")
        except FileNotFoundError:
            messagebox.showerror("Ошибка", "Файл output.txt не найден.")

    def run_script_by_action(self):
        self.save_matrix_to_file()
        if self.action_var.get() == "determinant":
            script_name = "main_det.py"
        else:
            script_name = "main_inv.py"

        try:
            subprocess.run(["python", script_name], check=True)
            self.load_result_from_file()
        except subprocess.CalledProcessError:
            messagebox.showerror("Ошибка", f"{script_name} завершился с ошибкой.")


if __name__ == "__main__":
    window = tk.Tk()
    app = MatrixCalculator(window)
    window.mainloop()
