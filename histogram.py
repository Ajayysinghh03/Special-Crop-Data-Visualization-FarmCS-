import plotly.express as px
import pandas as pd
df=pd.read_csv("df2013.csv")
fig = px.histogram(df, x='Production', nbins=20, title='Distribution of Production')
fig.show()
