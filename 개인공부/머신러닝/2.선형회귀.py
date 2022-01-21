import numpy as np


def prediction(theta_0, theta_1, x):
    return theta_0 + theta_1 * x


def prediction_difference(theta_0, theta_1, x, y):
    temp = prediction(theta_0, theta_1, x)
    return temp - y


def gradient_descent(theta_0, theta_1, x, y, iterations, alpha):
    for _ in range(iterations):
        error = prediction_difference(theta_0, theta_1, x, y)

        theta_0 = theta_0 - alpha * error.mean()
        theta_1 = theta_1 - alpha * (error * x).mean()
    return theta_0, theta_1


house_size = np.array([0.9, 1.4, 2, 2.1, 2.6, 3.3, 3.35,
                      3.9, 4.4, 4.7, 5.2, 5.75, 6.7, 6.9])


house_price = np.array([0.3, 0.75, 0.45, 1.1, 1.45, 0.9,
                       1.8, 0.9, 1.5, 2.2, 1.75, 2.3, 2.49, 2.6])

theta_0 = 2.5
theta_1 = 0

theta_0, theta_1 = gradient_descent(
    theta_0, theta_1, house_size, house_price, 200, 0.1)
print(theta_0, theta_1)
