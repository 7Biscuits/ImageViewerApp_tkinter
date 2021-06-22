from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title('Image Viewer')

img_1 = ImageTk.PhotoImage(Image.open('Images/anime_gin.jpg'))
img_2 = ImageTk.PhotoImage(Image.open('Images/anime_pfp.jpg'))
img_3 = ImageTk.PhotoImage(Image.open('Images/biscuitpfp.png'))
img_4 = ImageTk.PhotoImage(Image.open('Images/anime_gin.jpg'))
img_5 = ImageTk.PhotoImage(Image.open('Images/anime_pfp.jpg'))

image_list = [img_1, img_2, img_3, img_4, img_5]

my_label = Label(image=img_1)
my_label.grid(row=0, column=0, columnspan=3)

def img_forward(image_number):
	global my_label
	global forward_button
	global back_button

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])

	forward_button = Button(root, text=">", command=lambda: img_forward(image_number+1))
	back_button = Button(root, text="<", command=lambda: img_back(image_number-1))

	if image_number == 5:
		forward_button = Button(root, text=">", state=DISABLED)

	back_button.grid(row=1, column=0)
	forward_button.grid(row=1, column=2)
	my_label.grid(row=0, column=0, columnspan=3)
	
def img_back(image_number):
	global my_label
	global forward_button
	global back_button

	my_label.grid_forget()
	my_label = Label(image=image_list[image_number-1])
	my_label.grid(row=0, column=0, columnspan=3)

	forward_button = Button(root, text=">", command=lambda: img_forward(image_number+1))
	back_button = Button(root, text="<", command=lambda: img_back(image_number-1))
	back_button.grid(row=1, column=0)
	forward_button.grid(row=1, column=2)

	if image_number == 1:
		back_button = Button(root, text="<", state=DISABLED)


back_button = Button(root, text="<", command=img_back, state=DISABLED)
button_exit = Button(root, text="Exit", command=root.quit)
forward_button = Button(root, text=">", command=lambda: img_forward(2))


back_button.grid(row=1, column=0)
button_exit.grid(row=1, column=1)
forward_button.grid(row=1, column=2)

root.mainloop()