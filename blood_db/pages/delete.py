import streamlit as st

from blood_db import DonorListCreateRetrieveDeleteUpdate

st.title('delete')

id=st.number_input('Donor Id',min_value=0)

btn=st.button('delete')

if btn:
    b = DonorListCreateRetrieveDeleteUpdate()
    record = b.retrieve(id)

    if record:
        b.delete(id)
        st.write('deleted sucessfully')
    else:
        st.write('no record')