import os
import re
import platform
import subprocess

import tkinter as tk
from tkinter import filedialog as fd

from pdf import Pdf
from text import Text


OUT = "./out/sizes.txt"
WINDOWS = re.match("Windows", platform.system())

# TODO error handles if rc is not a folder, also error files if out is not a folder


class Application(tk.Frame):
    def __init__(self, master=None):
        """TODO: this seems long check to see what industry standard is"""
        super().__init__(master)
        self.master = master
        self.pack()
        self.images = []
        self.directory = None
        self.pdf_selected = None
        self.text_selected = None
        self.dialog = self.create_filedialog()
        self.checkboxes = self.create_checkboxes()
        self.size = self.create_size_btn()

    def create_convert_btn(self):
        return 1

    def create_size_btn(self):
        btn = tk.Button()
        btn["text"] = "write"
        btn["command"] = self.write
        btn.pack(side="top")
        return btn

    def create_checkboxes(self):
        self.pdf_selected = tk.IntVar()
        self.text_selected = tk.IntVar()

        frame = tk.LabelFrame(text="File type")
        frame.pack()

        c1 = tk.Checkbutton(frame, text="PDF", variable=self.pdf_selected, onvalue=1, offvalue=0)
        c1.pack()
        c2 = tk.Checkbutton(frame, text="Text", variable=self.text_selected, onvalue=1, offvalue=0)
        c2.pack()

        return c1, c2

    def create_title(self):
        return 1

    def create_filedialog(self):
        """
        TODO: get return value from dialog
        TODO: way to set the command to return value so i can initially define the self directory in init.
        """
        dialog = tk.Button()
        dialog["text"] = "Open a file"
        dialog["command"] = self.select_directory
        dialog.pack(side="top")
        return dialog

    def convert_img(self):
        """
        Converts a compressed slon.img to a usable png.
        @return:
        """

        for image in self.images:
            cp = subprocess.run(["slon-img2png", image] if WINDOWS else ["slon-img2png " + image],
                                stdout=subprocess.PIPE, shell=True)

            if cp.returncode != 0:
                print("error stopping conversion")
                break

    def select_directory(self):
        """
        TODO: anyway to tie gather to select via an event
        TODO: show current selected directory
        """
        self.directory = fd.askdirectory(
            title="Open a rc folder",
            initialdir="/",
            mustexist=True
        )

        self.gather_images(self.directory)

    def gather_images(self, path):
        """
        creates a list of string objects, each holding an entire file from a slotC project
        @param path: String of the path to the directory or file
        """
        status = 1

        try:
            for entry in os.scandir(path):
                if entry.is_file() and re.search(".img", entry.name):
                    self.images.append(path + "/" + entry.name)
                elif entry.is_dir():
                    self.gather_images(path + "/" + entry.name)
        except FileNotFoundError as error:
            status = 0
            print("Error opening rc folder:", error)

        return status

    def write(self):
        print(self.pdf_selected.get())
        if self.pdf_selected.get() == 1:
            pdf = Pdf(self.images)
            pdf.write_report()

        print(self.text_selected.get())
        if self.text_selected.get() == 1:
            text = Text(self.images)
            text.write_report()
