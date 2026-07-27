import streamlit as st

def show_upwork_fields():
    st.write("### 📋 Fill the Job Details")
    job_desc = st.text_area("1. Job Link or Description:", placeholder="Paste the client's Upwork job post here...")
    user_skills = st.text_input("2. Your Skills & Experience:", placeholder="e.g., Python Developer, Web Designer...")
    proposed_budget = st.text_input("3. Proposed Budget ($):", placeholder="e.g., $150, $500...")
    
    if job_desc or user_skills or proposed_budget:
        st.session_state.template_text = f"Write a professional Upwork proposal.\nClient Job: {job_desc}\nMy Skills: {user_skills}\nBudget: {proposed_budget}"
    st.write("---")
