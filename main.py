import streamlit as st

st.title("Welcome to Rao Azlan Website")
st.button("Submit")
st.header("Python")
st.subheader("Java")
st.markdown("I love Python")
st.color_picker("red")
st.text("My name is Muhammad Azlan")
name=st.text_input("Enter Your Name:")
Fname=st.text_input("Enter Your fName")
Address=st.text_area("Enter Your Detail:")
Class=st.selectbox("Enter Your Class:",(1,2,3,4,5,6,7,8,9,10))
button=st.button("Done")
if button :
    st.markdown(f"""
name :{name}
father name :{Fname}
address : {Address}
class :{Class}""")