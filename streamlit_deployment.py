#!/usr/bin/env python
# import the necessary packages
from cnn_cifar_model import *
import streamlit as st


col1, col2 = st.beta_columns(2)
with col1:
    st.image('https://github.com/vfp1/bts-dsf-2020/raw/main/Logo-BTS.jpg', use_column_width=True)
with col2:
    st.image('Logo_EM-300x300.png', width=60)
st.title("Image Classification with Keras")
st.header("A model based on Convolutional Neural Networks trained on CIFAR-10 Dataset")
col1, col2 = st.beta_columns(2)
st.subheader("By Ennio Maldonado")
st.write('To start upload an Image, the model will then try to predict to which\
 category you image is closest to. The output is going to be the list of\
 categories with probabilities (zero = not likely, one = extremely likeley)\
 starting from the most likely category your image belong to, down to the\
 least likely category.')
st.write('Categories: airplane, automobile, bird, cat,\
 deer, dog, frog, horse, ship or truck')

uploaded_file = st.file_uploader("Choose an Image to Classify ...",
                                 type=['jpeg','jpg','png','tiff'])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded Image.', use_column_width=True)
    st.write("Classifying...")
    result = modelo_chingon_predict(image)
    st.write(f"Most likely category is: {result[0][0]}, with probability:\
     {result[0][1]:.4f}")
    st.write(f"Second most likely category is: {result[1][0]}, with probability:\
     {result[1][1]:.4f}")
    st.write(f"It is most likely not: {result[9][0]}, with probability:\
     {1 - result[9][1]:.4f}")
