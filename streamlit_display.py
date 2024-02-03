import streamlit as st
import random

class StreamlitDisplay:
    def __init__(self, animes, custom_engine=False):
        self.animes = animes  # dictionaries in list
        self.custom_engine = custom_engine
        self.recommendation_main_title()

    def recommendation_main_title(self):
        try:
            if self.custom_engine:
                st.subheader('Top Recommendation')

            m1, m2, m3 = st.columns(3)
            m1.image(self.animes[0]['Image URL'], width=300, )
            m2.subheader(f"Anime Selected: {self.animes[0]['Name']}")
            m2.subheader(f"Anime Japanese Name: {self.animes[0]['Other name']}")
            m2.markdown(f"<h5>Anime Genres : {self.animes[0]['Genres']}</h5>", unsafe_allow_html=True)
            m2.markdown(f"<h5>Anime Worldwide Score: {self.animes[0]['Score']}</h5>", unsafe_allow_html=True)
            m2.markdown(f"<h5>Episodes Count: {self.animes[0]['Episodes']}</h5>", unsafe_allow_html=True)
            m2.markdown(f"<h5>Loved by: {self.animes[0]['Favorites']} people </h5>", unsafe_allow_html=True)
            m2.markdown(f"<h5>Aired On: {self.animes[0]['Aired_on']} </h5>", unsafe_allow_html=True)
            m3.caption(f"Anime Synopsis : {self.animes[0]['Synopsis']}")
        except:
            st.error('Recommendation NOT Complete. Try Again', icon='❗')
        self.recommendations()

    def recommendations(self):
        try:
            st.header("Recommended Animes are: ")
            cols1 = [col2, col3, col4, col5, col6] = st.columns(5)
            for i in range(5):
                with cols1[i]:
                    random_number = i + 1
                    st.image(self.animes[random_number]['Image URL'], width=225,
                             caption=self.animes[random_number]['Name'],
                             use_column_width='auto')
                    if self.custom_engine:
                        st.markdown(f"Recommendation Score: {self.animes[random_number]['Score']}")
                    else:
                        st.markdown(f"Anime Score: {round(self.animes[random_number]['Score'] * 10, 2)} %")


            cols2 = [col7, col8, col9, col10, col11] = st.columns(5)
            for i in range(5):
                with cols2[i]:
                    random_number = random.randint(16, 30)
                    st.image(self.animes[random_number]['Image URL'], width=225,
                             caption=self.animes[random_number]['Name'],
                             use_column_width='auto')
                    if self.custom_engine:
                        st.markdown(f"Recommendation Score: {self.animes[random_number]['Score']}")
                    else:
                        st.markdown(f"Anime Score: {round(self.animes[random_number]['Score'] * 10, 2)} %")

            st.success('Animes Recommendation Complete', icon='✅')
            if self.custom_engine:
                st.snow()
            else:
                self.animes.clear()
        except:
            st.error('Recommendation NOT Complete. Try Again', icon='❗')





# import streamlit as st
# import random
# from st_clickable_images import clickable_images
# from content_based import Collaborative
#
#
# class StreamlitDisplay:
#     def __init__(self, animes, custom_engine=False):
#         self.animes = animes  # dictionaries in list
#         self.custom_engine = custom_engine
#         self.recommendation_display()
#
#
#
#
#     def recommendation_display(self):
#         try:
#             if self.custom_engine:
#                 st.subheader('Top Recommendation')
#
#             m1, m2, m3 = st.columns(3)
#             m1.image(self.animes[0]['Image URL'], width=300, )
#             m2.subheader(f"Anime Selected: {self.animes[0]['Name']}")
#             m2.subheader(f"Anime Japanese Name: {self.animes[0]['Other name']}")
#             m2.markdown(f"<h5>Anime Genres : {self.animes[0]['Genres']}</h5>", unsafe_allow_html=True)
#             m2.markdown(f"<h5>Anime Worldwide Score: {self.animes[0]['Score']}</h5>", unsafe_allow_html=True)
#             m2.markdown(f"<h5>Episodes Count: {self.animes[0]['Episodes']}</h5>", unsafe_allow_html=True)
#             m2.markdown(f"<h5>Loved by: {self.animes[0]['Favorites']} people </h5>", unsafe_allow_html=True)
#             m2.markdown(f"<h5>Aired On: {self.animes[0]['Aired_on']} </h5>", unsafe_allow_html=True)
#             m3.caption(f"Anime Synopsis : {self.animes[0]['Synopsis']}")
#
#             st.header("Recommended Animes are: ")
#             col2, col3, col4, col5, col6 = st.columns(5)
#
#
#             with col2:
#                 col_2_value = random.randint(1, 3)
#                 st.image(self.animes[col_2_value]['Image URL'], width=225, caption=self.animes[col_2_value]['Name'],
#                          use_column_width='auto')
#
#
#                 if self.custom_engine:
#                     st.markdown(f"Recommendation Score: {self.animes[col_2_value]['Score']}")
#
#                 else:
#                     st.markdown(f"Recommendation Score: {round(self.animes[col_2_value]['Score'] * 10, 2)} %")
#
#             with col3:
#                 col_3_value = random.randint(4, 6)
#                 st.image(self.animes[col_3_value]['Image URL'], width=225, caption=self.animes[col_3_value]['Name'],
#                          use_column_width='auto')
#                 if self.custom_engine:
#                     st.markdown(f"Recommendation Score: {self.animes[col_3_value]['Score']}")
#
#                 else:
#                     st.markdown(f"Recommendation Score: {round(self.animes[col_3_value]['Score'] * 10, 2)} %")
#
#             with col4:
#                 col_4_value = random.randint(7, 9)
#                 st.image(self.animes[col_4_value]['Image URL'], width=225, caption=self.animes[col_4_value]['Name'],
#                          use_column_width='auto')
#                 if self.custom_engine:
#                     st.markdown(f"Recommendation Score: {self.animes[col_4_value]['Score']}")
#
#                 else:
#                     st.markdown(f"Recommendation Score: {round(self.animes[col_4_value]['Score'] * 10, 2)} %")
#
#             with col5:
#                 col_5_value = random.randint(10, 12)
#                 st.image(self.animes[col_5_value]['Image URL'], width=225, caption=self.animes[col_5_value]['Name'],
#                          use_column_width='auto')
#                 if self.custom_engine:
#                     st.markdown(f"Recommendation Score: {self.animes[col_5_value]['Score']}")
#
#                 else:
#                     st.markdown(f"Recommendation Score: {round(self.animes[col_5_value]['Score'] * 10, 2)} %")
#
#             with col6:
#                 col_6_value = random.randint(13, 15)
#                 st.image(self.animes[col_6_value]['Image URL'], width=225, caption=self.animes[col_6_value]['Name'],
#                          use_column_width='auto')
#                 if self.custom_engine:
#                     st.markdown(f"Recommendation Score: {self.animes[col_6_value]['Score']}")
#
#                 else:
#                     st.markdown(f"Recommendation Score: {round(self.animes[col_6_value]['Score'] * 10, 2)} %")
#
#             st.write(" ")
#             st.markdown("""---""")
#             st.write(" ")
#             col7, col8, col9, col10, col11 = st.columns(5)
#
#             with col7:
#                 col_7_value = random.randint(16, 18)
#                 st.image(self.animes[col_7_value]['Image URL'], width=225, caption=self.animes[col_7_value]['Name'],
#                          use_column_width='auto')
#                 if self.custom_engine:
#                     st.markdown(f"Recommendation Score: {self.animes[col_7_value]['Score']}")
#
#                 else:
#                     st.markdown(f"Recommendation Score: {round(self.animes[col_7_value]['Score'] * 10, 2)} %")
#
#             with col8:
#                 col_8_value = random.randint(19, 21)
#                 st.image(self.animes[col_8_value]['Image URL'], width=225, caption=self.animes[col_8_value]['Name'],
#                          use_column_width='auto')
#                 if self.custom_engine:
#                     st.markdown(f"Recommendation Score: {self.animes[col_8_value]['Score']}")
#
#                 else:
#                     st.markdown(f"Recommendation Score: {round(self.animes[col_8_value]['Score'] * 10, 2)} %")
#
#             with col9:
#                 col_9_value = random.randint(22, 24)
#                 st.image(self.animes[col_9_value]['Image URL'], width=225, caption=self.animes[col_9_value]['Name'],
#                          use_column_width='auto')
#                 if self.custom_engine:
#                     st.markdown(f"Recommendation Score: {self.animes[col_9_value]['Score']}")
#
#                 else:
#                     st.markdown(f"Recommendation Score: {round(self.animes[col_9_value]['Score'] * 10, 2)} %")
#
#             with col10:
#                 col_10_value = random.randint(25, 27)
#                 st.image(self.animes[col_10_value]['Image URL'], width=225, caption=self.animes[col_10_value]['Name'],
#                          use_column_width='auto')
#                 if self.custom_engine:
#                     st.markdown(f"Recommendation Score: {self.animes[col_10_value]['Score']}")
#
#                 else:
#                     st.markdown(f"Recommendation Score: {round(self.animes[col_10_value]['Score'] * 10, 2)} %")
#
#             with col11:
#                 col_11_value = random.randint(27, 30)
#                 st.image(self.animes[col_11_value]['Image URL'], width=225, caption=self.animes[col_11_value]['Name'],
#                          use_column_width='auto')
#                 if self.custom_engine:
#                     st.markdown(f"Recommendation Score: {self.animes[col_11_value]['Score']}")
#
#                 else:
#                     st.markdown(f"Recommendation Score: {round(self.animes[col_11_value]['Score'] * 10, 2)} %")
#
#             st.success('Animes Recommendation Complete', icon='✅')
#
#             if self.custom_engine:
#                 st.snow()
#             else:
#                 self.animes.clear()
#
#
#
#         except:
#             st.error('Recommendation NOT Complete. Try Again', icon='❗')

