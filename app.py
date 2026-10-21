import streamlit as st

# Page Configuration
st.set_page_config(page_title="Veeramanikandan P | ML Engineer", page_icon="🚀", layout="wide")

# Custom CSS for clean UI
st.markdown("""
    <style>
    .main {background-color: #0E1117;}
    h1, h2, h3 {color: #4CAF50;}
    .stButton>button {background-color: #4CAF50; color: white;}
    </style>
    """, unsafe_allow_html=True)

# Hero Section
col1, col2 = st.columns([3, 1])
with col1:
    st.title("Veeramanikandan P")
    st.subheader("Generative AI & Machine Learning Engineer")
    st.write("📍 Sivaganga, Tamil Nadu | 🎓 B.Tech AI & Data Science (Expected 2027)")
    st.write("Aspiring Machine Learning Engineer specializing in building end-to-end ML applications, agentic workflows, and deploying models.")
    
with col2:
    st.markdown("[LinkedIn](https://linkedin.com/in/mr-veeramanikandan-16v07p)")
    st.markdown("[GitHub](https://github.com/VEERA16-16k)")
    st.markdown("[Kaggle](https://kaggle.com/veeramanikandan1)")
    st.markdown("[Email](mailto:veeramanikandanpandidurai@gmail.com)")

st.divider()

# Skills Section
st.header("🛠️ Technical Skills")
sk_col1, sk_col2, sk_col3 = st.columns(3)
with sk_col1:
    st.markdown("**Machine & Deep Learning**")
    st.write("- Scikit-learn, XGBoost, PyTorch\n- CNNs (EfficientNet)\n- Feature Engineering & EDA")
with sk_col2:
    st.markdown("**Generative AI & Tools**")
    st.write("- LLM APIs (Groq), Pydantic\n- Agent Workflows\n- Git, GCP, VS Code")
with sk_col3:
    st.markdown("**Programming & Deployment**")
    st.write("- Python, SQL, C/C++\n- Streamlit, Flask\n- Pandas, NumPy")

st.divider()

# Projects Section
st.header("🚀 Featured Projects")

proj1, proj2 = st.columns(2)

with proj1:
    st.subheader("Top 2% - Spaceship Titanic (Kaggle)")
    st.write("Achieved a 0.8027 leaderboard score by building an optimized classification pipeline.")
    st.write("**Tech:** Python, Scikit-learn, XGBoost, Feature Engineering")
    st.markdown("[View Notebook/Repo](#)") # Replace # with actual link

    st.subheader("AI Social Publishing Agent")
    st.write("Built an AI-driven content pipeline using LLMs for automated enrichment and multi-platform publishing.")
    st.write("**Tech:** Groq APIs, Pydantic, Streamlit, SQLite")
    st.markdown("[View Repository](#)")

with proj2:
    st.subheader("Top 7% - BirdCLEF 2026 (Kaggle)")
    st.write("Developed an EfficientNet CNN pipeline to classify recordings across 185 bird species using spectrogram-based feature extraction.")
    st.write("**Tech:** PyTorch, CNNs, Audio Preprocessing")
    st.markdown("[View Notebook/Repo](#)")

    st.subheader("Customer Churn Prediction App")
    st.write("Analyzed customer behavior, trained a supervised classification model, and deployed an interactive web app for real-time predictions.")
    st.write("**Tech:** Pandas, Scikit-learn, Streamlit")
    st.markdown("[View App/Repo](#)")

st.divider()

# Experience & Education
st.header("💼 Experience & Education")
exp_col1, exp_col2 = st.columns(2)
with exp_col1:
    st.markdown("**Project Intern - Social Publishing Agent**")
    st.write("*RGreen Technologies | Jul 2026 - Aug 2026*")
    st.write("- Supported Python-based application integration and AI-agent workflow development.")
    
    st.markdown("**Machine Learning Intern**")
    st.write("*The Mind IT | Jul 2025*")
    st.write("- Worked on supervised/unsupervised learning, utilizing Pandas and Scikit-learn.")
    
with exp_col2:
    st.markdown("**B.Tech Artificial Intelligence and Data Science**")
    st.write("*PGP College of Engineering and Technology | 2023 - 2027*")
    
st.write("---")
st.write("Built with ❤️ using Streamlit. [View source code on GitHub](#).")