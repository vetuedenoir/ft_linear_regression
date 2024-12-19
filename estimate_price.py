import sys
from load_csv import load
import matplotlib.pyplot as plt


def estimatePrice(mileage: int, theta1, theta2):
    return (theta1 + (theta2 * mileage))


def print_graphe(km: list, price: list, estimation, px, py):
    plt.scatter(km, price)
    plt.scatter(estimation[0], estimation[1], color="red")
    plt.plot(px, py, color="orange")
    plt.ylabel("price")
    plt.xlabel("km")
    plt.title("Price estimation in fonction of km")
    plt.show()


def graphique(mileage, estimate, theta1, theta2):
    data = load("data.csv")
    if data is None:
        exit(0)
    km = data['km'].to_numpy(dtype=float)
    price = data['price'].to_numpy(dtype=float)
    p1 = estimatePrice(0, theta1, theta2)
    p2 = estimatePrice(250000, theta1, theta2)
    print_graphe(km, price, [mileage, estimate], [0, 250000], [p1, p2])


def read_in_file(name: str):
    try:
        f = open("theta.txt", 'r')
        l1 = f.readline()
        l2 = f.readline()
        f.close()
        assert len(l1) != 0 or len(l2) != 0, \
            "Error: File theta.txt not complete"
        assert l1[:9] == "theta1 = " and l2[:9] == "theta2 = ", \
            "Error: theta not found in file theta.txt"
        theta1 = float(l1[9:])
        theta2 = float(l2[9:])
        return theta1, theta2
    except AssertionError as e:
        print(e)
        exit(1)
    except Exception as e:
        print("Error:", e)
        exit(1)


def main():
    try:
        mileage = float(input("enter a mileage to predict the price, \
                              please: "))
        assert mileage >= 0, "Error: only number over 0 accepted"
        theta1, theta2 = read_in_file("theta.txt")

        estimate = estimatePrice(mileage, theta1, theta2)
        if (estimate < 0):
            estimate = 0

        print(f"The price is estimate at {estimate} for {mileage} km")

        if len(sys.argv) == 2:
            if sys.argv[1] == "-g":
                graphique(mileage, estimate, theta1, theta2)

    except Exception as e:
        print("Error:", e)
        exit(1)
    except AssertionError as e:
        print(e)
        exit(1)


if __name__ == "__main__":
    main()
