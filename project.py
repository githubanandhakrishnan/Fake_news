import streamlit as st
import pickle
import spacy

# Load the trained SVM model
with open(r"C:\Users\91735\Downloads\svm_model.pkl", 'rb') as f:
    sv = pickle.load(f)

# Load SpaCy model
nlp = spacy.load('en_core_web_sm')

def predict_news(input_text):
    # Vectorize input text
    x_input = nlp(input_text).vector.reshape(1, -1)
    # Predict using the loaded SVM model
    prediction = sv.predict(x_input)
    return prediction[0]

# Streamlit UI
st.title("News Classifier")
news_input = st.text_area("Enter the news:")
if st.button("Classify"):
    prediction = predict_news(news_input)
    if prediction == 1:
        st.write("Fake News")
    else:
        st.write("Real News")
