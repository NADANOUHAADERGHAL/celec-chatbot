import streamlit as st
import google.generativeai as genai

# Configure Google Generative AI
google_API_key = 'AIzaSyDLIjMgBkNtwWQvfYRS2X1ZD-bW-TOVz0s'
genai.configure(api_key=google_API_key)
model = genai.GenerativeModel('gemini-1.5-pro-latest')
convo = model.start_chat()

# Predefined responses
predefined_responses = {
    "how are you": "I'm good, thank you!",
    "good morning": "Good morning, have a good day!",
    "good night": "Good night, have a sweet dream!",
    "good evening": "Good evening to you too!",
    "what is celec club": "CELEC is a scientific club created in 1987 by students of the faculty of electronics and computer science (currently Electrical Engineering) of the USTHB in order to exchange their knowledge and their skills in the field of electronics.",
    "what is celec": "CELEC is a scientific club created in 1987 by students of the faculty of electronics and computer science (currently Electrical Engineering) of the USTHB.",
    "celec": "CELEC is a scientific club created in 1987 by students of the faculty of electronics and computer science (currently Electrical Engineering) of the USTHB.",
    "what is usthb": "The University of Science and Technology – Houari Boumediene is a university located in the town of Bab-Ezzouar 15 kilometres from Algiers, Algeria.",
    "usthb": "The University of Science and Technology – Houari Boumediene is a university located in the town of Bab-Ezzouar 15 kilometres from Algiers, Algeria.",
    "what is the capital of palestine": "The capital of Palestine is Al-Qods.",
    "what is arc": "A national robotics competition aimed at encouraging the integration of new technologies in various fields, organized by the Celec club.",
    "arc": "A national robotics competition aimed at encouraging the integration of new technologies in various fields, organized by the Celec club."

}


# Function to generate a response
def generate_response(input_text):
    try:
        input_lower = input_text.lower().strip()

        # Check if the input matches any predefined responses
        if input_lower in predefined_responses:
            return predefined_responses[input_lower]
        else:
            # Call the API for any other input
            response = convo.send_message(input_text)

            # Extract the clean response text from the API response
            if response and response.candidates and len(response.candidates) > 0:
                return response.candidates[0].content.parts[0].text.strip()
            else:
                return "Sorry, I couldn't generate a response from the API."

    except Exception as e:
        st.error(f"An error occurred: {e}")
        return "There was an error processing your request."

# Streamlit front-end UI design
background_image = "celec.png"
logo_image = "logo.png" 

st.markdown(
    f'''
    <style>
        body {{
            background-image: url('data:image/jpeg;base64,{st.image(background_image, use_column_width=True)}');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            background-attachment: fixed;
        }}
        .main-heading {{
            color: #2C3E50;
            text-align: center;
            font-family: 'Arial', sans-serif;
            margin-bottom: 20px;
            font-size: 36px;
            font-weight: bold;
            background-color: rgba(255, 255, 255, 0.8);
            padding: 10px;
            border-radius: 10px;
        }}
        .logo {{
            display: flex;
            justify-content: center;
            margin-bottom: 20px;
        }}
        .user-bubble, .assistant-bubble {{
            background-color: rgba(255, 255, 255, 0.7);
            border-radius: 15px;
            padding: 10px;
            margin: 5px 0;
            text-align: left;
            width: fit-content;
            max-width: 70%;
            font-family: 'Arial', sans-serif;
            color: #2C3E50;
            box-shadow: 1px 1px 5px rgba(0, 0, 0, 0.1);
        }}
        .chat-container {{
            display: flex;
            flex-direction: column;
            align-items: center;
        }}
        .input-container {{
            display: flex;
            flex-direction: row;
            align-items: center;
            gap: 10px;
            margin-bottom: 20px;
            justify-content: center;
        }}
        .text-input {{
            flex: 1;
            max-width: 400px;
        }}
    </style>

    <div class="logo">
        <img src="data:image/png;base64,{st.image(logo_image, use_column_width=True)}" style="max-width: 0px;"/>  <!-- Reduced max-width -->
    </div>
    <h1 class="main-heading">your celec chatbot 🤖</h1>
    <div class="chat-container">
    ''',
    unsafe_allow_html=True
)

# Adding input field in a single row
with st.container():
    user_input = st.text_input("Chat with Celec Chatbot:", key="user_input", label_visibility="collapsed", placeholder="Type your message here...")

# Process the input text
if user_input:
    response = generate_response(user_input)
    if response:
        st.markdown(f'<div class="assistant-bubble">🤖 {response}</div>', unsafe_allow_html=True)

# Close the chat-container div
st.markdown("</div>", unsafe_allow_html=True)
