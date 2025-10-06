
import streamlit as st

st.title("MY PROJECT")
st.header("This is a header")
st.subheader("This is a subheader")
st.text("I love AI VIET NAM")


import streamlit as st

st.write('I love AI VIET NAM')
st.write('## Heading 2')
st.write('$ \\sqrt{2x+2} $')
st.write('1 + 1 = ', 2)


import streamlit as st

def get_name():
    st.write("Thai")

agree = st.checkbox("I agree", on_change=get_name)

if agree:
    st.write("Great!")

st.radio(
    "Your favorite color:",
    ['Yellow', 'Blue'],
    captions=['Vàng', 'Xanh']
)


import streamlit as st

option = st.selectbox(
    "Your contact:",
    ("Email", "Home phone", "Mobile phone")
)

st.write("Selected:", option)


import streamlit as st

color = st.select_slider(
    "Your favorite color:",
    options=["red", "orange", "violet"]
)

st.write("My favorite color is", color)


import streamlit as st

if st.button("Say hello"):
    st.write("Hello")
else:
    st.write("Goodbye")

st.link_button(
    "Go to Google",
    "https://www.google.com.vn/"
)


import streamlit as st

number = st.number_input("Insert a number")
st.write("The current number is ", number)

values = st.slider(
    "Select a range of values",
    0.0, 100.0, (25.0, 75.0)
)
st.write("Values:", values)

import streamlit as st

messages = st.container(height=200)

if prompt := st.chat_input("Say something"):
    messages.chat_message("user").write(prompt)
    messages.chat_message("assistant").write(f"Echo: {prompt}")


import streamlit as st

uploaded_files = st.file_uploader(
    "Choose files",
    accept_multiple_files=True
)

for uploaded_file in uploaded_files:
    bytes_data = uploaded_file.read()
    st.write("filename:", uploaded_file.name)


import streamlit as st

if st.button("Say hello"):
    st.write("Hello")
else:
    st.write("Goodbye")

st.link_button(
    "Go to Google",
    "https://www.google.com.vn/"
)
