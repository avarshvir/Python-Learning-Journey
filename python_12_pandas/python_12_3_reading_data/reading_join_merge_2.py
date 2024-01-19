import pandas as pd

# Load the first CSV file
countries_covid_split1 = pd.read_csv("../python_datasets/countries-aggregated-split1.csv")
#print(countries_covid_split1)

# Load the second CSV file
countries_covid_split2 = pd.read_csv("../python_datasets/countries-aggregated-split2.csv")
print(countries_covid_split2)

# Merge with the second CSV file
countries_covid_merged = countries_covid_split1.merge(countries_covid_split2, how="left")
print(countries_covid_merged)

countries_covid_merged2 = countries_covid_split1.merge(countries_covid_split2, how="right")
print(countries_covid_merged2)

countries_covid_merged3 = countries_covid_split1.merge(countries_covid_split2, on="Recovered")
print(countries_covid_merged3)

