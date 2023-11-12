class Matrix:
    def __init__(self, rows_count, columns_count, data: list[list[int]] = None):
        self.rows_count = rows_count
        self.columns_count = columns_count
        self.data = data

    def valid_add_and_sub(self, other):
        if (isinstance(other, Matrix)
                and self.columns_count == other.columns_count and self.rows_count == other.rows_count):
            return True
        else:
            print('not valid matrix\n')
            return False

    def valid_mul(self, other):
        if isinstance(other, Matrix) and self.rows_count == other.columns_count:
            return True
        else:
            print('not valid Matrix\n')
            return False

    def __add__(self, other):
        if self.valid_add_and_sub(other):
            return Matrix(self.rows_count, self.columns_count,
                          [[self.data[row_num][column_num] + other.data[row_num][column_num]
                            for column_num in range(self.columns_count)] for row_num in range(self.rows_count)])

    def __sub__(self, other):
        if self.valid_add_and_sub(other):
            return Matrix(self.rows_count, self.columns_count,
                          [[self.data[row_num][column_num] - other.data[row_num][column_num]
                            for column_num in range(self.columns_count)] for row_num in range(self.rows_count)])

    def __mul__(self, other):
        if self.valid_mul(other):
            return Matrix(self.rows_count, other.columns_count,
                          [[sum(self.data[first_m_row][swap_index] * other.data[swap_index][second_m_col]
                                for swap_index in range(self.columns_count))
                            for second_m_col in range(other.columns_count)] for first_m_row in range(self.rows_count)])

    def transpose_matrix(self):
        return Matrix(self.columns_count, self.rows_count,
                      [[self.data[row_num][column_num]
                        for row_num in range(self.rows_count)] for column_num in range(self.columns_count)])

    def print_matrix(self):
        for row_num in range(self.rows_count):
            for column_num in range(self.columns_count):
                print(self.data[row_num][column_num], end="\t")
            print()
        print()