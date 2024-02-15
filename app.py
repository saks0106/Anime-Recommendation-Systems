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

#df_anime = pd.read_csv('df_anime.csv')
df_anime = pd.read_csv('animedb.csv')
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
    #def calling(user_selected_genres=[],scores=6.5, features=''):


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

    user_text = st.text_area(
        "Enter Anime Description, Main Characters, Synopsis, Anime Short Story or LEAVE it BLANK: ", )

    val = st.slider("Anime Rating Slider", min_value=3.0, max_value=8.0, value=6.5)
    search_anime = st.button('Search for Your Animes')
    if search_anime:
        #calling(user_selected_genres,val,user_text)
        similar_obj = CustomUser(user_selected_genres, val, user_text)
        similar_animes = similar_obj.requirement_based()
        StreamlitDisplay(similar_animes, custom_engine=True)

    #
    # popular_animes(disabled=True)
    # st.info('Based on the Anime Rating, Genres or Description You Choose from the BELOW options ,Recommendation '
    #         'Engine will Recommend Similar Animes! ')
    #
    # anime_genres = ['Comedy', 'Fantasy', 'Action', 'Adventure', 'Sci-Fi',
    #                 'Drama', 'Romance', 'Slice of Life', 'Supernatural', 'Hentai',
    #                 'Mystery', 'Avant Garde', 'Ecchi', 'Sports', 'Horror', 'Suspense',
    #                 'Award Winning', 'Boys Love', 'Gourmet', 'Girls Love', 'Erotica']
    #
    # nsfw = ['Ecchi', 'Erotica', 'Hentai']
    #
    # user_selected_genres = st.multiselect("Choose Genres:", options=anime_genres)
    # for genre in user_selected_genres:
    #     if genre in nsfw:
    #         st.warning('NSFW Genre(s) Selected :warning:')
    #         pass
    # val = st.slider("Anime Rating Slider", min_value=3.0, max_value=8.0, value=6.5)
    # user_text = st.text_area(
    #     "Enter Anime Description, Main Characters, Synopsis, Anime Short Story or LEAVE it BLANK: ", )
    #
    # if st.button('Search for Animes!'):
    #     similar_obj = CustomUser(user_selected_genres, val, user_text)
    #     similar_animes = similar_obj.requirementbased()
    #     StreamlitDisplay(similar_animes, custom_engine=True)

else:
    pass






#
# import random
#
# import streamlit as st
# import pandas as pd
# import pickle
# from content_based import Collaborative
# from custom_typed import CustomUser
# from streamlit_display import StreamlitDisplay
# import pandas as pd
# from nltk.corpus import stopwords
# from nltk.tokenize import word_tokenize
# from nltk.stem import PorterStemmer
# ps = PorterStemmer()
# import nltk
# nltk.download('punkt')
#
# st.set_page_config(
#     page_title="Your Anime Recommendation System",
#     page_icon=":rocket:",
#     layout="wide",  # Use "wide" layout to have a wider background
# )
#
# st.title('Welcome :clap: to Anime Recommendation Application :japanese_goblin:', )
# st.subheader(
#     'Based on the Anime :movie_camera: & Recommendation Engine :rocket: You Select, We will Recommend :smiling_face_with_3_hearts: you another 10 Animes :star:  to Binge Watch! '':heart_eyes:')
# st.image("Animewallpaper.png", width=1050)
# st.header('Please choose Recommendation :rocket: Engine or Popular Animes from Below ')
#
# top_animes_recommended = ['Cowboy Bebop','Naruto','One Piece','Hunter x Hunter',
#                           'Death Note','Bleach','Kimetsu no Yaiba','Vinland Saga',
#                           'Jujutsu Kaisen','Chainsaw Man','Haikyuu!!',
#                           'Monster','Black Clover','JoJo no Kimyou na Bouken: Adventure',
#                           'Fullmetal Alchemist: Brotherhood','Tokyo Ghoul']
#
# def popular_animes(disabled=False):
#     popular_anime = st.radio('Select any of the popular anime: ',
#                              options=top_animes_recommended,
#                              horizontal=True,disabled=disabled
#                              )
#     return popular_anime
#
#
# engine = st.radio('Select Any of the Recommendation Models below:',
#                   options=('Show Popular Animes','Content Based Recommendations', 'Custom Based Recommendations'),horizontal=True)
#
# df_anime = pd.read_csv('animedb.csv')
# ratings_per_user = pickle.load(open('pickle_files/ratings_per_user.pkl', 'rb'))
#
# if engine == 'Show Popular Animes':
#     popular_anime = popular_animes()
#     similar_animes_obj = Collaborative(popular_anime)
#     similar_animes = similar_animes_obj.find_similar_animes()
#     StreamlitDisplay(similar_animes, custom_engine=False)
#
#
# elif engine == 'Content Based Recommendations':
#     popular_animes(disabled=True)
#     st.info('Based on Anime You Select, Recommendation Engine will Recommend Similar Animes!')
#     anime_names = df_anime['Name'].tolist()
#     anime_selected = st.selectbox('Choose or Type Anime Name:', options=anime_names)
#     similar_animes_obj = Collaborative(anime_selected)
#     similar_animes = similar_animes_obj.find_similar_animes()
#     StreamlitDisplay(similar_animes, custom_engine=False)
#
#
#
# elif engine == 'Custom Based Recommendations':
#     popular_animes(disabled=True)
#     def calling(user_selected_genres=[],scores=6.5, user_text=''):
#         SimilarityArr = []
#         df_anime2 = pd.read_csv('animedb.csv')
#         #eng_sw = set(stopwords.words('english'))
#         features_token = word_tokenize(user_text)
#         #features_token_set = set([ps.stem(token) for token in features_token if token not in eng_sw])
#         features_token_set = set([ps.stem(token) for token in features_token])
#
#         # Filter anime based on user input genres and scores
#         genre_pattern = '|'.join(user_selected_genres)
#         genres_selected = df_anime2['Genres'].str.contains(genre_pattern)
#         df_anime2 = df_anime2[genres_selected]
#         df_anime2 = df_anime2[df_anime2['Score'] >= scores].sort_values(by='Score', ascending=False)
#         df_anime2.reset_index(inplace=True, drop=True)
#         df_anime2 = df_anime2.loc[:, 'anime_id':]
#         df_anime_dict = df_anime2.to_dict('records')
#
#         # Calculate similarity based on common words in synopsis
#         for anime_info in df_anime_dict:
#             summary = anime_info['Synopsis']
#             summary_token = word_tokenize(summary)
#             combo_summary_token_set = set([ps.stem(token) for token in summary_token])#set([ps.stem(token) for token in summary_token if token not in eng_sw])
#             common_count = len(features_token_set.intersection(combo_summary_token_set))
#             anime_info['Similarity'] = common_count
#
#         # Sort by similarity and select top recommendations
#         df_anime_dict = sorted(df_anime_dict, key=lambda k: k['Similarity'], reverse=True)
#         for i in range(min(30, len(df_anime_dict))):  # Limit to top 30 recommendations
#             anime_info = df_anime_dict[i]
#             SimilarityArr.append({
#                 "Name": anime_info['Name'],
#                 "Similarity": anime_info['Similarity'],
#                 "Genres": anime_info['Genres'],
#                 "Synopsis": anime_info['Synopsis'],
#                 "Other name": anime_info['Other name'],
#                 'Score': anime_info['Score'],
#                 'Episodes': anime_info['Episodes'],
#                 'Favorites': anime_info['Favorites'],
#                 'Image URL': anime_info['Image URL'],
#                 'Aired_on': anime_info['Aired_From']
#             })
#
#         return SimilarityArr
#
#
#     anime_genres = ['Comedy', 'Fantasy', 'Action', 'Adventure', 'Sci-Fi',
#                     'Drama', 'Romance', 'Slice of Life', 'Supernatural', 'Hentai',
#                     'Mystery', 'Avant Garde', 'Ecchi', 'Sports', 'Horror', 'Suspense',
#                     'Award Winning', 'Boys Love', 'Gourmet', 'Girls Love', 'Erotica']
#
#     nsfw = ['Ecchi', 'Erotica', 'Hentai']
#
#     user_selected_genres = st.multiselect("Choose Genres:", options=anime_genres)
#     for genre in user_selected_genres:
#         if genre in nsfw:
#             st.warning('NSFW Genre(s) Selected :warning:')
#             pass
#
#     user_text = st.text_area(
#         "Enter Anime Description, Main Characters, Synopsis, Anime Short Story or LEAVE it BLANK: ", )
#
#     val = st.slider("Anime Rating Slider", min_value=3.0, max_value=8.0, value=6.5)
#     similar_animes = calling(user_selected_genres,val,user_text)
#     StreamlitDisplay(similar_animes, custom_engine=True)
#
#
#
# else:
#     pass



