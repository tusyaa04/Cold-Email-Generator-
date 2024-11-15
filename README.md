Here's the README.md file code ready to paste:

# 📧 Cold Email Generator

*Cold Email Generator* is a Streamlit-based application that automates the creation of personalized and professional emails. It is designed for job applications, follow-ups, and professional networking, leveraging AI and ChromaDB to create highly relevant and engaging email drafts.

## Features

- *Dynamic Email Purposes*: Generate emails for:
  - Job Inquiries
  - Application Follow-ups
  - Professional Networking
- *Customizable Email Tone*: Choose from Formal, Casual, or Friendly tones for a personalized communication style.
- *Job Description Parsing*: Extracts structured job details from URLs for precise email generation (for Job Inquiry and Application Follow-up purposes).
- *Portfolio Integration*: Uses ChromaDB to match skills and projects from your portfolio to the email's purpose.
- *Networking Emails*: Generate professional networking emails without requiring a Job URL.

## Technologies Used

- *Python*: Core programming language.
- *Streamlit*: For an interactive user interface.
- *LangChain*: Manages the AI pipeline for text generation.
- *LLM (Large Language Models)*: Generates email content.
- *WebBaseLoader*: Parses content from job pages (for Job Inquiry and Application Follow-up).
- *ChromaDB*: Vector database for efficient portfolio queries.

## Prerequisites

Ensure the following are installed:

- *Python 3.8+*
- *pip* (Python package manager)
- *Streamlit*
- *LangChain*
- *ChromaDB*
- *dotenv*

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/cold-email-generator.git
   cd cold-email-generator

2. Install required dependencies:

pip install -r requirements.txt


3. Set up environment variables:

Create a .env file in the project directory.

Add your API key for the language model:

GROQ_API_KEY=your_groq_api_key




## Usage

1. Start the Streamlit app:

streamlit run mains.py


2. Open your browser and navigate to the local server URL (e.g., http://localhost:8501).


3. Provide the following inputs:

Profile Summary: A short summary of your skills and expertise for tailoring the email.

Email Tone: Choose from Formal, Casual, or Friendly.

Purpose of Email: Select one from:

Job Inquiry

Application Follow-up

Networking


Job URL (Required for Job Inquiry and Application Follow-up): The URL of the job posting.


4. For Networking, the Job URL is not required. Simply provide your Profile Summary and desired Email Tone, and the app will generate an email focused on professional connections, advice, or opportunities.


5. Click Generate Cold Email to get your personalized email.
![Screenshot (101)](https://github.com/user-attachments/assets/391dd2f6-54c0-4626-ad5c-9ae2687d7d90)
![Screenshot (110)](https://github.com/user-attachments/assets/16af1e6f-c9b9-40c1-9571-313b425dcaa2)

