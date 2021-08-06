import pandas as pd
import plotly.express as px

file_data = pd.read_csv('/Users/prathamarora/Downloads/Python_Projects/Data_Visualization/Copy+of+data+-+data.csv')

figure = px.scatter(file_data, x='date', y='cases', color='country')
figure.show()