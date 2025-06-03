import random

def divided_differences(x, y):
    n = len(x)
    coef = [0] * n
    coef[:] = y[:]
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            if x[i]!= x[i-j]:
                coef[i] = (coef[i] - coef[i - 1]) / (x[i] - x[i - j])
    return coef

def newton_polynomial(x_data, coef, x):
    n = len(coef)
    result = coef[0]
    for i in range(1, n):
        term = coef[i]
        for j in range(i):
            term *= (x - x_data[j])
        result += term
    return result

# داده‌ها

def generate_2D_datapoint(size,r1,r2):
    points = []
    for i in range(1,size):
        points.append(random.randint(r1,r2))
    return points
x_points = generate_2D_datapoint(1000, 1, 1000)
y_points = generate_2D_datapoint(1000, 1, 1000)
#print(x_points)
# محاسبه ضرایب
coefficients = divided_differences(x_points, y_points)

# تست: مقدار چندجمله‌ای در x = 3
x_test = 10
y_test = newton_polynomial(x_points, coefficients, x_test)

print("ضرایب چندجمله‌ای نیوتن:", coefficients)
print(f"مقدار چندجمله‌ای در x = {x_test}: {y_test}")