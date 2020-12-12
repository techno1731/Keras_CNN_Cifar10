#!/usr/bin/env python
# import the necessary packages
from ModeloChingon import *
import streamlit as st

st.title("Image Classification with Keras")
st.header("Convolutional Neural Networks trained on CIFAR-10 Dataset")
st.text("Upload an Image to predict the class")

uploaded_file = st.file_uploader("Choose an Image to Classify ...",
                                 type="jpeg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("Classifying...")
    results = modelo_chingon_predict(image)
    for (i, result) in enumerate(results):
        st.write("{}. {}: {:.4f}".format(i + 1, result[0],
                                      result[1]))
