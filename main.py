from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)  # this was auto breaking the page, so we set it false
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():  # this will give us access to each row in dataframe
    pdf.add_page()

    # HEADER PART
    pdf.set_font(family="Times", style="B", size=14)
    pdf.set_text_color(254, 0, 0)  # this is for red
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
    for j in range(30, 270, 10):
        pdf.line(10, j, 200, j)

    # FOOTER PART
    pdf.ln(260)
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(254, 0, 0)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R", border=0)

    for i in range(row["Pages"] - 1):
        pdf.add_page()
        for j in range(15, 270, 10):
            pdf.line(10, j, 200, j)
        # FOOTER PART
        pdf.ln(272)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(254, 0, 0)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R", border=0)
pdf.output("output.pdf")

# pdf.cell(w=0, h=12, txt="hello there!", align="L", ln=1, border=0)   # w=0 means 100%width, but if we give
# some integer than it will be set accordingly
# ln is about new line, if we set it o, then
# the second line will print and overwrite it
# because of no new line, and will start from
# specified width
# pdf.cell(w=0, h=12, txt="praveer this side!", align="L", ln=1, border=1)
