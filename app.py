import pickle
import streamlit as st
pick_out=open('HDP.pkl','wb')
pickle.dump(model,pick_out)
pick_out.close()
pick_in=open('HDP.pkl','rb')
m= pickle.load(pick_in)

html_temp = """ 
    <div style ="background-color:pink;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Healthy Heart App</h1> 
    </div> 
    """

st.markdown(html_temp, unsafe_allow_html = True) 

age=st.number_input('Age')
sex=st.number_input('Sex')
cpt=st.number_input('Chest pain type')
bp=st.number_input('BP')
cl=st.number_input('Cholesterol')
fbs=st.number_input('FBS over 120')
ekg=st.number_input('EKG results')
hr=st.number_input('Max HR')
ea=st.number_input('Exercise angina')
std=st.number_input('ST depression',step=1.,format="%.2f")
st=st.number_input('Slope of ST')
nvf=st.number_input('Number of vessels fluro')
th=st.number_input('Thallium')
pred=predict(age,sex,cpt,bp,cl,fbs,ekg,hr,ea,std,st,nvf,th)

if st.button("Predict"):
    if pred[0]==0:
        st.error('Warning! You have high risk of getting a heart attack!')
    else:
         st.success('You have lower risk of getting a heart disease!')
        
