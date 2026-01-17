import streamlit as st
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

from utils import clean_text, extract_text_from_pdf

# ================= PAGE CONFIG =================
st.set_page_config(
    page_title="HIRELENS ATS",
    page_icon="🎯",
    layout="wide"
)

# ================= THEME =================
st.markdown("""
<style>
body {
    background: linear-gradient(135deg, #667eea, #764ba2);
}

.main {
    background: linear-gradient(135deg, #f8fafc, #e0e7ff);
}

.card {
    background: white;
    padding: 25px;
    border-radius: 18px;
    box-shadow: 0 10px 25px rgba(0,0,0,0.15);
    margin-bottom: 20px;
}

.title {
    font-size: 42px;
    font-weight: 800;
    background: linear-gradient(90deg, #4f46e5, #06b6d4);
    -webkit-background-clip: text;
    color: transparent;
}

.subtitle {
    font-size: 18px;
    color: #475569;
}

.badge {
    display: inline-block;
    background: #22c55e;
    color: white;
    padding: 6px 14px;
    border-radius: 20px;
    font-size: 14px;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# ================= HEADER =================
st.markdown("<div class='title'>🎯 HIRELENS</div>", unsafe_allow_html=True)
st.markdown(
    "<div class='subtitle'>AI-Powered Intelligent Resume Screening System</div>",
    unsafe_allow_html=True
)

st.markdown("---")

# ================= INPUT SECTION =================
col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 📝 Job Description")
    job_description = st.text_area(
        "",
        height=230,
        placeholder="Example: Data Analyst with Python, SQL, Power BI, Machine Learning..."
    )
    st.markdown("</div>", unsafe_allow_html=True)

with col2:
    st.markdown("<div class='card'>", unsafe_allow_html=True)
    st.markdown("### 📤 Upload Resumes (PDF)")
    uploaded_files = st.file_uploader(
        "",
        type=["pdf"],
        accept_multiple_files=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ================= BUTTON =================
st.markdown("<center>", unsafe_allow_html=True)
analyze = st.button("🚀 Analyze & Rank Resumes", use_container_width=True)
st.markdown("</center>", unsafe_allow_html=True)

# ================= PROCESS =================
if analyze:
    if not job_description or not uploaded_files:
        st.warning("⚠️ Please provide job description and resumes.")
    else:
        with st.spinner("🤖 AI is analyzing resumes..."):
            resumes = []

            for file in uploaded_files:
                text = extract_text_from_pdf(file)
                resumes.append({
                    "Resume Name": file.name,
                    "Resume Text": text
                })

            df = pd.DataFrame(resumes)

            df["Cleaned Resume"] = df["Resume Text"].apply(clean_text)
            cleaned_jd = clean_text(job_description)

            vectorizer = TfidfVectorizer()
            tfidf = vectorizer.fit_transform(
                df["Cleaned Resume"].tolist() + [cleaned_jd]
            )

            scores = cosine_similarity(tfidf[-1], tfidf[:-1])[0]

            # 🔥 CONVERT TO PERCENTAGE
            df["Match %"] = (scores * 100).round(2)

            df = df.sort_values(by="Match %", ascending=False)

        st.success("✅ Resume Screening Completed")

        # ================= TABLE =================
        st.markdown("## 🏆 Candidate Ranking")
        st.dataframe(
            df[["Resume Name", "Match %"]],
            use_container_width=True
        )

        # ================= PROGRESS =================
        st.markdown("## 📊 Resume Match Strength")
        for _, row in df.iterrows():
            st.write(f"📄 **{row['Resume Name']}** — {row['Match %']}%")
            st.progress(int(row["Match %"]))

        # ================= BEST CANDIDATE =================
        best = df.iloc[0]
        st.markdown(
            f"""
            <div class="card">
            🏅 <b>Top Candidate</b><br><br>
            📄 <b>{best['Resume Name']}</b><br>
            🎯 Match Score: <span class="badge">{best['Match %']}%</span>
            </div>
            """,
            unsafe_allow_html=True
        )

        # ================= SKILL MATCH =================
        st.markdown("## 🧠 Skill Match (Top Resume)")
        jd_words = set(cleaned_jd.split())
        resume_words = set(best["Cleaned Resume"].split())
        matched = list(jd_words.intersection(resume_words))

        if matched:
            st.success("✅ Matching Skills")
            st.write(", ".join(matched[:25]))
        else:
            st.warning("⚠️ No strong skill overlap found")

        # ================= CHART =================
        st.markdown("## 📈 Top 5 Resume Comparison")
        chart_df = df.head(5)[["Resume Name", "Match %"]]
        st.bar_chart(chart_df.set_index("Resume Name"))

# ================= FOOTER =================
st.markdown("---")
st.markdown(
    "💼 **HIRELENS ATS** | NLP • Machine Learning • Streamlit",
    unsafe_allow_html=True
)
