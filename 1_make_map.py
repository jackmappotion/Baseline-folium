import folium
import pandas as pd

provider_df = pd.read_csv('./provider_info.csv',index_col=0)
customer_df = pd.read_csv('./customer_info.csv',index_col=0)

lat_main = pd.concat([provider_df['lat'],customer_df['lat']]).mean()
lng_main = pd.concat([provider_df['lng'],customer_df['lng']]).mean()

m = folium.Map(location=[lat_main, lng_main], tiles='openstreetmap', zoom_start=11)
m
