from utils.load_csv import load
from utils.estimatePrice import estimatePrice
from utils.ft_read_in_file import read_in_file


def coef_determination(y: list, pred: list):
    u = ((y - pred) ** 2).sum()
    v = ((y - y.mean()) ** 2).sum()
    return 1 - (u / v)


def model_perf(km, price,  t1, t2):
    pred = [estimatePrice(x, t1, t2) for x in km]
    return coef_determination(price, pred)


def main():
    data = load("data.csv")
    if data is None:
        return
    try:
        km = data['km'].to_numpy(dtype=float)
        price = data['price'].to_numpy(dtype=float)
        theta0, theta1 = read_in_file("theta.txt")
        print("model performance = ", model_perf(km, price, theta0, theta1))
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
