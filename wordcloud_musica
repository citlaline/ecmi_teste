import streamlit as st
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

text = input("Digite a letra de uma música sem pontuações: ")

def create_wordcloud(text, stopwords=None):
    wordcloud = WordCloud(stopwords=stopwords).generate(text.lower())

    plt.figure(figsize=(8, 8), facecolor=None)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    plt.tight_layout(pad=0)
    plt.show()

stopwords = set(STOPWORDS)

create_wordcloud(text, stopwords=stopwords)
