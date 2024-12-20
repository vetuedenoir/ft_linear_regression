def ft_std(nbs: list[float | int]):
    """
Calculate the standard deviation of a list of numbers.

    Args:
        numbers (List[float | int]): A list of float or integer numbers.

    return:
        float: The standart deviation
    """

    if len(nbs) == 0:
        return print("ERROR")
    mean = sum(nbs) / len(nbs)
    ecart = [x - mean for x in nbs]
    ecart = [x * x for x in ecart]
    std = (sum(ecart) / len(nbs)) ** 0.5
    return std
