import streamlit as st
from datetime import datetime, date, time

# =========================
# CLASS & OBJECT (OOP)
# =========================
class Todo:
    def __init__(self, task):
        self.task = task
        self.datetime = None
        self.done = False

    def set_datetime(self, dt):
        self.datetime = dt

    def mark_done(self):
        self.done = True


# =========================
# SESSION STATE
# =========================
if "name" not in st.session_state:
    st.session_state.name = ""

if "todos" not in st.session_state:
    st.session_state.todos = []


# =========================
# SIDEBAR PAGES
# =========================
page = st.sidebar.selectbox(
    "Pilih Halaman",
    (
        "Halaman 1 - Input Nama",
        "Halaman 2 - To Do List",
        "Halaman 3 - Tanggal & Waktu",
        "Halaman 4 - Notifikasi",
    ),
)

# =========================
# HALAMAN 1 - NAMA
# =========================
if page == "Halaman 1 - Input Nama":
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


# =========================
# HALAMAN 2 - TODO LIST
# =========================
elif page == "Halaman 2 - To Do List":
    st.title("Halaman 2 - To Do List")

    if not st.session_state.name:
        st.warning("Silakan isi nama di Halaman 1 terlebih dahulu")
    else:
        task = st.text_input("Masukkan tugas")

        if st.button("Tambah To Do"):
            if task:
                todo_obj = Todo(task)
                st.session_state.todos.append(todo_obj)
                st.success("To do berhasil ditambahkan")
            else:
                st.warning("Tugas tidak boleh kosong")

        st.subheader("Daftar To Do")
        for i, t in enumerate(st.session_state.todos):
            st.write(f"{i+1}. {t.task}")


# =========================
# HALAMAN 3 - TANGGAL & WAKTU
# =========================
elif page == "Halaman 3 - Tanggal & Waktu":
    st.title("Halaman 3 - Input Tanggal & Waktu")

    if not st.session_state.todos:
        st.warning("Belum ada to do di Halaman 2")
    else:
        selected = st.selectbox(
            "Pilih To Do",
            range(len(st.session_state.todos)),
            format_func=lambda x: st.session_state.todos[x].task,
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


# =========================
# HALAMAN 4 - NOTIFIKASI
# =========================
elif page == "Halaman 4 - Notifikasi":
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
