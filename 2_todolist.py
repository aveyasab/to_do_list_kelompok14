import streamlit as st
from todo import Todo

# INIT
if "name" not in st.session_state:
    st.session_state.name = ""

if "todos" not in st.session_state:
    st.session_state.todos = []

st.title("Halaman 2 - To Do List")

if st.session_state.name == "":
    st.warning("Isi nama dulu di Halaman 1")
else:
    task = st.text_input("Masukkan tugas")

    if st.button("Tambah"):
        if task:
            todo = Todo(task)          # object
            st.session_state.todos.append(todo)
            st.success("Tugas ditambahkan")
        else:
            st.warning("Tugas kosong")

    st.subheader("Daftar Tugas")

    for i in range(len(st.session_state.todos)):   # for
        st.write(f"{i+1}. {st.session_state.todos[i].task}")

