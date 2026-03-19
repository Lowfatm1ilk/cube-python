import streamlit as st
from openai import OpenAI

"""
# Hello World, Streamlit!

This is a website to demonstrate Streamlit's API.
You can stop looking at this now.

Please.
"""

client = OpenAI(api_key=st.secrets['json'] )

with st.form("my_form"):
    LanguageChoice = st.selectbox(
        "What language do you want to translate the message into?",
        [
            "English",
            "Chinese",
            "Spanish",
            "Japanese",
            "Koreon",
            "German",
            "Indian"
        ]
    )
    
    reason = st.text_area("Type the message.")

    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("It's interesting that you like " + LanguageChoice + ".")
        st.write("You say it's because:")
        st.write(f"""
        {reason}
        """)