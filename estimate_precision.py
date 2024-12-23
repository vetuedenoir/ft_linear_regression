from utils.load_csv import load
from utils.estimatePrice import estimatePrice
from utils.ft_read_in_file import read_in_file


def coef_determination(y: list, pred: list) -> float:
    """
    Computes the coefficient of determination (R²) for a given set of true values and predictions.

    Args:
        y (list): The actual values.
        pred (list): The predicted values.

    Returns:
        float: The R² score, indicating how well the predictions match the actual values.
    """
    u = ((y - pred) ** 2).sum()
    v = ((y - y.mean()) ** 2).sum()
    return 1 - (u / v)


def model_perf(km: list, price: list, t1: float, t2: float) -> float:
    """
    Evaluates the performance of a linear model by computing the R² score.

    Args:
        km (list): The list of distances (features) in kilometers.
        price (list): The list of corresponding prices (targets).
        t1 (float): The model parameter for the intercept (theta0).
        t2 (float): The model parameter for the slope (theta1).

    Returns:
        float: The R² score of the model's predictions.
    """
    pred = [estimatePrice(x, t1, t2) for x in km]
    return coef_determination(price, pred)


def main():
    """
    The main function to evaluate the model's performance.

    This function:
    - Loads data from a CSV file.
    - Extracts the 'km' and 'price' columns.
    - Reads model parameters (theta0 and theta1) from a file.
    - Computes and prints the model's performance using the R² score.
    """
    data = load("data.csv")
    if data is None:
        return
    try:
        km = data['km'].to_numpy(dtype=float)
        price = data['price'].to_numpy(dtype=float)
        theta0, theta1 = read_in_file("theta.txt")
        print("Model's performance = ", model_perf(km, price, theta0, theta1))
    except Exception as e:
        print("Error:", e)


if __name__ == "__main__":
    main()
