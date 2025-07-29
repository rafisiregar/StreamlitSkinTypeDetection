import streamlit as st  # type: ignore
import os
from PIL import Image

def show():
    st.title("Exploratory Data Analysis (EDA) - Dataset Jenis Kulit Wajah")

    # EDA 1
    st.header("1. Distribusi Persentase Data (Train, Validation, Test)")
    image = Image.open("eda/persentase.png")
    st.image(image, caption="Distribusi Data Train, Validation, dan Test")
    st.markdown("""
    Berdasarkan grafik pie chart di atas, dapat diketahui distribusi data setelah proses splitting:
    
    - **Training**: 60.8%  
    - **Testing**: 20.4%  
    - **Validation**: 18.8%

    Dari total **966 gambar yang telah dibersihkan**, proporsi data cukup ideal.  
    Komposisi jenis kulit juga menunjukkan persebaran relatif seimbang dengan dominasi kategori **normal** dan **oily**, serta kategori **dry** sebagai minoritas.

    **Catatan Per Subset:**
    - Normal: ±34–35%
    - Oily: ±34%
    - Dry: ±31%
    """)

    # EDA 2
    st.header("2. Analisis Tekstur (Local Binary Pattern)")
    image = Image.open("eda/lbp.png")
    st.image(image, caption="Contoh Tekstur Gambar Setiap Kelas")
    st.markdown("""
    **Dry:** Kasar, banyak garis, tampak retak.  
    **Normal:** Rata, noise rendah, visual bersih.  
    **Oily:** Kompleks, pori besar, penuh noise.  

    **Kesimpulan:**  
    LBP efektif membedakan karakter tekstur tiap jenis kulit secara jelas.
    """)

    # EDA 3
    st.header("3. Distribusi Warna (RGB Histogram)")
    image = Image.open("eda/rgb.png")
    st.image(image, caption="Histogram RGB per Kelas Kulit")
    st.markdown("""
    **Dry:** Dominasi merah, kontras tinggi, distribusi tidak merata.  
    **Normal:** RGB stabil & natural.  
    **Oily:** Banyak pantulan → kurva tajam di area terang.

    **Kesimpulan:**  
    RGB Histogram memperkuat perbedaan visual berdasarkan intensitas warna yang khas.
    """)

    # EDA 4
    st.header("4. Analisis Brightness dan Contrast")
    image = Image.open("eda/b&c.png")
    st.image(image, caption="Brightness dan Contrast per Kategori")
    st.markdown("""
    **Dry:** Cerah, kontras moderat.  
    **Normal:** Paling variatif, kontras lembut.  
    **Oily:** Cenderung terang & tajam, mendukung efek kilap.

    **Kesimpulan:**  
    Tingkat pencahayaan dan ketajaman membantu identifikasi kilap dan kekasaran pada permukaan kulit.
    """)

    # EDA 5
    st.header("5. Overview Dataset")
    image = Image.open("eda/overview.png")
    st.image(image, caption="Brightness dan Contrast per Kategori")
    st.markdown("""
    | **Variabel**   | **Kelas Paling Menonjol** | **Rata-rata (Mean)**           | **Standar Deviasi (Std)**    | **Keterangan**                                                                                                    |
    | -------------- | ------------------------- | ------------------------------ | ---------------------------- | ----------------------------------------------------------------------------------------------------------------- |
    | **RGB**        | Oily                      | R ≈ 118.9, G ≈ 101.2, B ≈ 93.2 | R ≈ 36.7, G ≈ 32.6, B ≈ 31.8 | Kelas Oily menunjukkan distribusi warna paling tinggi karena refleksi kilap wajah.                                |
    | **Brightness** | Oily                      | 0.410 – 0.424                  | ±0.13                        | Kecerahan tinggi terjadi pada kelas Oily karena nilai RGB tinggi secara linear meningkatkan brightness.           |
    | **Contrast**   | Tidak signifikan          | 0.30 – 0.31                    | ±0.06 – 0.07                 | Nilai kontras merata antar kelas, tidak menunjukkan perbedaan signifikan.                                         |
    | **Texture**    | Normal                    | 19.1                           | ±1.5                         | Kelas Normal memiliki tekstur tertinggi, mengindikasikan kulit kasar atau berpori bila kualitas gambar diabaikan. |
    **Kesimpulan:**  
    Kesimpulannya, kelas Oily dominan pada nilai warna dan brightness, sedangkan kelas Normal menonjol pada tekstur. Contrast relatif merata antar kelas. Karena kualitas gambar buruk dan padding hitam tak konsisten, augmentasi difokuskan pada zoom, bukan perubahan warna atau pencahayaan, guna menghindari overfitting dan menjaga keaslian pola kulit, sesuai rekomendasi Hu et al. (2019).
    """)
    
    st.markdown("---")
    st.success("EDA selesai. Dataset ini menunjukkan kualitas visual yang representatif untuk pengklasifikasian jenis kulit wajah.")
