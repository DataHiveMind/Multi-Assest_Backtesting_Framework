from dataclasses import dataclass
import yfinance as yf
import pandas as pd
import os

@dataclass
class data_loading():
    start : str
    end : str
    ticker : str

    def load_and_save_data(file_path, save_path):
        # Create the 'data/raw' directory if it doesn't exist
        os.makedirs(save_path, exist_ok = True)

        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(file_path)

        # Save the DataFrame to the specified directory
        df.to_csv(os.path.join(save_path, 'AAPL.csv'), index=False)



    def stock_data(self):
        data = yf.download(self.ticker, start = self.start, end = self.end)
        return data
    def bond_data(self):
        data = yf.download(self.ticker, start = self.start, end = self.end)
        return data
    def crypto_data(self):
        data = yf.download(self.ticker, start = self.start, end = self.end)
        return data
    def forex_data(self):
        data = yf.download(self.ticker, start = self.start, end = self.end)
        return data
    def commodity_data(self):
        data = yf.download(self.ticker, start = self.start, end = self.end)
        return data
    


if __name__ is "__main__":
    pass