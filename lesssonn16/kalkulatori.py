import streamlit as st
from final_project3 import result_label


def kalkulo(num1,num2,operation):
    if operation=="mbledhje":
        result = num1+num2
    elif operation=="zbrijte":
        result=num1-num2
    return  result
st.title("Simple Calculator")

num1 = st.number_input("Enter the first number",step=1)

num2 = st.number_input("Enter the second number", step=1)


operation = st.radio("selected operation",["mbledhje","zbrijte","shumezim","pjestim"])

result = kalkulo(num1,num2,operation)
st.write(result)