
import numpy as np
import pickle
import streamlit as st

# loading saved model
with open("model.sav", "rb") as model:
    loaded_model = pickle.load(model)

# creating prediction function
def diabetesPrediction(input_data):

    # changing into numpy array
    input_np_array = np.asarray(input_data)

    # reshaping the array as we are predicting for one instance
    input_data_reshape = input_np_array.reshape(1, -1)
    
    with st.spinner("Analyzing..."):
        prediction = loaded_model.predict(input_data_reshape)

    return "The person is not diabetic" if prediction[0] == 0 else "The person is diabetic"


def main():
    # giving title
    st.title("Diabetes predictor for Females")
    
    st.markdown('#### Enter your health details below to check diabetes risk💡')
    
    # Toggle for showing/hiding explanations
    show_explanations = st.toggle("Show Input explanations ...")
    
    # create two columns for better UI
    col1, col2 = st.columns(2)
    
    # getting input data
    with col1:
        pregnancies = st.number_input("Number of pregnancies: ", step=1, min_value=0, max_value=30)
        glucose = st.number_input("Glucose level: ", step=1, min_value=0, max_value=200)       
        bloodPressure = st.number_input("Blood Pressure value: ", step=1, min_value=0, max_value=200)        
        skinThickness = st.number_input("Skin Thickness: ", step=1, min_value=0, max_value=100)
    
    with col2:
        insulin = st.number_input("Insulin level: ", step=1, min_value=0, max_value=900)        
        BMI = st.number_input("BMI value: ",step=0.1, min_value=0.1, max_value=75.0)        
        diabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function value: ", step=0.01, min_value=0.00, max_value=5.00)   
        age = st.slider("Age of person: ",value=30, min_value=1, max_value=100)
    
    # Show explanations only if toggle is enabled
    if show_explanations:
        st.markdown("#### ❗ Input Descriptions")
        
        st.markdown("""
                    - _Higher number of pregnancies may increase diabetes risk._
                    - _Normal blood glucose level ranges from **70-140 mg/dL.**_
                    - _Normal blood pressure level ranges from **80-120 mmHg.**_
                    - _**Thicker skin** may indicate obesity, a diabetes-related condition._
                    - _Higher insulin resistance can indicate diabetes._
                    - _BMI > 25 is overweight, > 30 is obese. Higher BMI increases diabetes risk._
                    - _The Function score reflects genetic risk based on family history._
                    - _Diabetes risk increase significantly after **age of 45**._
                    """)
        
    # prediction
    diagnosis = ""
    
    # btn for prediction
    if st.button("Test result"):
        diagnosis = diabetesPrediction([pregnancies, glucose, bloodPressure, skinThickness, insulin, BMI, diabetesPedigreeFunction, age])
    
    st.success(diagnosis)


# to allow main() to run only when running this standalone file only.
if __name__ == "__main__":
    main()