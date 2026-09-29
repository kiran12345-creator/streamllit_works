import streamlit as st
from library_db import BookListCreateRetrieveDeleteUpdate
st.title('retrieve')
id=st.number_input('Book Id',min_value=0)
btn=st.button('retrieve')
b = BookListCreateRetrieveDeleteUpdate()
record=b.retrieve(id)
if btn:
    if record:
        st.write('title: ',record[1])
        st.write('author: ', record[2])
        st.write('price: ', record[3])
        st.write('language :' ,record[4])
        st.write('pages: ', record[5])

