def sum_up_diagonals(matrix):
    """Given a matrix [square list of lists], return sum of diagonals.

    Sum of TL-to-BR diagonal along with BL-to-TR diagonal:

        >>> m1 = [
        ...     [1,   2],
        ...     [30, 40],
        ... ]
        >>> sum_up_diagonals(m1)
        73

        >>> m2 = [
        ...    [1, 2, 3],
        ...    [4, 5, 6],
        ...    [7, 8, 9],
        ... ]
        >>> sum_up_diagonals(m2)
        30
    """
    matrix_size = len(matrix)
    diagonal_tl_br = [matrix[i][i] for i in range(matrix_size)]
    diagonal_bl_tr = [matrix[i][matrix_size - i - 1] for i in range(matrix_size)]
    sum_list = diagonal_tl_br
    sum_list.extend(diagonal_bl_tr)
    return sum(sum_list)


