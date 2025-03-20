import streamlit as st
import pandas as pd
import google.generativeai as genai
import PyPDF2
from fpdf import FPDF
import io

# Configure Gemini API
genai.configure(api_key="YOUR API KEY")

def extract_text_from_pdf(uploaded_file):
    """Extracts text from an uploaded PDF file."""
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    text = "".join([page.extract_text() for page in pdf_reader.pages if page.extract_text()])
    return text

def process_uploaded_file(uploaded_file):
    """Processes the uploaded CSV or PDF file and extracts data."""
    if uploaded_file is not None:
        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
            df.columns = df.columns.str.strip()  # Remove extra spaces from column names
            return df
        elif uploaded_file.name.endswith(".pdf"):
            return extract_text_from_pdf(uploaded_file)
    return None

def query_gemini(user_query, file_data):
    """Sends user query along with extracted schedule data to Gemini for response."""
    prompt = f"""
    You are an expert in clinic appointment scheduling. The following data contains doctor availability:
    {file_data}
    Based on this, answer the user's question accurately:
    User Query: {user_query}
    """
    model = genai.GenerativeModel("gemini-1.5-pro")
    response = model.generate_content(prompt)  
    return response.text if response else "I'm unable to fetch an answer. Please try rephrasing your query."

def generate_pdf(doctor, date, time):
    """Generates a PDF confirmation for the appointment."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, "Clinic Appointment Confirmation", ln=True, align='C')
    pdf.ln(10)
    pdf.cell(200, 10, f"Doctor: {doctor}", ln=True)
    pdf.cell(200, 10, f"Date: {date}", ln=True)
    pdf.cell(200, 10, f"Time: {time}", ln=True)
    
    # Use 'S' to return as string
    pdf_output = pdf.output(dest='S').encode('latin1')
    
    # Convert to BytesIO for Streamlit
    pdf_io = io.BytesIO(pdf_output)
    
    return pdf_io

# Streamlit UI
st.set_page_config(page_title="Clinic Appointment Chatbot", page_icon="🩺", layout="wide")

st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Chatbot", "Book Appointment"])

if page == "Chatbot":
    st.title("Clinic Appointment Chatbot 🩺")
    uploaded_file = st.file_uploader("Upload Clinic Schedule (CSV or PDF)", type=["csv", "pdf"])
    
    if uploaded_file:
        file_data = process_uploaded_file(uploaded_file)
        if file_data is not None:
            st.success("File uploaded successfully!")
            st.write(file_data.head())  # Debugging: Show first few rows
            user_query = st.text_input("Enter your query about doctor schedules:")
            if st.button("Ask Chatbot"):
                if user_query.strip():
                    response = query_gemini(user_query, file_data)
                    st.write("*Chatbot Response:*", response)
                else:
                    st.warning("Please enter a query before clicking the button.")
        else:
            st.error("Invalid file format. Please upload a valid CSV or PDF.")

elif page == "Book Appointment":
    st.title("Book a Doctor's Appointment 🏥")
    
    doctor = st.text_input("Enter Doctor's Name").strip()
    date = st.text_input("Enter Appointment Date (YYYY-MM-DD)").strip()
    time = st.text_input("Enter Appointment Time (HH:MM AM/PM)").strip()
    
    if st.button("Generate Appointment Confirmation"):
        if doctor and date and time:
            pdf = generate_pdf(doctor, date, time)
            st.success("Appointment confirmed! Download your appointment details below.")
            st.download_button(label="Download Confirmation PDF", data=pdf, file_name="appointment_confirmation.pdf", mime="application/pdf")
        else:
            st.warning("Please enter all details before generating the confirmation.")    
