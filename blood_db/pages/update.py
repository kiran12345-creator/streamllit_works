import streamlit as st

st.title('update')

from blood_db import DonorListCreateRetrieveDeleteUpdate

id = st.number_input('enter id', min_value=0)

name = st.text_input('enter donor name')

blood_group = st.text_input('blood group')

phone = st.text_input('phone')

city = st.text_input('city')

last_donation = st.date_input('last donation')

btn=st.button('update')

if btn:
    b = DonorListCreateRetrieveDeleteUpdate()
    b.update(id, name, blood_group, phone, city, last_donation)