import streamlit as st
from datetime import datetime

st.title("Halaman 4 - Notifikasi")

if not st.session_state.todos:
    st.warning("Belum ada to do")
else:
    now = datetime.now()
    st.write("🕒 Waktu sekarang:", now)

    st.subheader("Status To Do")
    for i, t in enumerate(st.session_state.todos):
        st.write(f"{i+1}. {t.task}")

        if t.datetime is None:
            st.info("Belum dijadwalkan")
        elif now >= t.datetime and not t.done:
            st.error("⏰ Waktunya mengerjakan tugas ini")
            t.mark_done()
        else:
            st.success("Masih ada waktu")
