def matrix_dot_vector(a: list[list[int|float]],b:list[int|float]) -> list[int|float]:

    if len(a[0]) != len(b):
		return -1

	result = []

	for row in a:
		result.append(sum(x * y for x,y in zip(row, b)))

	return result		