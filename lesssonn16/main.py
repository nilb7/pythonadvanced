import streamlit as st

def main():
    st.title("Hello World")

    st.button("click me")

st.checkbox("check me")

if st.checkbox("check me to show some text"):
    st.write("qiky tekst po shfaqet sepse ti e ke check katrorin e zbrazet")

if st.button("click"):
    st.write("Button Clicked")

name=st.text_input("Enter your name")

st.write("your name is: " ,name)

age = st.number_input("Enter your age",min_value=0,max_value=100)
st.write("your age is:" ,age)

message = st.text_area("enter a message")

if st.button("Succes"):
    st.success("Opperation was successful")

if __name__ == "__main__":
    main()