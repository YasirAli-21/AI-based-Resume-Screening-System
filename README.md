# 🛡️ YSENTRY AI – Professional Resume Analyzer

**Optimizing Career Paths through Intelligent Document Analysis & ATS Logic**

---

## 📚 Table of Contents
- 🌟 [Overview](#overview)
- 🎯 [Problem Statement](#problem-statement)
- 🚀 [Getting Started](#getting-started)
- 🛠️ [Tech Stack & Libraries](#tech-stack--libraries)
- 💻 [Project Execution](#project-execution)
- 🧠 [Analysis Logic & Technical Details](#analysis-logic--technical-details)
- ⚙️ [System Workflow](#system-workflow)
- 📊 [System Features](#system-features)
- ✨ [Future Enhancements](#future-enhancements)
- 👨‍💻 [Author](#author)

---

## 🌟 Overview <a name="overview"></a>
Job market mein competition bohot zyada hai aur aksar achay candidates sirf "ATS (Applicant Tracking System)" ki wajah se filter ho jate hain. **YSENTRY AI** ek specialized tool hai jo aapke resume ko scan karta hai aur batata hai ke wo Job Description (JD) ke mutabiq kitna perfect hai.

* **Smart Match Scoring:** Interactive SVG percentage circle ke zariye instant match score dikhata hai.
* **Role Prediction:** Aapke skills ko analyze kar ke aapka professional role predict karta hai.
* **Quantifiable Insights:** Batata hai ke kahan numbers (%) aur metrics add karne ki zaroorat hai.
* **Activity Intelligence:** Aapke career progress ko track karne ke liye last **21** ⚡ scans ki history rakhta hai.

---

## 🎯 Problem Statement <a name="problem-statement"></a>
Aksar candidates ko pata nahi chalta ke unka resume shortlist kyun nahi ho raha. Manual analysis mein bohot waqt lagta hai. **YSENTRY AI** is problem ko solve karta hai by providing:
1. Instant feedback on keyword matching.
2. Structural improvement suggestions.
3. Comparative analysis between Resume and Job Description.

---

## 🚀 Getting Started <a name="getting-started"></a>
Follow these steps to run YSENTRY AI locally:

### Step 1: Clone the Repository
`git clone https://github.com/YasirAli-21/YSentry-Resume-AI.git`

### Step 2: Navigate to the Project Directory
`cd YSentry-Resume-AI`

### Step 3: Setup Environment
* Create: `python -m venv .venv`
* Activate (Windows): `.\.venv\Scripts\activate`

### Step 4: Install Dependencies
`pip install flask pdfplumber`

---

## 🛠️ Tech Stack & Libraries <a name="tech-stack--libraries"></a>
* 🐍 **Python 3.10+** – Core programming.
* 🔥 **Flask** – Lightweight Web Framework.
* 📄 **Pdfplumber** – Advanced PDF text extraction logic.
* 🎨 **Tailwind CSS** – Professional & Responsive UI design.
* 📊 **Jinja2** – Dynamic templating for results and history.

---

## 💻 Project Execution <a name="project-execution"></a>
Run the Flask application:
`python app.py`

*Once running, visit: `http://127.0.0.1:5000`*

---

## 🧠 Analysis Logic & Technical Details <a name="analysis-logic--technical-details"></a>
The "Intelligence" of YSENTRY AI follows a systematic approach:



### 🔹 PDF Parsing
System uses `pdfplumber` to extract clean text from multi-page resumes without losing formatting context.

### 🔹 Keyword Analysis
Algorithm performs a case-insensitive check against industry-standard keywords (e.g., PMO, Software Engineer, Data Analyst).

### 🔹 Scoring Engine
Match score generate karne ke liye lexical density aur job-specific keyword frequency ka use kiya jata hai.

### 🔹 Recommendation Logic
System check karta hai ke kya resume mein "Action Verbs" aur "Quantifiable Metrics" (%) maujood hain ya nahi.

---

## ⚙️ System Workflow <a name="system-workflow"></a>
1. **Input:** User apna Resume (PDF) upload karta hai aur Job Description paste karta hai.
2. **Extraction:** PDF se sara text extract kar ke lowercase mein convert kiya jata hai.
3. **Processing:** Role detection aur score calculation logic run hota hai.
4. **Visualization:** Match score ek **Animated SVG Circle** mein dikhaya jata hai.
5. **Logging:** Result ko history table mein save kiya jata hai (Last **21** limit).

---

## 📊 System Features <a name="system-features"></a>
* 🔍 **Deep Scan:** Resume aur JD ka detailed comparison.
* 📈 **Visual Analytics:** Percentage circle for better readability.
* 📝 **Strengths & Weaknesses:** Detailed bullet points for improvement.
* 🕒 **Scan History:** Tracks exactly **21** previous attempts.
* 🖨️ **Print Ready:** Results ko PDF ya Paper par print karne ka option.

---

## ✨ Future Enhancements <a name="future-enhancements"></a>
* 🤖 **GPT Integration:** Detailed AI-generated summary recommendations.
* 📊 **Skills Radar Chart:** Visual representation of technical vs soft skills.
* 📂 **DOCX Support:** MS Word files parsing capability.
* 📧 **Email Reports:** Analysis results directly to the user's inbox.

---

## 👨‍💻 Author <a name="author"></a>
**Yasir Ali** | AI & Web Development | © 2026 YSENTRY

[![github](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/YasirAli-21)
[![linkedin](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yasisahito)