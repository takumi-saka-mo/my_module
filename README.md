# my_module
```python
tickers = [
    "^N225",    # 日経平均株価
    "xxxx.T"    # 任意のティッカーコード
]

company_list = [
    "Nikkei",      # 日経225
    "xxxxcompany"  # 企業名を命名
]

start = dt.datetime(2015, 1, 1)
end = dt.datetime(2024, 1, 1)
```

```python
pip install my_finance
import beta
beta(tickers, company_list, start, end)
```

 ✔ OK! 

 開始：2015-01-01 00:00:00
 終了：2024-01-01 00:00:00

Zensho           β =   0.5758
MCD              β =   0.2147
Skylark          β =   0.4208
KURA             β =   0.6176
YOSHINOYA        β =   0.3886
Saizeriya        β =   0.6175
DOUTOR           β =   0.4930
TOWA             β =   0.4309
RoyalHost        β =   0.6204
GlobalDyning     β =   0.6722
