import streamlit as st

# 1. Set the page configuration
st.set_page_config(
    page_title="Control Tower Dashboard",
    page_icon="🗼",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 2. Main Header & Description
st.title("🗼 Control Tower")
st.markdown("Welcome to the central command hub. Select a dashboard below to navigate to its specific metrics and reports.")

st.divider()

# 3. Create a clean 3-column layout
col1, col2, col3 = st.columns(3)

# Dashboard 1: Weekly Review
with col1:
    st.subheader("📊 Weekly Review")
    st.write("Track week-over-week performance, operational metrics, and routine reporting.")
    st.write("") # Spacer
    st.link_button(
        "Open Weekly Review ↗", 
        "https://weekly-review-dashboard.streamlit.app/", 
        use_container_width=True
    )

# Dashboard 2: Funnel Dashboard
with col2:
    st.subheader("🌪️ Funnel Dashboard")
    st.write("Analyze conversion rates, user journeys, and identify drop-offs.")
    st.write("") # Spacer
    st.link_button(
        "Open Funnel Dashboard ↗", 
        "https://ft-dash-ncqkpgmvddhs5f62awaffh.streamlit.app/", 
        use_container_width=True
    )

# Dashboard 3: Trust and Quality
with col3:
    st.subheader("🛡️ Trust & Quality")
    st.write("Monitor system integrity, quality assurance metrics, and safety standards.")
    st.write("") # Spacer
    st.link_button(
        "Open Trust & Quality ↗", 
        "https://tnq-dashboard-4njskh5grnuoukkdlseppi.streamlit.app/", 
        use_container_width=True
    )

# Optional: Add a footer
st.markdown("---")
st.caption("Maintained by [Your Name/Team] • Control Tower v1.0")
