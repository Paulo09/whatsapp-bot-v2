import streamlit as st
import openai

# Define a função para interagir com o ChatGPT
def chat_with_gpt(prompt):
    openai.api_key = "sua_chave_de_api_aqui"
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text

# Define o título e a barra lateral do Streamlit
st.title("Chatbot com ChatGPT")
user_input = st.text_area("Você: ", "")

# Verifica se o usuário enviou uma mensagem
if st.button("Enviar"):
    # Mostra a mensagem do usuário
    st.text("Usuário: " + user_input)
    
    # Obtém a resposta do ChatGPT
    response = chat_with_gpt(user_input)

    # Mostra a resposta do ChatGPT
    st.text("Chatbot: " + response)
