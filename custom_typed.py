import pandas as pd
from nltk.stem.porter import PorterStemmer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import warnings

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
        try:
            features = self.standardization(features)
            eng_sw = stopwords.words('english')
            features_token = word_tokenize(features)
            features_token_set = set([ps.stem(token) for token in features_token if token not in eng_sw])


            genre_pattern = '|'.join(user_input_genres)
            genres_selected = df_anime['Genres'].str.contains(genre_pattern)
            df_temp = df_anime[genres_selected]
            reqbased = df_temp[df_temp['Score'] >= scores].sort_values(by='Score', ascending=False)
            reqbased = reqbased.reset_index(drop=True)

            common_count = []
            for i in range(reqbased.shape[0]):
                summary = self.standardization(reqbased['Synopsis'][i])
                summary_features_token = word_tokenize(summary)
                combo_summary_token_set = set([ps.stem(token) for token in summary_features_token if token not in eng_sw])
                similarity = len(features_token_set.intersection(combo_summary_token_set))
                reqbased['Similarity'] = "{:.2f}%".format(similarity * 100)
                common_count.append(len(features_token_set.intersection(combo_summary_token_set)))

            reqbased['Similarity_Count'] = common_count
            reqbased = reqbased.sort_values(by='Similarity_Count', ascending=False).head(31)
            reqbased = reqbased[['Name','Similarity','Genres','Synopsis','Other name','Score','Episodes','Favorites','Image URL']]
            return list(reqbased.to_dict('records'))

        except:
            print(f"{features} not found!. Please Try Again")

