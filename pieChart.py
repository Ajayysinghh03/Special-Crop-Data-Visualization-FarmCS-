import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import matplotlib as plt
plt.use('TkAgg')

import seaborn as sns

# Load your data from the CSV file
df = pd.read_csv('df2013.csv')  # Replace 'yourfile.csv' with the actual file name

# Use a valid built-in color sequence
fig = px.pie(df, values='pct_production', names='State_Name', 
             title='Percentage Contribution of States to Agriculture',
             color_discrete_sequence=px.colors.qualitative.Pastel)  # Use Pastel from qualitative

# Update layout for a more beautiful look
fig.update_traces(textposition='inside', textinfo='percent+label')
fig.update_layout(showlegend=True)

# Display the pie chart
fig.show()
