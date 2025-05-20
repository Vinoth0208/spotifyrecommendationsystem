import sys

from model import model
from PIL import Image, ImageFilter
sys.path.insert(1,r"spotifyrecommendationsystem\venv\Lib\site-packages")
import streamlit_option_menu
from streamlit_option_menu import option_menu
from Data import data
from Datapreprocess import preprocess
import streamlit as st

icon=Image.open('image/images (1).png')
st.set_page_config(layout="wide", page_title=" Spotify Recommendation System", page_icon=icon)
selected=streamlit_option_menu.option_menu("Menu",["About", "Data", "Data Explore", "Recommendation model", "Conclusion"],
                                           icons=["exclamation-circle","search","bar-chart","globe","lightbulb",'telephone-forward' ],
                                           menu_icon="cast",
                                           default_index=0,
                                           orientation="horizontal",
                                           styles={"nav-link": {"font-size": "15px", "text-align": "centre",
                                                                "--hover-color": "#d1798e"},
                                                   "nav-link-selected": {"background-color": "#b30e35"},"width":"100%"},)


if selected=='About':
    col1,col2=st.columns([1,1.6])
    with col2:
        icon = Image.open('image/images (1).png')
        st.image(icon, width=50)
    with col1:
        st.header(":green[Spotify Recommendation System]")

    st.markdown(':blue[Technology used: Python, Streamlit, EDA, Plotly, Seaborn, Pandas, Machine learning]')

    st.markdown(":red[Introduction:]")
    st.text("""
    Welcome to our Spotify Recommendation System Application! We aim to provide you with a personalized music\n
    discovery experience based on your unique tastes and preferences. With our advanced algorithm and vast collection of songs,\n
    we'll help you find new tracks and albums that you're sure to love. Let's dive into the features and benefits of our application""")

    st.markdown(":blue[Intuitive User Interface:]")
    st.text("""
    Our application offers a user-friendly interface, allowing you to navigate seamlessly through different features and sections.\n
    The design is clean, modern, and visually appealing, ensuring a pleasant user experience.\n""")

    st.markdown(":green[Personalized Recommendations:]")
    st.text("""
    By analyzing your inputs our recommendation engine will generate tailored music suggestions just for you.\n
    Discover new tracks and hidden gems that resonate with your personal taste, keeping your music library fresh and exciting.""")
if selected== 'Data':
    data()
if selected== 'Data Explore':
    preprocess()
if selected=='Recommendation model':
    model()
if selected=='Conclusion':
    st.header(":green[Conclusion:]")
    col1, col2=st.columns([1,1])
    with col1:
        st.subheader(':orange[Album:]')
        st.write('''
        Top Album with respect to Popularity is "Deluxe"\n
        Top Album with respect to Track Genre is "Alternative Christmas 2022"\n
        Top Album with highest Duration is "Alternative Christmas 2022"\n
        Top Album with highest Percentage of Danceability is "Feliz Cumpleaños con Perreo"
        
        ''')

        st.subheader(':red[Artist:]')
        st.write('''
               Top Artist with respect to no of tracks is "The Beatles"\n
               Top Artist with respect to Albums is "The Beatles"\n
               Top Artist with respect to livness is "Charlie brown jr."\n
               Top Artist with highest Energy is "Linkin park"

               ''')

        with col2:
            st.subheader(':blue[Track:]')
            st.write('''
            Top Track with respect to Percentage of Acousticness is "Run Rudolph Run"\n
            Top Track with respect to Popularity is "Alone"\n
            Top Track with highest Energy is "Run Rudolph Run"\n
            Top Track with highest instrumentalness  is "X ultima vez"

            ''')
            st.subheader(':green[Genre]')
            st.write('''
                        Top Genre with respect to loudness is "latin"\n
                        Top Genre with respect to Popularity is "Pop-film"
                        ''')



if selected=='Contact':
    col1, col2=st.columns([0.5,1.5], gap='small')
    with col2:
        st.subheader("Name: :green[Vinoth Palanivel]")
        st.write("Degree: :green[Bachelor of Engineering in Electrical and Electronics Engineering]")
        st.write("E-mail: :green[vinothchennai97@gmail.com]")
        st.write("Mobile: :green[7904197698 or 9677112815]")
        st.write("Linkedin: :orange[https://www.linkedin.com/in/vinoth-palanivel-265293211/]")
        st.write("Github: :orange[https://github.com/Vinoth0208/]")
