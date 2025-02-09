import os
import pickle # pre trained model loading
import streamlit as st    # web app
from streamlit_option_menu import option_menu

#setting the page config
st.set_page_config(page_title='Prediction of Disease Outbreaks',
                   layout='wide',
                   page_icon="🧑‍⚕️")

#getting the working directory of main.py
working_dir = os.path.dirname(__file__)

#loading the saved models
diabetes_model= pickle.load(open(r"/Users/sakethramansrimattirumala/Desktop/GITAM/Third Year/SEM 6/Personal/AI project version 2_Refined_and_Official/training_models/diabetes_model.sav",'rb'))
heart_disease_model=pickle.load(open(r"/Users/sakethramansrimattirumala/Desktop/GITAM/Third Year/SEM 6/Personal/AI project version 2_Refined_and_Official/training_models/heart_model.sav",'rb'))
parkinsons_model= pickle.load(open(r"/Users/sakethramansrimattirumala/Desktop/GITAM/Third Year/SEM 6/Personal/AI project version 2_Refined_and_Official/training_models/parkinsons.sav",'rb'))

#sidebar for navigation
with st.sidebar:
    selected= option_menu('Prediction of disease outbreak system',
                          ['Diabetes Prediction',
                           'Heart Disease Prediction',
                           'Parkinsons prediction'],
                          menu_icon='hospital-fill',
                          icons=['activity','heart','person'],
                          default_index=0)

#diabetes prediction page
if selected=='Diabetes Prediction':
    st.title('Diabetes Prediction using Machine Learning')
    col1,col2,col3 = st.columns(3)
    with col1:
        pregnancies= st.text_input('Number of Pregnancies')
        SkinThickness= st.text_input('Skin Thickness value')
        DiabetesPedigreeFunction= st.text_input('Diabetes Pedigree Function value')
    with col2:
        Glucose= st.text_input('Glucose level')
        Insulin= st.text_input('Insulin level')
        Age= st.text_input('Age of the person')
    with col3:
        BloodPressure= st.text_input('Blood Pressure vakue ')
        BMI= st.text_input('BMI Value')
    diabetes_diagnosis= ''
    if st.button('Diabetes Test Result'):
        user_input = [pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction,Age]
        user_input = [float(x) for x in user_input]
        diabetes_prediction= diabetes_model.predict([user_input])
        if diabetes_prediction[0]==1:
            diabetes_diagnosis = 'The person is Diabetic'
        else:
            diabetes_diagnosis = 'The person is not Diabetic'
    st.success(diabetes_diagnosis)
#heart disease prediction page
if selected=='Heart Disease Prediction':
    st.title('Heart Disease Prediction using Machine Learning')
    col1,col2,col3 = st.columns(3)
    with col1:
        age= st.text_input('Age of the person')
        terestbps= st.text_input('Resting Blood Pressure')
        restecg= st.text_input('Resting Electrocardiographic Results')
        oldpeak= st.text_input('ST depression induced by exercise')
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect')
    with col2:
        sex = st.text_input('Sex: ')
        chol = st.text_input('Serum Cholestrol level in mg/dl:')
        thalach = st.text_input('Maximum Heart Rate Achieved')
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        cp = st.text_input('Chest Pain Types')
        fbs = st.text_input('Fasting Blood Sugar in mg/dl')
        exang = st.text_input('Exercise Induced Angina')
        ca = st.text_input('Major Vessels colored by Flourosopy')
    #predicting heart disease
    heart_diagnosis = ''
    if st.button('Heart Disease Test Result'):
        user_input = [age,sex,cp,terestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])
        if heart_prediction[0]==1:
            heart_diagnosis = 'The person has heart disease'
        else:
            heart_diagnosis = 'The person does not have heart disease'
    st.success(heart_diagnosis)
#parkinsons prediction page
if selected=='Parkinsons prediction':
    st.title('Parkinsons Prediction using Machine Learning')
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
        MDVP_Fo = st.text_input('MDVP:Fo(Hz)')
        MDVP_RAP = st.text_input('MDVP:RAP')
        Shimmer_APQ3 = st.text_input('Shimmer:APQ3')
        HNR = st.text_input('HNR')
        D2 = st.text_input('D2')
    with col2:
        MDVP_Fhi = st.text_input('MDVP:Fhi(Hz)')
        MDVP_PPQ = st.text_input('MDVP:PPQ')
        Shimmer_APQ5 = st.text_input('Shimmer:APQ5')
        RPDE = st.text_input('RPDE')
        PPE = st.text_input('PPE')
    with col3:
        MDVP_Flo = st.text_input('MDVP:Flo(Hz)')
        Jitter_DDP = st.text_input('Jitter:DDP')
        MDVP_APQ = st.text_input('MDVP:APQ')
        DFA = st.text_input('DFA')
    with col4:
        MDVP_Jitter = st.text_input('MDVP:Jitter(%)')  
        MDVP_Shimmer = st.text_input('MDVP:Shimmer')
        Shimmer_DDA = st.text_input('Shimmer:DDA')
        spread1 = st.text_input('spread1')
    with col5:
        MDVP_Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        MDVP_Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        NHR = st.text_input('NHR')
        spread2 = st.text_input('spread2')
    #predicting parkinsons
    parkinsons_diagnosis = ''
    if st.button('Parkinsons Test Result'):
        user_input = [MDVP_Fo,MDVP_Fhi,MDVP_Flo,MDVP_Jitter,MDVP_Jitter_Abs,MDVP_RAP,MDVP_PPQ,Jitter_DDP,MDVP_Shimmer,MDVP_Shimmer_dB,Shimmer_APQ3,Shimmer_APQ5,MDVP_APQ,Shimmer_DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
        user_input = [float(x) for x in user_input]
        parkinsons_prediction = parkinsons_model.predict([user_input])
        if parkinsons_prediction[0]==1:
            parkinsons_diagnosis = 'The person has Parkinsons Disease'
        else:
            parkinsons_diagnosis = 'The person does not have Parkinsons Disease'
    st.success(parkinsons_diagnosis)   