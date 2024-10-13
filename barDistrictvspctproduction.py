import plotly.express as px
import  pandas as pd
df=pd.read_csv("df2013.csv")
import plotly.express as px
# Sort by Production or Area, take the top N districts
top_districts = df.groupby('District_Name').sum().nlargest(20, 'Production').reset_index()
fig = px.bar(top_districts, x='Production', y='District_Name', orientation='h', title='Top 20 Districts by Production')
fig.show()

