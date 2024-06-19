import streamlit as st
import functions as fun
todos=fun.call()
def add_todo():
    t=st.session_state["newtodo"]+ "\n"
    todos.append(t)
    fun.change(todos)

st.title("My Todo App")
st.subheader("Hello, let's start!")
st.write("Being productive one step at a time")
for i, todo in enumerate(todos):  # Use enumerate to get index and item
    checkb = st.checkbox(todo, key=i)  # Set key using the index
    if checkb:
        todos.remove(todo)
        fun.change(todos)
        del st.session_state[todo]
        st.experimental_rerun()
st.text_input(label=" ",placeholder="Add a todo...",
              on_change=add_todo,key="newtodo")
