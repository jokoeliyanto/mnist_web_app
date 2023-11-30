import streamlit as st
import time
import numpy as np
import pandas as pd
import random
import pickle
from matplotlib import pyplot as plt 

X_test = np.load("testX.npy")
y_test = np.load("testy.npy")
filename = "svm_model.sav"
# load the model from disk
svm_load = pickle.load(open(filename, 'rb'))

st.set_page_config(page_title="Web App Angka MNIST", page_icon="logo_hoda.png")

st.write("# ⛺ :red[Klasifikasi Gambar Angka MNIST] ")
st.markdown(""":rainbow[--------------------------------------------------------------------------------------------------------------------------------------------]""")
st.image('mnist_images.png')
# file = st.file_uploader("Unggah gambar angka Anda:", type=["jpg", "png"])

st.markdown("#### Ambil secara random sampel dari data uji!")
data_rand = st.button("Mengambil data")

if data_rand:
    r = random.randrange(0, len(X_test), 1)

    fig, ax = plt.subplots(figsize=(15,15))
    ax.imshow(X_test[r], cmap='gray')

    for i in range(X_test[r].shape[0]):
        for j in range(X_test[r].shape[1]):
            ax.text(j, i, str(X_test[r][i, j]), color='r', ha='center', va='center')

    pred = svm_load.predict([X_test[r].flatten()])

    c1, c2 = st.columns([1,1])

    with c1:
        st.markdown("###### Data Acak Terambil")
        st.pyplot(fig, use_container_width=True)

    with c2:
        st.markdown("###### :red[Hasil Prediksi!]")
        st.markdown("""
            <style>
            .big-font {
                font-size:200px !important;
                text-align: center;
            }
            


            </style>
            """, unsafe_allow_html=True)

        st.markdown('<p class="big-font">{}</p>'.format(pred[0]), unsafe_allow_html=True)
    st.markdown(""":rainbow[--------------------------------------------------------------------------------------------------------------------------------------------]""")
    if pred == y_test[r]:
        st.markdown('## :green[Prediksi BENAR]')
    else :
        st.markdown('## :red[Prediksi SALAH]')


st.markdown(""":rainbow[--------------------------------------------------------------------------------------------------------------------------------------------]""")

st.markdown('<div style="text-align: center"> <b>Hobi Data © 2023</b> </div>',  unsafe_allow_html=True)
st.markdown('<div style="text-align: center"> Contributor : Joko Eliyanto, Indra Cahya Ramdani </div>', unsafe_allow_html=True)