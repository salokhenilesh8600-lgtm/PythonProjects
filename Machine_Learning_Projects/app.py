import streamlit as st
import pickle
import requests
import time

session = requests.Session()
def fetch_poster(movie_id):
    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US"
    for _ in range(3):  # retry 3 times
        try:
            response = requests.get(url, timeout=5)

            if response.status_code == 200:
                data = response.json()
                poster_path = data.get('poster_path')

                if poster_path:
                    return "https://image.tmdb.org/t/p/w500/" + poster_path
            else:
                st.write(response.status_code)

            return None

        except requests.exceptions.RequestException:
            time.sleep(1)  # wait before retry

    return None


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)),reverse=True,key=lambda x:x[1])[1:4]

    recommended_movies = []
    recommended_movies_poster = []


    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
        recommended_movies_poster.append(fetch_poster(movies.iloc[i[0]].movie_id))
        #time.sleep(0.1)
    return recommended_movies,recommended_movies_poster


movies = pickle.load(open('movies.pkl','rb'))
movies_names = movies['title'].values

similarity = pickle.load(open('similarity.pkl','rb'))

st.title('Movie Recommender System')

selected_movie_name = st.selectbox("Select Movies ", movies_names)

if st.button('Recommend'):
    names,posters = recommend(selected_movie_name)
    print(names,posters)
    cols = st.columns(3)
    for i, col in enumerate(cols):
        with col:
            st.text(names[i])
            if posters[i] is not None:
                st.image(posters[i])
            else:
                st.write("Image not available")          
        
        
    