import tkinter as tk
from tkinter import messagebox, simpledialog

import sympy as sp


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
        # self.result_value = "Empty"

        # Внешний вид
        self.window.title("Matrix Calculator")
        self.window.geometry(self.window_width + "x" + self.window_height)
        icon = tk.PhotoImage(master=window, file="UI/Matrix.png")
        window.iconphoto(False, icon)
        window.config(bg=self.total_background_color)
        self.window = window
        self.window.title("Matrix Calculator")

        self.action_var = tk.StringVar(value="determinant")
        self.size_var = tk.IntVar(value=2)

        # Выбор действия
        tk.Label(self.window, text="Выберите действие:", pady=4, bg=self.total_background_color,
                 font=(self.total_font_name, self.total_big_font_size)).pack()
        action_frame = tk.Frame(self.window, bg=self.total_background_color)
        tk.Radiobutton(action_frame, text="Найти определитель", padx=2, pady=4, bg=self.total_background_color,
                       font=(self.total_font_name, self.total_small_font_size), variable=self.action_var,
                       value="determinant" """, command=self.update_ui""").grid(row=0, column=0, stick="ew")
        tk.Radiobutton(action_frame, text="Найти обратную", padx=2, pady=4, bg=self.total_background_color,
                       font=(self.total_font_name, self.total_small_font_size), variable=self.action_var,
                       value="inverse" """, command=self.update_ui""").grid(row=0, column=1, stick="ew")
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
                       value="nxn",
                       font=(self.total_font_name, self.total_small_font_size),
                       command=self.get_matrix_size).grid(row=0, column=2, stick="ew")
        size_frame.pack()

        self.matrix_frame = tk.Frame(self.window)
        self.matrix_frame.pack()

        self.calculate_button = tk.Button(self.window, text="Вычислить", pady=4, bg=self.total_background_color,
                                          font=(self.total_font_name, self.total_middle_font_size),
                                          command=self.calculate)
        self.calculate_button.pack()

        self.latex_button = tk.Button(self.window, text="Предпросмотр Latex", pady=4, bg=self.total_background_color,
                                      font=(self.total_font_name, self.total_middle_font_size),
                                      command=self.preview_latex)
        self.latex_button.pack()

        self.result_text = tk.Text(self.window, padx=4, pady=4, height=15, width=60)
        self.result_text.pack()

        self.copy_button = tk.Button(self.window, text="Копировать", pady=4, bg=self.total_background_color,
                                     font=(self.total_font_name, self.total_middle_font_size), command=self.copy_result)
        self.copy_button.pack()

        self.update_ui()

    def get_matrix_size(self):
        """Функция для получения размера матрицы от пользователя."""
        size = simpledialog.askinteger("Введите размер матрицы n от 2 до 25", "Введите размер n x n:")
        if size is not None and 2 <= size <= 25:
            self.size_var.set(size)
            self.update_ui()
        elif size < 2 or size > 25:
            messagebox.showerror("Ошибка", "Неверный размер матрицы")

    def update_ui(self):
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

    def calculate(self):
        matrix_size = self.size_var.get()
        matrix_data = []

        for i in range(matrix_size):
            row_data = []
            for j in range(matrix_size):
                value = self.matrix[i][j].get()
                row_data.append(float(value) if value else 0)
            matrix_data.append(row_data)

        if self.action_var.get() == "determinant":
            sympy_matrix = sp.Matrix(matrix_data)
            determinant = sympy_matrix.det()
            # self.result_value = determinant.evalf()
            self.latex_code = sp.latex(determinant)
            self.result_text.delete(1.0, tk.END)
            self.result_text.insert(tk.END, f"Определитель: {determinant:.2f}\n\nLatex код:\n{self.latex_code}")
        else:
            try:
                inv_matrix = sp.Matrix(matrix_data).inv()
                # self.result_value = inv_matrix.tolist()
                self.latex_code = sp.latex(inv_matrix)
                self.result_text.delete(1.0, tk.END)
                self.result_text.insert(tk.END,
                                        f"Обратная матрица:\n{inv_matrix.tolist()}\n\nLatex код:\n{self.latex_code}")
            except ValueError:
                messagebox.showerror("Ошибка", "Матрица вырождена, обратная матрица не существует.")

    def preview_latex(self):
        self.result_text.delete(1.0, tk.END)
        self.result_text.insert(tk.END, f"Latex код:\n{self.latex_code}")

    def copy_result(self):
        self.window.clipboard_clear()
        self.window.clipboard_append(self.result_text.get(1.0, tk.END))
        # возможно имело в виду это:
        # self.window.clipboard_append(self.result_value)


if __name__ == "__main__":
    window = tk.Tk()
    app = MatrixCalculator(window)
    window.mainloop()
