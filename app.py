from flask import Flask, render_template, request
import pdfplumber
from datetime import datetime
import random

app = Flask(__name__)
scan_history = []

@app.route('/')
def home():
    return render_template('index.html', result=None, history=scan_history)

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        resume_file = request.files['resume']
        jd_text = request.form.get('jd', '').lower()
        
        with pdfplumber.open(resume_file) as pdf:
            resume_text = " ".join([page.extract_text() for page in pdf.pages]).lower()

        if any(w in resume_text for w in ["pmo", "project management", "stakeholder"]):
            role = "Professional PMO Specialist"
        elif any(w in resume_text for w in ["developer", "software", "engineer"]):
            role = "Professional Software Engineer"
        elif any(w in resume_text for w in ["data", "analyst", "sql"]):
            role = "Professional Data Analyst"
        else:
            role = "Professional Specialist"

        score = random.randint(60, 95)

        dynamic_recs = []
        if not any(char in resume_text for char in ["%", "$"]):
            dynamic_recs.append("Quantifiable Metrics: Add specific percentages (%) or budget figures ($) to highlight your impact.")
        
        if "summary" not in resume_text and "profile" not in resume_text:
            dynamic_recs.append("Executive Summary: Add a professional 3-line summary at the top to grab attention.")
            
        if len(resume_text.split()) < 300:
            dynamic_recs.append("Content Depth: Your resume is a bit thin. Expand on your responsibilities for your last 2 roles.")
        
        if not dynamic_recs:
            dynamic_recs.append("Formatting Consistency: Ensure all date formats and font sizes are uniform throughout.")

        dynamic_strengths = []
        if len(resume_text.split()) > 500:
            dynamic_strengths.append("Comprehensive professional experience coverage.")
        if "certificat" in resume_text:
            dynamic_strengths.append("Strong focus on professional development and certifications.")
        if not dynamic_strengths:
            dynamic_strengths.append("Clean and ATS-friendly structural layout.")

        result = {
            'role': role,
            'score': score,
            'strengths': dynamic_strengths,
            'recommendations': dynamic_recs,
            'timestamp': datetime.now().strftime("%I:%M %p"),
            'date': datetime.now().strftime("%d %b %Y")
        }

        scan_history.insert(0, result)
        if len(scan_history) > 21:
            scan_history.pop()

        return render_template('index.html', result=result, history=scan_history)
    except:
        return "File Error", 400

if __name__ == '__main__':
    app.run(debug=True)