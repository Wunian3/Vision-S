import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from matplotlib import pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def open_image():
    global image_path, image, hist, fig, ax, canvas
    image_path = filedialog.askopenfilename()
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    ###########change here to your code#######################
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    ##########################################################
    show_image(image, hist)

def show_image(image, hist):
    global fig, ax, canvas

    ax[0].imshow(image, cmap='gray')
    ax[0].set_title('Image')
    ax[0].axis('off')

    ax[1].plot(hist, color='black')
    ax[1].set_title('Histogram')
    ax[1].set_xlim([0, 256])
    ax[1].set_ylim([0, hist.max()])

    canvas.draw()

def gama_transform(gama=1.0):
    global image, fig, ax, canvas
    gamma = float(gama)
    gamma_corrected = np.power(image / 255.0, gamma) * 255.0
    gamma_corrected = gamma_corrected.astype(np.uint8)

    ###########change here to your code#######################
    hist_corrected = cv2.calcHist([gamma_corrected], [0], None, [256], [0, 256])
    ##########################################################

    ax[0].imshow(gamma_corrected, cmap='gray')
    ax[0].set_title('Image')
    ax[0].axis('off')

    ax[1].plot(hist_corrected, color='black')
    ax[1].set_title('Histogram')
    ax[1].set_xlim([0, 256])
    ax[1].set_ylim([0, hist_corrected.max()])

    canvas.draw()

def equalize_hist():
    #write your code here.
    #Note:cv2.equalizeHist(img) not allowed
    global image, fig, ax, canvas

    ###########change here to your code#######################
    image_corrected = cv2.equalizeHist(image)
    ##########################################################

    ###########change here to your code#######################
    hist_corrected = cv2.calcHist([image_corrected], [0], None, [256], [0, 256])
    ##########################################################

    ax[0].imshow(image_corrected, cmap='gray')
    ax[0].set_title('Image')
    ax[0].axis('off')

    ax[1].plot(hist_corrected, color='black')
    ax[1].set_title('Histogram')
    ax[1].set_xlim([0, 256])
    ax[1].set_ylim([0, hist_corrected.max()])

    canvas.draw()

root = Tk()
root.title("Image Transform Demo")

frame = Frame(root)
frame.pack(padx=10, pady=10)

open_button = Button(frame, text="Open Image", command=open_image)
open_button.pack(side=LEFT, padx=10)

gamma_label = Label(frame, text="Gamma:")
gamma_label.pack(side=LEFT)

gamma_scale = Scale(frame, from_=0.1, to=25.0, resolution=0.1, orient=HORIZONTAL, command=gama_transform)
gamma_scale.set(1.0)
gamma_scale.pack(side=LEFT)

hist_button = Button(frame, text="Hist equalize", command=equalize_hist)
hist_button.pack(side=LEFT, padx=10)

fig, ax = plt.subplots(1, 2, figsize=(10, 5))
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

root.mainloop()