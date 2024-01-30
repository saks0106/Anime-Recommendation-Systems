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

st.title('Anime Recommendation Application using 3 Approaches :japanese_goblin:', )
st.subheader('Based on the Anime :movie_camera: & Recommendation Engine :rocket: You Select, We will Recommend :smiling_face_with_3_hearts: you another 5 Animes :star:  to Binge Watch! '':heart_eyes:')
st.image("Animewallpaper.png", width=1050)
st.header('Please choose Recommendation :rocket: Engine: ')
st.warning('Please Wait Patiently while the Background Process is Complete :turtle:')


engine = st.radio('Select Any of the Recommendation Models below:',
                  options=('Content Based Recommendations','Custom Based Recommendations'))

df_anime = pd.read_csv('csv_files/df_anime.csv')
ratings_per_user = pickle.load(open('pickle_files/ratings_per_user.pkl', 'rb'))


if engine == 'Content Based Recommendations':
    st.info('Based on Anime You Select, Recommendation Engine will Recommend Similar Animes!')
    anime_names = df_anime['Name'].tolist()
    anime_selected = st.selectbox('Choose or Type Anime Name:', options=anime_names)
    similar_animes_obj = Collaborative(anime_selected)
    similar_animes = similar_animes_obj.find_similar_animes()
    StreamlitDisplay(similar_animes)
    st.balloons()


else:
    st.info('Based on the Anime Rating, Genres or Description You Choose from the BELOW options ,Recommendation Engine will Recommend Similar Animes! ')
    user_needs = CustomUser()
    val = st.slider("Anime Rating Slider", min_value=3.0, max_value=8.0, value=6.5)
    anime_genres = ['Comedy', 'Fantasy', 'Action', 'Adventure', 'Sci-Fi',
       'Drama', 'Romance', 'Slice of Life', 'Supernatural', 'Hentai',
       'Mystery', 'Avant Garde', 'Ecchi', 'Sports', 'Horror', 'Suspense',
       'Award Winning', 'Boys Love', 'Gourmet', 'Girls Love', 'Erotica']
    nsfw = ['Ecchi','Erotica','Hentai']
    user_selected_genres = st.multiselect("Choose Genres:",options=anime_genres)
    for genre in user_selected_genres:
        if genre in nsfw:
            st.warning('NSFW Genre(s) Selected :warning:')
            break
    user_text = st.text_area("Enter Anime Description, Main Characters, Synopsis, Anime Short Story or LEAVE it BLANK: ",)
    if st.button('Search for Animes!'):
        similar_animes = user_needs.requirementbased(user_selected_genres,val,user_text)
        StreamlitDisplay(similar_animes,custom_engine=True)







# else:
#     st.info('Based on the Count & Diversity of Animes a Random Database User has seen,Recommendation Engine will '
#             'Recommend Similar Animes! ')
#     st.info('Choose the Episode Count BELOW, We will recommend Animes watched by Similar Users!')
#     st.write(" ")
#     episode_count = st.slider(" ", min_value=1.0, max_value=3000.0, value=650.0)
#     random_user_id = int(ratings_per_user[ratings_per_user >= episode_count].sample(1, random_state=42).index[0])
#     user = UserAnime()
#     similar_users = user.find_similar_users(random_user_id)
#     user_pref = user.get_user_preferences(random_user_id)
#     similar_animes = user.get_recommended_animes(similar_users, user_pref)
#     StreamlitDisplay(similar_animes,user_engine=True)



