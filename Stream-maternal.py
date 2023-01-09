import pickle
import streamlit as st

#membaca model
Maternal_model = pickle.load(open('Maternal_model.sav', 'rb'))

#judul web
st.title ('data mining prediksi Maternal Health')
#nama inputan nilai Age,SystolicBP,DiastolicBP,BS,BodyTemp,HeartRate,RiskLevel
Age = st.text_input('input nilai Age')
SystolicBP = st.text_input('input nilai SystolicBP')
DiastolicBP = st.text_input('input nilai DiastolicBP')
BS = st.text_input('input nilai BS')
BodyTemp = st.text_input('input nilai BodyTemp')
HeartRate = st.text_input('input nilai HeartRate')

#code untuk prediksi
maternal_diagnosis =''

#membuat tombol untuk prediksi
if st.button('Prediksi Resiko'):
    Maternal_prediction = Maternal_model.predict([[Age,SystolicBP,DiastolicBP,BS,BodyTemp,HeartRate]])

    if(Maternal_prediction[0]==0):
        maternal_diagnosis = 'pasien Resiko Rendah'
    elif(Maternal_prediction[0]==1):
        maternal_diagnosis = 'pasien Resiko Sedang'
    else:
        maternal_diagnosis = 'pasien Resiko Tinggi'
st.success(maternal_diagnosis)