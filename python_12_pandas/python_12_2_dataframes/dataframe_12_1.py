import pandas as pd
data = {
    "Animal":["Lion","Tiger","Leopard","Jaguar","Cheetah","Black Panther","Puma","Snow Leopard"],
    "BiteForce" : [600,1000,600,1500,400,1500,450,600]
}
#load data into a DataFrame object:
df = pd.DataFrame(data)
print(df)

#refer to the row index:
print("row index...")
print(df.loc[0])
print(df.loc[[1,6]])

#index
print("index...")
print(pd.DataFrame(data, index=['a','b','c','d','e','f','g','h']))

#type
print(type(data))
print(type(df))

#info()
print("info()")
print(df.info())

#head()
print("head()")
print(df.head(0))
print(df.head(1))
print(df.head(4))
