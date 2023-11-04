import os

print('Задача 3. Файлы и папки\n')


def count_files_and_dir(cur_path, dir_count, fil_count, size):
    for i_el in os.listdir(cur_path):
        my_path = os.path.join(cur_path, i_el)
        if os.path.isfile(my_path):
            fil_count += 1
            size += os.path.getsize(my_path)
        elif os.path.isdir(my_path):
            dir_count += 1
            size += os.path.getsize(my_path)
            dir_count, fil_count, size = count_files_and_dir(my_path, dir_count, fil_count, size)

    return dir_count, fil_count, size


path = os.path.abspath('..')
directory_count, files_count, directory_size = count_files_and_dir(path, 0, 0, 0)
print(f'Размер каталога (в Кбайтах): {directory_size / 1024}')
print(f'Количество подкаталогов: {directory_count}')
print(f'Количество файлов: {files_count}')


