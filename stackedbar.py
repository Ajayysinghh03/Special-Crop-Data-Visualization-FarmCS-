import plotly.express as px
import pandas as pd
df = pd.read_csv('df2013.csv')
fig = px.bar(df, x='Crop', y='Production', color='Season', title='Season-wise Production for Each Crop')
fig.show()
