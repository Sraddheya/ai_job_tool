# Use the PyPDF2 library to extract text from a PDF file

import PyPDF2
import os
from openai import OpenAI
import docx2txt


def extract_text_from_pdf(pdf_path):
    """"This function extracts text from a PDF file and returns it as a string"""
    pdf_file = open(pdf_path, 'rb')
    pdfreader = PyPDF2.PdfReader(pdf_file)
    x = pdfreader.numPages
    text = ''
    for i in range(x):
        pageobj = pdfreader.getPage(i)
        text += pageobj.extractText()
    return text


def extract_text_from_docx(docx_path):
    """"This function extracts text from a docx file and returns it as a string"""
    text = docx2txt.process(docx_path)
    return text


"""Edge cases:
- No dates given
"""


def ai_extract_data_from_text(text):
    output_format = """{
    "name": xxxx,
    "experience": xxxx}"""

    job_format = """{
        "job_title": xxxx,
        "job_duration":xxxx,
        "company": xxxx,
        "skills": xxxx}"""

    """This function extracts data from text using OpenAI's API"""
    client = OpenAI(api_key=os.environ.get('OPENAI_API_KEY'))
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "You are a resume assistant, tasked with extracting information from resumes so anyone reading it can quickly get key information they are looking for. Do not provide any preamble or closing.",
            },
            {
                "role": "user",
                "content": f"Extract the following information and present it in the JSON format: {output_format} and repeat this for every job listed in the JSON format {job_format}. Do not provide any preamble or closing, just the raw JSON. Extract the tools listed in each job description by their mentions. Round the job durations to their nearest whole month, for example if someone has been in a role from September 2021 to September 2021 this will count as 1 month and November 2021 to April 2022 will count as 6 months. <resume>{text}<resume>",
            },
        ],
    )
    return completion.choices[0].message
