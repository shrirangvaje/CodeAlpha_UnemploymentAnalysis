import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data = pd.read_csv("Unemployment in India.csv")

data.columns = data.columns.str.strip()


data['Date'] = pd.to_datetime(data['Date'])


print(data.head())
print(data.info())


print(data.isnull().sum())


data.dropna(inplace=True)

plt.figure(figsize=(10,5))
plt.plot(data['Date'], data['Estimated Unemployment Rate (%)'], marker='o')
plt.title("Unemployment Rate Over Time in India")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


covid_data = data[data['Date'] >= '2020-03-01']

plt.figure(figsize=(10,5))
plt.plot(covid_data['Date'], covid_data['Estimated Unemployment Rate (%)'], color='red')
plt.title("Impact of COVID-19 on Unemployment Rate")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
