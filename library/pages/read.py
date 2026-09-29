import streamlit as st
from library_db import BookListCreateRetrieveDeleteUpdate
st.title('read')
btn=st.button('display all records')
if btn:
    b=BookListCreateRetrieveDeleteUpdate()
    records=b.list()
    if records:
        st.table(records)
    else:
        st.info('No record found')
