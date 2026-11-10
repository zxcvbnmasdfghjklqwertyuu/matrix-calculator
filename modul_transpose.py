def transpose_matrix(matrix):
    """Транспонирует матрицу: строки становятся столбцами."""
    rows = len(matrix)
    cols = len(matrix[0])
    result = []
    for j in range(cols):
        row = []
        for i in range(rows):
            row.append(matrix[i][j])
        result.append(row)
    return result
