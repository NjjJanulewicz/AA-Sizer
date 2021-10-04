from properties import Properties

OUT = "sizes.txt"


class Text:
    def __init__(self, images):
        self.images = images
        self.out = "sizes.txt"

    def write_report(self):
        print("write report")
        fp = open(self.out, "w")
        for image in self.images:
            prop = Properties(image)
            fp.write(prop.to_string())
        fp.close()
        print("done")
