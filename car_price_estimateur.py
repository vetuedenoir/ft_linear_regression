import sys
from utils.load_csv import load
from utils.ft_read_in_file import read_in_file
from utils.estimatePrice import estimatePrice
import matplotlib.pyplot as plt


def print_graphe(km: list, price: list, estimation, px, py):
    """
    Display a scatter plot of data points, a specific estimation point, and a regression line.

    Args:
        km (list): List of kilometers driven.
        price (list): List of car prices.
        estimation (list): A list containing the mileage and estimated price [mileage, price].
        px (list): List of x-coordinates for the regression line.
        py (list): List of y-coordinates for the regression line.

    Returns:
        None
    """
    plt.scatter(km, price)
    plt.scatter(estimation[0], estimation[1], color="red")
    plt.plot(px, py, color="orange")
    plt.ylabel("price")
    plt.xlabel("km")
    plt.title("Price estimation in fonction of mileage")
    plt.show()


def graphique(mileage, estimate, theta0, theta1):
    """
    Load data and plot a graph with the regression line, data points, and the specific estimation.

    Args:
        mileage (float): Mileage for which the price is estimated.
        estimate (float): Estimated price for the given mileage.
        theta0 (float): Intercept (theta0).
        theta1 (float): Slope (theta1).

    Returns:
        None
    """
    data = load("data.csv")
    if data is None:
        exit(0)
    km = data['km'].to_numpy(dtype=float)
    price = data['price'].to_numpy(dtype=float)
    p1 = estimatePrice(0, theta0, theta1)
    p2 = estimatePrice(250000, theta0, theta1)
    print_graphe(km, price, [mileage, estimate], [0, 250000], [p1, p2])


def main():
    """
    Main function to estimate car price based on mileage, using precomputed parameters.

    Prompts the user for a mileage input, reads parameters from a file, estimates the price,
    and optionally displays a graph.
    Use option -g to display a graphe.
    """
    try:
        mileage = float(input("Enter a mileage to predict the price, please: "))
        assert mileage >= 0, "Only numbers greater than or equal to 0 are accepted"
        theta0, theta1 = read_in_file("theta.txt")

        estimate = estimatePrice(mileage, theta0, theta1)
        if estimate < 0:
            estimate = 0

        print(f"The price is estimated at {estimate} for {mileage} km")

        if len(sys.argv) == 2:
            if sys.argv[1] == "-g":
                graphique(mileage, estimate, theta0, theta1)
            else:
                print("Error: only option -g supported")

    except Exception as e:
        print("Error:", e)
        exit(1)
    except AssertionError as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    main()
