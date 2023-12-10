import pandas as pd
import streamlit as st
from matplotlib import pyplot as plt
from sklearn import metrics
from sklearn.cluster import KMeans
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA
from sklearn.preprocessing import scale
from sklearn.preprocessing import MinMaxScaler
from mpl_toolkits.mplot3d import Axes3D


def model():
    df=pd.read_csv('Data.csv')
    df_cluster = df.copy()
    X = pd.DataFrame(df_cluster.iloc[:, [5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]].values)
    cols = df_cluster.iloc[:, [5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16,17,18,19]].columns
    X.columns = cols


    scaler = MinMaxScaler()
    scaled = pd.DataFrame(scaler.fit_transform(X))
    scaled.columns = cols
    tab1, tab2, tab3=st.tabs(['elbow-curve','Cluster','Prediction'])
    with tab1:
        col1, col2=st.columns([1,1])
        with col1:
            wcss = []
            for i in range(1, 15):
                kmeans = KMeans(n_clusters=i, init='k-means++', max_iter=113999, n_init=25, random_state=0)
                kmeans.fit(scaled)
                wcss.append(kmeans.inertia_)
            fig, ax = plt.subplots()
            plt.plot(range(1, 15), wcss, 'o')
            plt.plot(range(1, 15), wcss, '-', alpha=0.5)
            plt.title('Elbow Method')
            plt.xlabel('Number of Clusters')
            plt.ylabel('WCSS')
            st.pyplot(fig)

            scaled = scaler.fit_transform(X)
            kmeans = KMeans(n_clusters=11, init='k-means++', max_iter=113999, n_init=25, random_state=0)
            y_kmeans = kmeans.fit_predict(scaled)
        with col2:
            st.markdown('It is observed the curve getting more linear at point 11, So 11 cluster would be ideal')

    with tab2:
        fig, ax = plt.subplots(figsize=(13, 11))
        ax = fig.add_subplot(111, projection='3d')
        plt.scatter(scaled[y_kmeans == 0, 0], scaled[y_kmeans == 0, 1], s=50, c='red', label='Cluster 1')
        plt.scatter(scaled[y_kmeans == 1, 0], scaled[y_kmeans == 1, 1], s=50, c='blue', label='Cluster 2')
        plt.scatter(scaled[y_kmeans == 2, 0], scaled[y_kmeans == 2, 1], s=50, c='green', label='Cluster 3')
        plt.scatter(scaled[y_kmeans == 3, 0], scaled[y_kmeans == 3, 1], s=50, c='cyan', label='Cluster 4')
        plt.scatter(scaled[y_kmeans == 4, 0], scaled[y_kmeans == 4, 1], s=50, c='magenta', label='Cluster 5')
        plt.scatter(scaled[y_kmeans == 5, 0], scaled[y_kmeans == 5, 1], s=50, c='gray', label='Cluster 6')
        plt.scatter(scaled[y_kmeans == 6, 0], scaled[y_kmeans == 6, 1], s=50, c='purple', label='Cluster 7')
        plt.scatter(scaled[y_kmeans == 7, 0], scaled[y_kmeans == 7, 1], s=50, c='pink', label='Cluster 8')
        plt.scatter(scaled[y_kmeans == 8, 0], scaled[y_kmeans == 8, 1], s=50, c='silver', label='Cluster 9')
        plt.scatter(scaled[y_kmeans == 9, 0], scaled[y_kmeans == 9, 1], s=50, c='orange', label='Cluster 10')
        plt.scatter(scaled[y_kmeans == 10, 0], scaled[y_kmeans == 10, 1], s=50, c='orange', label='Cluster 11')


        plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:, 1], s=300, c='yellow', label='Centroids')
        plt.title('Clusters')
        plt.legend()
        st.pyplot(fig)

        kmeans = pd.DataFrame(data=y_kmeans, dtype=int)
        kmeans.columns = ['k_cluster']
        df_cluster = pd.concat([df_cluster, kmeans], axis=1)

        col1, col2 = st.columns([2, 2])
        with col1:
            st.subheader('Mean Popularity of each cluster')
            st.write(df_cluster.groupby(['k_cluster']).popularity.mean().sort_values(ascending=False))
        with col2:
            st.subheader('Song count in each cluster')
            st.write(df_cluster['k_cluster'].value_counts())
    with tab3:
        col1, col2=st.columns([1,1])
        with col1:
            with st.form('myform'):
                st.title("Enter some details of song type you're looking for:")
                popularity=st.slider('popularity',min_value=0, max_value=100)
                duration_ms=st.slider('duration_ms',min_value=8586, max_value=5237295)
                explicit = st.slider('explicit', min_value=0, max_value=1, step=1)
                danceability=st.slider('danceability',min_value=0.0, max_value=0.985)
                energy=st.slider('energy',min_value=0.0, max_value=1.0)
                key=st.slider('key',min_value=0, max_value=11)
                loudness=st.slider('loudness',min_value=-49.531, max_value= 4.532)
                mode=st.slider('mode',min_value=0.0, max_value=1.0)
                speechiness=st.slider('speechiness',min_value=0.0, max_value=0.965)
                acousticness=st.slider('acousticness',min_value=0.0, max_value=0.996)
                instrumentalness=st.slider('instrumentalness',min_value=0.0, max_value=1.0)
                liveness=st.slider('liveness',min_value=0.0, max_value=1.0)
                valence=st.slider('valence',min_value=0.0, max_value= 0.995)
                tempo=st.slider('tempo',min_value=0.0, max_value= 243.372)
                time_signature=st.slider('time_signature',min_value=0, max_value=5)
                submitted=st.form_submit_button('Submit')

        with col2:
            if submitted:
                data_input={'popularity':popularity, 'duration_ms':duration_ms, 'explicit':explicit,'danceability':danceability, 'energy':energy,
                            'key':key, 'loudness':loudness, 'mode':mode, 'speechiness':speechiness,
                            'acousticness':acousticness, 'instrumentalness':instrumentalness, 'liveness':liveness,
                            'valence':valence, 'tempo':tempo, 'time_signature':time_signature}
                y=pd.DataFrame(data_input, index=[0])
                X=pd.concat([X,y], axis=0)
                scaled = scaler.fit_transform(X)
                kmeans = KMeans(n_clusters=11, init='k-means++', max_iter=113999, n_init=25, random_state=0)
                y_kmeans = kmeans.fit_predict(scaled)
                y=pd.DataFrame(y_kmeans)
                clusterno=y.iloc[-1][0]
                result=df_cluster.query(f'k_cluster=={clusterno}')
                result=result[['track_id','track_name','album_name']]
                st.subheader(':green[Recommended songs are:]')
                st.write(result.head(10))




