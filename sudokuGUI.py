#!/usr/bin/python3
# https://www.technologyreview.com/2012/01/06/188520/mathematicians-solve-minimum-sudoku-problem/


import tkinter as tk
from tkinter import messagebox
from sudokugenerator import sudokuGenerator
try:
    from sudokupdf import save_pdf
    export_pdf = True
except ImportError:
    print('Export PDF not allowed. Install reportlab first.')
    export_pdf = False


class SudokuGame:
    def __init__(self, master):
        # print('Iniciando a classe SudokuGame')
        self.master = master
        self.score = 0

        self.board = [['?' for _ in range(9)] for _ in range(9)]
        self.solution = self.board

        self.create_widgets()
        clock()

    def create_widgets(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack(side='top', pady=15)

        # Create Sudoku Grid
        self.entries = [[None]*9 for _ in range(9)]

        for i in range(9):
            for j in range(9):
                self.entries[i][j] = tk.Entry(self.frame,
                                              width=3,
                                              font=('Helvetica', 30),
                                              justify='center',
                                              bg='white', fg='black',
                                              bd=5, relief='groove',
                                              highlightcolor='#DB0D2B',
                                              highlightthickness=2,
                                              #   highlightbackground="lightblue"
                                              )
                self.entries[i][j].grid(row=i, column=j)

                self.entries[i][j].bind(
                    '<Enter>', lambda x, box=self.entries[i][j]: box.config(
                        bg='light sky blue'))
                self.entries[i][j].bind(
                    '<Leave>', lambda x, box=self.entries[i][j]: box.config(
                        bg='white'))

                # insert gap between 3x3 blocks
                if j == 2 or j == 5:
                    self.entries[i][j].grid(padx=(0, 8), sticky='w')
                if i == 2 or i == 5:
                    self.entries[i][j].grid(pady=(0, 8), sticky='n')

                # insert sudoku initial hints
                if self.board[i][j] != 0:
                    self.entries[i][j].insert(0, str(self.board[i][j]))
                    self.entries[i][j].config(
                        state=tk.DISABLED,
                        disabledforeground='black'
                    )

    def desativar_entries(self, i, j):
        self.entries[i][j].config(
            state=tk.DISABLED,
            disabledforeground='#666666',
            disabledbackground='#666666'
        )
        if i < 8 or (i == 8 and j < 8):
            next_i = i if j < 8 else i+1
            next_j = (j+1) % 9
            root.after(10, self.desativar_entries, next_i, next_j)


def check_game():
    global clock_on
    for i in range(9):
        for j in range(9):
            value = app.entries[i][j].get()
            if len(value) != 1 or not value.isdigit():
                messagebox.showwarning(
                    'Not yet!',
                    'Fill the entire grid with numbers from 1 to 9.'
                )
                return False
            else:
                app.board[i][j] = int(value)

    if app.board == app.solution:
        clock_on = False
        app.score += 1
        SCORE.set(f'Score: {app.score}')
        app.desativar_entries(0, 0)
        messagebox.showinfo(
            'Congratulations!',
            f'You have completed the Sudoku puzzle in \
            {seconds_to_time(game_time)}!'
        )
    else:
        messagebox.showwarning(
            'Not yet!', 'Verify the numbers.'
        )


def new_game():
    app.frame.destroy()

    global game_time, clock_on
    game_time = 0
    clock_on = True

    NUMBER_INITIAL_VALUES = scale_hints.get()
    NUMBER_VALUES = 81 - NUMBER_INITIAL_VALUES

    if NUMBER_INITIAL_VALUES < 17 or NUMBER_INITIAL_VALUES > 81:
        messagebox.showwarning(
            'Warning', 'Hints should be between 17 and 81.'
        )
        return None

    app.board, app.solution = sudokuGenerator(NUMBER_VALUES)
    app.create_widgets()
    app.frame.focus_set()


def seconds_to_time(seconds):
    hours, rest = divmod(seconds, 3600)
    minutes, seconds = divmod(rest, 60)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


def clock():
    global game_time, clock_on
    if clock_on:
        game_time += 1
        label_time.config(text="Time: " + seconds_to_time(game_time))
    label_time.after(1000, clock)


def save_all_pdf():
    if export_pdf:
        save_pdf(app.board, output_file='sudoku-original.pdf')
        save_pdf(app.solution, output_file='sudoku-solution.pdf')
    else:
        print('Export PDF version not allowed. Install reportlab first.')
        messagebox.showwarning("Warning!",
                               "PDF version not allowed. \
                               Install reportlab first.")


def update_level(level):
    label_hints.config(text=choose_level(int(level)))


def choose_level(x):
    if x < 40:
        return f'Hints:\nHard'
    if x < 70:
        return f'Hints:\nMedium'
    return f'Hints:\nEasy'


if __name__ == '__main__':
    # print(tk.TclVersion)
    # print(tk.TkVersion)

    game_time = 0
    clock_on = False

    # Root Window
    root = tk.Tk()
    root.title('Sudoku')
    root.geometry('940x670')
    root.minsize(940, 670)

    # Frames (on Root Window)
    top_frame = tk.Frame(root, bg='#666666')
    center_frame = tk.Frame(root, bg='#ffffff')
    bottom_frame = tk.Frame(root, bg='#666666')

    # Packing Frames on Root Window
    top_frame.pack(side='top', fill=tk.X, expand=False)
    center_frame.pack(side='top', fill=tk.BOTH, expand=True)
    bottom_frame.pack(side='bottom', fill=tk.X, expand=False)

    # Integer values used to show/hide initial numbers
    NUMBER_INITIAL_VALUES = tk.IntVar()
    NUMBER_INITIAL_VALUES.set(17)
    NUMBER_VALUES = 81 - NUMBER_INITIAL_VALUES.get()

    # Score variable
    SCORE = tk.StringVar()
    SCORE.set(f'Score: {0}')

    # Top Frame items
    #
    # Label (hints)
    label_hints = tk.Label(top_frame,
                           width=7,
                           text=f"{choose_level(NUMBER_INITIAL_VALUES.get())}",
                           font=('Helvetica', 16),
                           bg='#666666', fg='#ffffff'
                           )

    # Scale (hints)
    scale_hints = tk.Scale(top_frame,
                           from_=17, to=80,
                           font=('Helvetica', 10),
                           fg='white', bg='#666666',
                           length=200,
                           orient=tk.HORIZONTAL,
                           variable=NUMBER_INITIAL_VALUES,
                           command=update_level
                           )

    # Label (game time)
    label_time = tk.Label(top_frame,
                          text='Time:',
                          font=('Helvetica', 16),
                          bg='#666666', fg='#ffffff'
                          )

    # Buttons (check/new/quit)
    check_game_button = tk.Button(top_frame,
                                  text='Check Game',
                                  font=('Helvetica', 16),
                                  command=check_game,
                                  bg='#666666', fg='#ffffff',
                                  activebackground='RoyalBlue3',
                                  activeforeground='black'
                                  )

    new_game_button = tk.Button(top_frame,
                                text='New Game',
                                font=('Helvetica', 16),
                                command=new_game,
                                bg='#666666', fg='#ffffff',
                                activebackground='RoyalBlue3',
                                activeforeground='black'
                                )

    pdf_button = tk.Button(top_frame,
                           text='PDF',
                           font=('Helvetica', 16),
                           command=save_all_pdf,
                           bg='#666666', fg='#ffffff',
                           activebackground='RoyalBlue3',
                           activeforeground='black'
                           )

    quit_button = tk.Button(top_frame,
                            text='Quit',
                            font=('Helvetica', 16),
                            command=root.quit,
                            bg='#666666', fg='gold',
                            activebackground='RoyalBlue3',
                            activeforeground='black'
                            )

    # Packing Top Frame items
    #
    # from left to right
    label_hints.pack(side='left', pady=5, padx=5)
    scale_hints.pack(side='left', padx=5, pady=5)
    label_time.pack(side='left', pady=5, padx=5)
    #
    # from right to left
    quit_button.pack(side='right', pady=5, padx=5)
    pdf_button.pack(side='right', pady=5, padx=5)
    new_game_button.pack(side='right', pady=5, padx=5)
    check_game_button.pack(side='right', pady=5, padx=5)

    # Main app which created de Sudoku grid
    app = SudokuGame(center_frame)

    # Bottom Frame Label
    label_footer = tk.Label(
        bottom_frame,
        text='Created by Thiago de Melo',
        font=('Helvetica', 12),
        fg='white', bg='#666666'
    )
    label_footer.pack(side='left', pady=5, padx=5)

    score_footer = tk.Label(
        bottom_frame,
        textvariable=SCORE,
        font=('Helvetica', 12),
        fg='white', bg='#666666'
    )
    score_footer.pack(side='right', pady=5, padx=5)

    # Binds
    check_game_button.bind('<Return>', lambda x: check_game())
    new_game_button.bind('<Return>', lambda x: new_game())
    quit_button.bind('<Return>', lambda x: root.quit())

    root.mainloop()
