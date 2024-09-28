import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import yfinance as yf

def beta(tickers, company_list, start, end):
    """yfinanceを用いてデータを取得後、ベータ値を計算する関数"""
    df = yf.download(tickers, start=start, end=end)["Close"]
    print()

    # colors
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    
    
    if "^N225" in df.columns:
        df.rename(columns={"^N225": "Nikkei"}, inplace=True)
        print(f'{GREEN} ✔ OK! {RESET}')
        print()
        print(f" 開始：{start}\n 終了：{end}")
    else:
        error_message = f'{RED}Error : 日経平均株価(^N225)を"Nikkei"として各リストに入力してください.{RESET}'
        return error_message
    print()
    df = df.pct_change(fill_method=None).dropna()

    for i, ticker in enumerate(tickers[1:], 1): # company_list内を探索
        try:
            lr = LinearRegression()
            X = df[["Nikkei"]].values
            Y = df[[ticker]].values
            
            X1 = np.delete(X, 0, 0)
            Y1 = np.delete(Y, 0, 0)

            lr.fit(X1, Y1)
            beta_value = lr.coef_[0][0]
            
            print(f'{company_list[i]:<15}  β = {beta_value:>8.4f}')
        except Exception  as e:
            #print("Error : 詳細！ここ！")
            return




if __name__ == '__main__':
    tickers = []
    company_list = []
    start = ""
    end = ""
    beta(tickers, company_list, start, end)