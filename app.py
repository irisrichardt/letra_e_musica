import requests
import streamlit as st
import pywhatkit as py
from deep_translator import GoogleTranslator

def buscar_letra(banda, musica):
    endpoint = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
    response = requests.get(endpoint)
    letra = response.json()["lyrics"] if response.status_code == 200 else ""
    return letra

def traduzir_letra(letra):
    tradutor = GoogleTranslator(target="pt")
    traducao = tradutor.translate(letra)
    return traducao

st.set_page_config(page_title="Letra e Música")

st.image("https://i.pinimg.com/originals/87/82/d2/8782d246868cbbc4fbc2adb816c20b74.jpg")
st.title("Letras de músicas")

banda = st.text_input("Digite o nome da banda: ", key="banda")
musica = st.text_input("Digite o nome da música: ", key="musica")
pesquisar = st.button("Pesquisar")
st.divider()

if "url" not in st.session_state:
    st.session_state["url"] = ""
if "letra" not in st.session_state:
    st.session_state["letra"] = ""
if "traducao" not in st.session_state:
    st.session_state["traducao"] = ""

if pesquisar:
    letra = buscar_letra(banda, musica)
    if letra:
        st.success("Encontramos sua música!! :D")
        nome_musica = f"{musica} {banda} video"
        url = py.playonyt(nome_musica, False, False)
        st.session_state["url"] = url
        st.session_state["letra"] = letra
        st.session_state["traducao"] = traduzir_letra(letra)
    else:
        st.error("Infelizemente não foi possível encontrar sua música :(")
        st.session_state["url"] = ""
        st.session_state["letra"] = ""
        st.session_state["traducao"] = ""

if st.session_state["url"]:
    st.markdown("""### Vídeo Clipe""")
    st.video(st.session_state["url"])

if st.session_state["letra"]:
    opcao = st.radio("Escolha o que deseja ver:", ["Letra Original", "Tradução"])
    if opcao == 'Letra Original':
        st.markdown("""### Letra""")
        st.text(st.session_state["letra"])
    else:
        st.markdown("""### Tradução""")
        st.text(st.session_state["traducao"])
