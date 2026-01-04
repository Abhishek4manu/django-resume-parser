# Django Resume Parser

A Django backend application that allows uploading resumes (PDF/DOCX), extracts text, and parses structured information like name, email, phone, skills, education, and experience.

---

## 🚀 Features

- Upload resume files in PDF or DOCX format
- Extract text from uploaded files
- Parse key information:
  - Name
  - Email
  - Phone number
  - Skills
  - Education
  - Experience
- Returns structured JSON response
- Handles scanned PDFs via OCR fallback

---

## 📁 Project Structure

resume_parser/
├── manage.py
├── resume_parser/ # Django project settings
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── parser/ # App for resume parsing
│ ├── views.py
│ ├── urls.py
│ ├── models.py
│ ├── serializers.py
│ └── services/
│ ├── file_handler.py
│ ├── text_extractor.py
│ ├── parser_engine.py
│ └── ocr_engine.py
└── media/
└── resumes/ # Uploaded resumes



## ⚙️ Setup Instructions

### 1. Clone Repository


git clone https://github.com/Abhishek4manu/django-resume-parser.git
cd django-resume-parser
2. Create and Activate Virtual Environment

python -m venv venv
Windows:


venv\Scripts\activate

3. Install Dependencies

pip install -r requirements.txt
4. Apply Migrations

python manage.py makemigrations
python manage.py migrate
5. Run Development Server

python manage.py runserver
Server runs at:

http://127.0.0.1:8000
📤 API Usage
Upload Resume
Endpoint:


POST /api/resume/upload/
Request:

Form data

Key: resume

Value: PDF or DOCX file

Response:

{
  "name": "John Doe",
  "email": "john.doe@gmail.com",
  "phone": "+91 1234567890",
  "skills": [...],
  "education": [...],
  "experience": [...]
}
🧩 System Dependencies
Poppler (for PDF text extraction)
Required for extracting text from PDFs

On Windows, download Poppler binaries and add the poppler/bin folder to the system PATH

Verify installation:


pdfinfo -v

Tesseract OCR (for scanned PDFs)
Required to handle scanned PDF files

Install Tesseract and make sure tesseract is in PATH

Verify installation:


tesseract --version
If these tools are not installed, the parser will return a clear error message for scanned PDFs.

📌 Notes
Parsing logic is rule-based using text extraction and regex

Handles basic resume formats

Not production optimized — designed for take-home assignment evaluation

Uploaded resume files are stored under media/resumes/ and not included in source control

👤 Author
Abhishek Manu
GitHub: https://github.com/Abhishek4manu
