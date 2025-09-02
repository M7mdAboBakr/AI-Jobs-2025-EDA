import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("ai_jobs_cleaned.csv")

st.set_page_config(
    page_title="Salary Analysis",
    page_icon="💵",
    layout="wide"
)

# --- Page Title ---

# --- Company Size vs Salary ---
st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>Average Monthly Salary by Company Size</h1>", unsafe_allow_html=True)
st.markdown("the salary is normalized to USD $ in all page charts")
fig1 = px.bar(
    df.groupby('company_size')['monthly_salary'].mean().reset_index(),
    x='company_size',
    y='monthly_salary',
    title='',
    color='company_size',
    template='simple_white',
    labels={'company_size': 'Company Size', 'monthly_salary': 'Avg Monthly Salary'})
fig1.update_traces(marker_line_color='white', marker_line_width=1, showlegend=False)
st.plotly_chart(fig1, use_container_width=True)
st.divider()

# --- Job Title vs Salary ---
st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>Average Monthly Salary by Job Title</h1>", unsafe_allow_html=True)
fig2 = px.bar(
    df.groupby('job_title')['monthly_salary'].mean().reset_index().sort_values(by='monthly_salary'),
    x='job_title',
    y='monthly_salary',
    title='',
    color='job_title',
    template='simple_white',
    labels={'job_title': 'Job Title', 'monthly_salary': 'Avg Monthly Salary'}
)
fig2.update_traces(marker_line_color='white', marker_line_width=1, showlegend=False)
st.plotly_chart(fig2, use_container_width=True)
st.divider()

# --- Company Name vs Salary ---
st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>Average Monthly Salary by Company Name</h1>", unsafe_allow_html=True)
fig3 = px.bar(
    df.groupby('company_name')['monthly_salary'].mean().reset_index().sort_values('monthly_salary', ascending=False),
    x='company_name',
    y='monthly_salary',
    title='',
    color='company_name',
    template='simple_white',
    labels={'company_name': 'Company Name', 'monthly_salary': 'Avg Monthly Salary'}
)
fig3.update_traces(marker_line_color='white', marker_line_width=1, showlegend=False)
st.plotly_chart(fig3, use_container_width=True)
st.divider()

# --- Job Title Info ---
st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>Job Title Info.</h1>", unsafe_allow_html=True)

job = st.selectbox("Select Job Title", df['job_title'].unique(), index=17)

col1, col2 = st.columns(2)

con1 = col1.container(border=True)
con1.metric(label="Avg Monthly Salary", value=round(df[df['job_title'] == job]['monthly_salary'].mean(), 2))

con2 = col2.container(border=True)
con2.metric(label="Avg Annual Salary", value=round(df[df['job_title'] == job]['monthly_salary'].mean() * 12, 2))
color_map = {
    "Entry": "#5DADE2",
    "Mid": "#27AE60", 
    "Senior": "#E67E22",
    "Executive": "#8E44AD"
}
fig4 = px.bar(
    df[df['job_title'] == job].experience_level.value_counts().reset_index(),
    color='experience_level',
    x='experience_level',
    y='count',
    template='simple_white',
    labels={'experience_level': 'Experience Level', 'count': '# of Jobs'},
    color_discrete_map=color_map,
    title='Top Experience Level'
)
fig4.update_traces(marker_line_color='white', marker_line_width=1, showlegend=False)
col1.plotly_chart(fig4, use_container_width=True)

color_map_employment = {
    "Full Time": "#2874A6",
    "Part Time": "#1ABC9C",
    "Freelance": "#E67E22",
    "Contract": "#6C3483"
}

fig5 = px.bar( 
    df[df['job_title'] == job].employment_type.value_counts().reset_index(), 
    x='employment_type', 
    y='count', 
    template='simple_white', 
    labels={'employment_type': 'Employment Type', 'count': '# of Jobs'}, 
    color='employment_type',
    color_discrete_map=color_map_employment,
    title='Top Employment Type'
) 

fig5.update_traces(marker_line_color='white', marker_line_width=1, showlegend=False) 
col2.plotly_chart(fig5, use_container_width=True)



