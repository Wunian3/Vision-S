import cv2

gray_image = cv2.imread('gray_image.png')

# 将图片尺寸缩小到原来的一半
resized_image = cv2.resize(gray_image, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)

# 将图片旋转180度
rotated_image = cv2.rotate(resized_image, cv2.ROTATE_180)

#水平翻转图片
flipped_image = cv2.flip(rotated_image, 1)

resized_path = 'resized_image.png'
rotated_path = 'rotated_image.png'
flipped_path = 'flipped_image.png'

cv2.imwrite(resized_path, resized_image)
cv2.imwrite(rotated_path, rotated_image)
cv2.imwrite(flipped_path, flipped_image)
