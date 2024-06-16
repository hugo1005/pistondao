import streamlit as st
import pandas as pd
import plotly.express as px
import base64

# Load your car data into a pandas dataframe (replace 'cars.csv' with your data path)
df = pd.read_csv('cars.csv')

# def render_svg(svg):
#     """Renders the given svg string."""
#     b64 = base64.b64encode(svg.encode('utf-8')).decode("utf-8")
#     html = r'<img src="data:image/svg+xml;base64,%s" alt="Car Price Analysis Dashboard" style="width: 275px;"/>' % b64
#     return html

# with open('logo.svg') as f:
#     svg = f.read()
#     logo_html = render_svg(svg)

# # Title 

# # Title with Markdown and logo
# st.markdown(f"# {logo_html}", unsafe_allow_html=True)
st.markdown(f"## Car Price Analysis Dashboard", unsafe_allow_html=True)

st.write("This dashboard allows you to explore car prices by Year, make, and model. Use the filters on the left to narrow down your search.")

# Sidebar for filters
st.sidebar.header("Filters")

# Year range filter
min_year, max_year = st.sidebar.slider("Year Range", df['Year'].min(), df['Year'].max(), (df['Year'].min(), df['Year'].max()))
filtered_df = df[(df['Year'] >= min_year) & (df['Year'] <= max_year)]

# Make filter (multiselect)
makes = list(df['Make'].unique())
selected_makes = st.sidebar.multiselect("Make", makes, default=makes)
filtered_df = filtered_df[filtered_df['Make'].isin(selected_makes)]

# Model filter (multiselect)
models = list(filtered_df['Model Family'].unique())
selected_models = st.sidebar.multiselect("Model Family", models, default=models)
filtered_df = filtered_df[filtered_df['Model Family'].isin(selected_models)]

# Scatter plot
fig = px.scatter(filtered_df, 
                 x="Year", y="Price_USD_Thousands", 
                 color="Make", title="Car Make Price by Year",  
                 labels={
                     "Price_USD_Thousands": "Price (USD, Thousands)",
                 },
                 color_discrete_sequence=px.colors.qualitative.Plotly)
st.plotly_chart(fig)

fig = px.scatter(filtered_df, 
                 x="Mileage", y="Price_USD_Thousands", 
                 color="Make", title="Car Make Price by Mileage",  
                 labels={
                     "Price_USD_Thousands": "Price (USD, Thousands)",
                 },
                 color_discrete_sequence=px.colors.qualitative.Plotly)
st.plotly_chart(fig)

fig = px.scatter(filtered_df, 
                 x="Year", y="Price_USD_Thousands", 
                 color="Model Family", title="Car Model Price by Year",  
                 labels={
                     "Price_USD_Thousands": "Price (USD, Thousands)",
                 },
                 color_discrete_sequence=px.colors.qualitative.Plotly)
st.plotly_chart(fig)

fig = px.scatter(filtered_df, x="Mileage", y="Price_USD_Thousands", 
                 color="Model Family", title="Car Model Price by Mileage",  
                 labels={
                     "Price_USD_Thousands": "Price (USD, Thousands)",
                 },
                 color_discrete_sequence=px.colors.qualitative.Plotly)

st.plotly_chart(fig)


# Additional information (e.g., number of cars displayed)
st.write(f"Number of Cars Displayed: {len(filtered_df)}")