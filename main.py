from fpdf import FPDF
import pandas as pd


pdf = FPDF(orientation="P", unit="mm", format="A4")
df = pd.read_csv("topics.csv")

for index, row in df.iterrows():    #this will give us access to each row in dataframe
    pdf.add_page()
    pdf.set_font(family="Times", style="B", size=14)
    pdf.set_text_color(254, 0, 0)   # this is for red
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", border=0, ln=1)
    pdf.line(x1=10, y1=20, x2=200, y2=20)


pdf.output("output.pdf")






# pdf.cell(w=0, h=12, txt="hello there!", align="L", ln=1, border=0)   # w=0 means 100%width, but if we give
                                                                # some integer than it will be set accordingly
                                                                # ln is about new line, if we set it o, then
                                                                # the second line will print and overwrite it
                                                                # because of no new line, and will start from
                                                                # specified width
# pdf.cell(w=0, h=12, txt="praveer this side!", align="L", ln=1, border=1)





