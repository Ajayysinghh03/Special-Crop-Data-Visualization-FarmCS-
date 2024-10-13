import plotly.express as px
import pandas as pd
df=pd.read_csv("df2013.csv")
fig = px.sunburst(df, path=['State_Name', 'Season', 'Crop'], values='pct_production', title='Production Breakdown by State, Season, and Crop')
fig.show()

