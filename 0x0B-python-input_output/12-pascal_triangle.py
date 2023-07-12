def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    triangle.append([1])

    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            value = triangle[i-1][j-1] + triangle[i-1][j]
            row.append(value)
        row.append(1)
        triangle.append(row)

    return triangle
