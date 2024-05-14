import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

texto = input("Digite a letra de uma música sem pontuações: ")
wordcloud = WordCloud(width=800, height=400).generate(texto.lower())

plt.imshow(wordcloud, interpolation='bilinear')
plt.axis("off")
plt.show()
st.pyplot()

wordcloud.to_file("wordcloud.png")

st.image("wordcloud.png", use_column_width=True)
