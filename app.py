import random

import streamlit as st
import pandas as pd
import pickle
from content_based import Collaborative
from custom_typed import CustomUser
from streamlit_display import StreamlitDisplay

st.set_page_config(
    page_title="Your Anime Recommendation System",
    page_icon=":rocket:",
    layout="wide",  # Use "wide" layout to have a wider background
)

st.title('Welcome :clap: to Anime Recommendation Application :japanese_goblin:', )
st.subheader(
    'Based on the Anime :movie_camera: & Recommendation Engine :rocket: You Select, We will Recommend :smiling_face_with_3_hearts: you another 10 Animes :star:  to Binge Watch! '':heart_eyes:')
st.image("Animewallpaper.png", width=1050)
st.header('Please choose Recommendation :rocket: Engine or Popular Animes from Below ')

top_animes_recommended = ['Cowboy Bebop','Naruto','One Piece','Hunter x Hunter',
                          'Death Note','Bleach','Kimetsu no Yaiba','Vinland Saga',
                          'Jujutsu Kaisen','Chainsaw Man','Haikyuu!!',
                          'Monster','Black Clover','JoJo no Kimyou na Bouken: Adventure',
                          'Fullmetal Alchemist: Brotherhood','Tokyo Ghoul']

def popular_animes(disabled=False):
    popular_anime = st.radio('Select any of the popular anime: ',
                             options=top_animes_recommended,
                             horizontal=True,disabled=disabled
                             )
    return popular_anime


engine = st.radio('Select Any of the Recommendation Models below:',
                  options=('Show Popular Animes','Content Based Recommendations', 'Custom Based Recommendations'),horizontal=True)

df_anime = pd.read_csv('df_anime.csv')
ratings_per_user = pickle.load(open('pickle_files/ratings_per_user.pkl', 'rb'))

if engine == 'Show Popular Animes':
    popular_anime = popular_animes()
    similar_animes_obj = Collaborative(popular_anime)
    similar_animes = similar_animes_obj.find_similar_animes()
    StreamlitDisplay(similar_animes, custom_engine=False)


elif engine == 'Content Based Recommendations':
    popular_animes(disabled=True)
    st.info('Based on Anime You Select, Recommendation Engine will Recommend Similar Animes!')
    anime_names = df_anime['Name'].tolist()
    anime_selected = st.selectbox('Choose or Type Anime Name:', options=anime_names)
    similar_animes_obj = Collaborative(anime_selected)
    similar_animes = similar_animes_obj.find_similar_animes()
    StreamlitDisplay(similar_animes, custom_engine=False)



elif engine == 'Custom Based Recommendations':
    popular_animes(disabled=True)
    st.info('Based on the Anime Rating, Genres or Description You Choose from the BELOW options ,Recommendation '
            'Engine will Recommend Similar Animes! ')

    anime_genres = ['Comedy', 'Fantasy', 'Action', 'Adventure', 'Sci-Fi',
                    'Drama', 'Romance', 'Slice of Life', 'Supernatural', 'Hentai',
                    'Mystery', 'Avant Garde', 'Ecchi', 'Sports', 'Horror', 'Suspense',
                    'Award Winning', 'Boys Love', 'Gourmet', 'Girls Love', 'Erotica']

    nsfw = ['Ecchi', 'Erotica', 'Hentai']

    user_selected_genres = st.multiselect("Choose Genres:", options=anime_genres)
    for genre in user_selected_genres:
        if genre in nsfw:
            st.warning('NSFW Genre(s) Selected :warning:')
            pass
    val = st.slider("Anime Rating Slider", min_value=3.0, max_value=8.0, value=6.5)
    user_text = st.text_area(
        "Enter Anime Description, Main Characters, Synopsis, Anime Short Story or LEAVE it BLANK: ", )

    if st.button('Search for Animes!'):
        similar_obj = CustomUser(user_selected_genres, val, user_text)
        similar_animes = similar_obj.requirementbased()
        StreamlitDisplay(similar_animes, custom_engine=True)

else:
    pass



