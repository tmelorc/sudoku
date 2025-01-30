import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
# from tkinter.ttk import Combobox
from pdf_generator import *
from sudokugenerator import sudokuGenerator


class DialogWindow(tk.Toplevel):
    def __init__(self, parent, export_function):
        super().__init__(parent)
        self.title("Create Sudoku PDF")
        self.geometry('400x200')
        self.export_function = export_function

        # main_font = ('Helvetica', 14)
        # self.option_add("*Font", main_font)

        self.selected_option = tk.StringVar(value='single')
        # self.num_pages = tk.StringVar()
        # self.per_pages = tk.IntVar()

        self.create_widgets()

    def create_widgets(self):

        # # Cria um estilo para o LabelFrame
        # style = ttk.Style()
        # style.configure('My.TLabelframe', font=('Helvetica', 16))

        top_frame = ttk.LabelFrame(self, text="PDF Options")
        top_frame.pack(padx=10, pady=10)
        top_frame.configure(borderwidth=2)

        # Radio buttons
        single_radio = ttk.Radiobutton(
            top_frame, text='Single-page', variable=self.selected_option, value='single')
        multipage_radio = ttk.Radiobutton(
            top_frame, text='Multi-page', variable=self.selected_option, value='multi')

        single_radio.grid(row=0, column=0, pady=10, padx=10, sticky='e')
        multipage_radio.grid(row=0, column=1, pady=10, padx=10, sticky='w')

        label_num_pages = ttk.Label(top_frame, text="Number of pages:")
        label_num_pages.grid(row=1, column=0, pady=10, padx=10, sticky='e')

        self.num_pages_entry = ttk.Entry(top_frame, width=4)
        self.num_pages_entry.grid(
            row=1, column=1, pady=10, padx=10, sticky='w')
        self.num_pages_entry.insert(0, '2')

        label_per_pages = ttk.Label(top_frame, text="Sudoku puzzles per page:")
        label_per_pages.grid(row=2, column=0, pady=10, padx=10, sticky='e')

        self.per_pages_combo = ttk.Combobox(
            top_frame, values=['1', '2', '4'], width=2)
        self.per_pages_combo.grid(
            row=2, column=1, pady=10, padx=10, sticky='w')
        self.per_pages_combo.current(2)

        export_button = ttk.Button(
            self, text="Create PDF", command=self.export_and_close)
        export_button.pack(pady=(0, 10))

    def export_and_close(self):
        selected_option = self.selected_option.get()
        num_pages = int(self.num_pages_entry.get())
        per_pages = int(self.per_pages_combo.get())
        print(f"Tipo:: {selected_option}")
        print(f"Páginas: {num_pages}")
        print(f"Por páginas: {per_pages}")
        self.export_function(selected_option, num_pages, per_pages)
        # self.destroy()


if __name__ == '__main__':
    root = tk.Tk()

    def foo(a, b, c):
        print(a, b, c)

    diag = DialogWindow(root, foo)

    diag.mainloop()
