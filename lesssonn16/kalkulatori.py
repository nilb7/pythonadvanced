import streamlit as st

def kalkulatori():
    st.title("Simple Calculator")

    num1 = st.number_input("Enter the first number",step=1)

    num2 = st.number_input("Enter the second number", step=1)


operation = st.radio("selected operation",["mbledhje","zbrijte","shumezim","pjestim"])

