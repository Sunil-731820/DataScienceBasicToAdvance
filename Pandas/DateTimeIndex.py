from tracemalloc import start
import pandas as pd
sr = pd.Series(["New york","Chocago","Toronto","Lisbon","Rio","Moscow"])
didx = pd.DatetimeIndex(start="2014-08-01 10:00",freq="W",periods=6,tz="Europe/Berlin")
sr.index = didx
print("The Series is ")
print(sr)

