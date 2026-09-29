import streamlit as st
st.title('update')
from library_db import BookListCreateRetrieveDeleteUpdate
id = st.number_input('enter id', min_value=0)
title = st.text_input('enter title')
author = st.text_input('enter author')
pages = st.number_input('number of pages')
language = st.text_input('language')
price = st.text_input('price')

btn=st.button('update')
if btn:
    b = BookListCreateRetrieveDeleteUpdate()
    b.update(id, title, author, pages, language, price)





