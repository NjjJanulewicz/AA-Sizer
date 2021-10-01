from properties import Properties


class Text:
    def __init__(self, images):
        self.images = images

    def write_report(self):
        fp = open(OUT, "w")
        for image in self.images:
            prop = Properties(image)
            fp.write(prop.to_string())
        fp.close()
