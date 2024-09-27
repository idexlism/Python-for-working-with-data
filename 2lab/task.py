from PIL import Image, ImageFilter
from PIL import ImageDraw, ImageFont
import sys
import glob

# Задание 1
def mergeRGB(pic):
    with Image.open(pic) as img:
        img.load() and img.show()

# Разбиваем изображение на слои
    red, green, blue = img.split()
    zeroed_band = red.point(lambda _: 0)

# Выделяем разные каналы RGB и выводим
    red_merge = Image.merge("RGB", (red, zeroed_band, zeroed_band))
    red_merge.show()

    green_merge = Image.merge("RGB", (zeroed_band, green, zeroed_band))
    green_merge.show()

    blue_merge = Image.merge("RGB", (zeroed_band, zeroed_band, blue))
    blue_merge.show()


# Задание 2

def find_color(image_path):
    image_path = sys.argv[1]
    image = Image.open(image_path)
    pixels = image.load()

    r_count = 0
    g_count = 0
    b_count = 0

    for i in range(image.size[0]):
        for j in range(image.size[1]):
            # Получить RGB значения пикселя
            r, g, b = pixels[i, j]
            r_count += r
            g_count += g
            b_count += b

    #средние значения RGB цветов
    redAvr = r_count / (image.size[0] * image.size[1])
    greenAvr = g_count / (image.size[0] * image.size[1])
    blueAvr = b_count / (image.size[0] * image.size[1])
    if redAvr > greenAvr and redAvr > blueAvr:
        print("Результат: RGB цвет, используемый больше всего - Красный")
    elif greenAvr > redAvr and greenAvr > blueAvr:
        print("Результат: RGB цвет, используемый больше всего - Зеленый")
    else:
        print("Результат: RGB цвет, используемый больше всего - Синий")

    # В конце пишем в терминале #python task.py pic.jpg

# Задание 3

def watermark(img, img_logo):
    with Image.open(img) as pic:
        pic.load()
    with Image.open(img_logo) as logo:
        logo.load()
    font = ImageFont.truetype("droid-sans.regular.ttf", 50)
    draw = ImageDraw.Draw(pic)
    draw.text((250, 300), "Watermark!!!", (230, 0, 200), font=font)
    logo = logo.convert("L")
    logo = logo.resize(
        (logo.width // 4, logo.height // 4)
    )
    logo = logo.filter(ImageFilter.CONTOUR)
    pic.paste(logo,(250,360), logo)
    pic.show()
    pic.save(f'task3.png')

# Задание 4

def create_card():
    # Размеры карточки
    width, height = 100, 100
    # Цвета
    blue_frame_color = (0, 0, 255)
    red_text_color = (255, 0, 0)
    # Толщина рамки
    frame_thickness = 5

    # Создаем шрифт для текста
    font = ImageFont.truetype("droid-sans.regular.ttf", 24)

    # Создание карточек
    for i in range(1, 4):
        # Создаем пустое изображение с белым фоном
        img = Image.new('RGB', (width, height), (255, 255, 255))
        draw = ImageDraw.Draw(img)
        draw.line([(0, 0), (100, 0), (100, 100), (0, 100), (0, 0)], width=5, fill=(0, 0, 255))

        textPos = (width // 2, height // 2)

        # Рисуем текст
        draw.text(textPos, str(i), fill=red_text_color, font=font)
        img.save(f'task3_card_{i}.png')
        img.show()

# Задание 5

def display_images(extension):
    #список всех изображений в текущей директории
    files = glob.glob(f"*.{extension}")

    if not files:
        print(f"Нет изображений с расширением .{extension} в текущей директории.")
        return

    for file in files:
        try:
            with Image.open(file) as img:
                # Создаем миниатюру
                img.thumbnail((150, 150))
                img.show(title=file)
        except Exception as e:
            print(f"Не удалось открыть изображение {file}: {e}")

    # В конце пишем в терминале #python task.py jpg


pic = "pic.jpg"
logo = "vote.jpg"
#mergeRGB(pic)
#find_color(pic)
#watermark(pic, logo)
#create_card()
#display_images('jpg')