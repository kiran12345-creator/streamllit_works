import streamlit as st
from library_db import BookListCreateRetrieveDeleteUpdate
st.title('welcome to library app')
b=BookListCreateRetrieveDeleteUpdate()
tab1,tab2,tab3,tab4,tab5=st.tabs(['Add','Read','retrieve','delete','update'])
with tab1:
    st.write('add')
    btn = st.button('display all records')
  
with tab2:
    st.write('read')
    b.create()
with tab3:
    st.write('retrieve')
with tab4:
    st.write('delete')
with tab5:
    st.write('update')