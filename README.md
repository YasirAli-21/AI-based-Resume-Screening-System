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
In a highly competitive job market, many talented candidates are filtered out by "ATS (Applicant Tracking Systems)" before a human ever sees their resume. **YSENTRY AI** is a specialized tool that bridges this gap by scanning your resume against specific Job Descriptions (JD) to ensure maximum compatibility.

* **Smart Match Scoring:** Features an interactive SVG percentage circle for instant visual feedback.
* **Role Prediction:** Automatically analyzes skills and experience to predict your professional role.
* **Quantifiable Insights:** Identifies missing metrics (%) and key action verbs required for modern resumes.
* **Activity Intelligence:** Tracks and displays exactly the last **21** ⚡ scans to help users monitor their improvement over time.

---

## 🎯 Problem Statement <a name="problem-statement"></a>
Most job seekers struggle to identify why their applications aren't receiving responses. Manual resume auditing is time-consuming and prone to human error. **YSENTRY AI** solves this by providing:
1. Instant feedback on keyword alignment.
2. Structural improvement suggestions.
3. Comparative analysis between candidate experience and job requirements.

---

## 🚀 Getting Started <a name="getting-started"></a>
Follow these steps to run YSENTRY AI on your local machine:

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
* 🐍 **Python 3.10+** – Primary logic and backend.
* 🔥 **Flask** – Lightweight web framework for the dashboard.
* 📄 **Pdfplumber** – Precision PDF text extraction.
* 🎨 **Tailwind CSS** – Modern, responsive UI/UX.
* 📊 **Jinja2** – Dynamic data rendering for results and history.

---

## 💻 Project Execution <a name="project-execution"></a>
Run the Flask application using:
`python app.py`

*Once initialized, visit: `http://127.0.0.1:5000` in your browser.*

---

## 🧠 Analysis Logic & Technical Details <a name="analysis-logic--technical-details"></a>
The "Intelligence" of YSENTRY AI follows a structured document processing pipeline:



### 🔹 PDF Parsing
The system utilizes `pdfplumber` to extract raw text from complex PDF layouts, ensuring no vital information is lost during the conversion.

### 🔹 Keyword Analysis
Our algorithm performs a case-insensitive cross-reference against a database of industry-specific keywords (e.g., PMO, Software Engineer, Data Scientist).

### 🔹 Scoring Engine
Scores are calculated using lexical density algorithms, measuring the frequency and relevance of match-keywords found within the resume relative to the JD.

### 🔹 Recommendation Logic
The system audits the resume for "Impact Metrics" and "Action Verbs," providing specific suggestions to make the resume more result-oriented.

---

## ⚙️ System Workflow <a name="system-workflow"></a>
1. **Input:** User uploads a Resume (PDF) and provides the target Job Description.
2. **Extraction:** Text is normalized to lowercase and stripped of redundant whitespace.
3. **Processing:** Role classification and scoring logic are triggered.
4. **Visualization:** Match results are rendered via an **Animated SVG Circle**.
5. **Logging:** The analysis is logged in the Activity History, maintaining a limit of exactly **21** recent scans.

---

## 📊 System Features <a name="system-features"></a>
* 🔍 **Deep Scan:** Comprehensive comparison between candidate profile and JD requirements.
* 📈 **Visual Analytics:** Real-time match-percentage visualization.
* 📝 **Actionable Feedback:** Granular strengths and recommendations for resume optimization.
* 🕒 **Scan History:** Persistent tracking of the last **21** scan events.
* 🖨️ **Print Ready:** Optimized UI for printing or saving analysis results as a report.

---

## ✨ Future Enhancements <a name="future-enhancements"></a>
* 🤖 **Large Language Model (LLM) Integration:** For hyper-personalized resume rewriting.
* 📊 **Competency Mapping:** Radar charts to visualize technical vs. soft skill balance.
* 📂 **Multi-format Support:** Extending parsing capabilities to `.docx` files.
* 📧 **Automated Reporting:** Sending detailed analysis reports directly via email.

---

## 👨‍💻 Author <a name="author"></a>
**Yasir Ali** |IT Enthusiast

[![github](https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/YasirAli-21)
[![linkedin](https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/yasisahito)