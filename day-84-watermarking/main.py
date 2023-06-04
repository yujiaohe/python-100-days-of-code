import os
from tkinter import *
import pyperclip
from tkmacosx import Button
from tkinter import filedialog as fd
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont, ImageColor


def select_files():
    filetypes = (
        ('png files', '*.png'),
        ('jpg files', '*.jpg'),
        ('jpeg files', '*.jpeg')
    )
    files = fd.askopenfiles(
        title="Select Files",
        initialdir='/',
        filetypes=filetypes
    )
    selected_files = "\n".join([file.name for file in files])
    # msg = f"You selected: \n{selected_files}"
    # messagebox.showinfo(title="Selected Files", message=msg)
    files_text.config(state=NORMAL)
    files_text.insert('1.0', selected_files)
    files_text.config(state=DISABLED)


def select_logo():
    filetypes = (
        ('png files', '*.png'),
        ('jpg files', '*.jpg'),
        ('jpeg files', '*.jpeg')
    )
    files = fd.askopenfiles(
        title="Select Files",
        initialdir='/',
        filetypes=filetypes
    )
    selected_files = "\n".join([file.name for file in files])
    logo_text.config(state='normal')
    logo_text.insert('1.0', selected_files)
    logo_text.config(state='disabled')


def add():
    files = files_text.get('1.0', END).strip()
    logo_files = logo_text.get('1.0', END).strip()
    logo_txt = logo_entry.get().strip()

    if files == '':
        messagebox.showerror("Error", message="Please select at least one file!")
        return
    if logo_files == '' and len(logo_txt) == 0:
        messagebox.showerror("Error", message="Please select at least one logo file or input logo text!")
        return

    files = files.split("\n")
    logo_files = logo_files.split("\n") if logo_files != '' else logo_files
    pre = "watermark"
    # add text watermark
    if len(logo_txt) != 0:
        text_watermark_files = []
        font = ImageFont.truetype('Arial.ttf', 35)
        for file in files:
            im = Image.open(file)
            draw = ImageDraw.Draw(im)

            # draw watermark in the bottom left corner
            color = default.get()
            rgb = ImageColor.getcolor(color, mode='RGBA')
            draw.text((10, im.size[1] - 50), logo_txt, font=font, fill=rgb)
            # im.show()

            save_file = f"images/{pre}_{file.split('/')[-1]}"
            im.save(f"{save_file}")
            text_watermark_files.append(save_file)
        files = text_watermark_files

    # add img watermark
    if len(logo_files) != 0:
        for file in files:
            im = Image.open(file)
            for num in range(len(logo_files)):
                logo_file = logo_files[num]
                im_logo = Image.open(logo_file)
                if im_logo.size[0] > 100 or im_logo.size[1] > 100:
                    im_logo.thumbnail((200, 200))

                # calculate the x, y coordinates of the im_log, margin = 5
                x = im_logo.size[0] + 5 + 200 * num
                y = im_logo.size[1] + 5
                # add watermark in the top left conor
                im.paste(im_logo, (x, y))
                # im.show()

                file_name = file.split("/")[-1]
                file_name = file_name[len(pre)+1:] if file_name[:len(pre)] == pre else file_name
                im.save(f"images/watermark_{file_name}")
    messagebox.showinfo(title="Add Watermark", message=f"Output: {os.getcwd()}/images")
    pyperclip.copy(f"{os.getcwd()}/images")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("WaterMarker")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=210, highlightthickness=0)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=0, row=0, columnspan=2)

# Labels
# files_label = Label(text="or drag your files here")
# files_label.grid(column=1, row=3)
logo_label = Label(text="or input logo text:")
logo_label.grid(column=0, row=4)
color_label = Label(text="Logo text color:")
color_label.grid(column=0, row=5)


# Entries
logo_entry = Entry(width=38)
logo_entry.grid(column=1, row=4)

# Texts
files_text = Text(window, height=5, width=50, state=DISABLED)
files_text.grid(column=1, row=2)
logo_text = Text(window, height=3, width=50, state=DISABLED)
logo_text.grid(column=1, row=3)

# Dropdown list
options = [
    "white",
    "black",
    "green",
    "blue",
    "purple",
]
default = StringVar()
default.set("white")
color_list = OptionMenu(window, default, *options)
# color_list = OptionMenu(window, default, "white", "black", "green", "blue", "purple")
color_list.grid(column=1, row=5)

# Buttons
files_button = Button(text="Select Files", width=100, bg='#ADEFD1', fg='#00203F', command=select_files)
files_button.grid(column=0, row=2)
logo_button = Button(text="Select Logo", width=100, bg='#ADEFD1', fg='#00203F', command=select_logo)
logo_button.grid(column=0, row=3)
mark_button = Button(text="Add watermark", width=150, bg='#ADEFD1', fg='#00203F', command=add)
mark_button.grid(column=1, row=6)

window.mainloop()
