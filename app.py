import streamlit as st
import math
import jiwer
import base64


transformation = jiwer.Compose([
    jiwer.ExpandCommonEnglishContractions(),
    jiwer.RemovePunctuation(),
    jiwer.RemoveMultipleSpaces(),
    jiwer.Strip(),
    jiwer.SentencesToListOfWords(),
    jiwer.RemoveEmptyStrings(),
    jiwer.ToLowerCase()
]) 
# st.title("Accuracy Calculator")
st.markdown("<h1 style='text-align: center; color: black;'>Accuracy Calculator</h1>", unsafe_allow_html=True)
col1, col2 = st.beta_columns([1, 1])
with col1:
    
    file_ = open("C:\\Users\\User\\streamlitapp\\design.gif", "rb")
    contents = file_.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    file_.close()
    st.markdown(
           f'<img src="data:image/gif;base64,{data_url}" alt=" design gif" width = 250 height=260>',
    
    
            unsafe_allow_html=True
    
            )

with col2:
# Alternative syntax, declare a form and use the returned object
# Forms can be declared using the 'with' syntax
    with st.form(key='my_form'):
        data = st.text_input(label='Enter transcript from app *')
        
        ref=st.text_input(label='Enter your own transcipt version *')
        
        submit_button1= st.form_submit_button(label='Calculate')
    
    # st.form_submit_button returns True upon form submit
    if submit_button1:
        st.subheader("**Accuracy of Speech Recognition**")
        if not data:
            st.warning("Please fill out text")
           
        if not ref:
            st.warning("Please fill out text")
        else:
        
            error=round(jiwer.wer(transformation(data),transformation(ref)),2)
            error1=jiwer.mer(transformation(data),transformation(ref))
            
            st.subheader(str(100-(error*100))+" % for WER")
            st.subheader(str(round(100-(error1*100),2))+" % for MER ")
   