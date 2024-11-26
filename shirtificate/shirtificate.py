from fpdf import FPDF

def make_pdf():
    pdf = FPDF(orientation="portrait", format="A4")
    pdf.set_font("Helvetica", 'B', 40)
    pdf.set_fill_color(255, 255, 255)
    pdf.add_page()
    return pdf

def add_image(pdf):
    pdf.image("shirtificate.png", x=0.5, y=40)
    return pdf

def add_title(pdf):
    pdf.cell(0, 10, 'CS50 Shirtificate', 0, 1, 'C')
    return pdf

def add_text_centered(pdf, text):
    a4_width = 210  # width in mm
    a4_height = 297  # height in mm
    x_center = a4_width / 2
    y_center = a4_height / 2

    # Set the font and size
    pdf.set_font('Helvetica', 'B', 20)  # Adjust the font and size as needed
    pdf.set_text_color(255, 255, 255)

    # Calculate width and height of the text to be added
    text_width = pdf.get_string_width(text)
    text_height = pdf.font_size

    # Calculate coordinates to center the text
    x_position = x_center - text_width / 2
    y_position = y_center - text_height / 2
    pdf.text(x_position, y_position-30, text)
    return pdf  # Don't forget to return the modified PDF object

def main():
    pdf = make_pdf()
    final_pdf = add_image(pdf)
    after_title = add_title(final_pdf)
    name = input("Name: ").strip()
    final = add_text_centered(after_title, name+' took CS50')
    final.output("shirtificate.pdf")

if __name__ == "__main__":
    main()
