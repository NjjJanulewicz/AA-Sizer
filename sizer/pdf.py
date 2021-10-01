from properties import Properties
from fpdf import FPDF


class Pdf:
    def __init__(self, images):
        self.images = images

    def write_report(self):
        document = FPDF()
        document.add_page()
        for image in self.images:
            prop = Properties(image)
            document.set_font('helvetica', size=12)
            for item in prop.to_string().split("\n"):
                if item:
                    document.cell(txt=item)
                    document.ln()
            document.image(image, x=20, y=60, alt_text="Snake logo of the fpdf2 library")
            document.ln(24)
        document.output("out/sizes.pdf")
