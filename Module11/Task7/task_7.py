from matrix import Matrix

m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
m1.print_matrix()

print("Матрица 2:")
m2.print_matrix()

print("Сложение матриц:")
matrix_summ = m1 + m2
matrix_summ.print_matrix()

print("Вычитание матриц:")
matrix_sub = m1 - m2
matrix_sub.print_matrix()

m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Умножение матриц:")
matrix_mul = m1 * m3
matrix_mul.print_matrix()

print("Транспонирование матрицы 1:")
transpose_matrix = m1.transpose_matrix()
transpose_matrix.print_matrix()

#Not valid Matrix
m4 = Matrix(1, 1)
m4.data = [[1, 2, 3]]
print('Невозможное умножение:')
not_valid_mul = m4 * m1
print('Невозможная сумма:')
not_valid_summ = m1 + m3