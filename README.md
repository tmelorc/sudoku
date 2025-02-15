# A Simple Sudoku Game (`sudokuGUI.py`)

## How to use

Download the Python files (`sudokuGUI.py`, `sudoku_generator.py`, `pdf_generator.py` and `pdf_dialog_window.py`).

Give execution permission to `sudokuGUI.py` with `chmod +x sudokuGUI.py` and execute it as `./sudokuGUI.py`.

Alternatively, you can run `python3 sudokuGUI.py`.

### Linux binary

You can download the binary file for Linux from Google Drive here: (https://drive.google.com/file/d/1F7RXNPbONjZmLt7uXGSoA55cwl8vrzuE/view?usp=sharing)

## The main window

![Main Window Screenshot](screenshot.png)

### Clues

Select the number of initial clues using the slider. The difficulty level changes according to the number of clues.

### New Game

After choosing the number of clues, click the `New Game` button to start the game. The clock will start and you can play by inserting numbers in the empty cells.

### Check Game

Use this button to verify your game. A feedback message will appear.

### Score

When you finish filling the empty cells and press the `Check Game` button, if your solution is correct, you will get one point, as shown in the bottom right corner.

### PDF

If the necessary Python module is installed, you can generate PDF files with the Sudoku grid. Press the `PDF` button and choose the PDF options as you wish. After, look for pdf files in the current directory.

![PDF Version](screenshot-pdf.png)
