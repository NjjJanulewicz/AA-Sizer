from properties import Properties

OUT = "./out/sizes.txt"


class Text:
    def __init__(self, images):
        self.images = images
        self.out = "out/sizes.pdf"

    def write_report(self):
        fp = open(self.out, "w")
        for image in self.images:
            prop = Properties(image)
            fp.write(prop.to_string())
        fp.close()
