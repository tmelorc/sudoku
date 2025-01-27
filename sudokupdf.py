# Function to export the grid as a PDF Sudoku

def save_pdf(grid, output_file='sudoku-original.pdf'):
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


if __name__ == '__main__':
    None
