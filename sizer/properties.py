import re
import platform
import subprocess

WINDOWS = re.match("Windows", platform.system())
PATH = "rc"


class Properties:
    def __init__(self, image):
        self.__extract(image)

    def __extract(self, image):
        (out, err) = subprocess.Popen(["slon-imginfo", image] if WINDOWS else ["slon-imginfo " + image],
                                      stdout=subprocess.PIPE, shell=True).communicate()
        arr = out.decode().strip().split("\r\n" if WINDOWS else "\n")

        for index, value in enumerate(arr):
            arr[index] = value.split(":")[1].strip()

        self.name = image.split(PATH + "/")[1]
        self.format, self.color_key, self.image_size, self.frame_size, self.frames = arr

    def to_string(self):
        return f'Name: {self.name}\nFormat: {self.format}\nColor key: {self.color_key}\n' \
               f'Image size: {self.image_size}\nFrame size: {self.frame_size}\nFrames: {self.frames}\n\n'
