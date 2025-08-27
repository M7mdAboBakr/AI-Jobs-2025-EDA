import pandas as pd
import streamlit as st
import plotly.express as px

df = pd.read_csv("ai_jobs_cleaned.csv")

st.set_page_config(
    page_title="Job Requirements Analysis",
    page_icon="🧑‍💻",
    layout="wide"
)

# --- Top Needed Skills --- 
st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>Top Needed Skills</h1>", unsafe_allow_html=True)
skill_dict = {}
for skill in df.drop(['job_title', 'experience_level', 'employment_type',
       'company_location', 'company_size', 'education_required',
       'years_experience', 'industry', 'company_name', 'monthly_salary',
       'remote_state',], axis=1).columns:
    skill_dict[skill] = df[skill].sum()

skill_df = pd.DataFrame(skill_dict.items(), columns=['skill', 'count'])

fig = px.line(skill_df.sort_values('count', ascending=False),
              x='skill', y='count',
              template='simple_white', markers=True,
              labels={'skill': 'Skill', 'count': '# of Jobs'})
st.plotly_chart(fig, use_container_width=True)

# --- Job Title Count ---
st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>Number of Jobs by Job Title</h1>", unsafe_allow_html=True)
fig = px.bar(
    df['job_title'].value_counts().reset_index(),
    x='job_title',
    y='count',
    template='simple_white',
    labels={'job_title': 'Job Title', 'count': '# of Jobs'},
    color='job_title'
)
fig.update_traces(marker_line_color='white', marker_line_width=1, showlegend=False)
st.plotly_chart(fig, use_container_width=True)
st.divider()

# --- Remote State vs Salary ---
st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>Average Monthly Salary by Remote State</h1>", unsafe_allow_html=True)
st.markdown("the salary is normalized to USD $ in all page charts")

fig = px.bar(
    df.groupby('remote_state')['monthly_salary'].mean().reset_index(),
    x='remote_state',
    y='monthly_salary',
    color='remote_state',
    template='simple_white',
    labels={'remote_state': 'Remote State', 'monthly_salary': 'Avg Monthly Salary'}
)
fig.update_traces(marker_line_color='white', marker_line_width=1, showlegend=False)
st.plotly_chart(fig, use_container_width=True)
st.divider()

# --- Experience Level vs Salary ---
st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>Average Monthly Salary by Experience Level</h1>", unsafe_allow_html=True)
fig = px.bar(
    df.groupby('experience_level')['monthly_salary'].mean().reset_index().sort_values('monthly_salary', ascending=False),
    x='experience_level',
    y='monthly_salary',
    color='experience_level',
    template='simple_white',
    labels={'experience_level': 'Experience Level', 'monthly_salary': 'Avg Monthly Salary'}
)
fig.update_traces(marker_line_color='white', marker_line_width=1, showlegend=False)
st.plotly_chart(fig, use_container_width=True)
st.divider()

# --- Years of Experience vs Salary ---
st.markdown("<h1 style='text-align: center; color: #ad79b5; font-size: 50px; font-weight: bold;'>Average Monthly Salary by Years of Experience</h1>", unsafe_allow_html=True)
fig = px.line(df.groupby('years_experience')['monthly_salary'].mean().reset_index(),
              x='years_experience', y='monthly_salary',
              template='simple_white', markers=True,
              labels={'years_experience': 'Years of Experience', 'monthly_salary': 'Avg Monthly Salary'})
st.plotly_chart(fig, use_container_width=True)