import streamlit as st
from datetime import date, time, datetime

# INIT
if "todos" not in st.session_state:
    st.session_state.todos = []

st.title("Halaman 3 - Jadwal")

if len(st.session_state.todos) == 0:
    st.warning("Belum ada to do")
else:
    pilihan = st.selectbox(
        "Pilih tugas",
        range(len(st.session_state.todos)),
        format_func=lambda x: st.session_state.todos[x].task
    )

    tgl = st.date_input("Tanggal", date.today())
    jam = st.time_input("Waktu", time(12, 0))

    if st.button("Simpan Jadwal"):
        dt = datetime.combine(tgl, jam)
        st.session_state.todos[pilihan].set_datetime(dt)
        st.success("Jadwal disimpan")

    for t in st.session_state.todos:    # for
        if t.datetime:
            st.write(f"{t.task} → {t.datetime}")

