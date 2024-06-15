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
for i in todos:
    checkb=st.checkbox(i,key=i)
    if checkb:
        todos.remove(i)
        fun.change(todos)
        del st.session_state[i]
        st.experimental_rerun()
st.text_input(label=" ",placeholder="Add a todo...",
              on_change=add_todo,key="newtodo")
