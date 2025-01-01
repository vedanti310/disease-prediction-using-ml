# Health Assistant Application

This repository contains a **Health Assistant** application that utilizes Machine Learning models to predict health conditions like **Diabetes** and **Heart Disease**. Additionally, it provides tailored Indian diet plans based on the prediction results and features an interactive chatbot for health-related discussions.

---

## Features

- **Disease Prediction**: 
  - Diabetes Prediction using user inputs such as glucose levels, BMI, age, etc.
  - Heart Disease Prediction using parameters like cholesterol levels, blood pressure, etc.
- **Diet Recommendations**: Suggests Indian diet plans based on the health condition.
- **Interactive Chatbot**: A chatbot for real-time health-related discussions and queries.
- **Streamlit Web App**: User-friendly interface for interaction.

---

## Technology Stack

1. **Frontend**: Streamlit for web interface.
2. **Backend**:
   - Machine Learning models trained using **Google Colab**.
   - Libraries: `pandas`, `numpy`, `scikit-learn`, `pickle`, `openai` (for chatbot).
3. **Models**:
   - Diabetes prediction model.
   - Heart disease prediction model.

---

## Getting Started

### Prerequisites

- Python 3.9 or above.
- Libraries:
  ```bash
  pip install streamlit pandas numpy scikit-learn streamlit-option-menu openai
  ```
- Trained machine learning models saved as `.sav` files:
  - `diabetes_model.sav`
  - `heart_disease_model.sav`

### File Structure

- `app.py`: Main application file.
- `diabetes_model.sav`: Trained diabetes prediction model.
- `heart_disease_model.sav`: Trained heart disease prediction model.
- `README.md`: Project documentation.

---

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/health-assistant.git
   cd health-assistant
   ```
2. Place the trained model files (`diabetes_model.sav`, `heart_disease_model.sav`) in the project directory.
3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```
4. Access the web app at `http://localhost:8501`.

---

## Workflow

1. **Data Training**:
   - The machine learning models were trained using datasets for diabetes and heart disease prediction.
   - Training was conducted on **Google Colab** for scalability and ease of use.
   - The models were exported as `.sav` files using the `pickle` library.

2. **Prediction**:
   - User inputs are taken via the Streamlit app.
   - Inputs are passed to the corresponding ML model for prediction.

3. **Diet Plans**:
   - Based on the prediction results, a tailored Indian diet plan is displayed.

4. **Chatbot**:
   - Integrated using OpenAI API for interactive health discussions.

---

## Future Enhancements

- Add more disease prediction models.
- Enhance chatbot capabilities with more health-related queries.
- Add multilingual support.

---

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request.

---
## Acknowledgments

- Datasets used for training.
- Libraries and frameworks: Streamlit, Scikit-learn, OpenAI.
- Tutorials and guides for machine learning and Streamlit development.

