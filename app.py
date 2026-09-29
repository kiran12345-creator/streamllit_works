import streamlit as st

#number_input()
num1=st.number_input('enter first number',min_value=0)
num2=st.number_input('enter second number',min_value=0)


#text_input()
text=st.text_input('enter your name')



#data
date=st.date_input('enter date of birth')


#button
btn=st.button('click')
#print(btn)
if btn:
    st.write(num1)
    st.write(num2)
    st.write(text)
    st.write(date)