def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == "row":
        means = [sum(row) / len(row) for row in matrix]

    elif mode == "column":
        means = [
            sum(matrix[i][j] for i in range(len(matrix))) / len(matrix)
            for j in range(len(matrix[0]))
        ]

    return means