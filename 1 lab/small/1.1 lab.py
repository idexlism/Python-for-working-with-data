import os
import shutil

def small(path):
    if path == "" or os.path.isdir(path) == False:
        path = "C:/Users/элбэг/Desktop/python для данных/1 lab/"
    small_files = []
    path_file = []
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path) and os.path.getsize(file_path) < 2048:
            small_files.append(filename)
            path_file.append(file_path)
            print(filename)
    new_dir = "small"
    new_path = os.path.join(path, new_dir)
    os.mkdir(new_path)
    if len(small_files) == 0:
        return
    else:
        for path in path_file:
            copy_file = shutil.copy2(path, new_path)






a = "C:/Users/элбэг/Desktop/python для данных/"
b = ""
small(b)