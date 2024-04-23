from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
pdf.set_auto_page_break(auto=False, margin=0)
# necessary to push footer downwards without needing
# to create multiple empty cells
# setting auto to False prevents outpouring of content to subsequent pages if the position is beyond the boundary of the page it's meant to be in

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    # Header
    pdf.add_page()
    pdf.set_font(family='Times', style='BI', size=24)
    pdf.set_text_color(100, 100, 100)  # RGB
    pdf.cell(w=0, h=12, txt=row["Topic"],
             align='L', ln=1)  # ln=1 means enable newline
    # pdf.cell(w=17, h=12, txt=row["Topic"],
    #          align='R', ln=1, border=1)

    # generates lines
    for index, y_coordinate in enumerate(range(20, 298, 10)):
        pdf.line(x1=10, y1=y_coordinate, x2=200, y2=y_coordinate)

    # footer
    pdf.ln(265)  # in mm(the length of A4 paper is 297mm)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row["Topic"],
             align='R')

    # spawns as many pages as stipulated in topics.csv
    for page in range(row['Pages'] - 1):
        pdf.add_page()

        # generates lines
        for index, y_coordinate in enumerate(range(20, 298, 10)):
            pdf.line(x1=10, y1=y_coordinate, x2=200, y2=y_coordinate)

        # footer
        pdf.ln(277)  # offset in mm(the length of A4 paper is 297mm)
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row["Topic"],
                 align='R')

# pdf.set_font(family='Times', style='U', size=10
# pdf.cell(w=0, h=12, txt='Gutten tag!', align='L', ln=1, border=1)

pdf.output('output.pdf')
