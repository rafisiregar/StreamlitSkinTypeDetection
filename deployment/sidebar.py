import streamlit as st  # type: ignore

def render_sidebar():
    st.sidebar.title("🧴 Deteksi Jenis Kulit Wajah")
    st.sidebar.markdown(
        """
        Aplikasi ini bertujuan untuk **mengidentifikasi jenis kulit wajah**
        guna memberikan rekomendasi produk kecantikan yang sesuai.
        Proses deteksi dilakukan menggunakan metode **Convolutional Neural Network (CNN)** 
        berbasis *Computer Vision*. Unggah gambar wajah untuk melihat prediksi secara real-time.
        """
    )
    st.sidebar.markdown("---")
    
    st.sidebar.markdown("### 🧭 Navigasi")
    selected = st.sidebar.radio("Pilih halaman:", ["Home", "Exploratory Data Analysis", "Prediction"])
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("Made by Rafi Siregar")

    return selected
