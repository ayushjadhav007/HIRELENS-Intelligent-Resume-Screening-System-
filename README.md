# HIRELENS-Intelligent-Resume-Screening-System-
HIRELENS is an AI-powered resume screening system designed to automate and simplify the candidate shortlisting process. The application analyzes PDF resumes and matches them against a given job description using Natural Language Processing (NLP) techniques, reducing manual screening effort and improving hiring efficiency

📌 Problem Statement
Recruiters often spend significant time manually reviewing resumes, which is time-consuming and prone to bias. There is a need for an intelligent system that can automatically screen resumes, rank candidates, and highlight skill relevance efficiently.

**✅ Solution Overview**

HIRELENS automates resume screening by:
-Extracting text from PDF resumes.
-Cleaning and preprocessing text using NLP.
-Converting text into numerical vectors using TF-IDF.
-Computing similarity scores between resumes and job descriptions.
-Ranking candidates with a percentage match score (0–100%).
-Displaying results in a visually rich Streamlit dashboard.

**🎯 Key Features**

📄 Upload multiple PDF resumes.
📝 Enter custom Job Description.
🧠 NLP-based text preprocessing.
📊 TF-IDF & Cosine Similarity scoring.
🎯 Match percentage out of 100.
🏆 Resume ranking (Best to Least match).
📈 Interactive UI with progress bars & tables.
🎨 Colorful and user-friendly dashboard.

**🛠️ Technologies Used**

-Python
-Streamlit (Frontend UI)
-Scikit-learn (TF-IDF, Cosine Similarity)
-NLTK (Text preprocessing)
-pdfplumber (PDF text extraction)
-Pandas & NumPy (Data handling)

**🧠 Project Workflow**

-Input Job Description
-Upload Resume PDFs
-Extract text from resumes
-Clean & preprocess text (NLP)
-Apply TF-IDF vectorization
-Calculate cosine similarity
-Convert score to percentage (0–100)
-Rank resumes
-Display results on Streamlit dashboard

**🗂️ Project Structure**

Resume_Screening/<br>
│
├── app.py              # Main Streamlit app<br>
├── utils.py            # Text cleaning & PDF extraction<br>
├── requirements.txt    # Project dependencies<br>
├── README.md           # Project documentation<br>
└── sample_resumes/     # Sample resume PDFs<br>




