

import os
import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   layout="wide",
                   page_icon="🧑‍⚕️")


# Loading the saved models (Ensure the file paths are correct)
diabetes_model = pickle.load(open('C:/Users/registrar/Desktop/diesase detection/diabetes_model.sav', 'rb'))
heart_disease_model = pickle.load(open('C:/Users/registrar/Desktop/diesase detection/heart_disease_model.sav', 'rb'))

# Indian Diet Plans for Diabetes and Heart Disease
diet_plan_diabetes = """
### **Indian Diet Plan for Diabetes**
#### **Breakfast:**
- Vegetable Poha (with peas, carrots, and beans).
- Ragi Dosa with coconut chutney or sambhar.
- Methi Thepla with low-fat yogurt.

#### **Mid-Morning Snack:**
- Roasted chana or almonds.
- Fresh fruit like guava, apple, or orange.

#### **Lunch:**
- Whole-grain Roti (Chapati) with brown rice.
- Dal Tadka with vegetables (bhindi, lauki).
- Low-fat curd or buttermilk.

#### **Evening Snack:**
- Moong Dal Chilla with mint chutney.
- Vegetable Soup.

#### **Dinner:**
- Vegetable Khichdi with dal and brown rice.
- Grilled Paneer.
- Green Salad with cucumber and tomatoes.

#### **General Tips:**
- Avoid sugary foods and drinks.
- Use natural sweeteners like stevia.
- Stick to high-fiber foods and minimize processed items.
"""

diet_plan_heart = """
### **Indian Diet Plan for Heart Disease**
#### **Breakfast:**
- Idli with Sambhar.
- Vegetable Upma with semolina and veggies.
- Multigrain Paratha with palak (spinach).

#### **Mid-Morning Snack:**
- Walnuts or unsalted pistachios.
- Fresh fruit like papaya, pomegranate, or watermelon.

#### **Lunch:**
- Bajra Roti or Jowar Roti with dal.
- Fish Curry with Omega-3 fatty fish.
- Steamed Vegetables like carrots and broccoli.

#### **Evening Snack:**
- Sprouts Salad with onions and lime.
- Masala Chai (with low-fat milk).

#### **Dinner:**
- Vegetable Soup (carrots, spinach, celery).
- Grilled Chicken or Tandoori Paneer.
- Millet-based Khichdi with vegetables.

#### **General Tips:**
- Avoid fried foods and salty snacks.
- Use olive oil or mustard oil for cooking.
- Focus on whole grains and plant-based foods.
"""

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System',
                           ['Diabetes Prediction',
                            'Heart Disease Prediction',
                            ],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Initialize session state variables
if 'prediction_made' not in st.session_state:
    st.session_state.prediction_made = False

if 'disease_type' not in st.session_state:
    st.session_state.disease_type = None

# Diabetes Prediction Page
if selected == 'Diabetes Prediction':
    # Page title
    st.title('Diabetes Prediction using ML')

    # Getting the input data from the user
    col1, col2, col3 = st.columns(3)
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function value')
    with col2:
        Age = st.text_input('Age of the Person')

    # Code for Prediction
    diab_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Diabetes Test Result'):
        user_input = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        user_input = [float(x) for x in user_input]
        diab_prediction = diabetes_model.predict([user_input])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
            st.session_state.prediction_made = True
            st.session_state.disease_type = 'diabetes'
        else:
            diab_diagnosis = 'The person is not diabetic'
            st.session_state.prediction_made = True
            st.session_state.disease_type = 'no_diabetes'

    st.success(diab_diagnosis)

    # Button to suggest Indian Diet Plan (Only after prediction)
    if st.session_state.prediction_made:
        if st.session_state.disease_type == 'diabetes':
            if st.button('Suggest Indian Diet Plan for Diabetes'):
                st.markdown(diet_plan_diabetes)
        else:
            if st.button('Suggest Indian Diet Plan for Non-Diabetic'):
                st.info("No specific diet plan is needed for non-diabetic individuals.")

# Heart Disease Prediction Page
if selected == 'Heart Disease Prediction':
    # Page title
    st.title('Heart Disease Prediction using ML')

    col1, col2, col3 = st.columns(3)
    with col1:
        age = st.text_input('Age')
    with col2:
        sex = st.text_input('Sex')
    with col3:
        cp = st.text_input('Chest Pain types')
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    with col3:
        fbs = st.text_input('Fasting Blood Sugar > 120 mg/dl')
    with col1:
        restecg = st.text_input('Resting Electrocardiographic results')
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    with col3:
        exang = st.text_input('Exercise Induced Angina')
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    with col2:
        slope = st.text_input('Slope of the peak exercise ST segment')
    with col3:
        ca = st.text_input('Major vessels colored by flourosopy')
    with col1:
        thal = st.text_input('thal: 0 = normal; 1 = fixed defect; 2 = reversible defect')

    # Code for Prediction
    heart_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        user_input = [age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]
        user_input = [float(x) for x in user_input]
        heart_prediction = heart_disease_model.predict([user_input])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
            st.session_state.prediction_made = True
            st.session_state.disease_type = 'heart_disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'
            st.session_state.prediction_made = True
            st.session_state.disease_type = 'no_heart_disease'

    st.success(heart_diagnosis)

    # Button to suggest Indian Diet Plan (Only after prediction)
    if st.session_state.prediction_made:
        if st.session_state.disease_type == 'heart_disease':
            if st.button('Suggest Indian Diet Plan for Heart Disease'):
                st.markdown(diet_plan_heart)
        else:
            if st.button('Suggest Indian Diet Plan for Non-Heart Disease'):
                st.info("No specific diet plan is needed for non-heart disease individuals.")



