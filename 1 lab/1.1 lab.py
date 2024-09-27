import os
import shutil
from pathlib import Path

def small(directory: Path):
    small_files = []
    for file in directory.glob('*'):
        if file.is_file() and file.stat().st_size < 2048: #выбираем меньше 2к
            small_files.append(file)
    if len(small_files) == 0:
        print("file not found")
        return
    else:
        for file in small_files:
            print(file) #вывод файлов

    small_dir = directory / 'small'
    small_dir.mkdir(exist_ok=True)
    for file in small_files:
        shutil.copy(file, small_dir)
    print(f"files save in: {small_dir}")

def check_files_in_directory(dirpath: Path, files):
    present_files = []
    absent_files = []

    for filename in files:
        file_path = dirpath / filename
        if file_path.exists():
            present_files.append(filename)
        else:
            absent_files.append(filename)

    # Выводим результаты на экран
    print("\nПрисутствующие файлы:")
    for f in present_files:
        print(f)

    print("\nОтсутствующие файлы:")
    for f in absent_files:
        print(f)

    # Записываем списки в файлы
    with open('present_files.txt', 'w') as present_file:
        present_file.write('\n'.join(present_files))

    with open('absent_files.txt', 'w') as absent_file:
        absent_file.write('\n'.join(absent_files))

    if not files:
        total_files = len(list(dirpath.glob('*')))
        total_size = sum(file.stat().st_size for file in dirpath.glob('*') if file.is_file())
        print(f"\nОбщая информация о папке:\nКоличество файлов: {total_files}\nОб��ий размер: {total_size} байт")


def create_missing_files_from_list(missing_files_path: Path, target_directory: Path):
    with open(missing_files_path, 'r') as file:
        missing_files = file.read().splitlines()

    for filename in missing_files:
        file_path = target_directory / filename
        if not file_path.exists():
            file_path.touch()  # Создает пустой файл
            print(f"Создан файл: {file_path}")
