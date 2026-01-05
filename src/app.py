import streamlit as st
import pandas as pd
import pickle
import os

# Define base paths to keep code portable
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, '../model/model.pkl')
DATA_PATH = os.path.join(BASE_DIR, '../data/clusters_new.xlsx') # Change to .csv if using csv

def load_resources():
    """Load the trained model and data."""
    try:
        with open(MODEL_PATH, "rb") as f:
            model = pickle.load(f)
        # Assuming the file is Excel based on original code. 
        # If using the CSV provided, change to pd.read_csv(DATA_PATH)
        data = pd.read_excel(DATA_PATH) if DATA_PATH.endswith('.xlsx') else pd.read_csv(DATA_PATH)
        return model, data
    except FileNotFoundError as e:
        st.error(f"Error loading resources: {e}. Please check the 'model' and 'data' folders.")
        return None, None

def scale_input(grad_marks, entrance_marks):
    """
    Standardize the input using mean and std from the training set.
    Stats derived from training data:
    Graduation Marks: Mean ~77.31, Std ~9.23
    Entrance Marks: Mean ~127.91, Std ~27.44
    """
    grad_scaled = (grad_marks - 77.3172) / 9.2327
    ent_scaled = (entrance_marks - 127.9162) / 27.4483
    return [grad_scaled, ent_scaled]

def get_prediction_message(cluster_label):
    """Return the user-friendly message based on the predicted cluster."""
    messages = {
        0: "Status: Not Selected. (Suggestion: Try again next year)",
        1: "Status: Selected! (Congratulations, you are eligible for the course)",
        2: "Status: Shortlisted for Second Exam. (Keep preparing!)",
        3: "Status: Selected for Interview. (Prepare your resume)"
    }
    # Default to a generic message if cluster is unexpected
    return messages.get(cluster_label, "Status: Under Review")

def main():
    st.set_page_config(page_title="Student Ability Classifier", layout="centered")
    
    st.title("🎓 Student Eligibility Predictor")
    st.write("Enter the student's marks to determine their eligibility status.")

    # Load resources
    model, _ = load_resources()
    
    if model is not None:
        # Input form
        with st.form("prediction_form"):
            col1, col2 = st.columns(2)
            
            with col1:
                gm = st.number_input("Graduation Marks (%)", min_value=0.0, max_value=100.0, step=0.1)
            with col2:
                em = st.number_input("Entrance Marks (out of 200)", min_value=0.0, max_value=200.0, step=1.0)
            
            submit_button = st.form_submit_button("Check Status")

        if submit_button:
            # Process input
            input_data = scale_input(gm, em)
            
            # Predict
            prediction = model.predict([input_data])[0]
            result_message = get_prediction_message(prediction)
            
            # Display Result with style
            if "Selected!" in result_message or "Interview" in result_message:
                st.success(result_message)
            elif "Shortlisted" in result_message:
                st.warning(result_message)
            else:
                st.error(result_message)

if __name__ == '__main__':
    main()