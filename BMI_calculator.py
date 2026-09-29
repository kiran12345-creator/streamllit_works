import streamlit as s
weight=s.number_input('enter weight in kg',min_value=1)
height=s.number_input('enter height in cm',min_value=1)
bmi=(weight//(height/100)**2)
button1=s.button('calculate')
s.write('BMI is ',bmi)
if button1:
    if bmi<18.5:
        s.info('under weight')
    elif 18.5 < bmi <25:
        s.success('normal')
    elif 25 < bmi < 30:
        s.warning('over weight')
    elif 'bmi>30'    :
        s.error('obese')
