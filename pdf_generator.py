# Copyright (c) 2025, Thiago de Melo <tmelo.mat@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
#
# Function to export the grid as a PDF Sudoku

import random


def export_pdf_singlepage(grid, output_file='sudoku-original.pdf'):
    try:
        from reportlab.pdfgen import canvas
        from reportlab.lib.units import cm

        # Dimensions
        page_width, page_height = 9 * cm, 9 * cm
        cell_width = page_width / 9
        cell_height = page_height / 9

        # Create Canvas
        pdf = canvas.Canvas(output_file)
        pdf.setPageSize((page_width, page_height))
        pdf.setTitle('Sudoku')
        pdf.setAuthor('Thiago de Melo')
        pdf.setSubject('A Simple Sudoku Game')
        pdf.setKeywords('github.com/tmelorc/sudoku')

        # Draw lines
        for i in range(10):
            line_width = 1
            if i % 3 == 0:
                line_width = 3
            pdf.setLineWidth(line_width)
            pdf.line(0, i * cell_height, page_width, i * cell_height)
            pdf.line(i * cell_width, 0, i * cell_width, page_height)

        # Write numbers
        for row in range(9):
            for col in range(9):
                x = col*cell_width + cell_width/2 - line_width
                y = (8 - row)*cell_height + cell_height/2 - line_width
                if grid[row][col] != 0:
                    pdf.drawString(x, y, str(grid[row][col]))

        pdf.save()

    except ImportError:
        print('Export PDF version not allowed. Install reportlab first.')


def export_pdf_multipage(num_pages, per_pages, clues=17, output_file='sudoku.pdf'):
    try:
        from reportlab.pdfgen import canvas
        from reportlab.lib.units import cm
        from reportlab.pdfbase import pdfmetrics
        from reportlab.pdfbase.ttfonts import TTFont
        from sudoku_generator import sudokuGenerator

        pdfmetrics.registerFont(
            TTFont('NumbersFont',
                   '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf')
        )

        # Dimensions
        page_width, page_height = 21 * cm, 29.7 * cm
        grid_width, grid_height = 9 * cm, 9 * cm
        cell_width = 1 * cm
        cell_height = 1 * cm

        # Draw lines
        def draw_lines(offset=(0, 0)):
            global line_width
            for i in range(10):
                line_width = 1
                if i % 3 == 0:
                    line_width = 3
                pdf.setLineWidth(line_width)
                pdf.setLineCap(2)
                pdf.line(
                    offset[0] + 0, offset[1] + i * cell_height,
                    offset[0] + grid_width, offset[1] + i * cell_height
                )
                pdf.line(
                    offset[0] + i * cell_width, offset[1],
                    offset[0] + i * cell_width, offset[1] + grid_height
                )

        # Write numbers
        def write_numbers(grid, offset=(0, 0)):
            pdf.setFont("NumbersFont", 14)
            for row in range(9):
                for col in range(9):
                    x = col*cell_width + cell_width/2 - line_width
                    y = (8 - row)*cell_height + cell_height/2 - line_width
                    if grid[row][col] != 0:
                        pdf.drawString(
                            offset[0] + x, offset[1] + y, str(grid[row][col])
                        )

        # Create Canvas
        pdf = canvas.Canvas(output_file)
        pdf.setPageSize((page_width, page_height))
        pdf.setTitle('Sudoku')
        pdf.setAuthor('Thiago de Melo')
        pdf.setSubject('A Simple Sudoku Game')
        pdf.setKeywords('github.com/tmelorc/sudoku')

        rows = {1: 1, 2: 2, 4: 2}
        cols = {1: 1, 2: 1, 4: 2}

        for _ in range(num_pages):
            pdf.translate(1*cm, 3*cm)
            for i in range(rows[per_pages]):
                for j in range(cols[per_pages]):
                    clues = random.randint(17, 60)
                    grid = sudokuGenerator(81 - clues)[0]

                    # TODO: use per_pages to adjust offset to always centers the grids
                    draw_lines(offset=(i*10*cm, j*12*cm))
                    write_numbers(grid, offset=(i*10*cm, j*12*cm))
            pdf.showPage()

        pdf.save()

    except ImportError:
        print('Export PDF version not allowed. Install reportlab first.')


if __name__ == '__main__':
    export_pdf_multipage(2, 4)
