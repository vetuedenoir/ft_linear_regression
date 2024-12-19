from load_csv import load
from ft_standard_deviation import ft_std
import numpy as np
import matplotlib.pyplot as plt


def normalize(data: list):
    return (data - data.mean()) / ft_std(data)


def denormalize_thetas(theta1, theta2, mean_x, std_x, mean_y, std_y):
    theta1_prime = std_y * theta1 - (std_y * theta2 * mean_x / std_x) + mean_y
    theta2_prime = std_y * theta2 / std_x
    return theta1_prime, theta2_prime


def print_graphe(km: list, price: list, t1, t2):
    plt.scatter(km, price)
    # plt.scatter(t1, t2, color="red")
    plt.ylabel("price")
    plt.xlabel("km")
    plt.title("Price estimation in fonction of km")
    plt.show()


def write_in_file(name: str, t1, t2):
    try:
        f = open(name, "w")
        f.write(f"theta1 = {t1}\n")
        f.write(f"theta2 = {t2}\n")
        f.close()
    except Exception as e:
        print("Error:", e)


def coef_determination(y: list, pred: list):
    u = ((y - pred) ** 2).sum()
    v = ((y - y.mean()) ** 2).sum()
    return 1 - (u / v)


def estimatePrice(mileage: int, theta1: float, theta2: float):
    return (theta1 + (theta2 * mileage))


def model_perf(km, price,  t1, t2):
    pred = [estimatePrice(x, t1, t2) for x in km]
    pred = np.array(pred)
    return coef_determination(price, pred)


def cost_function(x, y, theta1, theta2):
    m = len(x)
    total_cost = 0.0
    for i in range(m):
        prediction = estimatePrice(x[i], theta1, theta2)
        error = (prediction - y[i]) ** 2
        total_cost += error
    return total_cost / (2 * m)


def gradient1(x: list, y: list, theta1: float, theta2: float):
    res = 0

    for i in range(0, len(x)):
        res += (estimatePrice(x[i], theta1, theta2) - y[i])
    return res


def gradient2(x: list, y: list, theta1: float, theta2: float):
    res = 0

    for i in range(0, len(x)):
        res += ((estimatePrice(x[i], theta1, theta2) - y[i]) * x[i])
    return res


def gradient_descente(x: list, y: list, learning_rate: int, nb_iter: int):
    tmpT1 = 0.0
    tmpT2 = 0.0
    m = 1 / len(x)
    tmpCost1 = tmpCost2 = cost_function(x, y, tmpT1, tmpT2)

    for i in range(0, nb_iter):
        tmpT1 = tmpT1 - learning_rate * m * gradient1(x, y, tmpT1, tmpT2)
        tmpT2 = tmpT2 - learning_rate * m * gradient2(x, y, tmpT1, tmpT2)
        tmpCost1 = cost_function(x, y, tmpT1, tmpT2)
        if (tmpCost1 == tmpCost2):
            break
        tmpCost2 = tmpCost1
        # print(f"Pour i = {i} ", tmpCost1 * 100000)
    return tmpT1, tmpT2


def main():
    data = load("data.csv")
    if data is None:
        return
    try:
        km = data['km'].to_numpy(dtype=float)
        price = data['price'].to_numpy(dtype=float)
        km_normal = normalize(km)
        price_normal = normalize(price)
        theta1, theta2 = gradient_descente(km_normal, price_normal, 1, 200)
        theta1, theta2 = denormalize_thetas(theta1, theta2, km.mean(),
                                            ft_std(km), price.mean(), ft_std(price))
        print(f"theta1 = {theta1} et theta2 = {theta2}")
        write_in_file("theta.txt", theta1, theta2)
        print("model perf = ", model_perf(km, price, theta1, theta2))

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
