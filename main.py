from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()

    pdf.set_font(family='Times', style='BI', size=24)
    pdf.set_text_color(100, 100, 100)  # RGB
    pdf.cell(w=17, h=12, txt=row["Topic"],
             align='L', ln=1)
    pdf.line(x1=10, y1=21, x2=200, y2=21)

# pdf.set_font(family='Times', style='U', size=10
# pdf.cell(w=0, h=12, txt='Gutten tag!', align='L', ln=1, border=1)

pdf.output('output.pdf')
