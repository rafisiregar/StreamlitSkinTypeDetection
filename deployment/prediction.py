# type: ignore
import streamlit as st
import numpy as np
from PIL import Image
import tensorflow as tf
from tensorflow.keras.preprocessing import image as keras_image

# Load model dan label
model = tf.keras.models.load_model("deployment/best_model_r50.keras")
class_labels = ['dry', 'normal', 'oily']

# Streamlit UI
def show():
    st.title("🧴 Prediksi Jenis Kulit Wajah")
    st.markdown("Unggah gambar wajah untuk memprediksi apakah kulit tergolong **dry**, **normal**, atau **oily**.")

    uploaded_file = st.file_uploader("📤 Upload gambar wajah", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        st.subheader("🖼️ Gambar yang Diunggah")
        image_data = Image.open(uploaded_file).convert("RGB")
        st.image(image_data, width=350)

        st.markdown("### 📝 Pilih label sebenarnya (aktual):")
        selected_label = st.radio(" ", options=class_labels, horizontal=False, label_visibility="collapsed")

        if st.button("🔍 Submit & Prediksi"):
            # Preprocessing
            img_resized = image_data.resize((224, 224))
            img_array = keras_image.img_to_array(img_resized) / 255.0
            img_array = np.expand_dims(img_array, axis=0)

            # Predict
            prediction = model.predict(img_array)
            print("Raw prediction:", prediction)

            predicted_index = int(np.argmax(prediction))
            predicted_label = class_labels[predicted_index]
            confidence = float(np.max(prediction)) * 100

            # Output utama
            st.markdown("### 📌 Hasil Prediksi Model")
            st.success(f"**Klasifikasi:** Tipe Kulit **{predicted_label.capitalize()}**")
            st.info(f"**Probabilitas:** {confidence:.2f}%")

            # Ground truth
            st.markdown("---")
            st.markdown("### ✅ Hasil Aktual Data/Gambar")
            st.success(f"**Klasifikasi:** Tipe Kulit **{selected_label.capitalize()}**")

            # Perbandingan
            if predicted_label.lower() == selected_label.lower():
                st.success("✅ Prediksi sesuai dengan label yang dipilih.")
            else:
                st.error("❌ Prediksi tidak sesuai dengan label yang dipilih.")

# Run
if __name__ == "__main__":
    show()
