import streamlit as st
import pandas as pd

st.title("STUDENT MARKS CALCULATAR")

st.markdown("#### Enter student details and marks to calculate totals, percentage, and display results interactively.")
Name =st.text_input("Enter your name : ")
Roll_Number = st.text_input("Enter your roll number")
KANNADA = st.number_input("Enter the KANNADA marks ",min_value=0,max_value=100)
ENGLISH = st.number_input("Enter the ENGLISH marks",min_value=0,max_value=100)
HINDI = st.number_input("Enter the HINDI marks ",min_value=0,max_value=100)
MATHS = st.number_input("Enter the MATHS marks ",min_value=0,max_value=100)
SOCIAL_SCIENCE = st.number_input("Enter the SOCIAL SCIENCE marks ",min_value=0,max_value=100)
SCIENCE = st.number_input("Enter the SCIENCE marks ",min_value=0,max_value=100)
TOTAL = KANNADA+ENGLISH+HINDI+MATHS+SOCIAL_SCIENCE+SCIENCE
AVERAGE = TOTAL//6
if st.button("CALCULATE"):
    st.write("Name:                    ",Name)
    st.write("Roll number:           ",Roll_Number)

    data = {"Subjects":["KANNADA","ENGLISH","HINDI","MATHS","SOCIAL_SCIENCE","SCIENCE"],
        "marks":[KANNADA,ENGLISH,HINDI,MATHS,SOCIAL_SCIENCE,SCIENCE]}
    df = pd.DataFrame(data)
    st.table(df)

    TOTAL = KANNADA+ENGLISH+HINDI+MATHS+SOCIAL_SCIENCE+SCIENCE
    AVERAGE = TOTAL//6
    st.write("YOUR TOTAL MARKS ",TOTAL)
    st.write("YOUR AVERAGE MARKS  ",AVERAGE)
    if AVERAGE>=92:
        st.write("Grade: A+")
    elif AVERAGE>=85:
        st.write("Grade: A")
    elif AVERAGE>=70:
        st.write("Grade: B+")
    elif AVERAGE>=60:
        st.write("Grade: B")
    elif AVERAGE>=40:
        st.write("Grade: C+")
    else:
        st.write("Grade: C")
    if AVERAGE>=35:
       st.balloons()  
       st.success("pass")
    else:
        st.error("Fail")
else:
    st.error("please enter remaining subjects")


