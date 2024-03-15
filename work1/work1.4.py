import matplotlib.pyplot as plt
import numpy as np
# 假设图像的大小是100x100
size = (100, 100)
A = np.random.choice([0, 255], size=size)
B = np.random.choice([0, 255], size=size)

# 计算A和B的交集（逻辑与）和并集（逻辑或）
intersection = np.logical_and(A, B) * 255
union = np.logical_or(A, B) * 255

# 使用matplotlib在4x4网格中可视化A、B、交集和并集
fig, axes = plt.subplots(2, 2, figsize=(8, 8))

# 绘制每个图像
axes[0, 0].imshow(A, cmap='gray')
axes[0, 0].title.set_text('Image A')
axes[0, 0].axis('off')

axes[0, 1].imshow(B, cmap='gray')
axes[0, 1].title.set_text('Image B')
axes[0, 1].axis('off')

axes[1, 0].imshow(intersection, cmap='gray')
axes[1, 0].title.set_text('Intersection')
axes[1, 0].axis('off')

axes[1, 1].imshow(union, cmap='gray')
axes[1, 1].title.set_text('Union')
axes[1, 1].axis('off')

plt.tight_layout()
plt.show()
