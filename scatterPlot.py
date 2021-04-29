import pandas as pd
import plotly.express as px

df = pd.read_csv("C:/Users/sravy/White Hat Jr/C 103- Data Visualization/csv files/data.csv")
fig = px.scatter(df, x="Population", y="Per capita",
	          size="Percentage",color="Country",
                   size_max=60)
fig.show()