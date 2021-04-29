import pandas as pd

import plotly.express as px

#reading data from csv files
df = pd.read_csv("C:/Users/sravy/White Hat Jr/C 103- Data Visualization/csv files/data.csv")
fig = px.bar(df, x='Country', y='InternetUsers')
fig.show()