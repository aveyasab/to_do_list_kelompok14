import streamlit as st

st.sidebar.title("Menu")

page = st.sidebar.radio(
    "Pilih Halaman",
    (
        "Halaman 1 - Input Nama",
        "Halaman 2 - To Do List",
        "Halaman 3 - Jadwal",
        "Halaman 4 - Notifikasi",
    ),
)

if page == "Halaman 1 - Input Nama":
    exec(open("1_home.py", encoding="utf-8").read())
elif page == "Halaman 2 - To Do List":
    exec(open("2_todolist.py", encoding="utf-8").read())
elif page == "Halaman 3 - Jadwal":
    exec(open("3_schedule.py", encoding="utf-8").read())
elif page == "Halaman 4 - Notifikasi":
    exec(open("4_notification.py", encoding="utf-8").read())

