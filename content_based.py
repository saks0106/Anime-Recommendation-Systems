import numpy as np
import pandas as pd
import pickle
import warnings

warnings.filterwarnings(action='ignore')
pd.set_option('display.max_columns', None)

#------------------------------------------------------------------------------------
df_anime = pd.read_csv('df_anime.csv')
anime_weights = pickle.load(open('pickle_files/anime_weights.pkl', 'rb'))
anime_encoder = pickle.load(open('pickle_files/anime_encoder.pkl', 'rb'))


#------------------------------------------------------------------------------------------

class Collaborative:

    SimilarityArr = []
    def __init__(self,name):
        self.name = name

    def find_similar_animes(self,n=30):
        try:
            anime_name = df_anime[df_anime['Name'].str.lower() == self.name.lower()].iloc[0]
            anime_name_index = anime_name['anime_id']
            encoded_index = anime_encoder.transform([anime_name_index])[0]
            anime_name_weight = anime_weights[encoded_index]
            distances = np.dot(anime_weights, anime_name_weight)
            sorted_distances = distances.argsort()[::-1]
            top5_sorted_distances = sorted_distances[:n + 1]

            for anime_index in top5_sorted_distances:
                decoded_anime = anime_encoder.inverse_transform([anime_index])[0]
                anime_frame = df_anime[df_anime['anime_id'] == decoded_anime]
                anime_name = anime_frame['Name'].values[0]
                english_name = anime_frame['English name'].values[0]
                name = english_name if english_name != "UNKNOWN" else anime_name
                genre = anime_frame['Genres'].values[0]
                synopsis = anime_frame['Synopsis'].values[0]
                local_name = anime_frame['Other name'].values[0]
                score = anime_frame['Score'].values[0]
                episodes = anime_frame['Episodes'].values[0]
                fav = anime_frame['Favorites'].values[0]
                url = anime_frame['Image URL'].values[0]
                from_date = anime_frame['Aired_From'].values[0]

                similarity = distances[anime_index]
                similarity = "{:.2f}%".format(similarity * 100)

                Collaborative.SimilarityArr.append({"Name": name,
                                                    "Similarity": similarity,
                                                    "Genres": genre,
                                                    "Synopsis": synopsis,
                                                    "Other name": local_name,
                                                    'Score': score,
                                                    'Episodes': episodes,
                                                    'Favorites': fav,
                                                    'Image URL': url,
                                                    'Aired_on': from_date})

            return Collaborative.SimilarityArr

        except:
            print(f"{self.name} not found!. Please Try Again")


