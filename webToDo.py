# A new project needs to create with only the files
# required for this webToDo application
# this is required for web deployment, so
# Other users can use this application

import streamlit as st
import webfunction

todoList = webfunction.get_todos()

def addTodo():
    new_todo = st.session_state["newTodo"]+"\n"
    todoList.append(new_todo)
    webfunction.write_todos(todoList)
    st.session_state["newTodo"] = ""

st.title("My toDo app")
st.subheader("Choose an item")

for index, item in enumerate(todoList):
    checkboxes = st.checkbox(item, key=item)
    if checkboxes:
        todoList.pop(index)
        webfunction.write_todos(todoList)
        del st.session_state[item]
        st.rerun()

st.text_input(label="new todo", placeholder="add an item", on_change=addTodo, key="newTodo")