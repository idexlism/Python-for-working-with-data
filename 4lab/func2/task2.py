import moviepy.editor as mp
import argparse
from PIL import Image
from pathlib import Path

def main():
    parser = argparse.ArgumentParser()

    parser.add_argument('--src')  # Исходный файл видео
    parser.add_argument("--begin", default=0)  # Начальное время для извлечения кадров
    parser.add_argument("--end", default=1)  # Конечное время для извлечения кадров
    parser.add_argument("--path_output", default='.')
    parser.add_argument('--step', default='1')  # Шаг между извлекаемыми кадрами (по умолчанию 1)

    parser_args = parser.parse_args()
    source_file = parser_args.src
    begin = parser_args.begin
    end = parser_args.end
    output = parser_args.path_output
    step = parser_args.step

    video = mp.VideoFileClip(source_file)

    # Проверяем, что значение begin находится в допустимых пределах
    if float(begin) > video.duration or float(begin) < 0:
        print('Wrong argument begin!')
        print('Parametr --begin set to default - 0')
        begin = 0

    # Проверяем, что значение end находится в допустимых пределах
    if float(end) > video.duration or float(end) < 1:
        print('Wrong argument end!')
        print('Parametr --end set to default - 10')
        end = 1


    if not Path(output).exists():
        Path(output).mkdir()

    # Извлекаем кадры из видео в заданном диапазоне
    for i in range(int(begin), int(end), int(step)):
        frame = video.get_frame(i)
        dir_path = f'video({i}).jpg'
        img = Image.fromarray(frame)
        img_res = img.resize((250, img.height))
        img_res.save(f'{output}/{dir_path}')


main()