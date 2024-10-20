
import streamlit as st
import joblib
import numpy as np

# Load the saved model, vectorizer, and label encoder
logreg = joblib.load('final_logreg_model.pkl')
vectorizer = joblib.load('final_vectorizer.pkl')
label_encoder = joblib.load('final_label_encoder.pkl')

# Function to predict the category
def predict_category(text):
    # Transform the input text using the same vectorizer
    text_vectorized = vectorizer.transform([text])
    
    # Get the prediction from the model
    prediction = logreg.predict(text_vectorized)
    
    # Return the predicted class label
    return label_encoder.inverse_transform(prediction)[0]

# Streamlit app layout
st.title('News Classification Application')
st.subheader('Enter a news article to classify its category')

# Input text box
article_text = st.text_area('Enter article text:', height=300)

# When the user clicks the classify button
if st.button('Classify'):
    if article_text.strip() != "":
        category = predict_category(article_text)
        st.write(f'Predicted Category: {category}')
    else:
        st.write("Please enter some text to classify.")
