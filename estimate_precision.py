from load_csv import load
import numpy as np

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


def coef_determination(y: list, pred: list):
    u = ((y - pred) ** 2).sum()
    v = ((y - y.mean()) ** 2).sum()
    return 1 - (u / v)


def estimatePrice(mileage: int, theta1: float, theta2: float):
    return (theta1 + (theta2 * mileage))


def model_perf(km, price,  t1, t2):
    pred = [estimatePrice(x, t1, t2) for x in km]
    return coef_determination(price, pred)


def	main():
    data = load("data.csv")
    if data is None:
        return
    try:
        km = data['km'].to_numpy(dtype=float)
        price = data['price'].to_numpy(dtype=float)
        theta1, theta2 = read_in_file("theta.txt")
        print("model performance = ", model_perf(km, price, theta1, theta2))
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
	main()