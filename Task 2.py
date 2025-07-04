import pandas as pd

data = pd.read_excel("data.xlsx")


data.head()


summary = data.describe(include='all')
summary

from fpdf import FPDF

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Automated Data Report", ln=True, align='C')


for col in summary.columns:
    pdf.set_font("Arial", style='B', size=12)
    pdf.cell(200, 10, txt=f"\n{col} Summary", ln=True, align='L')
    pdf.set_font("Arial", size=12)
    
    for stat in summary.index:
        value = summary[col][stat]
        if pd.notnull(value):  # Avoid NaN
            line = f"{stat}: {value}"
            pdf.multi_cell(0, 10, txt=line, align='L')


pdf.output("report.pdf")

from IPython.display import IFrame
IFrame("report.pdf", width=600, height=300)
