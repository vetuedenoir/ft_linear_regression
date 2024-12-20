import pandas as pd


def load(path: str) -> pd.DataFrame:
    '''
Load a file .csv and return a pandas DataFrame.
    '''
    try:
        if ((path[-4:] != ".csv" or len(path) < 5)):
            print("Error: invalid format, only .csv accepted")
            return None
        data = pd.read_csv(path)
        return data
    except Exception as e:
        print("Error:", e)
    return None
