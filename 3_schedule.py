import streamlit as st
from datetime import datetime, date, time

st.title("Halaman 3 - Tanggal & Waktu")

if not st.session_state.todos:
    st.warning("Belum ada to do di Halaman 2")
else:
    selected = st.selectbox(
        "Pilih To Do",
        range(len(st.session_state.todos)),
        format_func=lambda x: st.session_state.todos[x].task
    )

    tgl = st.date_input("Pilih tanggal", date.today())
    jam = st.time_input("Pilih waktu", time(12, 0))

    if st.button("Simpan Jadwal"):
        dt = datetime.combine(tgl, jam)
        st.session_state.todos[selected].set_datetime(dt)
        st.success("Tanggal dan waktu berhasil disimpan")

    st.subheader("Jadwal To Do")
    for t in st.session_state.todos:
        if t.datetime:
            st.write(f"{t.task} → {t.datetime}")


