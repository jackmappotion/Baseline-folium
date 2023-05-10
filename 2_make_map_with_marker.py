import folium
from folium import Marker

import pandas as pd

provider_df = pd.read_csv('./provider_info.csv',index_col=0)
customer_df = pd.read_csv('./customer_info.csv',index_col=0)

lat_main = pd.concat([provider_df['lat'],customer_df['lat']]).mean()
lng_main = pd.concat([provider_df['lng'],customer_df['lng']]).mean()

m = folium.Map(location=[lat_main, lng_main], tiles='openstreetmap', zoom_start=13)

for _, row in group_df.iterrows():
    html = f'''
    {row['group_name']}<br>
    {row['address']}<br>
    '''
    iframe = folium.IFrame(html,
                        width=100,
                        height=100)
    popup=folium.Popup(iframe,max_width=100)
    tooltip=folium.Tooltip(iframe)
    Marker(location = [row['lat'], row['lng']],
           tooltip=row['group_name'],
           popup=folium.Popup(iframe,max_width=100),
           icon=folium.Icon(color='blue',icon='star')
          ).add_to(m)
m
