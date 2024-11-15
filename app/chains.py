import os
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.exceptions import OutputParserException
from dotenv import load_dotenv

load_dotenv()

class Chain:
    def __init__(self):
        self.llm = ChatGroq(temperature=0, groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.1-70b-versatile")

    def extract_jobs(self, cleaned_text):
        prompt_extract = PromptTemplate.from_template(
            """
            ### SCRAPED TEXT FROM WEBSITE:
            {page_data}
            ### INSTRUCTION:
            The scraped text is from the career's page of a website.
            Your job is to extract the job postings and return them in JSON format containing the following keys: `role`, `experience`, `skills` and `description`.
            Only return the valid JSON.
            ### VALID JSON (NO PREAMBLE):
            """
        )
        chain_extract = prompt_extract | self.llm
        res = chain_extract.invoke(input={"page_data": cleaned_text})
        try:
            json_parser = JsonOutputParser()
            res = json_parser.parse(res.content)
        except OutputParserException:
            raise OutputParserException("Context too big. Unable to parse jobs.")
        return res if isinstance(res, list) else [res]

    def write_mail(self, job, links, profile_summary, email_tone, email_purpose):
        prompt_email = PromptTemplate.from_template(
            """
            ### JOB DESCRIPTION:
            {job_description}

            ### INSTRUCTION:
            You are Tusyaa Sreerala, {profile_summary}.
            Write a cold email expressing your interest, describing your relevant skills, and any notable projects that align with the role. Include links to showcase your projects or academic work if relevant. 
            Add the most relevant portfolio links from the following: {link_list}.
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):
            """
        )
        chain_email = prompt_email | self.llm
        res = chain_email.invoke({
            "job_description": str(job),
            "profile_summary": profile_summary,
            "email_tone": email_tone,
            "email_purpose": email_purpose,
            "link_list": links
        })
        return res.content

    def write_networking_email(self, profile_summary, email_tone):
        prompt_networking = PromptTemplate.from_template(
            """
            ### INSTRUCTION:
            You are Tusyaa Sreerala, a professional with the following background: {profile_summary}.
            Your goal is to write a {email_tone} networking email to establish a professional connection, express interest in the industry or company, and politely seek advice or an informational meeting if possible.
            Do not provide a preamble.
            ### EMAIL (NO PREAMBLE):
            """
        )
        chain_networking = prompt_networking | self.llm
        res = chain_networking.invoke({
          
            "profile_summary": profile_summary,
            "email_tone": email_tone,
        })
        return res.content
