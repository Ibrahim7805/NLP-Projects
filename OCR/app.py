import streamlit as st
import numpy as np
import pytesseract
from PIL import Image
import re


pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

st.set_page_config(page_title="Smart OCR Scanner", layout="wide")



st.title("📄 Document Analysis")


upload = st.file_uploader('Upload your document...', type=['png', 'jpg', 'jpeg'])


lang_option = st.selectbox("Select Document Language",
                           options=["eng", "ara", "eng+ara"],
                           index=0,
                           help="Choose 'ara' for Arabic, 'eng' for English")


# --- 3. التحقق من الرفع ---
if upload is not None:
    # قراءة الصورة
    img = Image.open(upload)

    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader("🖼️ Preview")
        st.image(img, use_container_width=True)

    with col2:
        st.subheader("📊 Extraction Results")
        with st.spinner('Processing...'):
            # استخراج النص
            text = pytesseract.image_to_string(img, lang=lang_option)

            # تقسيم النص لأسطر وتنظيفها
            lines = [line.strip() for line in text.splitlines() if line.strip()]

            st.text_area("All Extracted Text", text, height=300)
            st.download_button("Download as TXT", text, file_name="scanned_doc.txt")
else:
    # رسالة تظهر في حالة عدم وجود ملف (تمنع حدوث الـ NameError)
    st.info("Please upload an image to start analysis.")