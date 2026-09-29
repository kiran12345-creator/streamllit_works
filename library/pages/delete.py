import streamlit as st

from library_db import BookListCreateRetrieveDeleteUpdate
st.title('delete')
id=st.number_input('Book Id',min_value=0)
btn=st.button('delete')
if btn:
    b = BookListCreateRetrieveDeleteUpdate()
    record = b.retrieve(id)
    if record:
        b.delete(id)
        st.write('deleted sucessfully')
    else:
        st.write('no record')