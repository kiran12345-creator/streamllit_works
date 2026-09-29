import streamlit as s
s.header('Division')
num1=s.number_input('enter first number',min_value=1)
num2=s.number_input('enter second number',min_value=1)
sum=num1/num2
btn=s.button('dIV')
if btn:
    s.write('quotient is',sum)