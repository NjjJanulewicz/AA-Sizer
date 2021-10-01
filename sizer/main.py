"""
Sizer is a simple utility for generating information about a SlotC project's art.
The information gathered will be color format, image size, frame size, and the number of frames.
Additionally a png will be created for each .img in the rc folder.
"""
# TODO error handles if rc is not a folder, also error files if out is not a folder

import os
import re
import platform
import subprocess
from pdf import Pdf
from text import Text

images = []
PATH = "rc"
OUT = "./out/sizes.txt"
WINDOWS = re.match("Windows", platform.system())


def gather_images(path):
    """
    creates a list of string objects, each holding an entire file from a slotC project
    @param path: String of the path to the directory or file
    """
    status = 1

    try:
        for entry in os.scandir(path):
            if entry.is_file() and re.search(".img", entry.name):
                images.append(path + "/" + entry.name)
            elif entry.is_dir():
                gather_images(path + "/" + entry.name)
    except FileNotFoundError as error:
        status = 0
        print("Error opening rc folder:", error)

    return status


def convert_img():
    """
    Converts a compressed slon.img to a usable png.
    @return:
    """

    for image in images:
        cp = subprocess.run(["slon-img2png", image] if WINDOWS else ["slon-img2png " + image],
                            stdout=subprocess.PIPE, shell=True)

        if cp.returncode != 0:
            print("error stopping conversion")
            break


def main():
    """Driver for sizer utility"""
    print(os.path.dirname(__file__))
    input_error = True
    gather_images(PATH)
    pdf = Pdf(images)
    text = Text(images)

    while input_error:
        user_in = input("Enter a command: ")
        if re.match("(h|elp)", user_in):
            print((
                      "\nusage: Sizer will decompile and gather information on all .img's in a SlotC project"
                      "\n\nCommands"
                      "\n\t%10s: lists all the available commands"
                      "\n\t%10s: List data for all images in a SlotC project to out/sizes.pdf"
                      "\n\t%10s: List data for all images in a SlotC project to out/sizes.txt"
                      "\n\t%10s: Converts "
                      "\n\t%10s: exits the program"
                      "\n"
                  ) % ("help", "pdf", "txt", "convert", "quit"))
        elif re.match("(pdf)", user_in):
            print("writing sizes to out/sizes.txt")
            # convert_img()
            pdf.write_report()
        elif re.match("(txt)", user_in):
            print("writing sizes to out/sizes.txt")
            # convert_img()
            text.write_report()
        elif re.match("convert", user_in):
            print("creating pngs in rc")
            convert_img()
        elif re.match("(q|uit)", user_in):
            input_error = False
        else:
            input_error = True
            print("no correct commands")


if __name__ == "__main__":
    main()
