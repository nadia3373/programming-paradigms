from math import sqrt

def mean(data):
    return sum(data) / len(data)

def pearson_correlation(x, y):
    n = len(x)

    mean_x, mean_y = mean(x), mean(y)

    numerator = sum((xi - mean_x) * (yi - mean_y) for xi, yi in zip(x, y))
    denominator = sqrt(sum((xi - mean_x)**2 for xi in x) * sum((yi - mean_y)**2 for yi in y))

    if denominator == 0:
        return 0

    correlation = numerator / denominator

    return correlation

array1 = [1, 2, 3, 4, 5]
array2 = [2, 3, 4, 5, 6]

result = pearson_correlation(array1, array2)
print(f'Корреляция Пирсона: {result}')
