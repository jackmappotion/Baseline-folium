import folium
from folium import Marker

import pandas as pd

provider_df = pd.read_csv('./provider_info.csv',index_col=0)
customer_df = pd.read_csv('./customer_info.csv',index_col=0)

lat_main = pd.concat([provider_df['lat'],customer_df['lat']]).mean()
lng_main = pd.concat([provider_df['lng'],customer_df['lng']]).mean()

m = folium.Map(location=[lat_main, lng_main], tiles='openstreetmap', zoom_start=13)

for _, row in group_df.iterrows():
    Marker(location = [row['lat'], row['lng']],
           popup=row['group_name'],
           icon=folium.Icon(color='blue',icon='star')
          ).add_to(m)

for _, row in makers_df.iterrows():
    Marker(location = [row['lat'], row['lng']],
           tooltip=row['makers_name'],
           popup=row['makers_name'],
           icon=folium.Icon(color='red',icon='star')
          ).add_to(m)   
m
