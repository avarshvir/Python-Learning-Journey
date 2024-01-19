import pandas as pd
countries_covid_data = pd.read_csv("../python_datasets/countries-aggregated.csv")
print(countries_covid_data.head())
print(countries_covid_data.tail())
print(countries_covid_data.info())

countries_covid_data["Date"] = pd.to_datetime(countries_covid_data["Date"])
print(countries_covid_data)
print(countries_covid_data["Date"].nunique())
print(countries_covid_data["Country"].nunique())

#loc
print(countries_covid_data.loc[160000])
print(countries_covid_data.set_index("Country").loc["India"])

#query
ccd = countries_covid_data.query("(Country == 'India') & (Date == '2021-01-01')")
print(ccd)

#mask
mask = (countries_covid_data["Country"] == "India") & (countries_covid_data["Date"] == "2021-02-01")
print(countries_covid_data[mask])

