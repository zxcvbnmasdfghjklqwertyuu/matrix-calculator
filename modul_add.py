def add_matrices(a, b):
    """Складывает две матрицы одинакового размера и возвращает результат."""
    rows = len(a)
    cols = len(a[0])
    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(a[i][j] + b[i][j])
        result.append(row)
    return result
