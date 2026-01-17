# HIRELENS-Intelligent-Resume-Screening-System-<br>
HIRELENS is an AI-powered resume screening system designed to automate and simplify the candidate shortlisting process. The application analyzes PDF resumes and matches them against a given job description using Natural Language Processing (NLP) techniques, reducing manual screening effort and improving hiring efficiency

**📌 Problem Statement<br>**
Recruiters often spend significant time manually reviewing resumes, which is time-consuming and prone to bias. There is a need for an intelligent system that can automatically screen resumes, rank candidates, and highlight skill relevance efficiently.

**✅ Solution Overview**

HIRELENS automates resume screening by:<br>
- Extracting text from PDF resumes.<br>
- Cleaning and preprocessing text using NLP.<br>
- Converting text into numerical vectors using TF-IDF.<br>
- Computing similarity scores between resumes and job descriptions.<br>
- Ranking candidates with a percentage match score (0–100%).<br>
- Displaying results in a visually rich Streamlit dashboard.<br>

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

- Python<br>
- Streamlit (Frontend UI)<br>
- Scikit-learn (TF-IDF, Cosine Similarity)<br>
- NLTK (Text preprocessing)<br>
- pdfplumber (PDF text extraction)<br>
- Pandas & NumPy (Data handling)<br>

**🧠 Project Workflow**

- Input Job Description<br>
- Upload Resume PDFs<br>
- Extract text from resumes<br>
- Clean & preprocess text (NLP)<br>
- Apply TF-IDF vectorization<br>
- Calculate cosine similarity<br>
- Convert score to percentage (0–100)<br>
- Rank resumes<br>
- Display results on Streamlit dashboard<br>

**🗂️ Project Structure**

Resume_Screening/<br>
│
├── app.py              # Main Streamlit app<br>
├── utils.py            # Text cleaning & PDF extraction<br>
├── requirements.txt    # Project dependencies<br>
├── README.md           # Project documentation<br>
└── sample_resumes/     # Sample resume PDFs<br>

**⚙️ Installation & Setup**<br>

**1️⃣ Clone the Repository**<br>
git clone https://github.com/ayushjadhav007/HIRELENS.git.<br>
cd HIRELENS.<br>

**2️⃣ Install Required Libraries**<br>
pip install -r requirements.txt<br>
**If needed manually:**<br>
pip install streamlit scikit-learn nltk pdfplumber pandas numpy<br>

**3️⃣ Download NLTK Data**<br>
import nltk<br>
nltk.download('stopwords')<br>
nltk.download('punkt')<br>

**▶️ How to Run the Project**<br>
Run this command in VS code terminal / CMD<br>
python -m streamlit run app.py<br>

**📊 How It Works (User Steps)**<br>

1.Enter Job Description<br>
2.Upload one or multiple PDF resumes<br>
3.Click Analyze Resumes<br>
4.View:<br>
    - Match percentage (0–100%)<br>
    - Ranked candidate list<br>
    - Skill relevance highlights<br>
    - Visual progress bars & charts<br>

**🚀 Future Enhancements**<br>

🔍 Skill-wise matching breakdown<br>
🤖 BERT / Transformer-based embeddings<br>
📄 Resume keyword highlighting<br>
📥 Export results to CSV/Excel<br>
🔐 User authentication<br>
☁️ Cloud deployment (AWS / Streamlit Cloud)<br>


**👤 Author**<br>

Ayush Jadhav<br>
Data Analytics & AI/ML Enthusiast<br>
📧 Email:ayush812jadhav@gmail.com<br>





