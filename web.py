import streamlit as st
import functions as fun
st.title("My Todo App")
st.subheader("Hello, let's start!")
st.write("Being productive one step at a time")
todos=fun.call()
for i in todos:
    st.checkbox(i)
st.text_input(label="",placeholder="Add a todo...")