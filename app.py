import streamlit as st
import pickle 
import pandas as pd

def recommend(movie):
    find_img = movies[movies["title"] == movie]
    movie_index = find_img.index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    recommend_movies = []
    recommend_movies_posters = []

    for i in movies_list:
        movie_id = i[0]
        title_name = movies.iloc[movie_id].title
        url = poster_imgs[poster_imgs["title"] == title_name]
        
        if not url.empty:
            urls = url.poster_img.values[0]
            recommend_movies.append(title_name)
            recommend_movies_posters.append(urls)
        else:
            recommend_movies.append(title_name)
            recommend_movies_posters.append("No Image Available")  # Placeholder if image not found
    
    return recommend_movies, recommend_movies_posters

# Load data
poster_url = pickle.load(open("poster_url.pkl", 'rb'))
poster_imgs = pd.DataFrame(poster_url)
movies_dict = pickle.load(open("movies_dict.pkl", 'rb'))
movies = pd.DataFrame(movies_dict)
similarity = pickle.load(open("similarity.pkl", "rb"))

# Streamlit app
st.title('Movie Recommender System')

selected_movie_name = st.selectbox(
    'Select a movie:',
    movies['title'].values
)

if st.button('Recommend'):
    names, posters = recommend(selected_movie_name)
    col1, col2, col3, col4, col5 = st.columns(5)

    if len(names) > 0:
        with col1:
            st.text(names[0])
            st.image(posters[0])

    if len(names) > 1:
        with col2:
            st.text(names[1])
            st.image(posters[1])

    if len(names) > 2:
        with col3:
            st.text(names[2])
            st.image(posters[2])
        
    if len(names) > 3:
        with col4:
            st.text(names[3])
            st.image(posters[3])

    if len(names) > 4:
        with col5:
            st.text(names[4])
            st.image(posters[4])
