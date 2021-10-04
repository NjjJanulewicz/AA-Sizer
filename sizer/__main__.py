"""
Sizer is a simple utility for generating information about a SlotC project's art.
The information gathered will be color format, image size, frame size, and the number of frames.
Additionally a png will be created for each .img in the rc folder.
"""

import tkinter as tk

from application import Application


def main():
    """Driver for sizer utility"""
    root = tk.Tk()
    root.title("Sizer")
    root.geometry("250x250")
    root.resizable(False, False)
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
