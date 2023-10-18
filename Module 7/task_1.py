print('Задача 1. Ревью кода\n')

students = {
    1: {
        'name': 'Bob',
        'surname': 'Vazovski',
        'age': 23,
        'interests': ['biology, swimming']
    },
    2: {
        'name': 'Rob',
        'surname': 'Stepanov',
        'age': 24,
        'interests': ['math', 'computer games', 'running']
    },
    3: {
        'name': 'Alexander',
        'surname': 'Krug',
        'age': 22,
        'interests': ['languages', 'health food']
    }
}


def f(students_dict):
    all_interests = [hobby for pers_id in students_dict for hobby in students_dict[pers_id]['interests']]
    surnames = [students_dict[pers_id]['surname'] for pers_id in students_dict]
    surnames_str = ''.join(surnames)
    return set(all_interests), len(surnames_str)


pairs = []
for person_id, info in students.items():
    pairs.append((person_id, info['age']))

interests, surnames_length = f(students)
print(f'Список пар «ID студента — возраст»: {pairs}')
print(f'Полный список интересов всех студентов: {interests}')
print(f'Общая длина всех фамилий студентов: {surnames_length}')
