import streamlit as st
from library_db import BookListCreateRetrieveDeleteUpdate
st.title('Add new record')

title=st.text_input('enter the title of book')
author=st.text_input('enter author name')
language=st.selectbox('language',['english','malayalam','hindi','french','spanish'])
pages=st.number_input('number of pages',min_value=0)
price=st.number_input('price of the book',min_value=0)
btn=st.button('ADD')
if btn:
    b=BookListCreateRetrieveDeleteUpdate()
    b.create(title,author,price,language,pages)
    st.success('record created sucessfully')
else:
    st.error('invalid response')