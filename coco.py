import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt

df = pd.read_csv('reviews_coco.csv')
rating = df['rating'][0]

def numeric_rating(rating):
    if type(rating) == str:
        rating = rating.strip()
        number = len(rating)
        if number > 1:
          if rating[-1] != rating[-2]:
              number = number - 0.5
        return number
    else:
        return rating

df['num_rating'] = df['rating'].apply(numeric_rating)

st.title('Distribuição de Ratings do filme Viva! A Vida é uma Festa')

df['num_rating'].plot(kind='hist', bins=20, title='num_rating')
plt.gca().spines[['top', 'right',]].set_visible(False)
