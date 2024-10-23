import os

from data_process import process_file

BASE_PATH = './stock_price_data_files'

directories = {
    'LSE': f'{BASE_PATH}/LSE',
    'NASDAQ': f'{BASE_PATH}/NASDAQ',
    'NYSE': f'{BASE_PATH}/NYSE'
}

num_files_to_sample = 2

for exchange, dir_path in directories.items():
    files = os.listdir(dir_path)[:num_files_to_sample]
    for file_name in files:
        file_path = os.path.join(dir_path, file_name)
        result = process_file(file_path)
        if result is not None:
            output_file = f'{BASE_PATH}/predictions/{file_name}_predicted.csv'
            result.to_csv(output_file, index=False)
            print(f"Predictions saved to {output_file}")
