import streamlit as st
from blood_db import DonorListCreateRetrieveDeleteUpdate

st.title('read')

btn=st.button('display all records')

if btn:
    b=DonorListCreateRetrieveDeleteUpdate()
    records=b.list()

    if records:
        st.table(records)
    else:
        st.info('No record found')