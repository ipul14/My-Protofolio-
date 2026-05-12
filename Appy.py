import streamlit as st
import os

st.set_page_config(
    page_title="Muchamad Nur Syaifulrahman | Portfolio",
    page_icon="👨‍✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Judul
st.title("Muchamad Nur Syaifulrahman")
st.markdown("**Airport Operation Management • Apron Movement Control Officer**")
st.caption("PT. Indonesia Weda Bay Industrial Park — Weda Bay Airport")

# Path file HTML
html_path = "Portofolio Muchamad Nur Syaifulrahman.html"

if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    st.components.v1.html(
        html_content,
        height=1900,      # Tinggi disesuaikan
        scrolling=True
    )
else:
    st.error("File HTML tidak ditemukan!")
    st.write("Pastikan nama file adalah: `Portofolio Muchamad Nur Syaifulrahman.html`")
