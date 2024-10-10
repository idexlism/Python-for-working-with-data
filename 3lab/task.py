import os
import sys
import numpy as np
from skimage import io, util, transform, exposure, filters
from skimage.util import random_noise
import matplotlib.pyplot as plt

# Определяем атомарные преобразования
def rotate_image(image, angle):
    return transform.rotate(image, angle)

def flip_image(image):
    return np.fliplr(image)

def change_brightness(image, factor):
    return exposure.adjust_gamma(image, factor)

def add_noise(image):
    return random_noise(image)

def resize_image(image, output_size):
    return transform.resize(image, output_size)

# Комплексное преобразование: комбинация нескольких атомарных
def complex_transformation(image):
    image = rotate_image(image, 30)
    image = flip_image(image)
    image = change_brightness(image, 1.5)
    return image

# Функция для аугментации изображений
def augment_images(folder_path, transformations):
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg') or filename.endswith('.png'):
            img_path = os.path.join(folder_path, filename)
            image = io.imread(img_path)

            for i, transform in enumerate(transformations):
                if transform == 'rotate':
                    augmented_image = rotate_image(image, 30)
                elif transform == 'flip':
                    augmented_image = flip_image(image)
                elif transform == 'brightness':
                    augmented_image = change_brightness(image, 1.5)
                elif transform == 'noise':
                    augmented_image = add_noise(image)
                elif transform == 'resize':
                    augmented_image = resize_image(image, (100, 100))  # Пример нового размера
                elif transform == 'complex':
                    augmented_image = complex_transformation(image)

                # Сохраняем новое изображение
                new_filename = f"{os.path.splitext(filename)[0]}_aug_{i}{os.path.splitext(filename)[1]}"
                new_img_path = os.path.join(folder_path, new_filename)
                io.imsave(new_img_path, (augmented_image * 255).astype(np.uint8))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python augment_images.py <path_to_folder>")
        sys.exit(1)

    folder_path = sys.argv[1]

    # Выбор преобразований
    transformations = []
    print("Выберите преобразования (введите номера через запятую):")
    print("1. Поворот (rotate)")
    print("2. Отзеркаливание (flip)")
    print("3. Изменение яркости (brightness)")
    print("4. Добавление шума (noise)")
    print("5. Изменение размера (resize)")
    print("6. Комплексное преобразование (complex)")

    choices = input("Ваш выбор: ")
    choices = choices.split(',')

    for choice in choices:
        if choice.strip() == '1':
            transformations.append('rotate')
        elif choice.strip() == '2':
            transformations.append('flip')
        elif choice.strip() == '3':
            transformations.append('brightness')
        elif choice.strip() == '4':
            transformations.append('noise')
        elif choice.strip() == '5':
            transformations.append('resize')
        elif choice.strip() == '6':
            transformations.append('complex')

    augment_images(folder_path, transformations)
