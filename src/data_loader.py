import pandas as pd

def load_data(file_path="data/sample_options_data.csv"):
    """
    Load options data.
    Columns: date, ticker, strike, expiry, type, price, underlying
    """
    df = pd.read_csv(file_path, parse_dates=['date', 'expiry'])
    df.dropna(inplace=True)
    return df
