import streamlit as st
st.sidebar.title("Enter your details")
#dropdown
batch=st.sidebar.selectbox("select your batch",["B1","B2","B3","B4","B5","B6"])
sub=st.sidebar.radio("select your subject",["python","fsd"])
if(sub=="python"):
    titl=st.text_input("Enter  python title")
    enr=st.text_input("Enter enrollment number")
    des=st.text_area("Project description")
elif(sub=="fsd"):
    titl=st.text_input("Enter  fsd title")
    enr=st.text_input("Enter enrollment number")
    des=st.text_area("Project description")
btn=st.button("submit")
if(btn):
    st.write(f"batch {batch}")    
    st.write(f"subject {sub}")
    st.write(f"title {titl}")
    st.write(f"enrollment {enr}")
    st.write(f"description {des}")
#     python -m streamlit run  appname.py  to run streamlit app run this ncode











