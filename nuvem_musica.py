import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

texto = st.text_input("Digite a letra de uma música sem pontuações: ")
if len(texto) > 0:
    wc = WordCloud(width=800, height=400).generate(texto.lower())
    plt.imshow(wc, interpolation='bilinear')
    plt.axis("off")
    plt.show()
    st.pyplot(plt)
