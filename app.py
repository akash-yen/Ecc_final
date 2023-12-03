import streamlit as st
import pandas as pd

users = pd.read_csv("all_user_recommendations.csv")

st.title("Movie Recommender System")
user_list = users['user_id'].unique()
selected_user = st.selectbox(
    "Select a user :",
    user_list
)

if st.button('Show Recommendation'):
    st.write("Recommended movies based on the user selected are :")
    recommended_movie_names = users[users['user_id'] == selected_user]
    df = pd.DataFrame(recommended_movie_names, columns=["original_title", "genres", "overview"])
    df = df.rename(columns={"original_title": "MovieTitle", "genres": "MovieGenre", "overview" : "MovieOverview"})
    st.table(df)

st.text("Project by : Akash, Tharun")