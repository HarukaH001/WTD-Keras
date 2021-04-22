import cv2

import os

def load_images_from_folder(folder):
    images = []
    for filename in os.listdir(folder):
        img = cv2.imread(os.path.join(folder,filename))
        if img is not None:
            images.append(img)
    return images

folder="./nd/Shiba_Inu"

imgs = load_images_from_folder(folder)

flip_img = []
for i in imgs:
    flip_img.append(cv2.flip(i, 1)) 
    flip_img.append(cv2.flip(i, 0))
    flip_img.append(cv2.flip(i, -1))
for i in range(len(flip_img)):
    cv2.imwrite(os.path.join(folder, 'augShi{}.jpg'.format(i)), flip_img[i])