import streamlit as s
s.header('multiplication')
num1=s.number_input('enter first number',min_value=0)
num2=s.number_input('enter second number',min_value=0)
sum=num1*num2
btn=s.button('MUL')
if btn:
    s.write('product is',sum)