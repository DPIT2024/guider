import pandas as pd
import streamlit as st
from datetime import datetime

feedback_df = pd.DataFrame(columns=['Timestamp', 'First Name', 'Last Name', 'Emoji', 'Comments'])

# Save feedback data to CSV file
def save_feedback_to_csv(feedback_data):
    feedback_data.to_csv('feedback.csv', index=False)

# Define the feedback form
def feedback_form():
    st.subheader("Feedback Form")
    first_name = st.text_input("First Name:")
    last_name = st.text_input("Last Name:")
    emoji = st.text_input("Emoji:")
    comments = st.text_area("Comments:", height=150)
    submit_button = st.button("Submit Feedback")

    if submit_button:
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        feedback_df.loc[len(feedback_df)] = [timestamp, first_name, last_name, emoji, comments]
        st.success("Thank you for your feedback!")

    save_feedback_to_csv(feedback_df)
