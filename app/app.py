import streamlit as st

st.title("Prediksi Penyakit Berdasarkan Gejala")
st.write("Website ini dibuat oleh Kelompok X untuk UAS Machine Learning.")

symptoms = st.text_input("Masukkan gejala (dipisahkan koma)")

if st.button("Prediksi"):
    st.write("Model belum dimasukkan. Menunggu anggota 2 & 3.")