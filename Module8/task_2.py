print('Задача 2. Поиск элемента — 2\n')

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}


def get_value(site_dict, key, depth=0, max_depth=float('inf')):
    if depth == max_depth:
        return None
    elif key in site_dict:
        return site_dict[key]

    for sub_el in site_dict.values():
        if isinstance(sub_el, dict):
            res = get_value(sub_el, key, depth + 1, max_depth)
            if res:
                break
    else:
        res = None

    return res


user_key = input('Введите искомый ключ: ')
need_depth = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if need_depth == 'y':
    user_depth = int(input('Введите максимальную глубину: '))
    print(get_value(site, user_key, max_depth=user_depth))
else:
    print(get_value(site, user_key))
