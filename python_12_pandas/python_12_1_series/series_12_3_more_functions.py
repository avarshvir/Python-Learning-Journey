import pandas as pd
data = pd.Series(['a','b','c','d'], index = [1,2,3,4])
data2 = pd.Series(['a','b','e','d'], index = [1,2,5,4])
print(data+data2)