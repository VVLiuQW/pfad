import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


url = "https://data.weather.gov.hk/weatherAPI/cis/csvfile/HKA/2024/daily_HKA_RH_2024.csv"
response = requests.get(url)

if response.ok:
    print("Data is OK")
    content = response.content.decode('utf-8')

    lines = content.splitlines()
    data = []

    for line in lines[1:]:  
        parts = line.split(',')
        if len(parts) >= 4:  
            try:
                year = parts[0]
                month = parts[1]
                day = parts[2]
                value = float(parts[3])  
                data.append([year, month, day, value])
            except ValueError:
                continue  

    df = pd.DataFrame(data, columns=['Year', 'Month', 'Day', 'Value'])
    
    df['Date'] = pd.to_datetime(df[['Year', 'Month', 'Day']])
    
    sns.set_theme(style="darkgrid")
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='Date', y='Value')
    plt.title('Mean Relative Humidity (%) - Hong Kong ')
    plt.xlabel('Date')
    plt.ylabel('Value')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

else:
    print(response.status_code)
