import streamlit as st # type:ignore
import sidebar as sd

# Set page config
st.set_page_config(page_title="Deteksi Jenis Kulit Wajah", layout="wide", initial_sidebar_state="expanded")
page = sd.render_sidebar()

import prediction 
import home 
import eda

if page == "Home":
    home.show()
elif page == "Prediction":
    prediction.show()
elif page == "Exploratory Data Analysis":
    eda.show()