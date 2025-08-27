import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("ai_jobs_cleaned.csv")

st.set_page_config(
    page_title="Geographical Analysis",
    page_icon="🌍",
    layout="wide"
)

# --- Company Location vs Salary ---
st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>Average Monthly Salary by Company Location</h1>", unsafe_allow_html=True)
st.markdown("the salary is normalized to USD $ in all page charts")

fig2 = px.bar(
    df.groupby('company_location')['monthly_salary'].mean().reset_index().sort_values('monthly_salary', ascending=False),
    x='company_location',
    y='monthly_salary',
    title='',
    color='company_location',
    template='simple_white',
    labels={'company_location': 'Company Location', 'monthly_salary': 'Avg Monthly Salary'}
)
fig2.update_traces(marker_line_color='white', marker_line_width=1, showlegend=False)
st.plotly_chart(fig2, use_container_width=True)
st.divider()

# --- Industry and Company Location vs Salary ---
st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>Average Monthly Salary by Industry and Company Location</h1>", unsafe_allow_html=True)
st.dataframe(pd.pivot_table(df, columns='company_location', index='industry', values='monthly_salary', aggfunc='mean').style.format('{:.2f}').background_gradient(cmap='Blues'))
