import streamlit as st
st.set_page_config(layout="wide")
st.title("norges bank investment data analysis")
st.write(
    "Let's dig into the data to see where norges bank is investing and how much they are investing in different regions and industries."
)
import streamlit as st
import pandas as pd
import plotly.express as px
from norges_data._bank import df

region = st.sidebar.multiselect("select region", df['Region'].unique(), default=df['Region'].unique())
filtered_df = df[df['Region'].isin(region)]

col1, col2 = st.columns(2)

with col1:
    st.subheader("USD")
    fig_country = px.bar(filtered_df.groupby('Country')['Market Value(USD)'].sum().nlargest(15).reset_index(), 
                         x='Country', y='Market Value(USD)', color='Market Value(USD)')
    st.plotly_chart(fig_country, use_container_width=True)

with col2:
    st.subheader("industry distribution")
    fig_industry = px.pie(filtered_df, values='Market Value(USD)', names='Industry')
    st.plotly_chart(fig_industry, use_container_width=True)

st.subheader("investment details")
st.dataframe(filtered_df[['Name', 'Country', 'Industry', 'Market Value(USD)', 'Ownership']])
