import streamlit as st
import os

st.set_page_config(
    page_title="Muchamad Nur Syaifulrahman | Portfolio",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.title("✈️ Muchamad Nur Syaifulrahman")
st.caption("Airport Operation Management • AMC Officer • Weda Bay Airport")

html_path = "Portofolio Muchamad Nur Syaifulrahman.html"

if os.path.exists(html_path):
    with open(html_path, "r", encoding="utf-8") as f:
        html_content = f.read()
    
    st.components.v1.html(
        html_content,
        height=1800,      # Tinggi yang cukup untuk portfolio
        scrolling=True,
        width=None
    )
    
    st.success("✅ Portfolio berhasil dimuat")
    
else:
    st.error("❌ File HTML tidak ditemukan!")
    st.write(f"Path yang dicari: `{html_path}`")
    st.info("Pastikan nama file persis sama (termasuk spasi)")
