import cv2
from matplotlib import pyplot as plt

# 读取RGB颜色图像
image = cv2.imread('pic1.jpg')

# 将图像转换为灰度并保存为PNG文件
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite('gray_image.png', gray_image)
# 使用Matplotlib以4x4布局显示图像
fig, axs = plt.subplots(4, 4, figsize=(10, 10))

# 原始图像
axs[0, 0].imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
axs[0, 0].set_title('Original Image')
axs[0, 0].axis('off')

#灰度图像
axs[0, 1].imshow(gray_image, cmap='gray')
axs[0, 1].set_title('Grayscale Image')
axs[0, 1].axis('off')

# 提取R, G, B通道
# OpenCV以BGR格式读取图像
B, G, R = cv2.split(image)

# 显示R, G, B通道的图像
axs[0, 2].imshow(R, cmap='Reds')
axs[0, 2].set_title('Red Channel')
axs[0, 2].axis('off')

axs[0, 3].imshow(G, cmap='Greens')
axs[0, 3].set_title('Green Channel')
axs[0, 3].axis('off')

axs[1, 0].imshow(B, cmap='Blues')
axs[1, 0].set_title('Blue Channel')
axs[1, 0].axis('off')

for i in range(1, 4):
    for j in range(4):
        axs[i, j].axis('off')

plt.tight_layout()
plt.show()


