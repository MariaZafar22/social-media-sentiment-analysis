import streamlit as st
import pickle
import re

# Models load karein
model = pickle.load(open('model.pkl', 'rb'))
tfidf = pickle.load(open('tfidf.pkl', 'rb'))


# Text clean function
def clean_text(text):
    text = re.sub(r'@[\w]*', '', text)
    text = re.sub(r'[^a-zA-Z#]', ' ', text)
    text = text.lower()
    return text


# App UI
st.title("🎭 Social Media Sentiment Analyzer")
st.subheader("Tweet ka sentiment check karein")

user_input = st.text_area("Yahan tweet likhein:")

if st.button("Analyze Sentiment"):
    if user_input == "":
        st.warning("Kuch text likhein!")
    else:
        cleaned = clean_text(user_input)
        vectorized = tfidf.transform([cleaned])
        result = model.predict(vectorized)[0]

        if result == 0:
            st.success(" Positive Sentiment")
        elif result == 1:
            st.error(" Negative Sentiment")
        else:
            st.warning("Neutral Sentiment")
