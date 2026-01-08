import streamlit as st
from numpy import random
if(st.button("generate number")):
    num=random.randint(1,101)
    if(num<=30):
        st.image("bd2.jpg")
    elif(num<=60):
        st.audio("krish.mp3")
    else:
      st.video("samplevideo.mp4")
    st.write(f"your number was",num)  

