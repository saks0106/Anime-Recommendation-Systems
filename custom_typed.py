import pandas as pd
import streamlit as st
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import warnings

import tensorflow as tf
import re

ps = PorterStemmer()

warnings.filterwarnings(action='ignore')
pd.set_option('display.max_columns', None)



def standardization(data):
    x = tf.strings.lower(data)  # all strings to lower
    x = tf.strings.regex_replace(x, "<[^>]+>", "")  # removing html
    x = tf.strings.regex_replace(x, "[%s]" % re.escape('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'),
                                 " ")  # removing punctuation
    x = x.numpy()
    x = x.decode('utf-8')
    return x


class CustomUser:

    def __init__(self, user_input_genres, scores, features):
        self.user_input_genres = user_input_genres
        self.scores = scores
        self.features = features
        self.SimilarityArr = []
        self.df_anime2 = pd.read_csv('df_anime.csv')


    def requirementbased(self):

        try:
            features = standardization(self.features)
            eng_sw = stopwords.words('english')
            features_token = word_tokenize(features)
            features_token_set = set([ps.stem(token) for token in features_token if token not in eng_sw])

            genre_pattern = '|'.join(self.user_input_genres)
            genres_selected = self.df_anime2['Genres'].str.contains(genre_pattern)
            self.df_anime2 = self.df_anime2[genres_selected]
            self.df_anime2 = self.df_anime2[self.df_anime2['Score'] >= self.scores].sort_values(by='Score',ascending=False)
            self.df_anime2.reset_index(inplace = True, drop = True)
            self.df_anime2 = self.df_anime2.loc[:,'anime_id':]
            #st.dataframe(self.df_anime2)
            df_anime_dict = self.df_anime2.to_dict('records')
            for i in range(len(df_anime_dict)):
                summary = df_anime_dict[i]['Synopsis']
                summary = standardization(summary)
                summary_features_token = word_tokenize(summary)
                combo_summary_token_set = set(
                    [ps.stem(token) for token in summary_features_token if token not in eng_sw])
                common_count = len(features_token_set.intersection(combo_summary_token_set))
                df_anime_dict[i]['Similarity'] = common_count

            df_anime_dict = sorted(df_anime_dict, key=lambda k: k['Similarity'], reverse=True)


            for i in range(31):
                anime_name = df_anime_dict[i]['Name']
                similarity = df_anime_dict[i]['Similarity']
                genre = df_anime_dict[i]['Genres']
                synopsis = df_anime_dict[i]['Synopsis']
                local_name = df_anime_dict[i]['Other name']
                score = df_anime_dict[i]['Score']
                episodes = df_anime_dict[i]['Episodes']
                fav = df_anime_dict[i]['Favorites']
                url = df_anime_dict[i]['Image URL']
                from_date = df_anime_dict[i]['Aired_From']

                self.SimilarityArr.append({"Name": anime_name,
                                           "Similarity": similarity,
                                           "Genres": genre,
                                           "Synopsis": synopsis,
                                           "Other name": local_name,
                                           'Score': score,
                                           'Episodes': episodes,
                                           'Favorites': fav,
                                           'Image URL': url,
                                           'Aired_on':from_date})

            return self.SimilarityArr



        except:
            print(f"{self.features}  not found!. Please Try Again")
