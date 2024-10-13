import plotly.express as px
import pandas as pd
df=pd.read_csv("df2013.csv")
fig = px.treemap(df, path=['State_Name', 'Crop'], values='pct_production', title='State and Crop Hierarchy by Production')
fig.show()
