import requests
import streamlit as st
import pywhatkit as py

def buscar_letra(banda, musica):
  endpoint = f"https://api.lyrics.ovh/v1/{banda}/{musica}"
  response = requests.get(endpoint)
  letra = response.json()["lyrics"] if response.status_code == 200 else ""
  return letra

st.set_page_config(page_title="Letra e Música")

st.image("https://i.pinimg.com/originals/87/82/d2/8782d246868cbbc4fbc2adb816c20b74.jpg")
st.title("Letras de músicas")

banda = st.text_input("Digite o nome da banda: ", key="banda")
musica = st.text_input("Digite o nome da música: ", key="musica")
pesquisar = st.button("Pesquisar")
st.divider()

if pesquisar:
  letra = buscar_letra(banda, musica)
  if letra:
    nome_musica = f"{musica} {banda} video"
    url = py.playonyt(nome_musica, False, False)
    st.success("Encontramos sua música!! :D")
    st.markdown("""### Vídeo Clipe""")
    st.video(url)
    st.markdown("""### Letra""")
    st.text(letra)
  else:
    st.error("Infelizemente não foi possível encontrar a música :(")

