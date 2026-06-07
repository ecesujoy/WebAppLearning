# A new project needs to create with only the files
# required for this webToDo application
# this is required for web deployment, so
# other users can use this application

# "pip freeze > requirements.txt" will create a requirements.txt file
# in the project directory. This is the file which will uploaded to the
# server where we host the webapp. So that the Server should know all the
# Python libraries the server needs to install in order to run the app.
# You are telling server what packages are required
# "pip freeze" -> will list all the required pkg names
# "pip freeze > requirements.txt" -> will write those pkgs in the req.txt file
# need to add in version control>git
# create a repo in github, copy the url, "pycharm>git>ManageRemote>add the url"

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