from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()
    pdf.set_font("Arial", size=16, style='B')
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=24, txt=row["Topic"], ln=1, align='L')
    pdf.line(10, 28, 200, 28)


pdf.output("output.pdf")