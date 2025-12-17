
import streamlit as st

st.title("Halaman 1 - Input Nama")

name = st.text_input("Masukkan nama kamu")

if st.button("Simpan Nama"):
    if name:
        st.session_state.name = name
        st.success("Nama berhasil disimpan")
    else:
        st.warning("Nama tidak boleh kosong")

if st.session_state.name:
    st.info(f"Halo, {st.session_state.name} 👋")