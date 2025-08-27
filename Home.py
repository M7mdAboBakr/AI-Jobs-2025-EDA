import pandas as pd
import streamlit as st
from streamlit_lottie import st_lottie
import requests

# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="AI Job Market Data",
    page_icon=":bar_chart:",
    layout="wide"
)

# ================== LOAD DATA ==================
df = pd.read_csv("ai_jobs_cleaned.csv")  # غير الاسم حسب ملفك

# ================== HELPER FUNCTION ==================
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# ================== HEADER ==================
st.markdown("""
# 🤖 Global AI Job Market & Salary Trends 2025  

Welcome to the **AI Job Market Dashboard**!  
This app provides an overview of a **synthetic dataset** designed to simulate global AI job market trends, salaries, and industry insights.  
Perfect for data science learners, career researchers, and analysts to explore and practice!  
""")

# ================== LOTTIE ANIMATIONS ==================

lottie_coding = load_lottieurl("https://lottie.host/0f0018a3-131f-4488-bb64-904c481a7d61/aTDeq7s1Yk.json")
st_lottie(lottie_coding, height=500, width=900)


# ================== ABOUT THE DATA ==================
st.markdown("""
## 📊 Dataset Overview  

- The dataset is **synthetic (not real-world)** — generated algorithmically to simulate job market dynamics.  
- It covers AI and ML job positions, salaries, company sizes, remote work trends, and required skills.  
- Great for **exploration, visualization, and career market research**.  

### 🔑 Key Features:
- **15,000 job listings** from **50+ countries** 🌍  
- **Salaries in multiple currencies** (normalized to USD 💵)  
- **Experience levels**: Entry, Mid, Senior, Executive 🧑‍💻  
- **Company size impact** on salary & job trends 🏢  
- **Remote work patterns** and geographic variations 🌐  
- **Skills demand analysis** across industries 🛠️  

📥 Data available on [**Kaggle**](https://www.kaggle.com/datasets/bismasajjad/global-ai-job-market-and-salary-trends-2025/data)
""")

# ================== SNAPSHOT OF DATA ==================
st.markdown("## 🗂️ Data Snapshot")
st.dataframe(df.head(10))

# ================== NEXT SECTIONS ==================
st.markdown("""
## 🔍 What You Can Explore Next  

### 💵 Salary Analysis 
- Discover how **company size** impacts salary levels  
- Compare **job titles** to see which roles are the most rewarding  
- Identify the **top-paying companies** in the AI market  
 
### 🌍 Geographic Analysis 
- Explore salary differences across **countries and regions**  
- See how **industries vary by location** in terms of compensation  
 
### 🧑‍💻 Job Requirements 
- Uncover the **most in-demand AI/ML skills** in the market  
- Analyze how **years of experience** shape monthly pay  
- Compare **experience levels** (Entry, Mid, Senior, Executive) to spot career growth patterns

---
👉 Use the sidebar to navigate to deeper **Analysis Pages**.
""")

