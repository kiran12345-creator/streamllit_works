import streamlit as st
from blood_db import DonorListCreateRetrieveDeleteUpdate

st.title('Add new donor')

name=st.text_input('enter donor name')
blood_group=st.selectbox('blood group',['A+','A-','B+','B-','AB+','AB-','O+','O-'])
phone=st.text_input('enter phone number')
city=st.text_input('enter city')
last_donation=st.date_input('last donation')

btn=st.button('ADD')

if btn:
    b=DonorListCreateRetrieveDeleteUpdate()
    b.create(name,blood_group,phone,city,last_donation)
    st.success('record created sucessfully')
else:
    st.error('invalid response')