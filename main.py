import random

from modul_add import add_matrices
from modul_mult import multiply_matrices
from modul_transpose import transpose_matrix


def create_matrix(rows, cols):
    """Создаёт матрицу rows x cols из случайных чисел от 1 до 9."""
    matrix = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(random.randint(1, 9))
        matrix.append(row)
    return matrix


def print_matrix(matrix):
    """Выводит матрицу построчно с выравниванием."""
    for row in matrix:
        for elem in row:
            print(str(elem).rjust(4), end="")
        print()
    print()


def read_size(prompt):
    """Запрашивает целое число больше нуля."""
    while True:
        try:
            value = int(input(prompt))
        except ValueError:
            print("Ошибка: нужно ввести целое число.")
            continue
        if value > 0:
            return value
        print("Ошибка: число должно быть больше нуля.")


def main():
    operation = input("Введите операцию (+, *, T): ").strip()

    if operation == "+":
        rows = read_size("Введите количество строк: ")
        cols = read_size("Введите количество столбцов: ")
        a = create_matrix(rows, cols)
        b = create_matrix(rows, cols)
        print("Матрица A:")
        print_matrix(a)
        print("Матрица B:")
        print_matrix(b)
        print("Результат:")
        print_matrix(add_matrices(a, b))
    elif operation == "*":
        rows_a = read_size("Введите строки A: ")
        cols_a = read_size("Введите столбцы A (= строки B): ")
        cols_b = read_size("Введите столбцы B: ")
        a = create_matrix(rows_a, cols_a)
        b = create_matrix(cols_a, cols_b)
        print("Матрица A:")
        print_matrix(a)
        print("Матрица B:")
        print_matrix(b)
        print("Результат:")
        print_matrix(multiply_matrices(a, b))
    elif operation in ("T", "t"):
        rows = read_size("Введите строки: ")
        cols = read_size("Введите столбцы: ")
        a = create_matrix(rows, cols)
        print("Матрица A:")
        print_matrix(a)
        print("Транспонированная:")
        print_matrix(transpose_matrix(a))
    else:
        print("Ошибка! Допустимые операции: +, *, T")


if __name__ == "__main__":
    main()
