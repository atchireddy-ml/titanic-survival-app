import streamlit as st
import joblib 
import pandas as pd
st.title("Titanic Survival Prediction")
st.write("Enter the details of the passenger to predict survival probability.")
st.image("https://www.titanicmuseum.org/wp-content/uploads/2019/01/Titanic-leaving-Southampton-Colour.jpg",width=200)
st.sidebar.title("Input fields")
pclass = st.sidebar.selectbox("Passenger Class", [1, 2, 3])
sex = st.sidebar.selectbox("Sex", ["male", "female"])
age = st.sidebar.slider("Age", 0, 100,  30)
Fare=st.sidebar.number_input("Fare", min_value=0.0, value=32.20)
# Predict button
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

if st.button("Predict"):
    model = load_model()
    input_data = pd.DataFrame({
        "Pclass": [pclass],
        "Sex": [1 if sex == "male" else 0],
        "Age": [age],
        "Fare": [Fare]
    })


    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.success("The passenger is likely to survive.")
    else:        st.error("The passenger is unlikely to survive.")  
with st.expander("About the Model"):
    st.write("The model is trained on the Titanic dataset to predict survival based on passenger class, sex, age, and fare. It uses a logistic regression algorithm to make predictions.")

