# HIRELENS-Intelligent-Resume-Screening-System-<br>
HIRELENS is an AI-powered resume screening system designed to automate and simplify the candidate shortlisting process. The application analyzes PDF resumes and matches them against a given job description using Natural Language Processing (NLP) techniques, reducing manual screening effort and improving hiring efficiency

**📌 Problem Statement<br>**
Recruiters often spend significant time manually reviewing resumes, which is time-consuming and prone to bias. There is a need for an intelligent system that can automatically screen resumes, rank candidates, and highlight skill relevance efficiently.

**✅ Solution Overview**

HIRELENS automates resume screening by:<br>
-Extracting text from PDF resumes.<br>
-Cleaning and preprocessing text using NLP.<br>
-Converting text into numerical vectors using TF-IDF.<br>
-Computing similarity scores between resumes and job descriptions.<br>
-Ranking candidates with a percentage match score (0–100%).<br>
-Displaying results in a visually rich Streamlit dashboard.<br>

**🎯 Key Features**

📄 Upload multiple PDF resumes.<br>
📝 Enter custom Job Description.<br>
🧠 NLP-based text preprocessing.<br>
📊 TF-IDF & Cosine Similarity scoring.<br>
🎯 Match percentage out of 100.<br>
🏆 Resume ranking (Best to Least match).<br>
📈 Interactive UI with progress bars & tables.<br>
🎨 Colorful and user-friendly dashboard.<br>

**🛠️ Technologies Used**

-Python<br>
-Streamlit (Frontend UI)<br>
-Scikit-learn (TF-IDF, Cosine Similarity)<br>
-NLTK (Text preprocessing)<br>
-pdfplumber (PDF text extraction)<br>
-Pandas & NumPy (Data handling)<br>

**🧠 Project Workflow**

-Input Job Description<br>
-Upload Resume PDFs<br>
-Extract text from resumes<br>
-Clean & preprocess text (NLP)<br>
-Apply TF-IDF vectorization<br>
-Calculate cosine similarity<br>
-Convert score to percentage (0–100)<br>
-Rank resumes<br>
-Display results on Streamlit dashboard<br>

**🗂️ Project Structure**

Resume_Screening/<br>
│
├── app.py              # Main Streamlit app<br>
├── utils.py            # Text cleaning & PDF extraction<br>
├── requirements.txt    # Project dependencies<br>
├── README.md           # Project documentation<br>
└── sample_resumes/     # Sample resume PDFs<br>

**⚙️ Installation & Setup**<br>

**1️⃣ Clone the Repository**
git clone https://github.com/ayushjadhav007/HIRELENS.git.
cd HIRELENS.

**2️⃣ Install Required Libraries**
pip install -r requirements.txt
**If needed manually:**
pip install streamlit scikit-learn nltk pdfplumber pandas numpy

**3️⃣ Download NLTK Data**
import nltk
nltk.download('stopwords')
nltk.download('punkt')

**▶️ How to Run the Project**
Run this command in VS code terminal / CMD
python -m streamlit run app.py

**📊 How It Works (User Steps)**

1.Enter Job Description
2.Upload one or multiple PDF resumes
3.Click Analyze Resumes
4.View:
    -Match percentage (0–100%)
    -Ranked candidate list
    -Skill relevance highlights
    -Visual progress bars & charts

**🚀 Future Enhancements**

🔍 Skill-wise matching breakdown
🤖 BERT / Transformer-based embeddings
📄 Resume keyword highlighting
📥 Export results to CSV/Excel
🔐 User authentication
☁️ Cloud deployment (AWS / Streamlit Cloud)  


**👤 Author**

Ayush Jadhav
Data Analytics & AI/ML Enthusiast
📧 Email:ayush812jadhav@gmail.com





