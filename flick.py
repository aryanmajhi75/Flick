# import streamlit as st
# import Movies.getMovies
# import Lists,Shows,Movies
# import Lists.getList
# import Shows.getShows
# import pandas as pd

# # Set the page title
# st.title("Hello, Streamlit!")

# # Add some text
# st.write("Welcome to your Streamlit app hosted on port 5050!")

# st.sidebar()

# movies=Movies.getMovies.movies_data
# # st.write(movies)
# data = [(item['name'], item['year']) for item in movies]
# df = pd.DataFrame(data, columns=['Title', 'Year'])
# st.write("Available Movies :")
# st.dataframe(df)

# shows=Shows.getShows.data_list
# # st.write(shows)
# data = [(item['title'], item['year']) for item in shows['tv_results']]
# df = pd.DataFrame(data, columns=['Title', 'Year'])
# st.write("Available Shows :")
# st.dataframe(df)

import streamlit as st
import pandas as pd
import Movies.getMovies
import Lists, Shows, Movies
import Lists.getList
import Shows.getShows

# Set the page title
st.set_page_config(page_title="My Streamlit App", layout="wide")

# Create tabs for navigation
tabs = st.tabs(["Home", "Movies", "Shows"])

# Home Page
with tabs[0]:
    st.title("Home")
    st.write("Welcome to your Streamlit app hosted on port 5050!")

# Movies Page
with tabs[1]:
    st.title("Movies")
    st.write("Available Movies:")

    movies = Movies.getMovies.movies_data
    data = [(item['name'], item['year']) for item in movies]
    df = pd.DataFrame(data, columns=['Title', 'Year'])
    st.dataframe(df)

# Shows Page
with tabs[2]:
    st.title("Shows")
    st.write("Available Shows:")

    shows = Shows.getShows.data_list
    data = [(item['title'], item['year']) for item in shows['tv_results']]
    df = pd.DataFrame(data, columns=['Title', 'Year'])
    st.dataframe(df)
