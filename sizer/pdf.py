import os
from properties import Properties
from fpdf import FPDF


class Pdf:
    def __init__(self, images):
        self.images = images
        self.font_size = 12
        self.out = "out/sizes.pdf"

    def write_report(self):
        document = FPDF()
        document.add_page()
        for image in self.images:
            prop = Properties(image)
            document.set_font('helvetica', size=12)
            document.cell(txt=prop.name, border=1, align="C",
                          link=f'file:///{os.path.dirname(os.path.realpath(__file__))}/{image[:len(image) - 3]}png')
            document.ln()
            for item in prop.to_string().split("\n")[1:]:
                if item:
                    document.cell(txt=item)
                    document.ln()
            document.ln(24)
        document.output(self.out)
