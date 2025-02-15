import tkinter as tk
import tkinter.ttk as ttk
from tkinter import *
from pdf_generator import *


class DialogWindow(tk.Toplevel):
    def __init__(self, parent, export_function):
        super().__init__(parent)
        self.title("Create Sudoku PDF")
        self.geometry('400x250')
        self.export_function = export_function

        self.selected_option = tk.StringVar(value='single')
        self.clues_range = tk.StringVar(value='40-65')
        self.clues_min = 17
        self.clues_max = 80

        self.create_widgets()

    def create_widgets(self):
        # Top Frame
        top_frame = ttk.LabelFrame(self, text="PDF Options")
        top_frame.pack(padx=10, pady=10)
        top_frame.configure(borderwidth=2)

        # Radio Buttons
        single_radio = ttk.Radiobutton(
            top_frame, text='Single-page', variable=self.selected_option, value='single')
        multipage_radio = ttk.Radiobutton(
            top_frame, text='Multi-page', variable=self.selected_option, value='multi')

        single_radio.grid(row=0, column=0, pady=10, padx=10, sticky='e')
        multipage_radio.grid(row=0, column=1, pady=10, padx=10, sticky='w')

        # Number of pages
        label_num_pages = ttk.Label(top_frame, text="Number of pages:")
        label_num_pages.grid(row=1, column=0, pady=10, padx=10, sticky='e')

        self.num_pages_entry = ttk.Entry(top_frame, width=4)
        self.num_pages_entry.grid(
            row=1, column=1, pady=10, padx=10, sticky='w')
        self.num_pages_entry.insert(0, '2')

        # Puzzles per pages
        label_per_pages = ttk.Label(top_frame, text="Sudoku puzzles per page:")
        label_per_pages.grid(row=2, column=0, pady=10, padx=10, sticky='e')

        self.per_pages_combo = ttk.Combobox(
            top_frame, values=['1', '2', '4'], width=2)
        self.per_pages_combo.grid(
            row=2, column=1, pady=10, padx=10, sticky='w')
        self.per_pages_combo.current(2)

        # Clues
        label_clues_range = ttk.Label(top_frame, text="Clues range:")
        label_clues_range.grid(row=3, column=0, pady=10, padx=10, sticky='e')

        self.clues_range_entry = ttk.Entry(top_frame, width=6)
        self.clues_range_entry.grid(
            row=3, column=1, pady=10, padx=10, sticky='w')
        self.clues_range_entry.insert(0, self.clues_range.get())

        export_button = ttk.Button(
            self, text="Create PDF", command=self.export_and_close)
        export_button.pack(pady=(0, 10))

    def export_and_close(self):
        selected_option = self.selected_option.get()
        num_pages = int(self.num_pages_entry.get())
        per_pages = int(self.per_pages_combo.get())
        clues_range_min = int(self.clues_range_entry.get().split('-')[0])
        clues_range_max = int(self.clues_range_entry.get().split('-')[1])
        # print(clues_range_min, clues_range_max)
        self.export_function(selected_option, num_pages,
                             per_pages, clues_range_min, clues_range_max)
        self.destroy()


if __name__ == '__main__':
    root = DialogWindow(None, None)
    root.mainloop()
