from utils.load_csv import load
from utils.ft_standard_deviation import ft_std
from utils.estimatePrice import estimatePrice
import sys
import matplotlib.pyplot as plt


def normalize(data: list):
    """
    Normalize a dataset by centering it around its mean and dividing by its standard deviation.

    Args:
        data (list): List or array of numerical data.

    Returns:
        list: The normalized data.
    """
    return (data - data.mean()) / ft_std(data)


def denormalize_thetas(theta0, theta1, mean_x, std_x, mean_y, std_y):
    """
    Denormalize the parameters (theta0, theta1) after gradient descent on normalized data.

    Args:
        theta0 (float): Normalized intercept.
        theta1 (float): Normalized slope.
        mean_x (float): Mean of the original x values.
        std_x (float): Standard deviation of the original x values.
        mean_y (float): Mean of the original y values.
        std_y (float): Standard deviation of the original y values.

    Returns:
        tuple: Denormalized theta0 and theta1.
    """
    theta0_prime = std_y * theta0 - (std_y * theta1 * mean_x / std_x) + mean_y
    theta1_prime = std_y * theta1 / std_x
    return theta0_prime, theta1_prime


def print_graphe(km: list, price: list, t1, t2):
    """
    Display a scatter plot of the data and a regression line.

    Args:
        km (list): List of kilometers driven.
        price (list): List of car prices.
        t1 (float): Intercept (theta0).
        t2 (float): Slope (theta1).

    Returns:
        None
    """
    p1 = estimatePrice(0, t1, t2)
    p2 = estimatePrice(250000, t1, t2)
    plt.scatter(km, price)
    plt.plot([0, 250000], [p1, p2], color="orange")
    plt.ylabel("price")
    plt.xlabel("km")
    plt.title("Price estimation in fonction of km")
    plt.show()


def write_in_file(name: str, t1, t2):
    """
    Write theta values into a file.

    Args:
        name (str): Name of the file.
        t1 (float): Intercept (theta0).
        t2 (float): Slope (theta1).

    Returns:
        None
    """
    try:
        with open(name, "w") as f:
            f.write(f"theta0 = {t1}\n")
            f.write(f"theta1 = {t2}\n")
    except Exception as e:
        print("Error:", e)


def coef_determination(y: list, pred: list):
    """
    Calculate the coefficient of determination (R²) to evaluate the model's accuracy.

    Args:
        y (list): Actual values.
        pred (list): Predicted values.

    Returns:
        float: R² value indicating the proportion of variance explained by the model.
    """
    u = ((y - pred) ** 2).sum()
    v = ((y - y.mean()) ** 2).sum()
    return 1 - (u / v)


def cost_function(x, y, theta0, theta1):
    """
    Compute the cost function for linear regression.

    Args:
        x (list): km.
        y (list): price.
        theta0 (float): Intercept.
        theta1 (float): Slope.

    Returns:
        float: Computed cost.
    """
    m = len(x)
    total_cost = 0.0
    for i in range(m):
        prediction = estimatePrice(x[i], theta0, theta1)
        error = (prediction - y[i]) ** 2
        total_cost += error
    return total_cost / (2 * m)


def gradient1(x: list, y: list, theta0: float, theta1: float):
    """
    Compute the partial derivative of the cost function with respect to theta0.

    Args:
        x (list): km.
        y (list): price.
        theta0 (float): Intercept.
        theta1 (float): Slope.

    Returns:
        float: Gradient with respect to theta0.
    """
    res = 0
    for i in range(len(x)):
        res += (estimatePrice(x[i], theta0, theta1) - y[i])
    return res


def gradient2(x: list, y: list, theta0: float, theta1: float):
    """
    Compute the partial derivative of the cost function with respect to theta1.

    Args:
        x (list): km.
        y (list): price.
        theta0 (float): Intercept.
        theta1 (float): Slope.

    Returns:
        float: Gradient with respect to theta1.
    """
    res = 0
    for i in range(len(x)):
        res += ((estimatePrice(x[i], theta0, theta1) - y[i]) * x[i])
    return res


def gradient_descente(x: list, y: list, learning_rate: int, nb_iter: int):
    """
    Perform gradient descent to minimize the cost function and find optimal parameters.

    Args:
        x (list): km.
        y (list): price.
        learning_rate (int): Learning rate for gradient descent.
        nb_iter (int): Maximum number of iterations.

    Returns:
        tuple: Optimized theta0 and theta1.
    """
    tmpt0 = 0.0
    tmpt1 = 0.0
    m = 1 / len(x)
    epsilon = 1e-11

    for i in range(nb_iter):
        prev_tmpt0 = tmpt0
        prev_tmpt1 = tmpt1
        tmpt0 = tmpt0 - learning_rate * m * gradient1(x, y, tmpt0, tmpt1)
        tmpt1 = tmpt1 - learning_rate * m * gradient2(x, y, tmpt0, tmpt1)
        # print(f"prev0 {prev_tmpt0} et ", f"t0 {tmpt0} and ", f"prev1 {prev_tmpt1} et ", f"t1 {tmpt1}")
        if i != 0 and abs(prev_tmpt0 - tmpt0) < epsilon and abs(prev_tmpt1 - tmpt1) < epsilon:
            break
    return tmpt0, tmpt1


def main():
    """
    Main function to load data, normalize features, perform gradient descent,
    denormalize the parameters, and optionally display a plot.

    Use option -g to display a graphe.
    """
    data = load("data.csv")
    if data is None:
        return
    try:
        km = data['km'].to_numpy(dtype=float)
        price = data['price'].to_numpy(dtype=float)
        km_normal = normalize(km)
        price_normal = normalize(price)
        theta0, theta1 = gradient_descente(km_normal, price_normal, 0.5, 200)
        theta0, theta1 = denormalize_thetas(theta0, theta1, km.mean(),
                                            ft_std(km), price.mean(), ft_std(price))
        print(f"theta0 = {theta0} et theta1 = {theta1}")
        write_in_file("theta.txt", theta0, theta1)
        if len(sys.argv) == 2:
            if sys.argv[1] == "-g":
                print_graphe(km, price, theta0, theta1)
            else:
                print("Error: only option -g supported")

    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
