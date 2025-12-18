import streamlit as st
from datetime import datetime
import pytz

st.title("⏰ Cek Notifikasi To-Do")

# Validasi data
if "todo_text" not in st.session_state:
    st.warning("Silakan isi to-do dan waktu terlebih dahulu.")
    st.stop()

wib = pytz.timezone("Asia/Jakarta")

now = datetime.now(wib)
st.write("🕒 Waktu sekarang (WIB):", now.strftime("%H:%M:%S"))

target_datetime = datetime.combine(
    st.session_state.todo_date,
    st.session_state.todo_time
)
target_datetime = wib.localize(target_datetime)

st.write("🎯 Waktu target:", target_datetime.strftime("%H:%M:%S"))

# ===== TOMBOL CEK =====
if st.button("🔔 Cek Notifikasi"):
    if now >= target_datetime:
        st.success(f"Waktunya mengerjakan: {st.session_state.todo_text}")
    else:
        sisa = target_datetime - now
        menit = sisa.seconds // 60
        st.info(f"⏳ Belum waktunya ({menit} menit lagi)")

