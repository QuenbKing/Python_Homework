import json

print('Задача 6. Поиск разницы между двумя JSON-файлами (пример из реального тестового задания на должность '
      'Python-разработчика уровня Junior)\n')

diff_list = ['services', 'staff', 'datetime']
diff_data = dict()

with open('json_new.json', 'r', encoding='UTF-8') as file:
    new_data = json.load(file)

with open('json_old.json', 'r', encoding='UTF-8') as file:
    old_data = json.load(file)


def find_diff(key, old_dict, new_dict):
    for my_key in new_dict.keys():
        if my_key == key and old_dict[my_key] != new_dict[my_key]:
            return new_dict[my_key]
        elif isinstance(new_dict[my_key], dict) or isinstance(old_dict[my_key], dict) and my_key != key:
            value = find_diff(key, old_dict[my_key], new_dict[my_key])
            if value is None:
                continue
            return value


for el_key in diff_list:
    diff = find_diff(el_key, old_data, new_data)
    if diff is not None:
        diff_data[el_key] = diff

print(diff_data)

with open('result.json', 'w', encoding='UTF-8') as file:
    json.dump(diff_data, file, indent=4)
