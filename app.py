import streamlit as st

st.title("My first WebApp")

st.subheader("This App is the Best")

st.selectbox("Gender", ["Male","Female", "Other"])

w = st.number_input("How much do you weigh")
h = st.number_input("How tall are you in metres")

def bmi_calc(w,h):
    bmi = round(w/(h**2),1)
    return bmi
a1,a2 = st.columns(2)

with a1:
    st.checkbox("Accept")
    st.text_input("What is your name")
    st.number_input("How old are you now",step=1)
    
with a2:
    st.checkbox("Reject")
    st.text_area("Address")
    st.date_input("Date of last visit")
    
if st.button("Calculate"):
    st.balloons()
    st.write(bmi_calc(w,h))

