import streamlit as st
import pickle
import numpy as np
from PIL import Image

st.set_page_config(layout="wide")

def load_model():
  with open('saved_steps.pkl', 'rb') as file:
    data = pickle.load(file)
  return data

# execution 
data = load_model()

model = data["model"]
label_country = data["label_country"]
label_education = data["label_education"]

# create the prediction page
def show_prediction_page():
  st.title("Dev Salary Prediction")
  
  st.write("""### Let's input some information to predict your future income:""")
  
  image = Image.open('stackoverflow.png')
  
  st.image(image)
  
  countries = (
    "United States of America",
    "Russian Federation",
    "Germany",
    "United Kingdom of Great Britain and Northern Ireland",
    "India",
    "Canada",
    "France",
    "Brazil",
    "Spain",
    "Netherlands",
    "Poland",
    "Australia",
    "Italy",
    "Sweden",
    "Switzerland"
    "Russian Federation",
    "Turkey",
    "Austria",
    "Israel",
    "Denmark",
    "Portugal",
    "Belgium",
    "Czech Republic",
    "Norway",
    "Mexico",
    "Finland",
    "New Zealand",
    "Greece",
    "Portugal",
    "Ukraine",
    "Romania",
    "Turkey",
    "South Africa",
    "Ireland",
    "Hungary",
    "Colombia",
    "Argentina",
    "Pakistan",
    "Bulgaria",
    "Japan",
    "China",
    "Lithuania",
    "Slovenia",
    "Slovakia",
    "Bangladesh",
    "Indonesia",
    "Croatia",
    "Singapore",
    "Estonia",
    "Philippines",
    "Serbia",
    "Chile",
    "Other",
  )
  
  education = (
        "No degree",
        "Bachelor’s degree",
        "Master’s degree",
        "PhD",
    )
  
  country = st.selectbox("Country", countries)
  education = st.selectbox("Education", education)
  experience = st.slider("Years of Experience", 0, 50, 1)
  
  button = st.button("Predict My Salary")
  # if click the button, then this is True:
  if button:
    X = np.array([[country, education, experience]])
    X[:, 0] = label_country.transform(X[:,0])
    X[:, 1] = label_education.transform(X[:,1])
    X = X.astype(float)
    
    salary = model.predict(X)
    st.subheader(f"Your estimated salary is ${salary[0]:.2f}")
  
