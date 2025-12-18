import streamlit as st

# INIT SESSION
if "name" not in st.session_state:
    st.session_state.name = ""

st.title("Halaman 1 - Input Nama")

def simpan_nama(nama):        # function
    st.session_state.name = nama

nama = st.text_input("Masukkan nama kamu")

if st.button("Simpan"):
    if nama != "":            # if
        simpan_nama(nama)
        st.success("Nama tersimpan")
    else:                     # else
        st.warning("Nama tidak boleh kosong")

if st.session_state.name:
    st.info(f"Halo, {st.session_state.name} 👋")

