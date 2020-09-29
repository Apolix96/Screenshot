from PIL import Image, ImageGrab
from tkinter import *

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 2)
    window.geometry(f'{width}x{height}+{x}+{y}')

def screen_shot():
    current_name = name_screen.get()
    img = ImageGrab.grab()
    img.save(f'{current_name}.bmp', "BMP")
    img.mode
    # parametrs cube obl
    # img2 = ImageGrab.grab((100,100,300,300))
    # img2.save('screen.bmp', "BMP")
    # img2.size


if __name__ == "__main__":
    root = Tk()
    root.title("screenshot")
    root.resizable(height = False, width = False)
    center_window(root) # set center window

    label_information = Label(
        text = "Write name for screenshot"
    )
    label_information.place(x = 20, y = 20)
    name_screen = StringVar()
    name_entry = Entry(
        textvariable = name_screen
    )
    name_entry.place(x = 30, y = 40)

    btn_screenshot = Button(
        root,
        width = 10, height = 2,
        padx = '25', pady = '2',
        text="Tap screenshot screen",
        command=screen_shot
    )
    btn_screenshot.place(x = 30, y = 100)
    root.mainloop()
