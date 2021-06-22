import tkinter
from tkinter import *
from PIL import ImageTk, Image

root = tkinter.Tk()
root.title('Image Viewer')

img_1 = ImageTk.PhotoImage(Image.open('Images/anime_gin.jpg'))
img_2 = ImageTk.PhotoImage(Image.open('Images/anime_pfp.jpg'))
img_3 = ImageTk.PhotoImage(Image.open('Images/biscuitpfp.png'))
img_4 = ImageTk.PhotoImage(Image.open('Images/anime_gin.jpg'))
img_5 = ImageTk.PhotoImage(Image.open('Images/anime_pfp.jpg'))

img_list = [img_1, img_2, img_3, img_4, img_5]

img_label = Label(image=img_1)
img_label.grid(row=0, column=0, columnspan=3)

def img_forward(img_num):
    global img_label
    global forward_button
    global back_button

    img_label.grid_forget()
    img_label = Label(image = img_list[img_num - 1])
    img_label.grid(row=0, column=0, columnspan=3)

    forward_button = Button(text='>', padx=5, command=lambda: img_forward(img_num + 1))
    back_button = Button(text='<', padx=5, command=lambda: img_backward(img_num - 1))

    forward_button.grid(row=1, column=2)
    back_button.grid(row=1, column=0)

    if img_num == 5:
	    forward_button = Button(root, text=">", state=DISABLED)


def img_backward():
    global img_label
    global forward_button
    global back_button

def exit():
    root.quit()

back_button = Button(text='<', padx=5, command=img_backward)
exit_button = Button(text='Exit', command=exit)
forward_button = Button(text='>', padx=5, command=lambda: img_forward(2))

forward_button.grid(row=1, column=2)
exit_button.grid(row=1, column=1)
back_button.grid(row=1, column=0)

root.mainloop()
