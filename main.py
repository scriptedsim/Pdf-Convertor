from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')
df = pd.read_csv('topics.csv')
pdf.set_auto_page_break(auto=False, margin=0)

for index, row in df.iterrows():

    #Set up the title page
    pdf.add_page()
    pdf.set_font("Arial", size=16, style='B')
    pdf.set_text_color(100, 100, 100)
    pdf.cell(w=0, h=24, txt=row["Topic"], ln=1, align='L')
    pdf.line(10, 28, 200, 28)

    #Set up footer
    pdf.ln(240)
    pdf.set_font("Arial", size=10, style='I')
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=24, txt=row["Topic"], ln=1, align='R')

    for i in range(row["Pages"] - 1):
        pdf.add_page()

        #Set up footer
        pdf.ln(260)
        pdf.set_font("Arial", size=10, style='I')
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=24, txt=row["Topic"], ln=1, align='R')



pdf.output("output.pdf")