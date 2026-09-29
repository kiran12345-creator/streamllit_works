import streamlit as st
from blood_db import DonorListCreateRetrieveDeleteUpdate

st.title('retrieve')

id=st.number_input('Donor Id',min_value=0)

btn=st.button('retrieve')

b=DonorListCreateRetrieveDeleteUpdate()
record=b.retrieve(id)

if btn:
    if record:
        st.write('name: ',record[1])
        st.write('blood group: ', record[2])
        st.write('phone: ', record[3])
        st.write('city: ', record[4])
        st.write('last donation: ', record[5])