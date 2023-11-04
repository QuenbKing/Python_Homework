import copy

print('Задача 3. Глубокое копирование\n')

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам {0} недорого',
        },
        'body': {
            'h2': 'У нас самая низкая цена на {0}',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}


def get_value(site_dict, text):
    for key in site_dict.keys():
        if isinstance(site_dict[key], dict):
            get_value(site_dict[key], text)
        elif isinstance(site_dict[key], str) and '{0}' in site_dict[key]:
            site_dict[key] = site_dict[key].format(text)


sites = {}
sites_count = int(input('Сколько сайтов: '))
for i in range(sites_count):
    new_site = copy.deepcopy(site)
    product_name = input('Введите название продукта: ')
    get_value(new_site, product_name)
    sites_dict_key = f'Сайт для {product_name}'
    sites[sites_dict_key] = new_site

    for dict_key, value in sites.items():
        print(f'{dict_key}\n{value}')

