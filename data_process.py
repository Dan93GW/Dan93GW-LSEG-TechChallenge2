import random

import numpy as np
import pandas as pd


def read_stock_data(file_path):
    try:
        data = pd.read_csv(file_path, header=None)
        data.columns = ['Stock-ID', 'Timestamp', 'Stock Price']
        return data
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def get_random_10_consecutive(data):
    total_points = len(data)
    if total_points < 10:
        return None
    start_index = random.randint(0, total_points - 10)
    return data.iloc[start_index:start_index + 10]

def predict_next_3(data_points):
    second_highest = sorted(data_points)[-2]
    n_plus_1 = second_highest
    n_plus_2 = data_points[-1] + (n_plus_1 - data_points[-1]) / 2
    n_plus_3 = n_plus_2 + (n_plus_1 - n_plus_2) / 4
    return [n_plus_1, n_plus_2, n_plus_3]

def process_file(file_path):
    data = read_stock_data(file_path)
    if data is None or len(data) < 10:
        print(f"Not enough data in {file_path}")
        return None
    stock_prices = get_random_10_consecutive(data)
    if stock_prices is None:
        print(f"Not enough consecutive data points in {file_path}")
        return None
    price_series = stock_prices['Stock Price'].values
    predicted_prices = predict_next_3(price_series)
    stock_id = stock_prices['Stock-ID'].iloc[0]
    timestamps = stock_prices['Timestamp'].values
    output = {
        "Stock-ID": [stock_id] * 13,
        "Timestamp": list(timestamps) + ['n+1', 'n+2', 'n+3'],
        "Stock Price": list(price_series) + predicted_prices
    }
    return pd.DataFrame(output)
