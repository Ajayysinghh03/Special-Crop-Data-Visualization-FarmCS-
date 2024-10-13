import plotly.express as px
import pandas as pd
df=pd.read_csv("df2013.csv")
pivot_table = df.pivot_table(values='pct_production', index='State_Name', columns='Crop', aggfunc='sum')
fig = px.imshow(pivot_table, labels=dict(x="Crop", y="State", color="Production"), title="State vs Crop Production")
fig.show()
