from fpdf import FPDF

pdf_output = "shirtificate.pdf"

def main():
    shirt_name = f"{input('Name: ')} took CS50"
    my_pdf = FPDF(orientation="P", unit="mm", format="A4")

    my_pdf.add_page()
    my_pdf.set_font("Helvetica", size=42)

#    my_pdf.cell(10, 10, 'Hello World!', 1)

    my_pdf.cell(w=my_pdf.epw, border=0, text="CS50 Shirtificate", align="C")
    my_pdf.image("shirtificate.png", x="C", w=my_pdf.epw, y=my_pdf.h-my_pdf.eph)
    my_pdf.set_y(my_pdf.eph/3)
    my_pdf.set_font(size=21)
    my_pdf.set_text_color(r=255, g=255, b=255)
    my_pdf.cell(w=my_pdf.epw, text=shirt_name, align="C", new_x="CENTER", new_y="TOP", border=0)






    my_pdf.output(pdf_output)



if __name__ == "__main__":
    main()

