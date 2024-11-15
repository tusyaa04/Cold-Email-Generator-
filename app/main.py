import streamlit as st
from langchain_community.document_loaders import WebBaseLoader
from chains import Chain
from portfolio import Portfolio
from utils import clean_text

# Initialize Portfolio and Chain instances
portfolio = Portfolio()
chain = Chain()

# Streamlit UI configuration
st.set_page_config(layout="wide", page_title="Cold Email Generator", page_icon="📧")

# App title
st.title("📧 Cold Email Generator")

# User Input Fields

profile_summary = st.text_area("Profile Summary (e.g., Full-stack developer with expertise in MERN stack)")
email_tone = st.selectbox("Email Tone", ["Formal", "Casual", "Friendly"])
email_purpose = st.selectbox("Purpose of Email", ["Job Inquiry", "Application Follow-up", "Networking"])

# URL input only if the purpose is not Networking
if email_purpose != "Networking":
    url_input = st.text_input("Enter a Job URL:", value="https://jobs.nike.com/job/R-43849?from=job%20search%20funnel")
submit_button = st.button("Generate Cold Email")

if submit_button:
    try:
        if email_purpose == "Networking":
            # Generate a Networking email without job URL
            email = chain.write_networking_email( profile_summary, email_tone)
            st.subheader("Generated Networking Email")
            st.code(email, language='markdown')
        else:
            # Load the web content if URL is provided
            loader = WebBaseLoader([url_input])
            data = clean_text(loader.load().pop().page_content)
            
            # Extract job details and generate email
            jobs = chain.extract_jobs(data)
            portfolio.load_portfolio()

            # Generate cold email for each job
            for job in jobs:
                skills = job.get('skills', [])
                links = portfolio.query_links(skills)
                email = chain.write_mail(job, links,profile_summary, email_tone, email_purpose)
                st.subheader(f"Cold Email for Job: {job.get('role')}")
                st.code(email, language='markdown')
                
    except Exception as e:
        st.error(f"An Error Occurred: {e}")
