import streamlit as st
from app import Todo

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
