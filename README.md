# 🎭 Social Media Sentiment Analyzer

A machine learning web application that analyzes tweets and classifies their sentiment as **Positive**, **Negative**, or **Neutral**, built with Python, Scikit-learn, and Streamlit.

---

## 🚀 Features

- Clean, simple, and interactive Streamlit UI
- Real-time sentiment analysis of tweets/text
- Text preprocessing (removes mentions, special characters, converts to lowercase)
- Input validation to prevent empty submissions
- Instant visual feedback — success, error, and warning messages based on sentiment

---

## 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application framework |
| Scikit-learn | Machine learning model |
| Pickle | Model serialization/loading |
| Regex (re) | Text cleaning and preprocessing |

---

## 📁 Project Structure

social-media-sentiment-analyzer/
│
├── app.py              # Main Streamlit application
├── model.pkl           # Trained sentiment classification model
├── tfidf.pkl            # TF-IDF vectorizer used during preprocessing
└── README.md           # Project documentation

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.9+
- pip

### Installation

1. Clone the repository and move into the project folder

2. Create and activate a virtual environment

python -m venv .venv

Windows:
.venv\Scripts\activate

macOS/Linux:
source .venv/bin/activate

3. Install dependencies

pip install -r requirements.txt

4. Run the application

streamlit run app.py



---

## 💡 How It Works

1. The user enters a tweet or text in the input box.
2. Upon clicking Analyze Sentiment, the app validates that the text isn't empty.
3. The text is cleaned (mentions and special characters removed, converted to lowercase).
4. The cleaned text is vectorized using the TF-IDF vectorizer (tfidf.pkl).
5. The pre-trained model (model.pkl) predicts the sentiment.
6. The result is displayed instantly:
   - ✅ Positive Sentiment
   - ❌ Negative Sentiment
   - ⚠️ Neutral Sentiment

---

## 📊 Model Details

The sentiment classification model was trained using Scikit-learn on labeled tweet data, then serialized with pickle along with its TF-IDF vectorizer for fast loading and inference within the app.

---

## 🐛 Troubleshooting

If you encounter a scikit-learn import error, try reinstalling the packages:

pip uninstall scikit-learn -y
pip install scikit-learn

---

## 🔮 Future Improvements

- Improve model accuracy with a larger, more diverse dataset
- Add support for batch tweet analysis
- Add sentiment confidence scores/probability display
- Deploy the app on Streamlit Cloud / Render for public access

---

## 🧑‍💻 Author

MariaZafar22

---

## 📄 License

This project is licensed under the MIT License.
