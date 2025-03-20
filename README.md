# Clinic Appointment Chatbot 🏥

This is a **Streamlit-based AI-powered Clinic Appointment Chatbot** that allows users to:
- **Upload doctor schedules (CSV/PDF)** and query doctor availability using **Google Gemini AI**.
- **Book doctor appointments** and generate **PDF confirmation receipts**.

---

## Features
✅ Upload doctor schedules in CSV or PDF format  
✅ AI-powered chatbot to answer doctor availability queries  
✅ Book an appointment by selecting a doctor, date, and time  
✅ Generate a downloadable **PDF confirmation** for the appointment  

---

## 🚀 Getting Started

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/your-username/clinic-appointment-chatbot.git
cd clinic-appointment-chatbot
```

### 2️⃣ Set Up a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

---

## 🔑 Google Gemini API Key Setup

This chatbot uses **Google Gemini AI** to process doctor schedule queries. You need to configure an API key.

### How to Get a Gemini API Key:
1. Go to [Google AI Studio](https://aistudio.google.com/)
2. Sign in with your Google account
3. Generate an API key from the **API Keys** section
4. Copy the API key

### Add API Key to the Project:
1. Open the `app.py` file
2. Replace the `api_key` value in this line:
   ```python
   genai.configure(api_key="YOUR_GEMINI_API_KEY_HERE")
   ```
3. Save the file

---

## 🏃‍♂️ Running the Application
After setting up everything, run the application using Streamlit:
```bash
streamlit run app.py
```

This will open the web app in your browser.

---

## 📂 File Upload Instructions
### CSV File Format Example
The uploaded CSV file should contain doctor names, specialties, available days, and available time slots. Example:
```csv
Doctor_Name,Specialty,Available_Days,Available_Time
Dr. Aisha Patel,Cardiologist,Monday,Wednesday,Friday,10:00 AM - 1:00 PM
Dr. Raj Malhotra,Dermatologist,Tuesday,Thursday,Saturday,2:00 PM - 5:00 PM
```

### PDF File
The chatbot can also process PDFs containing doctor schedules extracted from hospital records.

---

## 🏥 Booking an Appointment
1. Go to the **Book Appointment** section
2. Enter:
   - Doctor's Name
   - Appointment Date (YYYY-MM-DD)
   - Appointment Time (HH:MM AM/PM)
3. Click **"Generate Appointment Confirmation"**
4. Download the **PDF confirmation**

---

## 📜 License
This project is licensed under the **MIT License**.

---
