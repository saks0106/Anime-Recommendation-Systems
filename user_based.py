# import numpy as np
# import pickle
# import pandas as pd
#
# #---------------------------------------------------------------------------------------
# anime_weights = pickle.load(open('pickle_files/anime_weights.pkl', 'rb'))
# user_weights = pickle.load(open('pickle_files/user_weights.pkl', 'rb'))
# anime_encoder = pickle.load(open('pickle_files/anime_encoder.pkl', 'rb'))
# user_encoder = pickle.load(open('pickle_files/user_encoder.pkl', 'rb'))
# ratings_per_user = pickle.load(open('pickle_files/ratings_per_user.pkl', 'rb'))
# df = pd.read_csv('csv_files/df_user_scores.csv')
# # df_anime = pd.read_csv('csv_files/df_anime.csv')
#
#
#
# #df_user_score csv link
# # url_score = 'https://drive.google.com/file/d/1k3P9Euh0LRtazQYvrPR8ohTnt6gCBb1W/view?usp=sharing'
# # url_score='https://drive.google.com/uc?id=' + url_score.split('/')[-2]
# # df = pd.read_csv(url_score,encoding='unicode_escape')
#
# #df_anime csv link
# url_anime = 'https://drive.google.com/file/d/1_6GUa3BAuNkrCuicjacEoQszOO8SKubp/view?usp=drive_link'
# url_anime='https://drive.google.com/uc?id=' + url_anime.split('/')[-2]
# df_anime = pd.read_csv(url_anime,encoding='unicode_escape')
#
# #-----------------------------------------------------------------------------------------
#
# class UserAnime:
#     def find_similar_users(self, user_id,):
#         try:
#             SimilarityArr = []
#             index = user_id
#             encoded_index = user_encoder.transform([index])[0]
#             weights = user_weights
#             distances = np.dot(weights, weights[encoded_index])
#             sorted_distances = distances.argsort()[::-1]
#             top_sorted_distances = sorted_distances[0:31]
#
#             for i in top_sorted_distances:
#                 similarity = distances[i]
#                 decoded_index = user_encoder.inverse_transform([i])[0]
#                 SimilarityArr.append({"similar_users": decoded_index, "similarity": similarity})
#             Frame = pd.DataFrame(SimilarityArr).sort_values(by="similarity", ascending=False)
#             return Frame
#
#         except:
#             print(f'{user_id} Not present, Try Another')
#
#
#
#
#     def get_user_preferences(self, user_id):
#         animes_watched_by_user = df[df['user_id'] == user_id]
#         user_rating_percentile = np.percentile(animes_watched_by_user['rating'], 95)
#         animes_watched_by_user = animes_watched_by_user[animes_watched_by_user.rating >= user_rating_percentile]
#         top_animes_by_user = (animes_watched_by_user.sort_values(by="rating", ascending=False).anime_id.values)
#         anime_df_rows = df_anime[df_anime["anime_id"].isin(top_animes_by_user)]
#         anime_df_rows = anime_df_rows[["Name", "Genres"]]
#
#         return anime_df_rows
#
#
#
#
#     def get_recommended_animes(self, similar_users, user_pref, n=31):
#         recommended_animes = []
#         anime_list = []
#
#         for user in similar_users.similar_users.values:
#             preferred_animes = self.get_user_preferences(int(user))
#             pref_list = preferred_animes[~preferred_animes["Name"].isin(user_pref["Name"].values)]
#             anime_list.append(pref_list.Name.values)
#
#         if len(anime_list) == 0:
#             print("No anime recommendations available for the given users.")
#             return pd.DataFrame()
#
#         anime_list = pd.DataFrame(anime_list)
#         sorted_list = pd.DataFrame(pd.Series(anime_list.values.ravel()).value_counts()).head(n)
#         anime_count = df['anime_id'].value_counts()
#
#         for i, anime_name in enumerate(sorted_list.index):
#             if isinstance(anime_name, str):
#                 try:
#                     anime_id = df_anime[df_anime.Name == anime_name].anime_id.values[0]
#                     name = df_anime[df_anime['Name'] == anime_name]['Name'].values[0]
#                     genre = df_anime[df_anime.Name == anime_name].Genres.values[0]
#                     synopsis = df_anime[df_anime.Name == anime_name].Synopsis.values[0]
#                     local_name = df_anime[df_anime.Name == anime_name]['Other name'].values[0]
#                     score = df_anime[df_anime.Name == anime_name]['Score'].values[0]
#                     episodes = df_anime[df_anime.Name == anime_name].Episodes.values[0]
#                     fav = df_anime[df_anime.Name == anime_name].Favorites.values[0]
#                     url = df_anime[df_anime.Name == anime_name]['Image URL'].values[0]
#                     n_user_pref = anime_count.get(anime_id,0)  # Get the total count of users who have watched this anime
#
#                     recommended_animes.append({
#                         "Name": name,
#                         "Similarity": n_user_pref,
#                         "Genres": genre,
#                         "Synopsis": synopsis,
#                         'Other name': local_name,
#                         'Score': score,
#                         'Episodes': episodes,
#                         'Favorites': fav,
#                         'Image URL': url
#                     })
#
#                     recommended_animes = sorted(recommended_animes, key=lambda x: x['Similarity'])
#                 except:
#                     pass
#
#         return recommended_animes
#
#
