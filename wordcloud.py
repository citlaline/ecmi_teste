import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

text = input("Digite a letra de uma música sem pontuações: ")

wordcloud = WordCloud().generate(text.lower())

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()
