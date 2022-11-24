import pandas as pd
import numpy as np
a = [1,2,3,4,5]
name=["Sunil","abhisek","Harish","arti","Suman"]
df = pd.DataFrame(a,name)
print("Before Converting data into Html Table")
df.to_html("Table1.html")
html_file = df.to_html()
print("after converting the data into HTMl Table")
print(df)
