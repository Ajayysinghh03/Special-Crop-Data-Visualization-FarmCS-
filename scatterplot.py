import plotly.express as px
import pandas as pd
df = pd.read_csv('df2013.csv')
fig = px.scatter(df, x='Area', y='pct_production', color='Crop', title='Area vs Production for Different Crops')
fig.show()
