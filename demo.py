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


