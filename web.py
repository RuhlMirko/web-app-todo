import streamlit as st
import functions

todo_list = functions.get_todo_list()


def add_todo():
    todo_local = st.session_state['new_todo']

    todo_list.append(todo_local + '\n')
    functions.set_todo_list(todo_list)

    st.session_state['new_todo'] = ""  # Clears the text input


st.title("My todo app")
st.subheader("This is my web todo app")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todo_list):
    checkbox = st.checkbox(todo.strip('\n'), key=todo)
    if checkbox:
        todo_list.pop(index)
        functions.set_todo_list(todo_list)
        del st.session_state[todo]
        st.rerun()  # Needed for checkboxes

st.text_input(label="New Todo:", placeholder="Add new todo", on_change=add_todo, key='new_todo')

# st.session_state
