import pandas as pd
import streamlit as st
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import warnings
import random

import string
import tensorflow as tf
import re
string.punctuation
ps = PorterStemmer()
warnings.filterwarnings(action='ignore')
pd.set_option('display.max_columns', None)
df_anime = pd.read_csv('df_anime.csv')


class CustomUser:

    def standardization(self,data):
        x = tf.strings.lower(data)  # all strings to lower
        x = tf.strings.regex_replace(x, "<[^>]+>", "")  # removing html
        x = tf.strings.regex_replace(x, "[%s]" % re.escape('!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'),
                                     " ")  # removing punctuation
        x = x.numpy()
        x = x.decode('utf-8')
        return x

    def requirementbased(self,user_input_genres, scores, features):
        self.df_anime2 = df_anime.copy()
        try:
            features = self.standardization(features)
            eng_sw = stopwords.words('english')
            features_token = word_tokenize(features)
            features_token_set = set([ps.stem(token) for token in features_token if token not in eng_sw])

            if len(user_input_genres) != 0:
                genre_pattern = '|'.join(user_input_genres)
                genres_selected = self.df_anime2['Genres'].str.contains(genre_pattern)
                self.df_anime2 = self.df_anime2[genres_selected]

            self.df_anime2 = self.df_anime2[self.df_anime2['Score'] >= scores].sort_values(by='Score', ascending=False)
            self.df_anime2 = self.df_anime2.reset_index(drop=True)

            for i in range(self.df_anime2.shape[0]):
                summary = self.standardization(self.df_anime2['Synopsis'][i])
                summary_features_token = word_tokenize(summary)
                combo_summary_token_set = set([ps.stem(token) for token in summary_features_token if token not in eng_sw])
                self.df_anime2['Similarity'] = len(features_token_set.intersection(combo_summary_token_set))
            self.df_anime2 = self.df_anime2.sort_values(by='Similarity', ascending=False)
            st.dataframe(self.df_anime2)
            for i in range(30):
                anime_name = self.df_anime2['Name'].values[i]
                similarity = self.df_anime2['Similarity'].values[i]
                genre = self.df_anime2['Genres'].values[i]
                synopsis = self.df_anime2['Synopsis'].values[i]
                local_name = self.df_anime2['Other name'].values[i]
                score = self.df_anime2['Score'].values[i]
                episodes = self.df_anime2['Episodes'].values[i]
                fav = self.df_anime2['Favorites'].values[i]
                url = self.df_anime2['Image URL'].values[i]

                SimilarityArr = []
                SimilarityArr.append({"Name": anime_name,
                                      "Similarity": similarity,
                                      "Genres": genre,
                                      "Synopsis": synopsis,
                                      "Other name": local_name,
                                      'Score': score,
                                      'Episodes': episodes,
                                      'Favorites': fav,
                                      'Image URL': url})

            return SimilarityArr

        except:
            print(f"{features} not found!. Please Try Again")

