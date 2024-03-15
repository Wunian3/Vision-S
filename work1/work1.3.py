from PIL import Image
import numpy as np

img_path = 'gray_image.png'
image = Image.open(img_path)
# 转换为numpy数组
img_array = np.array(image)

# 检查图像是否为RGB格式（3个通道）
if len(img_array.shape) == 3 and img_array.shape[2] == 3:
    # # 如果图像已经是RGB格式
    rgb_image = img_array
elif len(img_array.shape) == 2 or (len(img_array.shape) == 3 and img_array.shape[2] == 1):
    #  如果图像是灰度的或者只有一个通道，将它转换为RGB。
    rgb_image = np.stack((img_array,) * 3, axis=-1)
else:
    # 如果图像有alpha通道，去除它并转换为RGB。
    rgb_image = img_array[:, :, :3]

# 获取中心点
center_point = (rgb_image.shape[0] // 2, rgb_image.shape[1] // 2)

# 定义中心点周围31x31的邻域
half_size = 15
start_row = max(center_point[0] - half_size, 0)
end_row = min(center_point[0] + half_size + 1, rgb_image.shape[0])
start_col = max(center_point[1] - half_size, 0)
end_col = min(center_point[1] + half_size + 1, rgb_image.shape[1])

#将31x31的邻域设置为红色（255,0,0）
rgb_image[start_row:end_row, start_col:end_col] = [255, 0, 0]
#  转换回PIL图像
red_center_image = Image.fromarray(rgb_image)
new_img_path = 'red_center_image.png'
red_center_image.save(new_img_path)


