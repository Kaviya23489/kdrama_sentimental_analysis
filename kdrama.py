# kdrama_sentiment_app.py

import streamlit as st
from textblob import TextBlob

st.set_page_config(page_title="K-Drama Review Analyzer", page_icon="🎬")

st.title("🎭 K-Drama Sentiment Analyzer")
st.write("Analyze the emotional tone of your K-Drama review!")

# Input box
review = st.text_area("✍️ Enter your K-Drama review here:", height=200)

if st.button("🧠 Analyze Sentiment"):
    if review:
        blob = TextBlob(review)
        sentiment_score = blob.sentiment.polarity

        if sentiment_score > 0.1:
            st.success("🌸 Positive Sentiment")
        elif sentiment_score < -0.1:
            st.error("💔 Negative Sentiment")
        else:
            st.info("😐 Neutral Sentiment")

        st.markdown(f"**Sentiment Score:** `{sentiment_score:.2f}`")
    else:
        st.warning("Please enter a review to analyze.")
