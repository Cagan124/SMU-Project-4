# Import the required modules
import pandas as pd
pd.set_option('display.max_columns', None)
import json

# Machine Learning
from sklearn.preprocessing import StandardScaler
from scipy.spatial import distance
from sklearn import preprocessing
from sklearn.neighbors import NearestNeighbors


# suppress warnings
import warnings
warnings.filterwarnings('ignore')

class ModelHelper():
    def __init__(self):
    # select features for the model
        self.features = ['track_genre_acoustic',
    'track_genre_afrobeat',
    'track_genre_alt-rock',
    'track_genre_alternative',
    'track_genre_ambient',
    'track_genre_anime',
    'track_genre_black-metal',
    'track_genre_bluegrass',
    'track_genre_blues',
    'track_genre_brazil',
    'track_genre_breakbeat',
    'track_genre_british',
    'track_genre_cantopop',
    'track_genre_chicago-house',
    'track_genre_children',
    'track_genre_chill',
    'track_genre_classical',
    'track_genre_club',
    'track_genre_comedy',
    'track_genre_country',
    'track_genre_dance',
    'track_genre_dancehall',
    'track_genre_death-metal',
    'track_genre_deep-house',
    'track_genre_detroit-techno',
    'track_genre_disco',
    'track_genre_disney',
    'track_genre_drum-and-bass',
    'track_genre_dub',
    'track_genre_dubstep',
    'track_genre_edm',
    'track_genre_electro',
    'track_genre_electronic',
    'track_genre_emo',
    'track_genre_folk',
    'track_genre_forro',
    'track_genre_french',
    'track_genre_funk',
    'track_genre_garage',
    'track_genre_german',
    'track_genre_gospel',
    'track_genre_goth',
    'track_genre_grindcore',
    'track_genre_groove',
    'track_genre_grunge',
    'track_genre_guitar',
    'track_genre_happy',
    'track_genre_hard-rock',
    'track_genre_hardcore',
    'track_genre_hardstyle',
    'track_genre_heavy-metal',
    'track_genre_hip-hop',
    'track_genre_honky-tonk',
    'track_genre_house',
    'track_genre_idm',
    'track_genre_indian',
    'track_genre_indie',
    'track_genre_indie-pop',
    'track_genre_industrial',
    'track_genre_iranian',
    'track_genre_j-dance',
    'track_genre_j-idol',
    'track_genre_j-pop',
    'track_genre_j-rock',
    'track_genre_jazz',
    'track_genre_k-pop',
    'track_genre_kids',
    'track_genre_latin',
    'track_genre_latino',
    'track_genre_malay',
    'track_genre_mandopop',
    'track_genre_metal',
    'track_genre_metalcore',
    'track_genre_minimal-techno',
    'track_genre_mpb',
    'track_genre_new-age',
    'track_genre_opera',
    'track_genre_pagode',
    'track_genre_party',
    'track_genre_piano',
    'track_genre_pop',
    'track_genre_pop-film',
    'track_genre_power-pop',
    'track_genre_progressive-house',
    'track_genre_psych-rock',
    'track_genre_punk',
    'track_genre_punk-rock',
    'track_genre_r-n-b',
    'track_genre_reggae',
    'track_genre_reggaeton',
    'track_genre_rock',
    'track_genre_rock-n-roll',
    'track_genre_rockabilly',
    'track_genre_romance',
    'track_genre_sad',
    'track_genre_salsa',
    'track_genre_samba',
    'track_genre_sertanejo',
    'track_genre_show-tunes',
    'track_genre_singer-songwriter',
    'track_genre_ska',
    'track_genre_sleep',
    'track_genre_soul',
    'track_genre_spanish',
    'track_genre_study',
    'track_genre_swedish',
    'track_genre_synth-pop',
    'track_genre_tango',
    'track_genre_techno',
    'track_genre_trance',
    'track_genre_trip-hop',
    'track_genre_turkish',
    'track_genre_world-music',
    #'popularity',
    'duration_ms',
    'explicit',
    'danceability',
    'energy',
    'key',
    'loudness',
    'mode',
    'speechiness',
    'acousticness',
    'instrumentalness',
    'liveness',
    'valence',
    'tempo',
    'time_signature']
    # define a function to recommend songs based on a given song name
        
    def makePredictions(self, track_name, track_artist, playlist_length):
            # code somehow broke and the read_csv needed to be updated
            df = pd.read_csv('Resources/df_final.csv')
            df_final = df.copy()
            df_final['track_artist'] = df_final['artists']
        
            # define the number of nearest neighbors to consider
            k = playlist_length

            # initialize the model with the number of neighbors
            model = NearestNeighbors(n_neighbors=k)

            # fit the model to the data
            model.fit(df_final[self.features])
            
            # get the track_id of the given track name
            track_id = df_final[(df_final['track_name'] == track_name) & (df_final['track_artist'] == track_artist)]['track_id'].iloc[0]

            # print(f"track id: {track_id}")
            
            # get the index of the tracks in the model dataframe
            idx = df_final[df_final['track_id'] == track_id].index[0]
            # print(f"idx: {idx}")

            # get the features of the tracks
            track_features = df_final.loc[idx, self.features].values.reshape(1, -1)
            
            # find the k nearest neighbors
            distances, indices = model.kneighbors(track_features)
            # print(f"distances: {distances[0]}")
            
            # get the track names of the nearest neighbors
            tracks = df_final.iloc[indices[0]]
            tracks["distance"] = distances[0]
            

            # apply filters
            # tracks = tracks.loc[tracks.track_name == track_name]   
            # tracks = tracks.loc[tracks.artists == track_artist] 
            # print(f"tracks: {tracks}") 

            cols = ['track_id', 'track_name','artists', 'album_name', 'distance', 'popularity']

            tracks = tracks.loc[:, cols]
            tracks = tracks.sort_values(by = "distance")
            tracks = tracks.iloc[0:]

            return json.loads(tracks.to_json(orient='records'))
    
    def makePredictions2(self, track_name, track_artist, playlist_length):
            # code somehow broke and the read_csv needed to be updated
            df = pd.read_csv('Resources/df_final.csv')
            df_final = df.copy()
            df_final['track_artist'] = df_final['artists']
            df_final_pop = df_final.loc[df_final.popularity <= 0].reset_index(drop=True)


        
            # define the number of nearest neighbors to consider
            k = playlist_length

            # initialize the model with the number of neighbors
            model = NearestNeighbors(n_neighbors=k)

            # fit the model to the data
            model.fit(df_final_pop[self.features])
            
            # get the track_id of the given track name
            track_id = df_final[(df_final['track_name'] == track_name) & (df_final['track_artist'] == track_artist)]['track_id'].iloc[0]

            # print(f"track id: {track_id}")
            
            # get the index of the tracks in the model dataframe
            idx = df_final[df_final['track_id'] == track_id].index[0]
            # print(f"idx: {idx}")

            # get the features of the tracks
            track_features = df_final.loc[idx, self.features].values.reshape(1, -1)
            
            # find the k nearest neighbors
            distances, indices = model.kneighbors(track_features)
            # print(f"distances: {distances[0]}")
            
            # get the track names of the nearest neighbors
            tracks = df_final_pop.iloc[indices[0]]
            tracks["distance"] = distances[0]
            

            # apply filters
            # tracks = tracks.loc[tracks.track_name == track_name]   
            # tracks = tracks.loc[tracks.artists == track_artist] 
            # print(f"tracks: {tracks}") 


            cols = ['track_id', 'track_name','artists', 'album_name', 'distance', 'popularity']

            tracks = tracks.loc[:, cols]
            tracks = tracks.sort_values(by = "distance")
            tracks = tracks.iloc[0:]

            return json.loads(tracks.to_json(orient='records'))
            
    