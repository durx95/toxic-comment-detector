import streamlit as st
import pickle

# Page config
st.set_page_config(
    page_title="Toxic Comment Detector",
    page_icon="🧠",
    layout="centered"
)

# Custom CSS (UI Enhancement)
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
        color: white;
    }
    .stTextArea textarea {
        background-color: #262730;
        color: white;
        border-radius: 10px;
    }
    .stButton button {
        background-color: #ff4b4b;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        font-size: 18px;
    }
    .stButton button:hover {
        background-color: #ff1c1c;
    }
    </style>
""", unsafe_allow_html=True)

# Load model
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

# Header
st.markdown("<h1 style='text-align: center;'>🧠 Toxic Comment Detector</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: gray;'>AI-powered comment toxicity analysis</p>", unsafe_allow_html=True)

st.divider()

# Input Section
st.subheader("💬 Enter Your Comment")
user_input = st.text_area("", placeholder="Type your comment here...")

# Prediction Button
if st.button("🔍 Analyze Comment"):
    if user_input.strip() != "":
        
        # Preprocess
        text = user_input.lower()
        text_vector = vectorizer.transform([text])

        # Prediction
        result = model.predict(text_vector)
        prob = model.predict_proba(text_vector)

        confidence = round(max(prob[0]) * 100, 2)

        st.divider()

        # Output Section
        st.subheader("📊 Result")

        if result[0] == 1:
            st.error(f"🚨 Toxic Comment Detected\n\nConfidence: {confidence}%")
            st.progress(int(confidence))
        else:
            st.success(f"✅ Non-Toxic Comment\n\nConfidence: {confidence}%")
            st.progress(int(confidence))

    else:
        st.warning("⚠️ Please enter a comment first.")

st.divider()

# Footer
st.markdown("""
<hr>
<p style='text-align: center; font-size:14px; color:gray;'>
 👨‍💻 Developed by <b>Durgesh Maurya</b> <br>
🚀 AI | Data Science Enthusiast <br><br>
 Built with ❤️ using Machine Learning & Streamlit
</p>
""", unsafe_allow_html=True)