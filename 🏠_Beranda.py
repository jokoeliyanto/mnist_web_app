import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Klasifikasi Gambar Angka MNIST",
    page_icon="logo_hoda.png",
)

st.write("# ⛺ :red[Klasifikasi Gambar Angka MNIST]")


st.markdown(""":rainbow[--------------------------------------------------------------------------------------------------------------------------------------------]""")
st.markdown('<div style="text-align: center"> <b>وَعَلَّمَ ءَادَمَ ٱلْأَسْمَآءَ كُلَّهَا ثُمَّ عَرَضَهُمْ عَلَى ٱلْمَلَـٰٓئِكَةِ فَقَالَ أَنۢبِـُٔونِى بِأَسْمَآءِ هَـٰٓؤُلَآءِ إِن كُنتُمْ صَـٰدِقِينَ  </div>',  unsafe_allow_html=True)
st.markdown('<div style="text-align: center , font-family:   Helvetica, sans-serif"> Dan <b>Dia ajarkan kepada Adam nama-nama (benda) semuanya</b>, kemudian Dia perlihatkan kepada para malaikat, seraya berfirman, "Sebutkan kepada-Ku nama semua benda ini, jika kalian yang benar!"</div>',  unsafe_allow_html=True)
st.markdown('<div style="text-align: center"> <b>QS Al-Baqarah : 31</b> </div>',  unsafe_allow_html=True)
st.markdown(""":rainbow[--------------------------------------------------------------------------------------------------------------------------------------------]""")

st.markdown(
    """
    Bagaimana komputer bisa mengenali gambar angka seperti manusia? Ini merupakan contoh masalah klasifikasi yang juga merupakan bagian awal dari pembahasan Computer Vision. 
"""
)

st.markdown(
    """
    **👈 Anda bisa mengakses Web App Klasifikasi Gambar Angka MNIST** pada sidebar di samping!

    ### Dataset Gambar Angka MNIST
"""
)

st.markdown(
    """
    - Data Gambar Angka MNIST diambil dari web berikut [Angka MNIST](https://www.tensorflow.org/datasets/catalog/mnist)
    - Ini merupakan dataset gambar/tulisan tangan angka 0 - 9   
    - Data ini disimpan dalam numpy array berukuran 28x28 yaitu nilai piksel warna gray untuk membentuk tampilan gambar angka
    - Dataset terdiri dari 60000 data latih dan 10000 data uji 
    - Kita akan mempelajari bagaimana membagun pemodelan klasifikasi untuk gambar tulisan tangan angka MNIST
    

    ### Visualisasi Dataset Gambar Angka MNIST

    Secara umum, dataset ini merupakan gambar angka yang telah distandarisasi menjadi matriks gradasi warna ukuran 28x28 untuk setiap angka sebagai berikut:

"""
)

st.image("angka mnist dataset.png")

st.markdown(
"""
    Lebih detail lagi, setiap gambar pada data ini dapat divisualisasikan dalam bentuk matriks seperti berikut:
"""
)

st.image("angka mnist sampel.png")


st.markdown(
"""
    ### Pemodelan Klasifikasi Gambar Angka MNIST
    Berikut kami telah melakukan pemodelan Klasifikasi Gambar Angka MNIST dengan hasil sebagai berikut:
"""
)


df_pre= pd.DataFrame({ 'Support Vector Machine' : [97.92],
                        'Naive Bayes' : [55.58],
                        'Decicion Tree' : [87.79],
                        'Gradien Boosting' : [97.89]
})

df_p = df_pre.style.highlight_max(color = 'red', axis = 1)
# df_p_f = AgGrid(df_pre)
st.dataframe(df_p, use_container_width=True, hide_index=True)

st.markdown(
"""
    Berdasarkan hasil di atas, maka akan diimplementasi model **:red[Support Vector Machine]** pada web-app ini
"""
)
st.markdown(""":rainbow[--------------------------------------------------------------------------------------------------------------------------------------------]""")

st.markdown('<div style="text-align: center"> <b>Hobi Data © 2023</b> </div>',  unsafe_allow_html=True)
st.markdown('<div style="text-align: center"> Contributor : Joko Eliyanto, Indra Cahya Ramdani </div>', unsafe_allow_html=True)
    
