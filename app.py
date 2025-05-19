import streamlit as st
from transformers import pipeline

st.set_page_config(page_title="AI Notes Summarizer", layout="wide")

st.title("🧠 AI Notes Summarizer")
st.write("Masukkan teks panjang di bawah ini untuk diringkas oleh model AI.")

text_input = st.text_area("Teks Input", height=300)

if st.button("Ringkas"):
    with st.spinner("Merangkum..."):
        summarizer = pipeline("summarization")
        result = summarizer(text_input, max_length=100, min_length=25, do_sample=False)

if result and 'summary_text' in result[0]:
    summary = result[0]['summary_text']
else:
    summary = "Tidak dapat menghasilkan ringkasan. Coba masukkan teks yang lebih panjang."

        st.subheader("💡 Hasil Ringkasan:")
        st.success(summary)
