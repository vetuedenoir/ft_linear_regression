def estimatePrice(mileage: int, theta0: float, theta1: float) -> float:
    """
    Estimates the price of an item (e.g., a car) based on its mileage and precomputed parameters.

    Args:
        mileage (int): The mileage of the item for which the price is to be estimated.
        theta0 (float): The intercept (baseline price) of the linear regression model.
        theta1 (float): The slope (rate of price decrease or increase per unit of mileage) of the model.

    Returns:
        float: The estimated price calculated using the formula: theta0 + (theta1 * mileage).
    """
    return (theta0 + (theta1 * mileage))
