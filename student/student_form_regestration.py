import streamlit as s
from datetime import date
s.subheader('student Registration form')
n=s.text_input('name')
a=s.number_input('age',min_value=0)
d=s.date_input('DOB',min_value=date(2000,1,1),
                        max_value=date.today(),
                         value=date.today())
e=s.text_input('email')
g=s.radio('Gender',['male','female'])
sb=s.selectbox('choose domain',['dot net','testing','python'])
b=s.button('register')
if b :
    s.write('name : ',n)
    s.write('age : ',a )
    s.write('doB : ',d )
    s.write('email : ',e )
    s.write('gender : ',g )
    s.write('domain : ',sb )

