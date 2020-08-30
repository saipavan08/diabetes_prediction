import streamlit as st
import pickle
import numpy as np
model=pickle.load(open('model.pkl','rb'))    


def main():
    html_temp = """
    <div style="background-color:#E68676 ;padding:10px">
    <h2 style="color:white;text-align:center;">Diabetes Prediction ML App </h2>
    </div>
    """
    st.markdown(html_temp, unsafe_allow_html=True)
    
    Pregnancies = st.number_input("Number of Pregnancies eg.2")
    Glucose=st.number_input("Glucose (mg/dL) eg.80")
    BloodPressure=st.number_input("Blood Pressure (mmHg) eg.80")
    SkinThickness=st.number_input("Skin Thickness (mm) eg.20")
    Insulin=st.number_input("Insulin (IU/mL) eg.80")
    BMI=st.number_input("Body Mass Index (Kg/m^2) eg.23.1")
    DiabetesPedigreeFunction=st.number_input("Diabetes Pedigree Function eg.0.52")
    Age=st.slider("Age eg.34",1,100)
    
    data=np.array([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]])
    
    if st.button("predict"):
        prediction=model.predict(data)
        pred='{0}'.format(prediction[0])
        if pred == '1':
            st.error("Suffering from Diabetes")
        else:
            st.success("Not Suffering from Diabetes")


if __name__ == '__main__':
    main()
    
