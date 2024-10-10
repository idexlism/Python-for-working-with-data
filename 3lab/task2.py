import os
import sys
import numpy as np
from skimage import io, util, transform, exposure, filters
from skimage.util import random_noise
import matplotlib.pyplot as plt
from PIL import Image

def histogram_matplot(pic):
    image = Image.open(pic)
    r, g, b = image.split()
    # Создание гистограмм
    plt.figure(figsize=(10, 5))

    # Гистограмма для красного канала
    plt.subplot(1, 3, 1)
    plt.hist(r.getdata(), bins=256, color='red', alpha=0.7)
    plt.title('Красный канал')
    plt.xlim([0, 255])

    # Гистограмма для зеленого канала
    plt.subplot(1, 3, 2)
    plt.hist(g.getdata(), bins=256, color='green', alpha=0.7)
    plt.title('Зеленый канал')
    plt.xlim([0, 255])

    # Гистограмма для синего канала
    plt.subplot(1, 3, 3)
    plt.hist(b.getdata(), bins=256, color='blue', alpha=0.7)
    plt.title('Синий канал')
    plt.xlim([0, 255])

    # Настройка общего заголовка и отображение
    plt.suptitle('Гистограмма цветовых каналов изображения 1')
    plt.tight_layout()
    plt.show()

def histogram_skimage(pic):
    image_path = pic
    image = io.imread(image_path)
    if image.ndim == 3:  # Цветное изображение
        # Разделение на цветовые каналы
        r = image[:, :, 0].ravel()
        g = image[:, :, 1].ravel()
        b = image[:, :, 2].ravel()

        # Создание гистограмм
        plt.figure(figsize=(10, 5))

        #для красного канала
        plt.subplot(1, 3, 1)
        plt.hist(r, bins=256, color='red', alpha=0.7)
        plt.title('Красный канал')
        plt.xlim([0, 255])

        #для зеленого канала
        plt.subplot(1, 3, 2)
        plt.hist(g, bins=256, color='green', alpha=0.7)
        plt.title('Зеленый канал')
        plt.xlim([0, 255])

        #для синего канала
        plt.subplot(1, 3, 3)
        plt.hist(b, bins=256, color='blue', alpha=0.7)
        plt.title('Синий канал')
        plt.xlim([0, 255])

    plt.suptitle('Гистограмма цветовых каналов изображения 2')
    plt.tight_layout()
    plt.show()

pict = 'dog.jpg'
histogram_matplot(pict)
histogram_skimage(pict)