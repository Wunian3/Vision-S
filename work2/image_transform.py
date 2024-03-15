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
    # hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    hist = calculate_histogram(image)

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

def calculate_histogram(image):
    histogram = [0] * 256
    # 获取图像的高度和宽度
    height, width = image.shape
    # 遍历图像的每个像素
    for i in range(height):
        for j in range(width):
            # 获取当前像素的亮度值
            pixel_value = image[i, j]
            # 对应亮度值的计数加1
            histogram[pixel_value] += 1

    # 将列表转换为numpy数组并返回
    return np.array(histogram)


def gama_transform(gama=1.0):
    global image, fig, ax, canvas
    gamma = float(gama)
    gamma_corrected = np.power(image / 255.0, gamma) * 255.0
    gamma_corrected = gamma_corrected.astype(np.uint8)

    ###########change here to your code#######################
    hist_corrected = calculate_histogram(gamma_corrected)
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
    global image, fig, ax, canvas

    hist = calculate_histogram(image)
    cdf = np.cumsum(hist)
    cdf_normalized = cdf * float(hist.max()) / cdf.max()
    # 创建一个映射表，将旧的像素值映射到新的像素值
    cdf_m = np.ma.masked_equal(cdf_normalized, 0)
    cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())
    cdf_final = np.ma.filled(cdf_m, 0).astype('uint8')

    # 应用映射到原始图像
    image_corrected = cdf_final[image]

    # 重新计算均衡化后的直方图
    hist_corrected = calculate_histogram(image_corrected)

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