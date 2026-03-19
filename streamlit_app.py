import streamlit as st
from openai import OpenAI

system_prompt = """
You are gonna be a translator for thuser and you will translate their message into a language of their choice.
"""
client = OpenAI(api_key=st.secrets['json'] )
chat_history = [
    {"role": "system", "content": system_prompt},
    {"role":"user","content":'the language'}


]


    
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
            "Hindi"
        ]
    )
    
    message = st.text_area("Type the message.")

    submitted = st.form_submit_button("Submit")
    if submitted:
        chat_history.append(
        {"role": "user", "content": 'this is the language to translate to: ' + LanguageChoice + "this is the message to translate: respond with this message in the language chosen:  " + message})

        response = client.chat.completions.create(
            model='gpt-4o',
            messages=chat_history
        )

        st.write(response.choices[0].message.content)


        