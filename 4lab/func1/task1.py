import moviepy.editor as mp
import argparse

def main():
    parser = argparse.ArgumentParser()

    # Добавляем аргументы для парсинга
    parser.add_argument('--src')  # Исходный файл видео
    parser.add_argument("--begin", default=0)  # Начальное время для обрезки (по умолчанию 0)
    parser.add_argument("--end", default=1)  # Конечное время для обрезки (по умолчанию 1)
    parser.add_argument("--output", default='output_video.mp4')  # Имя выходного файла (по умолчанию 'output_video.mp4')

    # Парсим аргументы командной строки
    parser_args = parser.parse_args()
    source_file = parser_args.src  # Получаем исходный файл из аргументов

    video = mp.VideoFileClip(source_file)

    # Получаем значения начала и конца обрезки из аргументов
    begin = parser_args.begin
    end = parser_args.end
    output_file = parser_args.output  # Получаем имя выходного файла

    # Проверяем, что значение begin находится в допустимых пределах
    if float(begin) > video.duration or float(begin) < 0:
        print('Wrong argument begin!')
        print('Parametr --begin set to default - 0')
        begin = 0

    # Проверяем, что значение end находится в допустимых пределах
    if float(end) > video.duration or float(end) < 1:
        print('Wrong argument end!')
        print('Parametr --end set to default - 1')
        end = 1

    # Обрезаем видео на заданном отрезке
    sub_video = video.subclip(begin, end)
    sub_video.write_videofile(output_file)

main()