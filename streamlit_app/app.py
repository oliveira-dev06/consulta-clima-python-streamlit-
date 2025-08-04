import streamlit as st
import requests

API_KEY = "d069873afb530a2c3ccdab98ca633053"

st.title("Utilizando Streamlit com API de Clima")

cidade = st.text_input("Digite sua cidade para saber o clima!")

if st.button("Confirmar"):
    link = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={API_KEY}&units=metric&lang=pt_br"
    resposta = requests.get(link)
    dados = resposta.json()

    temperatura = dados['main']['temp']
    descricao = dados['weather'][0]['description']
    st.write(f" {cidade} está com {temperatura}°C")
    st.write(f"Condição: {descricao}")
    if temperatura >= 26:
        st.image('img/calor.png')
        st.write("🌞 Passa o protetor, porque hoje está quente ein!")

    elif temperatura >= 20:
        st.image("img/agradavel.png")
        st.write("🌅 Hoje o clima está agradável")

    else:
        st.image("img/frio.png")
        st.write("⛄ Pega um agasalho, porque hoje está frio!")

if st.button("Limpar"):
    st.session_state['cidade'] = ""
    st.rerun()
