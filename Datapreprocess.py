import pandas as pd
import plotly.express as px
import  streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

def preprocess():
    df = pd.read_parquet("Data/0000 (1).parquet")
    print(df.columns)
    df.drop(columns="Unnamed: 0", axis=1, inplace=True)
    print(df.info())
    print(df.isna().sum())
    df.dropna(inplace=True)
    print(df.isna().sum())
    print(df['album_name'].nunique())
    df['album_name'] = df['album_name'].replace('^\W', "", regex=True)
    df['album_name'].replace('', "No album name aavilable", inplace=True)

    tab1, tab2, tab3, tab4, tab5= st.tabs(['Album Insights', 'Track Insights', "Artists",'Genre Insights', 'Common Insights'])
    with tab1:
        d = df.groupby(['album_name'], as_index=False)['popularity'].count()
        d = d.head(10)
        d.sort_values("popularity", ascending=False, inplace=True)
        image=px.bar(d, x=d.album_name, y=d.popularity, barmode='stack', color='album_name', title="Top 10 Album Name vs Popularity")
        st.plotly_chart(image, use_container_width=True)

        d = df.groupby(['album_name'], as_index=False)['track_genre'].count()
        d.sort_values("track_genre", ascending=False, inplace=True)
        d=d.head(10)
        image = px.bar(d, x=d.album_name, y=d.track_genre, barmode='stack', color='track_genre',title="Top 10 Album Name vs track_genre")
        st.plotly_chart(image, use_container_width=True)

        d = df.groupby(['album_name'], as_index=False)['duration_ms'].sum()
        d.sort_values("duration_ms", ascending=False, inplace=True)
        d = d.head(10)
        image = px.funnel(d, x=d.album_name, y=d.duration_ms, color='album_name',
                       title="Top 10 Album Name vs duration in ms")
        st.plotly_chart(image, use_container_width=True)

        d = df.groupby(['album_name'], as_index=False)['danceability'].sum()
        d.sort_values("danceability", ascending=False, inplace=True)
        d = d.head(10)
        image = px.pie(names=d.album_name, values=d.danceability,
                       title="Top 10 Album Name and  % of danceability")
        st.plotly_chart(image, use_container_width=True)

    with tab2:
        d = df.groupby(['track_name'], as_index=False)['acousticness'].sum()
        d.sort_values("acousticness", ascending=False, inplace=True)
        d = d.head(10)
        image = px.pie(names=d.track_name, values=d.acousticness,
                       title="Top 10 Track Name % acousticness")
        st.plotly_chart(image, use_container_width=True)

        d = df.groupby(['track_name'], as_index=False)['popularity'].sum()
        d.sort_values("popularity", ascending=False, inplace=True)
        d = d.head(10)
        image = px.bar(d, y=d.track_name, x=d.popularity, color='track_name', title="Top 10 Track Name vs Popularity")
        st.plotly_chart(image, use_container_width=True)

        d = df.groupby(['track_name'], as_index=False)['energy'].sum()
        d.sort_values("energy", ascending=False, inplace=True)
        d = d.head(10)
        image = px.bar(d, x=d.track_name, y=d.energy, color='track_name', title="Top 10 Track Name vs energy")
        st.plotly_chart(image, use_container_width=True)


        d = df.groupby(['track_name'], as_index=False)['speechiness'].sum()
        d.sort_values("speechiness", ascending=False, inplace=True)
        d = d.head(10)
        image = px.scatter(d, x=d.track_name, y=d.speechiness, color='track_name', symbol="track_name",title="Top 10 Track Name vs speechiness")
        st.plotly_chart(image, use_container_width=True)

        d = df.groupby(['track_name'], as_index=False)['instrumentalness'].count()
        d.sort_values("instrumentalness", ascending=False, inplace=True)
        d = d.head(10)
        image = px.bar(d, y=d.track_name, x=d.instrumentalness, color='instrumentalness', orientation='h',
                           title="Top 10 Track Name vs instrumentalness")
        st.plotly_chart(image, use_container_width=True)

    with tab3:
        d = df.groupby('artists', as_index=False)['track_genre'].count()
        d.sort_values("track_genre", ascending=False, inplace=True)
        d = d.head(10)
        image = px.bar(d, x=d.track_genre, y=d.artists, color='track_genre',
                       title="Top 10 artists vs no of track_genre")
        st.plotly_chart(image, use_container_width=True)

        d = df.groupby(['artists'], as_index=False)['album_name'].count()
        d.sort_values("album_name", ascending=False, inplace=True)
        d = d.head(10)
        image = px.area(d, x=d.artists, y=d.album_name, color='album_name',
                        title="Top 10 Artists Name vs albums")
        st.plotly_chart(image, use_container_width=True)

        d = df.groupby(['artists'], as_index=False)['liveness'].sum()
        d.sort_values("liveness", ascending=False, inplace=True)
        d = d.head(10)
        image = px.funnel(d, x=d.artists, y=d.liveness, color='liveness',
                        title="Top 10 Artists Name vs liveness")
        st.plotly_chart(image, use_container_width=True)

        d = df.groupby(['artists'], as_index=False)['speechiness'].count()
        d.sort_values("speechiness", ascending=False, inplace=True)
        d = d.head(10)
        image = px.scatter(d, x=d.artists, y=d.speechiness, color='artists', symbol="artists",
                           title="Top 10 Artists Name vs speechiness")
        st.plotly_chart(image, use_container_width=True)

        col1,col2= st.columns([1,1])

        with col1:
            d = df.groupby(['artists'], as_index=False)['loudness'].count()
            d.sort_values("loudness", ascending=False, inplace=True)
            d = d.head(10)
            image = px.pie(names=d.artists, values=d.loudness,
                               title="least 10 Artists Name and % loudness")
            st.plotly_chart(image, use_container_width=True)

        with col2:
            d = df.groupby(['artists'], as_index=False)['loudness'].count()
            d.sort_values("loudness", ascending=False, inplace=True)
            d = d.tail(10)
            image = px.pie(names=d.artists, values=d.loudness,
                               title="least 10 Artists Name and % loudness")
            st.plotly_chart(image, use_container_width=True)

        d = df.groupby(['artists'], as_index=False)['energy'].sum()
        d.sort_values("energy", ascending=False, inplace=True)
        d = d.head(10)
        image = px.bar(d, x=d.artists, y=d.energy, color='artists',
                           title="Top 10 Artists Name vs energy")
        st.plotly_chart(image, use_container_width=True)


    with tab4:
        d = df.groupby(['track_genre'], as_index=False)['popularity'].sum()
        d.sort_values("popularity", ascending=False, inplace=True)
        d = d.head(10)
        image = px.bar(d, x=d.track_genre, y=d.popularity, color='track_genre',
                           title="Top 10 track_genre  vs popularity")
        st.plotly_chart(image, use_container_width=True)

        d=df.groupby('time_signature', as_index=False)['track_genre'].count()
        d.sort_values("track_genre", ascending=False, inplace=True)
        d = d.head(10)
        image = px.scatter(d, x=d.track_genre, y=d.time_signature, color='track_genre',
                       title="time_signature vs no of track_genre")
        st.plotly_chart(image, use_container_width=True)

        d = df.groupby(['track_genre'], as_index=False)['loudness'].sum()
        d.sort_values("loudness", ascending=False, inplace=True)
        d = d.head(10)
        image = px.bar(d, x=d.track_genre, y=d.loudness, color='track_genre',
                       title="Top 10 track_genre  vs loudness")
        st.plotly_chart(image, use_container_width=True)
    with tab5:
        d=df.drop(columns=['track_id', 'artists', 'album_name', 'track_name', 'track_genre'])

        image=px.density_heatmap(data_frame=d.corr(), color_continuous_scale='agsunset', title='Correlation')
        st.plotly_chart(image,use_container_width=True)

        fig, ax = plt.subplots()
        sns.set(font_scale=0.25)
        sns.heatmap(d.corr(),annot=True,ax=ax)
        st.pyplot(fig)

        st.write(d.corr())

    df.to_csv('Data.csv')




