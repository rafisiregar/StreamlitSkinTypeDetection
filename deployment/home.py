import streamlit as st # type:ignore
import matplotlib.pyplot as plt

def show():
    st.title("🧴 Dashboard Deteksi Jenis Kulit Wajah")

    st.markdown("""
### 🎯 Tujuan Dashboard

Dashboard ini dikembangkan untuk:
- Mengeksplorasi data gambar wajah berdasarkan jenis kulit.
- Memprediksi kategori kulit wajah: **dry**, **normal**, atau **oily** menggunakan model deep learning (CNN)
- Menyajikan visualisasi performa model secara interaktif dan informatif.

---

### 💡 Latar Belakang Studi Kasus

Saya adalah seorang **data scientist** di salah satu klinik kecantikan ternama di Jakarta. Seiring meningkatnya permintaan akan solusi perawatan kulit yang lebih **personalisasi**, tim kami berinisiatif mengembangkan teknologi berbasis *machine learning* untuk mengenali jenis kulit seseorang secara otomatis: **berminyak**, **kering**, atau **normal**.

---

### 🧠 Arsitektur Model

Model ini pakai **ResNet50** pretrained dari ImageNet, difungsikan sebagai feature extractor dengan bobot yang dibekukan untuk ekstraksi fitur. Lalu ditambah beberapa layer custom seperti **Dense**, **Dropout**, dan **BatchNormalization** buat klasifikasi ke 3 kelas: `dry`, `normal`, `oily`.

Optimisasi menggunakan **SGD** (learning rate 0.001, momentum 0.9), plus **EarlyStopping** agar mencegah overfitting.

**Hasil Evaluasi:**
-  Akurasi Data Train: **35.8%**
-  Akurasi Data Testing: **34.3%**
-  Model sering salah fokus memprediksi kelas *normal* 
-  Skor f1 untuk *dry* dan *oily* masih rendah

> Kesimpulan: Model kuat secara arsitektur, namun performanya masih belum maksimal. Perlu perbaikan pada kualitas data yang diterima, proses augmentasi, atau fine-tuning layer dari model-model yang telah digunakan.

---

### 📁 Dataset yang Digunakan

Model ini dilatih menggunakan dataset dari:

- [Kaggle: Oily, Dry and Normal Skin Types Dataset](https://www.kaggle.com/datasets/shakyadissanayake/oily-dry-and-normal-skin-types-dataset)
- Dataset ini telah **dimodifikasi dan dibersihkan** berdasarkan hasil analisis lanjutan yang dapat diakses pada link [Google Drive](https://drive.google.com/file/d/1yj7q6PpGgSyvAobcTm04imGK-cyosdVb/view?usp=sharing).
- Dataset mencakup 3 kelas jenis kulit wajah:
  - **Dry**
  - **Normal**
  - **Oily**

**Distribusi citra setelah dibersihkan:**
""")

    # Tampilkan pie chart
    labels = ['Training (677)', 'Testing (195)', 'Validation (94)']
    sizes = [677, 195, 94]
    colors = ['#8ecae6', '#ffb703', '#fb8500']

    fig, ax = plt.subplots(figsize=(3.5, 3.5))
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    st.pyplot(fig)

    st.markdown("---")

    st.markdown("""
### 🛠️ Petunjuk Penggunaan Aplikasi

- Gunakan sidebar di sebelah kiri untuk navigasi:
  - 🔍 Home
  - 📊 Expanatory Data Analysis
  - 📷 Prediksi Gambar

- Unggah gambar wajah dalam format **.jpg** atau **.png**
- Model akan menampilkan hasil prediksi jenis kulit dan tingkat kepercayaannya secara otomatis
- Hasil pemodelan belum menunjukan presisi yang optimal, namun tetap dapat digunakan untuk demonstrasi pada tahapan early development pengembangan program ini.

---

Selamat mencoba dan semoga bermanfaat! 🌿✨
""")
