import streamlit as s
s.header('ADDITION')
num1=s.number_input('enter first number',min_value=0)
num2=s.number_input('enter second number',min_value=0)
sum=num1+num2
btn=s.button('ADD')
if btn:
    s.write('sum is',sum)