import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import mysql.connector

# Load the trained model
model = load_model('crop_disease_model.h5')

# Define disease categories
disease_classes = {
    0: 'Tomato_healthy',
    1: 'Tomato_Tomato_mosaic_virus',
    2: 'rl_Vi rus',
    3: 'Tomato_Target_Spot',
    4: 'Potato',
    5: 'Potato_Late_blight',
    6: 'Potato_Early_blight',
    7: 'pep per_',
    8: 'Pepper_bell',
    9: 'bell',
    10: 'healthy',
    11: 'Bacterial_spot'
}

# Establish connection to MySQL database
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Adarsh@2003",
    database="cropdisease"
)

# Streamlit UI
st.title('Crop Disease Identification')

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image', use_column_width=True)
    st.write("")
    st.write("Classifying...")

    # Preprocess the uploaded image
    img = image.resize((128, 128))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)

    # Predict the disease
    prediction = model.predict(img)

    # Get the predicted class
    predicted_class = disease_classes[np.argmax(prediction)]

    # Display the predicted disease with big and highlighted text
    st.markdown(f"<h1 style='text-align: center; color: red;'>Predicted Disease: {predicted_class}</h1>", unsafe_allow_html=True)

    # Save the uploaded image to MySQL database
    cursor = conn.cursor()
    insert_query = "INSERT INTO uploaded_images (image) VALUES (%s)"
    cursor.execute(insert_query, (uploaded_file.read(),))
    conn.commit()
    cursor.close()

conn.close()
